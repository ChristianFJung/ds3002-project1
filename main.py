# -*- coding: utf-8 -*-


"""
list prompt example
"""
from __future__ import print_function, unicode_literals

from pprint import pprint

from PyInquirer import prompt, Separator

from examples import custom_style_2
import pandas as pd
import time
from colors import colors


print("""
Hello thereπ \n 
I'm Lebron Roboto,  an interactive March Maddness data console. 
I can do all sort of things from subset by school to help give you stats on this dataset.

All instructions will always be in ( ). 

Use your arrow keys to get started and shoot your shot! :
π π π π\n
""")

df = pd.read_csv("data/ncaa-mens-historical.csv")

allSchools = list(set(list(df.Winner.values) + list(df.Loser.values)))
allSchools = sorted(allSchools)
aS =[]
for i in allSchools:
    aS.append({"name":i})


def to_tsv(data,filename="out.tsv"):
    data.to_csv("output/"+ filename, index=False, sep="\t")

def to_csv(data,filename="out.csv"):
    data.to_csv("output/"+ filename, index=False)


def to_json(data,filename="out.json"):
    data.to_json("output/"+ filename, orient="table")

# def print_summary(data):



menu = [
    {
        'type': 'list',
        'qmark': "βΉοΈββοΈ",
        'name': 'command',
        'message': 'What do you want to do?',
        'choices': [
            'Print Data',
            'Get Stats',
            'Export Data',
            "Subset Data",
             Separator(),
            'Quit',
            
        ]
    },

]






export_menu = [
    {
        'type': 'list',
        'name': 'format',
        'message': 'What format should we export it in?',
        'choices': [
            'csv','tsv','json',Separator(), "Go Back"
           
            
        ]
    },

    {
        'type': 'input',
        'name': 'fileName',
        'message': 'What\'s should we call the file?',
        'default': lambda e: "out." + e["format"],
        'validate': lambda val: ("." in val)  or 'don\'t forget the file extension',
        'when': lambda e: "Go Back" not in e["format"] 
    },

]


subset_menu = [
    {
        'type': 'checkbox',
        'qmark': 'π',
        'message': 'Select colleges',
        'name': 'colleges',
        'choices': aS,
        'validate': lambda answer: 'You must choose at least one option.' \
            if len(answer) == 0 else True
    },

    {
        'type': 'confirm',
        'name': 'override',
        'message': 'Do you want to have your subset override the orginal dataset? (helpful for exporting and to see stats)',
        # 'when': lambda answers: answers['bacon']
    },

]

while True:
    answers = prompt(menu, style=custom_style_2)

    if answers["command"] == "Print Data":
        print(colors.fg.orange, "\n π¨οΈ  Printing Data  π¨οΈ\n",colors.reset)
        print (df,"\n\n")

    if answers["command"] == "Get Stats":
        print(colors.fg.orange, "\n π  Getting Stats  π \n",colors.reset)

        print (df.describe(),"\n\n")

    if answers["command"] == "Subset Data":
        print(colors.fg.orange, "\n  βοΈ Subsetting Data  βοΈ \n",colors.reset)

        e = prompt(subset_menu)
        sub = df[df.Winner.isin(e["colleges"]) | df.Winner.isin(e["colleges"]) ]

        if e["override"] == True:
            df = sub.copy()

        print(colors.fg.orange, "\n  βοΈSubsetted to include the following:", e["colleges"], "βοΈ \n",colors.reset)
        print(sub,"\n\n") 

    if answers["command"] == "Export Data":
        print(colors.fg.orange, "\n  π€ Exporting Data  π€ \n",colors.reset)

        e = prompt(export_menu)
        # print(e)

        if e["format"] == 'tsv':
            to_tsv(df,e["fileName"])
        elif e["format"] == 'csv':
            to_csv(df,e["fileName"])
        elif e["format"] == 'json':
            to_json(df,e["fileName"])
        if  e["format"] != 'Go Back':
            print("\n Exported", e["fileName"], "to  output folder \n\n")


    if answers["command"] == "Quit":

        print("\n Goodbye  π’  \n\n")
        break;

    
        

    time.sleep(1.5)

    