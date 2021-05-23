import tkinter as tk
import tkinter.scrolledtext
import openai
from api.gpt import GPT, Example, set_openai_key
import json
from examples.receipe_example import receipe_example

questionVar=None  # question variable for question entry widget
KEY_NAME = "OPENAI_KEY"
output_text = None     #text widget for output
example = None

def getBlankExample():
    # Construct GPT object and show some examples
    gpt = GPT(engine="davinci", temperature=0.5, max_tokens=100)

    gpt.add_example(Example("Who are you?", "I'm an example."))
    gpt.add_example(Example("What are you?", "I'm an example."))

    return gpt

#Get GPT constructed in a example and then
def runExample(prompt):
    gpt = example.getGPT()

    response = gpt.submit_request(prompt)

    offset = 0
    if not gpt.append_output_prefix_to_query:
        offset = len(gpt.output_prefix)
        ret = {'text': response['choices'][0]['text'][offset:]}
    else:
        ret = None
    return ret
    


#########################################################################
#   Class App
#########################################################################
def CloseApp():
    quit()

#########################################################################
#   Load Example
#########################################################################
def LoadExample():
    global example
    example = receipe_example()

    #update gui
    if example is not None:
        title = example.getTitle()
        frameInput.config(text = title)

        sample = example.getSample()
        questionVar.set(sample)

        buttonSubmit.config(state="active")
#########################################################################
#   Submit question to GPT
#########################################################################
def Submit():
    global example

    if example is None:
        tk.messagebox.showerror ("Error", "Failed to load example")
        return

    #get the question
    prompt = questionVar.get()

    answer = runExample(prompt)
    if answer == None:
        output_text.insert(tk.INSERT,'No Answer.')
    else:
        if answer['text']=="" or answer['text']=="\n":
            output_text.insert(tk.INSERT,'No Answer.')
        else:
            output_text.insert(tk.INSERT, answer['text'])
    output_text.update_idletasks()

#########################################################################
#   Main
#########################################################################
if __name__ == "__main__":

    # read JSON file
    with open('api/GPT_SECRET_KEY.json', 'r') as keyfile:
        data=keyfile.read()

    # parse file
    keys = json.loads(data)

    set_openai_key(keys[KEY_NAME])

    mainWindow  = tk.Tk()
    mainWindow.geometry("500x400")        #main frame of 500*400
    mainWindow.title("GPT3 Sandbox with GUI by Yan Zhao")

    frameInput = tk.LabelFrame(mainWindow, text = "Ask a Question:", width=450, height=300, bd=2)
    frameInput.place(x=20, y=10)

    label1 = tk.Label(frameInput, text='Question: ')
    label1.config(font=('Arial', 10))
    label1.place(x=30, y = 30)

    questionVar = tk.StringVar()       #store password input

    questionEntry = tk.Entry(frameInput, bd = 2, width = 50,  textvariable=questionVar)
    questionEntry.place(x=100, y=30)

    labelAnwser = tk.Label(frameInput, text='Answer:')
    labelAnwser.place(x=20, y=120)

    output_text = tk.scrolledtext.ScrolledText(frameInput, width=50, height=6, bg='light gray')
    output_text.place(x=20, y= 160)
        
    #get Example
    buttonGetExample = tk.Button(frameInput, text="Get Example", width=20, height=2, command=LoadExample, bd=2)
    buttonGetExample.place(x=20,y=60)

    #submit to GPT
    buttonSubmit = tk.Button(frameInput, text="Submit", width=20, height=2, command=Submit, bd=2)
    buttonSubmit.place(x=200,y=60)
    buttonSubmit.config(state="disabled")


    #Close App
    buttonClose = tk.Button(mainWindow, text="Close", width=30, height=2, command=CloseApp, bd=2)
    buttonClose.place(x=20,y=340)

    mainWindow.mainloop()