import tkinter as tk
from tkinter import ttk
import random 
app=tk.Tk()
app.title("My App")
app.geometry("600x400")

First_Name=["Ahmed","Mohamed","Ali","Khaled","Mahmoud","Hassan","Omar","Othman","Yousef","Yahia"]
Last_Name2=["Ahmed","Mohamed","Ali","Khaled","Mahmoud","Hassan","Omar","Othman","Yousef","Yahia"]


Table = ttk.Treeview(app,
                     columns=("name","age","adderss"),  # to set the columns
                     show="headings"   # to hide the first column
                     )

Table.heading("name",text="Name")
Table.heading("age",text="Age")
Table.heading("adderss",text="Adderss")

# Table.insert(parent="",index=0,iid=0,values=("Ahmed",20,"Egypt"))
# Table.insert(parent="",index=1,iid=1,values=("Mohamed",30,"Egypt"))
# Table.insert(parent="",index=2,iid=2,values=("Ali",40,"Egypt"))
# Table.insert(parent="",index=3,iid=3,values=("Khaled",50,"Egypt"))
# Table.insert(parent="",index=4,iid=4,values=("Mahmoud",60,"Egypt"))
# Table.insert(parent="",index=5,iid=5,values=("Hassan",70,"Egypt"))

for i in range(100):
    firstN = random.choice(First_Name)
    Last_Name = random.choice(Last_Name2)
    Email=f'{firstN},{Last_Name}@gamil.com'
    t=(firstN,Last_Name,Email)
    Table.insert(parent="",index=0,values=t)
    
    
    
def item_select(_):
    print(Table.selection())
    for i in Table.selection():
       print(Table.item(i)['values'])

Table.bind('<<TreeviewSelect>>', item_select)

Table.pack()

app.mainloop()