import tkinter as tk
from tkinter import messagebox as msgbox

def welcomeMessage (price):
    #create a tkinter root window
    window = tk.Toplevel(root)
    window.title("Simi Services")
    window.geometry("500x200")

    label_1= tk.Label(window, text= f"The price is 3500")
    label_1.pack()
    label_2 = tk.Label(window, text="U may now proceed to pay")
    label_2.pack()

    #Run tkinter event loop
    root.mainloop()

def welcomeMessage2 (price):
    #create a tkinter root window
    window = tk.Toplevel(root)
    window.title("Simi Services")
    window.geometry("500x200")

    label_3= tk.Label(window, text= f"The price is 10000")
    label_3.pack()
    label_4 = tk.Label(window, text="U may now proceed to pay")
    label_4.pack()

    #Run tkinter event loop
    root.mainloop()

def welcomeMessage3 (price):
    #create a tkinter root window
    window = tk.Toplevel(root)
    window.title("Simi Services")
    window.geometry("500x200")

    label_1= tk.Label(window, text= f"The price is 5000")
    label_1.pack()
    label_2 = tk.Label(window, text="U may now proceed to pay")
    label_2.pack()

    #Run tkinter event loop
    root.mainloop()

def submit():    
    location = location_entry.get()
    weight = int(weight_entry.get())

    if location == "Lekki" and weight >= 10:
        welcomeMessage(location)
    elif location == "Epe" and weight >= 10:
        welcomeMessage2(location)
    elif location == "Epe" and weight < 10:
        welcomeMessage3(location)
    else:
        msgbox.showerror("Price Checker", "Not yet delivering in your region :)")

#Create main window
root=tk.Tk()
root.title("Price Checker")
root.geometry("500x200")


#Create username label and entry
location_label= tk.Label(root, text ="Location:")
location_label.pack()
location_entry = tk.Entry(root)
location_entry.pack()

#Create password label and entry
weight_label= tk.Label(root, text = "Weight: ")
weight_label.pack()
weight_entry= tk.Entry(root)
weight_entry.pack()

#Create submit button
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack()

#stying the button
submit_button.config(fg="blue", bg= "white")

#Run the main event loop
root.mainloop()