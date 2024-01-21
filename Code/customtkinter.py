import customtkinter
from tkinter import filedialog

def button_callback():
    folder_path = filedialog.askdirectory(title="Select a folder")
    if folder_path:
        print("Selected folder:", folder_path)
    else:
        print("No folder selected")
    


app = customtkinter.CTk()


app.title("my app")
app.geometry("1200x800")

button = customtkinter.CTkButton(app, text="my button", command=button_callback)
button.grid(row=0, column=2, padx=0, pady=0)

# entry = customtkinter.CTkEntry(app, placeholder_text="CTkEntry", width=140 , height=50 ,font=("Arial", 20))
# entry.grid(row=0, column=4, padx=0, pady=0)


def optionmenu_callback(choice):
    print("optionmenu dropdown clicked:", choice)

optionmenu_var = customtkinter.StringVar(value="option 2")
optionmenu = customtkinter.CTkOptionMenu(app,values=["option 1", "option 2"],
    command=optionmenu_callback,
    variable=optionmenu_var)

progressbar = customtkinter.CTkProgressBar(app, orientation="horizontal" ,)

V=2
def slider_event(value):
    print(value)

slider = customtkinter.CTkSlider(app, from_=0, to=100, command=slider_event)



def switch_event():
    print("switch toggled, current value:", switch_var.get())

switch_var = customtkinter.StringVar(value="on")
switch = customtkinter.CTkSwitch(app, text="CTkSwitch", command=switch_event,
    variable=switch_var, onvalue="on", offvalue="off")




switch.grid(row=5, column=2, padx=40, pady=40)

slider.grid(row=12, column=2, padx=40, pady=40)

Value_1 = 9
rr=40
def segmented_button_callback(value):
    
    #global Value_1
    global rr
    rr+=1
    print("segmented button clicked:", value)
    label = customtkinter.CTkLabel(app, text=value, fg_color="transparent")
    label.grid(row=16, column=2, padx=rr, pady=40)

    


segemented_button_var = customtkinter.StringVar(value="Value 1")
segemented_button = customtkinter.CTkSegmentedButton(app, values=["Value 1","Value 8", "Value 2", "Value 3"],
    command=segmented_button_callback,
    variable=segemented_button_var)


segemented_button.grid(row=13, column=2, padx=40, pady=40)



app.mainloop()

