"""Idea taken from https://www.notion.so/Sentence-Email-Generator-a36d269ce8e94cc58daf723f8ba8fe3e"""


from api import GPT, Example
class command_to_email_example():
    def __init__(self):
        # Construct GPT object and show some examples
        self.gpt = GPT(engine="davinci",
                temperature=0.4,
                max_tokens=60)

        self.gpt.add_example(Example('Thank John for the book.',
                                'Dear John, Thank you so much for the book. I really appreciate it. I hope to hang out soon. Your friend, Sarah.'))

        self.gpt.add_example(Example('Tell TechCorp I appreciate the great service.',
                                'To Whom it May Concern, I want you to know that I appreciate the great service at TechCorp. The staff is outstanding and I enjoy every visit. Sincerely, Bill Johnson'))

        self.gpt.add_example(Example('Invoice Kelly Watkins $500 for design consultation.',
                                'Dear Ms. Watkins, This is my invoice for $500 for design consultation. It was a pleasure to work with you. Sincerely, Emily Fields'))

        self.gpt.add_example(Example('Invite Amanda and Paul to the company event Friday night.',
                                'Dear Amanda and Paul, I hope this finds you doing well. I want to invite you to our company event on Friday night. It will be a great opportunity for networking and there will be food and drinks. Should be fun. Best, Ryan'))


    def getGPT(self):
        return self.gpt
    
    def getTitle(self):
        return "Command to email generator"
    
    def getSample(self):
        return "Ask RAM Co. if they have new storage units in stock."


