'URL Shortener with Python'

from tkinter import *
import pyshorteners as ps
import webbrowser

def input_url():
    global short_url
    url = url_entry.get()
    shortener = ps.Shortener()
    short_url = shortener.tinyurl.short(url)
    label_short_url.config(text=short_url)
    label_short_url.bind("<Button-1>", lambda e: [webbrowser.open(short_url), root.destroy()])

root = Tk()
root.title('ÚRL Shortner')
root.geometry('350x150')

url_label = Label(root, text='Enter your URL')
url_label.grid(row=0, column=0, padx= 5, pady= 5)

url_entry = Entry(root, width=30)
url_entry.grid(row=0, column=1, padx= 5, pady= 5)

short_url_label = Label(root, text='Short URL:')
short_url_label.grid(row=2, column=0, padx=5, pady=5)

label_short_url = Label(root, text='', cursor='hand2', fg='blue')
label_short_url.grid(row=2, column=1, padx=5, pady=5)
label_short_url.bind('<Button-1>', lambda e: [webbrowser.open(short_url), root.destroy()])

submit = Button(root, text='Shorten', background='gray', command=input_url)
submit.grid(row=1, columnspan=4, padx=5, pady=5)

root.mainloop()

