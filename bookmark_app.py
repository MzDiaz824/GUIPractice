import tkinter as tk
import webbrowser
#create event to connect to genomics data
def genomeDB(event):
    webbrowser.open_new_tab('https://www.ncbi.nlm.nih.gov/labs/virus/vssi/#/')
def BlastSearch(event):
    webbrowser.open_new_tab('https://blast.ncbi.nlm.nih.gov/Blast.cgi')
def OMIM(event):
    webbrowser.open_new_tab('https://www.ncbi.nlm.nih.gov/omim')
#create window for events
genoWindo = tk.Tk()
genoWindo.geometry("600x200")
genoWindo.title("Genome Database Search Options")
#create label
labelGW = tk.Label(text='Choose Your Genome Search')
labelGW.grid(column = 0, row= 0)
#font styling
labelGW = tk.Label(text = 'Genome Database Search Options', font = ('Calibri', 24))
#create Buttons for each link
buttonVir = tk.Button(genoWindo, text="NIH Genome DataBase")
buttonVir.grid(column = 1, row = 1)
buttonBlast = tk.Button(genoWindo, text = 'BLAST Search')
buttonBlast.grid(column =2, row =1)
buttonOMIM = tk.Button(genoWindo, text = 'OMIM Search')
buttonOMIM.grid(column= 3, row = 1)
#BIND THE BUTTONS
buttonVir.bind('<Button-1>', genomeDB)
buttonBlast.bind('<Button-1>', BlastSearch)
buttonOMIM.bind('<Button-1>', OMIM)
genoWindo.mainloop()