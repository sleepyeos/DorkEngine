#! /usr/bin/env python
# @AUTHOR sleepyeos

# DORKENGINE V0.1

import PySimpleGUI as sg
import webbrowser
import os

class DorkEngine:
    def __init__(self):
        self.dorks = []
        self.load_dorks()
        print('[+]  ' + str(len(self.dorks)) + ' DORKS LOADED\n\n');
        self.init_ui()

    def load_dorks(self):
        files = [f for f in os.listdir('./dorks')]
        print('[!] ' + str(len(files)) + ' files loaded.')
        for current_file in files:
            self.dorks.append('[[[---%s---]]])' % current_file)
            with open('./dorks/' + current_file, 'r') as f:
                lines = [l.strip() for l in f.readlines()]
                self.dorks.extend(lines)

    def init_ui(self):
        sg.ChangeLookAndFeel('DarkPurple4')
        self.layout = [
            [sg.Listbox(
                values=[d for d in self.dorks if d],
                size=(50, 25),
                key='listbox',
            )],
            [sg.Text('Custom: '),
             sg.InputText(key='custom',
                          size=(42,1))],
            [sg.Checkbox('inurl:',
                         key='inurl'),
             sg.Checkbox('intitle:',
                         key='intitle') ,
             sg.Checkbox('quote',
                         key='quote'),
             sg.Checkbox('intext:',
                         key='intext'),
             sg.Checkbox('Customdork',
                         key='customcheck')],
            [sg.Button('Google'),
             sg.Button('Yandex'),
             sg.Button('DDG'),
             sg.Button('Exit')]
        ]
        window = sg.Window('Dork Engine', self.layout)

        while True:
            event, v = window.read()
            if event is None or event == 'Exit':
                break
            else:
                if event in ['Google', 'Yandex', 'DDG']:

                    ## DORK PROCESSING
                    if v['customcheck']:
                        dork = v['custom']
                    else:
                        dork = v['listbox'][0]
                    if v['quote']:
                        dork = '"' + dork + '"'
                    if v['inurl']:
                        dork = 'inurl:' + dork
                    if v['intitle']:
                        dork = 'intitle:' + dork
                    if v['intext']:
                        dork = 'intext:' + dork

                    ## LAUNCH SEARCH
                    if event == 'Google':
                        search = 'google.com/search?q=' + dork
                    elif event == 'Yandex':
                        search = 'https://yandex.com/search/?text=' + dork
                    elif event == 'DDG':
                        search = 'https://duckduckgo.com/?q=' + dork
                    
                    webbrowser.open(search, new=2)

de = DorkEngine()
