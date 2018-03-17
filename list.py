import os
from azure.storage.blob import BlockBlobService

key_env_var_name = 'IMPRINTER_STORAGE_KEY'

storage_account = 'imprinter'
storage_key = os.environ[key_env_var_name]
container_orig_name = 'orig'
container_imprinted_name = 'imprinted'

block_blob_service = BlockBlobService(account_name=storage_account, account_key=storage_key)

local_path = os.getcwd()
file_name = "fen1.jpg"
file_path = os.path.join(local_path, file_name)

print(file_path)

block_blob_service.create_blob_from_path(container_orig_name, file_name, file_path)

blobs = block_blob_service.list_blobs(container_orig_name)
for blob in blobs:
    print(blob.properties.server_encrypted)
    print(blob.name)


