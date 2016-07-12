
from tkinter import *

myFavCars = {1:'VOLKSWAGEN',2:'BMW',3:'JEEP SAHARA',4:'LANDROVER' }



def list_cars(myFavCars):
    for car in myFavCars:
        print(car,myFavCars[car])

rides = list_cars(myFavCars)

tk = Tk()

canvas = Canvas(tk, width= 1000, height= 1000)
canvas.pack()
canvas.create_text(100,30,text ='CARS', font= ('Times',35),fill= 'Green')

canvas.create_text(116,100,text = '1. VOLKSWAGEN', font= ('Helvetica',15),fill = 'Blue')
canvas.create_text(73,125,text = '2. BMW', font= ('Helvetica',15),fill = 'Blue')
canvas.create_text(115,152,text = '3. JEEP SAHARA', font= ('Helvetica',15),fill = 'Blue')
canvas.create_text(110,176,text = '4. LANDROVER', font= ('Helvetica',15),fill = 'Blue')
