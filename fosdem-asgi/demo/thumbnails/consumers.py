from channels.consumer import SyncConsumer


class GenerateConsumer(SyncConsumer):
    def generate(self, message):
        print("Encoding: " + message["url"])
