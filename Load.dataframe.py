import pandas as pd
from google.cloud import storage

# Paramètres
bucket_name = "bnt-ecommerce-bucket"
source_blob_name = "input/2019-Oct.csv"  # Chemin dans le bucket
destination_file_name = "test-2029-OCT.csv"  # Chemin local (tu peux ajouter ./ ou un dossier)

# Connexion au client GCS
storage_client = storage.Client()
bucket = storage_client.bucket(bucket_name)
blob = bucket.blob(source_blob_name)

# Télécharger le fichier dans ton dossier local
blob.download_to_filename(destination_file_name)

print(f"✅ Fichier '{source_blob_name}' téléchargé en local sous '{destination_file_name}'")
