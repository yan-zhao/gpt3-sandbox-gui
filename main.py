import tkinter as tk
import tkinter.scrolledtext
import openai
from api.gpt import GPT, Example, set_openai_key
import json
from examples.reicipe_example import reicipe_example

questionVar=None
KEY_NAME = "OPENAI_KEY"
info = None

def getBlankExample():
    # Construct GPT object and show some examples
    gpt = GPT(engine="davinci", temperature=0.5, max_tokens=100)

    gpt.add_example(Example("Who are you?", "I'm an example."))
    gpt.add_example(Example("What are you?", "I'm an example."))

    return gpt

#Get GPT constructed in a example and then
def runExample(prompt):
    example = reicipe_example()
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

def Submit():
    #get the question
    prompt = questionVar.get()

    answer = runExample(prompt)
    if answer == None:
        info.insert(tk.INSERT,'No Answer.')
    else:
        info.insert(tk.INSERT, answer['text'])
    info.update_idletasks()

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

    passwordEntry = tk.Entry(frameInput, bd = 2, width = 50,  textvariable=questionVar)
    passwordEntry.place(x=100, y=30)

    labelAnwser = tk.Label(frameInput, text='Answer:')
    labelAnwser.place(x=20, y=120)

    info = tk.scrolledtext.ScrolledText(frameInput, width=50, height=6, bg='light gray')
    info.place(x=20, y= 160)



    #submit to GPT
    buttonClose = tk.Button(frameInput, text="Submit", width=20, height=2, command=Submit, bd=2)
    buttonClose.place(x=20,y=60)


    #Close App
    buttonClose = tk.Button(mainWindow, text="Close", width=30, height=2, command=CloseApp, bd=2)
    buttonClose.place(x=20,y=340)

    mainWindow.mainloop()