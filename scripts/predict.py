import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import os

# Chemin du modèle sauvegardé (adapter si nécessaire)
MODEL_PATH = 'models/mon_mod_entrainer_tbc.h5'
model = load_model(MODEL_PATH)

# Taille des images attendue par le modèle
IMG_SIZE = 224

def predict_image(image_path):
    """
    Charge une image, effectue une prédiction avec le modèle entraîné.

    Args :
        image_path (str) : chemin vers l'image à tester.

    Retourne :
        label (str) : 'Tuberculose' ou 'Normal' en fonction de la prédiction.
        probability (float) : la probabilité associée à la prédiction.
    """
    # Vérifier si le modèle existe
    if not os.path.exists(MODEL_PATH):
        print(f"Erreur : le modèle n'a pas été trouvé dans {MODEL_PATH}. Entraîne ton modèle d'abord.")
        return

    # Charger le modèle
    model = load_model(MODEL_PATH)

    # Charger et redimensionner l'image
    img = load_img(image_path, target_size=(IMG_SIZE, IMG_SIZE))
    # Convertir l'image en tableau numpy et normaliser
    img_array = img_to_array(img) / 255.0
    # Ajouter une dimension pour faire une batch
    img_array = np.expand_dims(img_array, axis=0)

    # Faire la prédiction
    pred = model.predict(img_array)[0][0]
    # Définir la classe en fonction du seuil 0.5
    if pred > 0.5:
        label = 'Tuberculose'
    else:
        label = 'Normal'

    print(f"Prédiction : {label} (Probabilité={pred:.2f})")
    return label, pred

# Exemple d'utilisation
#if __name__ == "__main__":
 #   # Modifier ce chemin pour tester avec ta propre image
  #  test_image_path = 'chemin/vers/ton/image.jpg'
   # predict_image(test_image_path)