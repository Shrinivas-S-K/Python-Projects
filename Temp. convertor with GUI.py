from tkinter import *

def kf():
    x=entry.get()
    if x!="":
        cel=float(x)                                                
        far=(9/5*(cel))+32            #Celcius to farenheit formula
        kel=cel+273.15                 #Celcius to kelcin formula
        Label(root,text="\nTemperature in farenheit:").pack()
        Label(root,text=far).pack()     #Display farenheit
        Label(root,text="\nTemperature in Kelvin:").pack()
        Label(root,text=kel).pack()        #Diaplay Kelvin

def ck():
    x=entry.get()
    if x!="":
        far=float(x)                                                
        cel=(far-32)*(5/9)            
        kel=((5/9)*far)+459.67                 #Celcius to kelcin formula
        Label(root,text="\nTemperature in Celcius:").pack()
        Label(root,text=cel).pack()     #Display farenheit
        Label(root,text="\nTemperature in Kelvin:").pack()
        Label(root,text=kel).pack()        #Diaplay Kelvin

def cf():
    x=entry.get()
    if x!="":
        kel=float(x)                                                
        cel=kel-273.15           
        far=(kel-273.15)*(9/5)+32                 #Celcius to kelcin formula
        Label(root,text="\nTemperature in Celcius:").pack()
        Label(root,text=cel).pack()     #Display Farinheit
        Label(root,text="\nTemperature in farenheit:").pack()
        Label(root,text=far).pack() 

root=Tk()                                  #Root window created using 'Tk()' function
root.title("Temperatur Converter")        #Name of the window panal
root.geometry("400x700")                    #Dimentation
root.configure(bg='gray')              

Label(root,text="\nEnter a Temperature in Celcius.").pack()
entry=Entry(root)                          #Input from the user
entry.pack()
Button(root,text="Calculate K and F",command=kf).pack()      #Submit button

Label(root,text="\nEnter a Temperature in farenheit.").pack()
entry=Entry(root)                          #Input from the user
entry.pack()
Button(root,text="Calculate C and K",command=ck).pack()


Label(root,text="\nEnter a Temperature in Kelvin.").pack()
entry=Entry(root)                          #Input from the user
entry.pack()
Button(root,text="Calculate C and F",command=cf).pack()

#Button(root,text='Clear Screan',command=entry.delete(0, 'end')).pack()

root.mainloop()