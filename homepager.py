#!/usr/bin/python
# Version 1.0 beta
# By WeepingDogel
import os
import argparse
import toml

class Information:
    '''
    This class contains the functions which are used to show 
    something about the program and the helpful informations.
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
        print('By WeepingDogel')
    def GetParser(self):
        '''
        Options
        Here is the place to store the options of the program.
        '''
        parser = argparse.ArgumentParser(description="A simple generator of homepage.")
        parser.add_argument('-i','--input', help='The input txt file.',required=True)
        return parser
    def LoadToml(self,filename):
        fileobj = open(filename)
        config = toml.load(fileobj)
        return config
class Execution:
    def StepOne(self, txt):
        # The step one, use titlegetter generate a html file from the txt.
        if os.path.exists('public') == False:
            os.system('mkdir public')
        if os.path.exists('temp') == False:
            os.system('mkdir temp')
        os.system('titlegetter -b -i '+ txt + ' -f html -o temp/temp.html')
    def StepTwo(self,html,title,bio):
        # Copy the content of the html file, and write into a other html file.
        # Try to make a page.
        os.system('cp resources/style.css public/style.css')
        page = open('public/index.html','w')
        links = open('temp/temp.html')
        page.write('<!DOCTYPE html>\n')
        page.write('<html>\n')
        page.write('<head>\n')
        page.write('<meta charset="utf-8"/>\n')
        page.write('<link rel="stylesheet" type="text/css" href="style.css">\n')
        page.write('<meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
        page.write('<title>' + title + '</title>\n')
        page.write('</head>\n')
        page.write('<body>\n')
        page.write('<div class="top">\n')
        page.write('<h1 class="toptitle">' + title + '</h1>\n')
        page.write('</div>\n')
        page.write('<div class="menu">\n')
        page.write('<p>' + bio + '</p>\n')
        page.write('</div>\n')
        page.write('<div class="grid-container">\n')
        page.write('<div class="content">')
        page.write('<li>' + links.read() + '</li>')
        page.write('</div>\n')
        page.write('</div>\n')
        page.write('</body>\n')
        page.write('</html>\n')
def main():
    '''
The main function, all the things will be begun here.
    '''
    Exe = Execution()
    Info = Information()
    Info.ShowLogo()
    parser = Info.GetParser()
    args = parser.parse_args()
    config = Info.LoadToml('config/config.toml')
    Exe.StepOne(args.input)
    Exe.StepTwo('temp/temp.html',config['Main']['TopTitle'],config['Main']['Bio'])
main()