
from api import GPT, Example
class latex_example():
    def __init__(self):
        # Construct GPT object and show some examples
        self.gpt = GPT(engine="davinci",
                temperature=0.5,
                max_tokens=100)

        self.gpt.add_example(Example('Two plus two equals four', '2 + 2 = 4'))
        self.gpt.add_example(
            Example('The integral from zero to infinity', '\\int_0^{\\infty}'))
        self.gpt.add_example(Example(
            'The gradient of x squared plus two times x with respect to x', '\\nabla_x x^2 + 2x'))
        self.gpt.add_example(Example('The log of two times x', '\\log{2x}'))
        self.gpt.add_example(
            Example('x squared plus y squared plus equals z squared', 'x^2 + y^2 = z^2'))
        self.gpt.add_example(
            Example('The sum from zero to twelve of i squared', '\\sum_{i=0}^{12} i^2'))
        self.gpt.add_example(Example('E equals m times c squared', 'E = mc^2'))
        self.gpt.add_example(Example('H naught of t', 'H_0(t)'))
        self.gpt.add_example(Example('f of n equals 1 over (b-a) if n is 0 otherwise 5',
                                'f(n) = \\begin{cases} 1/(b-a) &\\mbox{if } n \\equiv 0 \\\ # 5 \\end{cases}'))

    def getGPT(self):
        return self.gpt
    
    def getTitle(self):
        return "Text to equation"
    
    def getSample(self):
        return "x squared plus 2 times x"

