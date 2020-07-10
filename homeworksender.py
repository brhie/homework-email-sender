import smtplib
from email.message import EmailMessage
from pathlib import Path
import tkinter as tk
from PIL import Image, ImageTk
import os


root = tk.Tk()

root.title('EmailSender')
canvas = tk.Canvas(root, height=700, width=700, bg='#263D42')
canvas.pack()

frame = tk.Frame(root, bg="deep sky blue")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

name = tk.Label(root, text="Homework Sender", font=('Herculanum', 30))
name.pack()

my_image = ImageTk.PhotoImage(Image.open('./bgpic.jpeg').resize((600, 600)))
background_label = tk.Label(frame, image=my_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)



def open_file():
    os.system('open email_list.txt')


def add():
    if email.get() == "":
        error_label = tk.Label(
            frame, text="Please Enter a Text", bg="deep sky blue")
        error_label.pack()
    else:
        with open('./email_list.txt', mode='a') as file:
            file.write(f'\n{email.get()}')
        label = tk.Label(
            frame, text=f"Successfully Added '{email.get()}'' to Database", bg="deep sky blue")
        label.pack()
        email.delete(0, 'end')


def send():
    try:
        with open('./email_list.txt', mode='r') as file:
            for line in file:
                email = EmailMessage()
                email['Subject'] = 'Homework'
                email['From'] = f'{email}'
                email['to'] = line
                email.set_content(homework.get())

                with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
                    smtp.ehlo()
                    smtp.starttls()
                    smtp.login(email, password)
                    smtp.send_message(email)
                    print(f'sending email to {line}...')
                    lable1 = tk.Label(frame, text=f"Sending Email to {line}...")
                    lable1.pack()

        label2 = tk.Label(frame, text="All Done!")
        label2.pack()
        homework.delete(0, 'end')
    except:
        error_label = tk.Label(frame, text="Error Occurred", bg="deep sky blue")
        error_label.pack()
        homework.delete(0, 'end')


def login():
    pass

email = tk.Entry(frame, width=30, font=('Helvetica', 25))
email.pack(padx=10, pady=10)

addMail = tk.Button(frame, text="Add Email", padx=10,
                    pady=5, bg='#263D42', command=add)
addMail.pack()

homework = tk.Entry(frame, width=30, font=('Helvetica', 25))
homework.pack(padx=10, pady=10, ipady=30)

sendMail = tk.Button(frame, text="Send Homework",
                     padx=10, pady=5, bg="#263D42", command=send)
sendMail.pack(pady=10)

openFile = tk.Button(frame, text="Modify the Database File", padx=10, pady=5, bg="#263D42", command=open_file)
openFile.pack(side='bottom')





root.mainloop()
