import sys
import requests as r

try:
    if sys.argv[1] == "pass":
        p = r.get("http://oo-ozo.000webhostapp.com/pass2.txt")
        print(p.text)
    elif sys.argv[1] == "google":
        p = r.get("https://oo-ozo.000webhostapp.com/google.txt")
        print(p.text)
    elif sys.argv[1] == "ip":
        p = r.get("http://oo-ozo.000webhostapp.com/pass.txt")
        print(p.text)
except:
    print("wrong argv")
