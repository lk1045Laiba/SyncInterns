from tkinter import *
from twilio.rest import Client
import random
from tkinter import messagebox

class otp_verifier(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1000x580+200+80")
        self.configure(bg="#FFFFFF")
        self.resizable(False, False)
        self.n = str(self.generate_otp())
        self.client = Client("ACf2dbec3b9c97c80459ed764498d8c648", "cfdbe9c047c93ef13bc52821064bfeea")
        self.client.messages.create(to=("+01234567888"),
                                    from_="+1361566788",
                                    body=self.n
                                    )
        self.Labels()
        self.Entry()
        self.Buttons()

    def generate_otp(self):
        return random.randrange(1000, 10000)

    def Labels(self):
        self.c = Canvas(self, bg="#468284", width=400, height=280)   #hexa for grey
        self.c.place(x=290, y=120)

        self.upper_frame = Frame(self, bg="#468284", width=1500, height=130)  #hexa for blue
        self.upper_frame.place(x=0, y=0)

        self.picture = PhotoImage(file="otp.png")
        self.k = Label(self.upper_frame, image=self.picture, bg="red")
        self.k.place(x=80, y=35)

        self.j = Label(self.upper_frame, text="Verify OTP", font="TimesNewRoman 38 bold", bg="#FFFFFF", fg="black")
        self.j.place(x=370, y=35)

    def Entry(self):
        self.User_Name = Text(self, font="calibri 20", borderwidth=2, wrap=WORD, width=23, height=1)
        self.User_Name.place(x=330, y=200)

    def Buttons(self):
        self.submitButtonImage = PhotoImage(file="submit.png")
        self.submitButton = Button(self, image=self.submitButtonImage, command=self.checkOTP, border=0)
        self.submitButton.place(x=540, y=290)

        self.respondOTPImage = PhotoImage(file="resend.jpg")
        self.resendOTP = Button(self, image=self.respondOTPImage, command=self.resendOTP, border=0)
        self.resendOTP.place(x=290, y=290)

    def resendOTP(self):
        self.n = str(self.generate_otp())
        self.client = Client("ACab0224b6a24f1a7c9452fc574090a2ee", "bd01e2450e4d8f96a873de70754e2172")
        self.client.messages.create(to=("+923314727027"),
                                    from_="+15154173086",
                                    body=self.n
                                    )

    def checkOTP(self):
        self.userInput = int(self.User_Name.get(1.0, "end-1c"))
        try:
            if self.userInput == int(self.n):
                messagebox.showinfo("showinfo", "Verification Successful")
                self.n = "done"
            else:
                messagebox.showinfo("showinfo", "Wrong OTP")
        except:
            messagebox.showinfo("showinfo", "INVALID OTP")


if __name__ == "__main__":
    window = otp_verifier()
    window.mainloop()

