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
            'csv','tsv','json'
           
            
        ]
    },

]


subset_menu = [
    {
        'type': 'checkbox',
        'qmark': '😃',
        'message': 'Select toppings',
        'name': 'colleges',
        'choices': aS,
        'validate': lambda answer: 'You must choose at least one topping.' \
            if len(answer) == 0 else True
    }
]

while True:
    answers = prompt(menu, style=custom_style_2)

    if answers["command"] == "Print Data":
        pprint (df)

    if answers["command"] == "Get Stats":
        pprint (df.describe())

    if answers["command"] == "Subset Data":
        e = prompt(subset_menu)
        sub = df[df.Winner.isin(e["colleges"]) | df.Winner.isin(e["colleges"]) ]
        print(sub) 
        print(e)
    
    if answers["command"] == "Export Data":
        e = prompt(export_menu)
        print(e)

        if e["format"] == 'tsv':
            to_tsv(df)
        elif e["format"] == 'csv':
            to_csv(df)
        elif e["format"] == 'json':
            to_json(df)

        print("exported as",e["format"], "in output folder")


    if answers["command"] == "Quit":
        break;

    
        

    time.sleep(3)

    