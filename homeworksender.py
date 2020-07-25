import smtplib
import os
from email.message import EmailMessage
import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()

root.title('EmailSender')
canvas = tk.Canvas(root, height=700, width=700, bg='#263D42')
canvas.pack()

frame = tk.Frame(root, bg="deep sky blue")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

name = tk.Label(root, text="Homework Sender", font=('Herculanum', 30))
name.pack()

# opens background picture
my_image = ImageTk.PhotoImage(Image.open('./bgpic.jpg').resize((600, 600)))
background_label = tk.Label(frame, image=my_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


# gets called by openFile button
def open_file():
    os.system('open email_list.txt')


# gets called by addMail button
def add():
    if email.get() == "":
        error_label = tk.Label(
            frame, text="Please Enter a Text", bg="deep sky blue")
        error_label.pack()
    else:
        with open('./email_list.txt', mode='a') as my_file:
            my_file.write(f'\n{email.get()}')
        label = tk.Label(
            frame, text=f"Successfully Added '{email.get()}'' to Email List", bg="deep sky blue")
        label.pack()
        email.delete(0, 'end')


# gets called by sendMail button
def send():
    try:
        with open('./email_list.txt', mode='r') as email_list_file:
            for line in email_list_file:
                email = EmailMessage()
                email['Subject'] = 'Homework'
                email['From'] = account
                email['to'] = line
                email.set_content(homework.get())

                with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
                    smtp.ehlo()
                    smtp.starttls()
                    smtp.ehlo()
                    smtp.login(account, password)
                    smtp.send_message(email)
                    print(f'sending email to {line}...')
                    lable1 = tk.Label(
                        frame, text=f"Sending Email to {line}...")
                    lable1.pack()

        label2 = tk.Label(frame, text="All Done!", bg="deep sky blue")
        label2.pack()
        homework.delete(0, 'end')
    except:
        error_label = tk.Label(
            frame, text="Error Occurred", bg="deep sky blue")
        error_label.pack()
        homework.delete(0, 'end')


# declare a global variable that both login and add_cred functions can use
user_email = None
user_pw = None


def login():
    global user_email
    global user_pw
    user_email = tk.Entry(frame, width=20, font=('Helvetica', 20))
    user_email.pack(padx=10, pady=0)

    user_pw = tk.Entry(frame, width=20, font=('Helvetica', 20))
    user_pw.pack(padx=10, pady=0)

    confirm = tk.Button(
        frame, text="Confirm Account", padx=10, pady=5, bg="#263D42", command=add_cred)
    confirm.pack()


# writes credentials
def add_cred():
    global user_email
    global user_pw
    with open('./user_file.txt', mode='w') as file:
        file.write(f'{user_email.get()} {user_pw.get()}')
    label = tk.Label(frame, text='Logged in. Please restart',
                     bg='deep sky blue')
    label.pack()
    user_email.delete(0, 'end')
    user_pw.delete(0, 'end')


email = tk.Entry(frame, width=30, font=('Helvetica', 25))
email.pack(padx=10, pady=10)

addMail = tk.Button(frame, text="Add Email", padx=10,
                    pady=5, bg='#263D42', command=add)
addMail.pack()

homework = tk.Entry(frame, width=30, font=('Helvetica', 25))
homework.pack(padx=10, pady=10, ipady=20)

sendMail = tk.Button(frame, text="Send Homework",
                     padx=10, pady=5, bg="#263D42", command=send)
sendMail.pack(pady=10)

openFile = tk.Button(frame, text="Change Email List",
                     padx=10, pady=5, bg="#263D42", command=open_file)
openFile.pack(side='bottom')

changeAccount = tk.Button(frame, text="Change Account",
                          padx=10, pady=5, bg='#263D42', command=login)
changeAccount.pack(side='bottom')


with open('./user_file.txt', mode='r') as file:
    text = file.readline()
    if len(text.split()) == 2:  # proper account and password pair
        account = text.split()[0]
        password = text.split()[1]
        user_label = tk.Label(frame, text=account, bg="#49A")
        user_label.pack(side='bottom')

    elif text == '':
        Login = tk.Button(frame, text="Login", padx=15,
                          pady=10, bg="#263D42", command=login)
        Login.pack(side='bottom')
        sendMail.destroy()  # unable to send email if there isn't user email
        changeAccount.destroy()  # cannot change account if there isn't one

    else:
        login_error_label = tk.Label(
            frame, text='Unknown Error While Logging in', bg='deep sky blue')
        login_error_label.pack()
        sendMail.destroy()  # unable to send email if there is an error


if __name__ == "__main__":
    root.mainloop()
