""" Manage the queue for the log messages """

import config
from log import Log

from azure.storage.queue import QueueService

import os

class Queue:
    def __init__(self):
        self.log = Log()
        self.queue_type = os.environ['ACS_LOGGING_QUEUE_TYPE']
        self.log.info("Queue type: " + self.queue_type)

        if self.queue_type == "AzureStorageQueue":
            self.createAzureQueues()
        elif self.queue_type == "LocalFile":
            self.file_queue = open(config.UNPROCESSED_LOG_FILE, 'w+')
        else:
            self.log.error("Unknown queue type: " + queue_type)

    def createAzureQueues(self):
        """Create a 'logqueue' for unprocessed log messages. Entries in the
'logqueue' will be dequeued, processed and deleted upon success.
        """

        # FIXME: remove hardcoded account name and key
        global queue_service 
        queue_service = QueueService(account_name='acstest', account_key='vCyk6qOZQWzGLQrBMMYsG+a2HQm0FuMyLEv1zqn1/8ll11kaAP37BrxVmfj9PWnFHSGmoEWSUXl4q6SCodFzYg==')
        queue_service.create_queue('logqueue')

    def close(self):
        """Perform any necessary clearnup on the queue
           at the end of a run.
        """
        if self.queue_type == "AzureStorageQueue":
            pass
        elif self.queue_type == "LocalFile":
            self.file_queue.close()
        else:
            self.log.error("Unknown queue type: " + queue_type)
        

    def enqueue(self, msg, level = "INFO"):
        msg = level + " - " + msg
        if self.queue_type == "LocalFile":
            file_queue.write(msg + '\n')
        elif self.queue_type == "AzureStorageQueue":
            queue_service.put_message('logqueue', msg)
        self.log.debug(msg)

    def dequeue(self):
        messages = []
        if self.queue_type == "LocalFile":
            with open(config.UNPROCESSED_LOG_FILE, 'r') as f:
                messages = f.readlines()[1]
        elif self.queue_type == "AzureStorageQueue":
            messages = queue_service.get_messages('logqueue')
        return messages

    def delete(self, message):
        queue_service.delete_message('logqueue', message.message_id, message.pop_receipt)
        #  with open(config.PROCESSED_LOG_FILE, 'a') as processed:
        #    processed.write(log)
        #  os.remove(config.UNPROCESSED_LOG_FILE)
