from tkinter import *
from pytube import YouTube
from tkinter import filedialog
root=Tk()

def submit():
    val=e1.get()
    global yt
    yt = YouTube(val)
    a=yt.title
    b=yt.views
    c=yt.length
    d=yt.rating
    title_value = Label (root,text=a).place(x = 100,y = 150)
    views_value = Label (root,text=str(b)).place(x = 100,y = 200)
    length_value = Label (root,text=str(c)).place(x = 100,y = 250)
    rating_value = Label (root,text=str(d)).place(x = 100,y = 300)
    file_path = filedialog.askdirectory()
    display=Label (root,text="Downloading....").place(x = 100,y = 400)
    ys = yt.streams.get_highest_resolution()
    ys.download(file_path)
    display2=Label (root,text="Downloaded").place(x = 100,y = 450)


root.geometry('700x500')
link = Label (root,text="Enter the link of YouTube video you want to download :  ")
link.place(x = 30,y = 100)
get_e1=StringVar
e1 = Entry(root,width = 50)
e1.place(x =350,y = 100) 
title = Label (root,text="Title : ")
title.place(x = 30,y = 150)
views = Label (root,text="Views : ")
views.place(x = 30,y = 200)
length = Label (root,text="Length : ")
length.place(x = 30,y = 250)
rating = Label (root,text="Rating : ")
rating.place(x = 30,y = 300)
buttonCal = Button(root, text="Download", command=submit).place(x=30,y=350)
root.mainloop()