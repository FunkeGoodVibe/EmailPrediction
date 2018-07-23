main_directory = ""

import os

from os import listdir
from os.path import isfile, join

my_text_emails = [f for f in listdir(main_directory) if isfile(join(main_directory, f))]
my_text_emails

dodgy_phrases = ['not to be discussed', 'unfortunately']

for filename in my_text_emails:
    # Read content from file
    file = open(main_directory + '/' + filename)
    # print(filename)
    content = file.read()

    # Remove other character that might get in the way
    content = content.replace('"', '')
    content = content.replace('.', '')

    # Split content into words
    splitcontent = content.split()
  
    # Join  content back together with a single space between words
    joinedcontent = ""
    for word in splitcontent:
        joinedcontent += word.lower() + ' '

    # Check if any dodgy phrase is in the content
    dodgy = False
    for dw in dodgy_phrases:
        if joinedcontent.find(dw) != -1:
            dodgy = True

    if dodgy:
        print(filename)

for my_txt_emails in os.listdir(main_directory):
    content = file.read()
    splitcontent = content.split()

file.close()

