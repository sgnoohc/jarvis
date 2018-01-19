#!/usr/bin/python
import cgi, cgitb
import os, sys, commands
import json
import commands
import ast
import datetime

def inputToDict(form):
    d = {}
    for k in form.keys():
        # print k, form[k].value
        d[k] = form[k].value
    return d


form = cgi.FieldStorage()

print "Content-type:text/html\r\n"

# inp = {"name": "", "username": "", "page": "Other", "otherPage": ""}
inp = inputToDict(form)

# for some reason, can't use $USER, must do whoami
status, user = commands.getstatusoutput("whoami")

if "data" not in inp:
    sys.exit()

data = inp["data"]
action = inp["action"]
fname = "./note.txt"

if action == "take":

    lines = open(fname, "r").readlines()

    fhin = open(fname, "w")
    fhin.write("-----------------------------------------------\n")
    fhin.write("Date: %s\n"%str(datetime.datetime.now().strftime("%x")))
    fhin.write("Time: %s\n"%str(datetime.datetime.now().strftime("%X")))
    #fhin.write("Location: %s %s\n"%(inp["latitude"], inp["longitude"])
    fhin.write("Message:\n")
    fhin.write("\n")
    fhin.write("%s\n"%str(data))
    fhin.write("\n")
    fhin.write("\n")

    for line in lines:
        fhin.write(line)

#    os.system("gpg --passphrase-fd 3 --always-trust -c --batch note.txt 3<phrase")
#    os.system("rm note.txt")

elif action == "clear":

    fhin = open(fname, "w+")
    fhin.write("")

#    os.system("gpg --passphrase-fd 3 --always-trust -c --batch note.txt 3<phrase")
#    os.system("rm note.txt")

