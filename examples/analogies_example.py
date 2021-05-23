"""Idea taken from https://www.notion.so/Analogies-Generator-9b046963f52f446b9bef84aa4e416a4c"""

from api import GPT, Example
class analogies_example():

    def __init__(self):
        # Construct GPT object and show some examples
        self.gpt = GPT(engine="davinci",
                temperature=0.5,
                max_tokens=100)

        self.gpt.add_example(Example('Neural networks are like',
                                'genetic algorithms in that both are systems that learn from experience.'))
        self.gpt.add_example(Example('Social media is like',
                                'a market in that both are systems that coordinate the actions of many individuals.'))
        self.gpt.add_example(Example(
            'A2E is like', 'lipofuscin in that both are byproducts of the normal operation of a system.'))
        self.gpt.add_example(Example('Haskell is like',
                                'LISP in that both are functional languages.'))
        self.gpt.add_example(Example('Quaternions are like',
                                'matrices in that both are used to represent rotations in three dimensions.'))
        self.gpt.add_example(Example('Quaternions are like',
                                'octonions in that both are examples of non-commutative algebra.'))

    def getGPT(self):
        return self.gpt
    
    def getTitle(self):
        return "Analogies generator"
    
    def getSample(self):
        return "Memes are like"
