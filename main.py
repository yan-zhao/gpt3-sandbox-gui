import tkinter as tk
import tkinter.scrolledtext

#########################################################################
#   Class App
#########################################################################
def CloseApp():
    quit()

def Submit():
    quit()

#########################################################################
#   Main
#########################################################################
if __name__ == "__main__":
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
    info.configure(state="disabled")      #only can disable the text after the insert


    #submit to GPT
    buttonClose = tk.Button(frameInput, text="Submit", width=20, height=2, command=Submit, bd=2)
    buttonClose.place(x=20,y=60)


    #Close App
    buttonClose = tk.Button(mainWindow, text="Close", width=30, height=2, command=CloseApp, bd=2)
    buttonClose.place(x=20,y=340)

    mainWindow.mainloop()