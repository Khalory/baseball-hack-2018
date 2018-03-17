import os
from azure.storage.queue import QueueService, QueueMessageFormat

#key_env_var_name = 'IMPRINTER_STORAGE_KEY'
#os.environ[key_env_var_name]

storage_account = 'imprinter'
storage_key = "qELnM/SC2Sx90GcLebvUCruxz/ibFlUpa4JP9pQSdXxURJPIeHHQfIBULswkO9XToZe4wH61OqhlLyen6+wSgA=="
queue_name = 'imprintresults'

queue_service = QueueService(account_name=storage_account, account_key=storage_key)
#queue_service.encode_function = QueueMessageFormat.binary_base64encode

queue_service.put_message(queue_name, u'http://www.baseballhackday.com/images/agnew.jpg')
        
messages = queue_service.peek_messages(queue_name)
for message in messages:
    print(message.content)  # either message1 or message 2
