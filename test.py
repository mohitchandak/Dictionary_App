import json
from difflib import get_close_matches
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Dictionary")
root.geometry("700x300")
root.configure(bg="black")
global my_input
my_input = Entry(root, width=60, borderwidth=3)
my_input.insert(0, "Please enter a word")
my_input.pack()

def SearchWord():
    data = json.load(
        open("C:/Users/surendra/Desktop/Python/TkinterApp1/mohit first project/data.json"))

    global my_word
    my_word = my_input.get()

    def translate(w):   
        w = w.lower()
        if w in data:
            return data[w]
        elif w.title() in data:
            return data[w.title()]
        elif w.upper() in data:
            return data[w.upper()]
        elif len(get_close_matches(w, data.keys())) > 0:
            print("did you mean %s instead" %
                get_close_matches(w, data.keys())[0])
            decide = input("press y for yes or n for no: ")
            if decide == "y":
                return data[get_close_matches(w, data.keys())[0]]
            elif decide == "n":
                return("Wrong word!")
            else:
                return("You have entered wrong input please enter just y or n: ")
        else:
            print("pugger your paw steps on wrong keys")


    output = translate(my_word)
    if type(output) == list:
        for item in output:
            messagebox.showinfo("Result","The Word Definiton is: " + item)
            user_msg =   messagebox.askyesno("Ask","Do you want to find another word?")

            if (user_msg.lower())=='yes':
                output = translate(my_word)
                for item in output:
                    messagebox.showinfo("Result", "The Word Definiton is: " + item)
                    user_msg = messagebox.askyesno("Ask", "Do you want to find another word?")
            else:
                messagebox.showinfo("Thank You!","Thank you for using our program!")

            
    else:
        print(output)




my_Btn = Button(root,text="Click Me!",bg="red",command=SearchWord) # Creted button
my_Btn.pack() # Put button on window

root.mainloop()
