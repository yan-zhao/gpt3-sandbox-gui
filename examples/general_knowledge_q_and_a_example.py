
from api import GPT, Example
class general_knowledge_q_and_a_example():
    def __init__(self):
        question_prefix = 'Q: '
        question_suffix = "\n"
        answer_prefix = "A: "
        answer_suffix = "\n\n"

        # Construct GPT object and show some examples
        self.gpt = GPT(engine="davinci",
                temperature=0.5,
                max_tokens=100,
                input_prefix=question_prefix,
                input_suffix=question_suffix,
                output_prefix=answer_prefix,
                output_suffix=answer_suffix,
                append_output_prefix_to_query=True)

        self.gpt.add_example(Example('What is human life expectancy in the United States?',
                                'Human life expectancy in the United States is 78 years.'))
        self.gpt.add_example(
            Example('Who was president of the United States in 1955?', 'Dwight D. Eisenhower was president of the United States in 1955.'))
        self.gpt.add_example(Example(
            'What party did he belong to?', 'He belonged to the Republican Party.'))
        self.gpt.add_example(Example('Who was president of the United States before George W. Bush?',
                                'Bill Clinton was president of the United States before George W. Bush.'))
        self.gpt.add_example(Example('In what year was the Coronation of Queen Elizabeth?',
                                'The Coronation of Queen Elizabeth was in 1953.'))

    def getGPT(self):
        return self.gpt
    
    def getTitle(self):
        return "Question to Answer"
    
    def getSample(self):
        return "Who wrote the song 'Hey Jude'?"


