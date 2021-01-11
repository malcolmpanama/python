# -*- coding: utf-8 -*-
#! python3

#Automate the Boring Stuff with Python - Chapter 8 Practice Project - Mad Libs

#madlibs.py - A program to let users set their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file.

import re

mad_libs = open("C:\\Users\\b_jim\\OneDrive\\Escritorio\\MADLIBS.txt", "w")
mad_libs.write('''The ADJECTIVE panda walked to the NOUN and then VERB.
A nearby NOUN was unaffected by these events.''')
mad_libs.close()

mad_libs = open("C:\\Users\\b_jim\\OneDrive\\Escritorio\\MADLIBS.txt")
content = mad_libs.read()
mad_libs.close()
check = re.compile(r'ADJECTIVE|NOUN|VERB|ADVERB')

while True:
    result = check.search(content)
    if result == None:
        break
    elif result.group() == "ADJECTIVE" or result.group() == "ADVERB":
        print("Enter an %s:" % (result.group().lower()))
    elif result.group() == "NOUN" or result.group() == "VERB":
        print("Enter a %s:" % (result.group().lower()))
    i = input()
    content = check.sub(i, content, 1)
    
print(content)
print("Name your file:")
name = input()
new_file = open(".\\%s.txt" % (name), "w")
new_file.write(content)
new_file.close()
