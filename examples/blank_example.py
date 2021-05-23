from api import GPT, Example
class blank_example():

    def __init__(self):
        # Construct GPT object and show some examples
        self.gpt = GPT(engine="davinci", temperature=0.5, max_tokens=100)

        self.gpt.add_example(Example("Who are you?", "I'm an example."))
        self.gpt.add_example(Example("What are you?", "I'm an example."))

    def getGPT(self):
        return self.gpt
    
    def getTitle(self):
        return "Prompt"
    
    def getSample(self):
        return "Where are you?"

