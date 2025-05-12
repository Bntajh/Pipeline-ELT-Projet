#importer la librarie de google cloud storage pour permettre l'interaction avec les fichiers dans les buckets.
from google.cloud import storage

#definir une fonction
def lister_files(bucket_name) :
    client = storage.Client(project="valued-cumulus-458918-i8") #créer un client GCS en spécifiant le projet GC à utiliser via son ID
    bucket = client.get_bucket("bnt-ecommerce-bucket") #récuprer une référence au bucket spécifié à partir du client

    print(f"Fichier dans le bucket '{bucket.name}':") #afficher un message indiquant qu'on va lister les fichiers
    for blob in bucket.list_blobs(): #creer une condition qui va permettre de parcourir tous les objets contenus dans le bucket
        print(blob.name)

lister_files("bnt-ecommerce-bucket")
