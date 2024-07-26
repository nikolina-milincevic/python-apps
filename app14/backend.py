import openai

# for this app to work, you need you own valid api key


class Chatbot:
    def __init__(self):
        openai.api_key = "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"
        
    def get_response(self, user_input):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_input,
            max_tokens=3000,
            temperature=0.5  
            # closer to 0 is more precise but more rigid, 
            # closer to 1 is less precise but more diverse
        ).choices[0].text()
        return response
    

if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.get_response("Write a joke.")
    print(response)