import os
from azure.storage.queue import QueueService, QueueMessageFormat

#key_env_var_name = 'IMPRINTER_STORAGE_KEY'
#os.environ[key_env_var_name]

storage_account = 'imprinter'
storage_key = "qELnM/SC2Sx90GcLebvUCruxz/ibFlUpa4JP9pQSdXxURJPIeHHQfIBULswkO9XToZe4wH61OqhlLyen6+wSgA=="
queue_name = 'imprintrequests'

queue_service = QueueService(account_name=storage_account, account_key=storage_key)
queue_service.decode_function = QueueMessageFormat.binary_base64decode

# messages = queue_service.peek_messages(queue_name)
messages = queue_service.get_messages(queue_name)
for message in messages:
    print(message.content)

message = messages[0]
queue_service.delete_message(queue_name, message.id, message.pop_receipt)
        
messages = queue_service.peek_messages(queue_name)
for message in messages:
    print(message.content)  # either message1 or message 2
