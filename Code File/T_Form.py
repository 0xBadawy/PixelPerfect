import customtkinter

# =================== window setup ===================
customtkinter.set_appearance_mode("dark") # "dark" or "light"
app = customtkinter.CTk()
app.title("CTkSwitch Demo")
app.geometry("1600x800")


def button_callback():
    print(checkbox_1.get())


# =================== main ===================

checkbox_1 = customtkinter.CTkCheckBox(app, text="checkbox 1"  ,command=button_callback)
print(checkbox_1.get())
checkbox_1.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="w")

app.mainloop()
