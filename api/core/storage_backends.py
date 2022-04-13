from storages.backends.azure_storage import AzureStorage
import os


class AzureMediaStorage(AzureStorage):
    account_name = os.environ["AZURE_ACCOUNT_NAME"]
    account_key = os.environ["AZURE_ACCOUNT_KEY"]  # Must be replaced by your <storage_account_key>
    azure_container = 'media'
    expiration_secs = None