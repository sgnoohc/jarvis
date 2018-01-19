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

# inp = {"name": "", "username": "", "page": "Other", "otherPage": ""}
inp = inputToDict(form)

# for some reason, can't use $USER, must do whoami
status, user = commands.getstatusoutput("whoami")

f = open("jarvis.js")
lines = f.readlines()
inblock = False
o = open("help.txt", "w")
for line in lines:
    if inblock:
        if line.strip() == "{":
            continue
        if line.strip() == "}":
            inblock = False
            continue
        o.write(line.strip().split("'")[1] + "\n")
    if line.find("var commands") != -1:
        inblock = True
f.close()
o.close()
print "Content-type:text/html\r\n"
print "Done"
