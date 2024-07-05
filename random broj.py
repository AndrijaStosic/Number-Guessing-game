from tkinter import *
import random

prozor = Tk()

tajp_rendom_broj = IntVar()

broj_pokusaja = 10
neki_broj = random.randint(1, 100)  

def proveravanje():
    global broj_pokusaja

    uneseni_broj = tajp_rendom_broj.get()

    if uneseni_broj == neki_broj:
        output_label.configure(text='You Won!')
    elif uneseni_broj < neki_broj:
        broj_pokusaja -= 1
        output_label.configure(text="""You didn't guess.
 The number is greater than """ + str(uneseni_broj) + ". You have " + str(broj_pokusaja) + """
 more attempts""")
    else:
        broj_pokusaja -= 1
        output_label.configure(text="""You didn't guess.
The number is lower than """ + str(uneseni_broj) + ". Imaš još " + str(broj_pokusaja) + """ 
more attempts""")

    entry.delete(0, END)

    if broj_pokusaja == 0:
        output_label.configure(text="Game over. The number was: " + str(neki_broj))

def pokreni_proveru():
    proveravanje()

prozor.title("Pogodi broj")
prozor.geometry('300x200') 
prozor.config(bg='#E6E6FA')  
output_label = Label(prozor, bg='#E6E6FA')  
output_label.grid(row=4, column=0, pady=10)  

pocetni_tekst = Label(prozor, text="Guess the number", font="Arial 14 bold", bg='#E6E6FA')  
pocetni_tekst.grid(row=0, column=0, pady=10) 

drugi_tekst = Label(prozor, text="Enter a number from 1 to 100:", bg='#E6E6FA')  
drugi_tekst.grid(row=1, column=0)  
entry = Entry(prozor, textvariable=tajp_rendom_broj)
entry.grid(row=2, column=0, padx=10, pady=5)  

dugme_provera = Button(prozor, text="Guess", command=pokreni_proveru)
dugme_provera.grid(row=3, column=0, pady=10)  

mainloop()
