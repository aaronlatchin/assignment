Igbo_dictionary = {"bia": 'come',
                   "eze": 'king',
                   "nri": 'food',
                   "isi": 'head',
                   "ire": 'tongue',
                   "onu": 'mouth',
                   "aka": 'hand',
                   "nkita": 'dog',
                   "agwa": 'beans',
                   "akpa": 'bag',
                   "nye": 'give/present',
                   "chineke": 'lord',
                   "ehi": 'cow',
                   "ewu": 'goat',
                   "ube": 'pear',
                   "imela": 'thank you',
                   "oyi": 'cold',
                   "ekpere": 'prayer',
                   "ego": 'money',
                   "chukwu": 'God'}

Spanish_dictionary ={"hola": 'hello',
                     "adios": 'goodbye',
                     "gracias":'thank you',
                     "por favor":'please',
                     "si": 'yes',
                     "no":'no',
                     "buenos dias":'good morning',
                     "buenas noches":'good night',
                     "lo siento":'I am sorry',
                     "familia":'family',
                     "amigo":'friend',
                     "luz":'light',
                     "agua":'water',
                     "comida":'food',
                     "casco":'helmet',
                     "zapatos":'shoes'}

from tkinter import Tk, Entry, Button, Label, StringVar,Menubutton,Menu

window = Tk()
window.geometry("600x250")
window.title("Igbo_dictionary")


mb= Menubutton(window,text="Select language")
mb.menu= Menu(mb)
mb["menu"]=mb.menu



def openNewWindow():
    word = StringVar()
    word_entry = Entry(window, textvariable=word, font=('ariel', 19))
    word_entry.pack()


    result = StringVar()
    result_label = Label(window, textvariable=result)
    result_label.pack()


    def search (word):
        if word in Igbo_dictionary:
            result.set(Igbo_dictionary[word])
            print(Igbo_dictionary[word])
        else:
            result.set("not found")


    search_btn = Button(window, text="search", command=lambda: search(word.get()))
    search_btn.pack()
  
def spanish():
     word = StringVar()
     word_entry = Entry(window, textvariable=word, font=('ariel', 19))
     word_entry.pack()


     result = StringVar()
     result_label = Label(window, textvariable=result)
     result_label.pack()


     def search (word):
        if word in Spanish_dictionary:
            result.set(Spanish_dictionary[word])
            print(Spanish_dictionary[word])
        else:
            result.set("not found")
            
     search_btn = Button(window, text="search", command=lambda: search(word.get()))
     search_btn.pack()
mb.menu.add_command(label="Igbo dictionary",command=(openNewWindow))
mb.pack()

menu2_btn=Button(window,text="spanish Language",command=(spanish))
menu2_btn.pack() 

window.mainloop()

