from fastapi import FastAPI, File, UploadFile, HTTPException, Header
from pydantic import BaseModel
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import gdown
from io import BytesIO
from PIL import Image
import tensorflow as tf
import os


os.environ['CUDA_VISIBLE_DEVICES'] = ''

tf.config.set_visible_devices([], 'GPU')

# Fonction pour charger le modèle à partir d'un fichier Google Drive
def load_model_from_drive(file_id: str):
    url = f'https://drive.google.com/uc?id={file_id}'
    output_path = 'mon_mod_entrainer_tbc.h5'
    gdown.download(url, output_path, quiet=False)
    return load_model(output_path)

# Charger le modèle à partir de Google Drive
DRIVE_FILE_ID = '1j-UAGDqqPgZ2RVXKFqIBVqfhLpzIpEL7'  # Remplacez-le par votre ID fichier Google Drive
model = load_model_from_drive(DRIVE_FILE_ID)

# Taille de l’image
IMG_SIZE = 224

# Clé API pour la sécurité
API_KEY = "5431-Eg__01"

# Instance FastAPI
app = FastAPI()

@app.post("/predict")
async def predict(
    file: UploadFile = File(...),
    x_api_key: str = Header(None)
):
    # Vérification de la clé API
    #if x_api_key != API_KEY:
     #   raise HTTPException(status_code=403, detail="Non autorisé. Vérifiez votre clé API.")

    # Vérifier que le fichier est une image
    if not file.content_type.startswith('image/'):
        raise HTTPException(status_code=400, detail="Le fichier n'est pas une image.")

    # Lire le contenu du fichier
    image_bytes = await file.read()

    # Charger l’image avec PIL
    image = Image.open(BytesIO(image_bytes)).convert('RGB')
    # Redimensionner
    image = image.resize((IMG_SIZE, IMG_SIZE))
    # Convertir en array
    img_array = img_to_array(image) / 255.0
    # Ajouter une dimension batch
    img_array = np.expand_dims(img_array, axis=0)

    # Prédiction
    pred = model.predict(img_array)[0][0]
    label = 'Tuberculose' if pred > 0.5 else 'Normal'
    probability = float(pred)

    return {
        "label": label,
        "probability": probability
    }
