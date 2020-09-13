import requests

import json

from requests.models import Response
from tkinter import *
from tkinter.messagebox import showinfo,showerror


def send_sms(numbers,message):
    url = 'https://www.fast2sms.com/dev/bulk'
    params= {
        'authorization':'XRmHudjY0k9KTMBvyWwc5PGxIC2rVzOqniU7bJ6p1s3AhS8eagHYbT0hMf9rNL1yP26gmCZqcBxJuv4z',
        'sender_id':'FSTSMS',
        'message':message,
        'language':'english',
        'route':'p',
        'numbers':numbers



    }
    response =requests.get(url, params=params)
    dict= response.json()
    print(dict)
    return dict.get('return')



def button_click():
    num=textNumber.get()
    msg=textMessage.get("1.0",END)
    r=send_sms(num,msg)
    if r ==True:
        showinfo("Send Success","Successfully sent :)")
    else:
        showerror("Error","Oops!Something went wrong :(")


# send_sms("8660964842","hi idiot")
#creating GUI
root=Tk()
root.title("Message Sender ")
root.geometry("400x550")
font=("Helvetica",22,"bold")

textNumber=Entry(root,font=font)
textNumber.pack(fill=X,pady=20)

textMessage=Text(root)
textMessage.pack(fill=X,pady=10)

sendButton=Button(root,text="SEND MESSAGE",command=button_click)
sendButton.pack()



root.mainloop()