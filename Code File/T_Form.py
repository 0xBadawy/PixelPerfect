import customtkinter

app = customtkinter.CTk()
app.title("CTkSwitch Demo")
app.geometry("500x500")


def switch_event():
    print("switch toggled, current value:", switch_var.get())

switch_var = customtkinter.StringVar(value="on")
switch = customtkinter.CTkSwitch(app, text="CTkSwitch", command=switch_event,
    variable=switch_var, onvalue="on", offvalue="off")


switch.grid(row=5, column=2, padx=40, pady=40)


app.mainloop()
