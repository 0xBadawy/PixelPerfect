import customtkinter

app = customtkinter.CTk()
app.title("CTkSwitch Demo")
app.geometry("500x500")



val=0

def switch_event():
    global val
    if(val % 2==0):
        customtkinter.set_appearance_mode("dark")
        val+=1
    else:
        customtkinter.set_appearance_mode("light")
        val+=1
    print(val)

switch_var = customtkinter.StringVar(value="on")
switch = customtkinter.CTkSwitch(app, text="CTkSwitch", command=switch_event,
    variable=switch_var, onvalue="on", offvalue="off")


switch.grid(row=5, column=2, padx=40, pady=40)


app.mainloop()
