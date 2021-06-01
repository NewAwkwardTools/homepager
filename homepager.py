#!/usr/bin/python
# Version 1.0 beta
# By WeepingDogel
import os
import argparse
import toml

class Infomation:
    '''
    This class contains the functions which are used to show 
    something about the program and the helpful infomations.
    '''
    def ShowLogo(self):
        print('''
╔╗─╔╗────────╔═══╗
║║─║║────────║╔═╗║
║╚═╝╠══╦╗╔╦══╣╚═╝╠══╦══╦══╦═╗
║╔═╗║╔╗║╚╝║║═╣╔══╣╔╗║╔╗║║═╣╔╝
║║─║║╚╝║║║║║═╣║──║╔╗║╚╝║║═╣║
╚╝─╚╩══╩╩╩╩══╩╝──╚╝╚╩═╗╠══╩╝
────────────────────╔═╝║
────────────────────╚══╝
        ''')
        print('v 1.0 beta')
        print('''
        By WeepingDogel
        ''')
    def GetParser(self):
        '''
        Options

        Here is the place to store the options of the program.
        '''
        parser = argparse.ArgumentParser(description="A simple generator of homepage")
        parser.add_argument('-a', action='store_true')
        return parser
def main():
    '''
The main function, all the things will be begun here.
    '''
    Info = Infomation()
    Info.ShowLogo()
    parser = Info.GetParser()
    args = parser.parse_args()
    if args.a == True:
        print('success!')
main()