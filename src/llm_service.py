import ollama as ol 

class ChatService:
    def __init__(self, model):
        self.model= model

    def generate(self,messages):
        response = ol.chat(self.model,messages,stream=False)
        return response['message']['content']

    def generate_stream(self,messages):
        return ol.chat(self.model,messages,stream=True)