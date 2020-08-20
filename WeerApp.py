import tkinter as tk
import requests
from tkinter import Menu
from tkinter import messagebox as mBox
from tkinter import font
from decimal import Decimal



def format_response(weather): #Maken van functie format response
    try:
        name = weather['name'] #Sla data op in name variable
        desc = weather['weather'][0]['description'] #Sla data op in desc variable
        temp = weather['main']['temp'] #Sla data op in temp variable
        celcius = round((temp -32) / 1.8) #opgekregen data opslaan in celcius variable (Omrekenen van fahrenheit naar celcius) aka afronden op 2 decimalen
        
        final_str = 'Stad: %s \nOmstandigheden: %s \nTemperatuur (°C): %s' % (name, desc, celcius) #String die te zien is in prototype

    except:
        final_str = 'Data kon niet opgehaald worden' #Als data niet opgehaald kan worden display de tekst

    return final_str #return de waarde van final_str

def get_weather(city): #maken van functie met parameter city
    weather_key = 'PRIVATE_KEY' #API key
    url = 'https://api.openweathermap.org/data/2.5/weather' #Link naar de website van openweather (voor api)
    params = {'APPID': weather_key, 'q': city, 'units': 'imperial'} #geef aan welke params we gebruiken
    response = requests.get(url, params=params) #Stuur een request naar de URL en de params
    weather = response.json() #Haal Json data terug op
    label['text'] = format_response(weather) #Zet de opgehaalde data in het tekstvak in het prototype


root = tk.Tk() #tk.Tk opslaan in root variable
root.title("Prototype - WeersApp") #Dit is de titel van de applicatie


#Globale variabelen
HEIGHT = 500
WIDTH = 600

#CANVAS GEDEELTE
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

#BACKGROUND GEDEELTE
background_image = tk.PhotoImage(file='test.png') #Storen van background image in een variable
background_label = tk.Label(root, image=background_image) #Plaats image in root window van tk label
background_label.place(relwidth=1, relheight=1) #Plaats met width 1 en height 1

#Frame gedeelte (blauwe vakje bovenaan)
frame = tk.Frame(root, bg='#80c1ff', bd=5) #Kleur met border width meegeven
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n') #Opmaak van blokje hier meegeven (anchor geeft aan in het midden)

#Invulveld in het frame gedeelte maken
entry = tk.Entry(frame, font=('Helvetica', 20)) #Geef aan dat het font 20px is met Helvetica
entry.place(relwidth=0.65, relheight=1) #Hoogte en breedte meegeven

#Plaatsen van button hier
button = tk.Button(frame, text='Haal gegevens op', font=('Helvetica', 11), command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

#Hier komen de uitkomsten op basis van de API
lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

#maak wit vakje over de lower frame
label = tk.Label(lower_frame, font=('Helvetica', 15))
label.place(relwidth=1, relheight=1)


# Het veranderen van het icoontje
root.iconbitmap('wolkje.ico') #veranderen van het icoon links boven


#het maken van een menu bar
menuBar = Menu(root)
root.config(menu=menuBar)

#Afsluiten van GUI functie
def _quit():
    root.quit()
    root.destroy()
    exit()

#Maken van popup message box voor help
def _msgBox():
    mBox.showinfo('Python Message Info box','ProtoType WeersApp \nDit is een project gemaakt voor een SRP punt \n \nRowin Ruizendaal\n500813624\nCommunication & multi media design')


#Toevoegen van menu items
fileMenu = Menu(menuBar, tearoff=0) #zet HR streep goed neer
fileMenu.add_command(label="New") #onderdeel van kopje
fileMenu.add_separator() #Houdt het per onderdeel
fileMenu.add_command(label="Exit", command=_quit) #onderdeel van kopje aanroepen van functie _quit
menuBar.add_cascade(label="File", menu=fileMenu) #bepaalt welke tekst het kopje krijgt

#toevoegen van een ander menu
helpMenu = Menu(menuBar, tearoff=0)
helpMenu.add_command(label="About", command=_msgBox)
menuBar.add_cascade(label="Help", menu=helpMenu)




root.mainloop()