import customtkinter

def button_callback():
    print("button pressed")

app = customtkinter.CTk()


app.title("my app")
app.geometry("1200x800")

# button = customtkinter.CTkButton(app, text="my button", command=button_callback)
# button.grid(row=0, column=2, padx=0, pady=0)

# entry = customtkinter.CTkEntry(app, placeholder_text="CTkEntry", width=140 , height=50 ,font=("Arial", 20))
# entry.grid(row=0, column=4, padx=0, pady=0)


def optionmenu_callback(choice):
    print("optionmenu dropdown clicked:", choice)

optionmenu_var = customtkinter.StringVar(value="option 2")
optionmenu = customtkinter.CTkOptionMenu(app,values=["option 1", "option 2"],
    command=optionmenu_callback,
    variable=optionmenu_var)

progressbar = customtkinter.CTkProgressBar(app, orientation="horizontal" ,)

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

app.mainloop()

