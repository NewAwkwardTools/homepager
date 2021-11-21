#!/usr/bin/python
# Version 1.3 beta
# By WeepingDogel
import os
import argparse
import toml


class Information:
    '''
    This class contains the functions which are used to show 
    something about the program and the helpful information.
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
        print('v 1.3 beta')
        print('By WeepingDogel')

    def GetParser(self):
        '''
        Options
        Here is the place to store the options of the program.
        '''
        parser = argparse.ArgumentParser(
            description="A simple generator of homepage.")
        parser.add_argument(
            '-i', '--input', help='The input txt file.', required=True)
        return parser

    def LoadToml(self, filename):
        fileobj = open(filename)
        config = toml.load(fileobj)
        return config


class Execution:

    def GetCSS(self, config):
        # Before generating the HTML file, we should get the css.
        # And we should know which css style the user want.
        # So add this function to do it.
        if config['Preference']['Blur'] == False:
            if os.path.exists("/usr/share/homepager/styleBlurOFF.css"):
                os.system('cp /usr/share/homepager/styleBlurOFF.css public/style.css')
            else:
                os.system('cp resources/styleBlurOFF.css public/style.css')
            print(' File "styleBlurOFF.css" saved as:' +
              os.getcwd() + '/public/style.css')
        elif config['Preference']['Blur'] == True:
            if os.path.exists("/usr/share/homepager/styleBlurON.css"):
                os.system('cp /usr/share/homepager/styleBlurON.css public/style.css')
            else:
                os.system('cp resources/styleBlurON.css public/style.css')
            print('File "styleBlurON.css" saved as:' + 
            os.getcwd() + '/public/style.css')

    def StepOne(self, txt):
        # The step one, use titlegetter to generate a html file from the txt.
        if os.path.exists('public') == False:
            os.mkdir('public')
        if os.path.exists('temp') == False:
            os.mkdir('temp')
        os.system('titlegetter -b -i ' + txt + ' -f html -o temp/temp.html')

    def StepTwo(self, html, title, bio):
        # Copy the content of the html file, and write into a other html file.
        # Try to make a page.
        if os.path.exists("/usr/share/homepager/index.js"):
            os.system('cp /usr/share/homepager/index.js public/index.js')
        else:
            os.system('cp resources/index.js public/index.js')
        print(' File "index.js" saved as:' + 
                os.getcwd() + '/public/index.js')
        if os.path.exists("/usr/share/homepager/searchbar.html"):
            SearchBar = open('/usr/share/homepager/searchbar.html')
        else:
            SearchBar = open('resources/searchbar.html')
        page = open('public/index.html', 'w')
        links = open('temp/temp.html')
        page.write('<!DOCTYPE html>\n')
        page.write('<html>\n')
        page.write('<head>\n')
        page.write('<meta charset="utf-8"/>\n')
        page.write('<script src="index.js"></script>')
        page.write('<link rel="stylesheet" type="text/css" href=style.css>\n')
        page.write(
            '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
        page.write('<title>' + title + '</title>\n')
        page.write('</head>\n')
        page.write('<body>\n')
        page.write('<div class="top">\n')
        page.write('<h1 class="toptitle">' + title + '</h1>\n')
        page.write('<p>' + bio + '</p>\n')
        page.write('</div>\n')
        page.write(SearchBar.read())
        page.write('<div class="grid-container">\n')
        page.write('<div class="content">')
        page.write('<li>' + links.read() + '</li>')
        page.write('</div>\n')
        page.write('</div>\n')
        page.write('</body>\n')
        page.write('</html>\n')
        page.close()
        print(' File "index.html" saved as:' +
              os.getcwd() + '/public/index.html')
        os.system('rm -rfv temp')


def main():
    '''
The main function, all the things will be begun here.
    '''
    Exe = Execution()
    Info = Information()
    Info.ShowLogo()
    parser = Info.GetParser()
    args = parser.parse_args()
    '''
    if os.path.exists(str(os.getenv('XDG_CONFIG_HOME' + '/homepager/config.toml'))):
        config = Info.LoadToml(
            os.getenv('XDG_CONFIG_HOME' + '/homepager/config.toml'))
    elif os.path.exists('/etc/homepager/config.toml'):
        config = Info.LoadToml('/etc/homepager/config.toml')
    else:
    '''
    config = Info.LoadToml('config/config.toml')
    
    Exe.GetCSS(config)
    Exe.StepOne(args.input)
    Exe.StepTwo('temp/temp.html', config['Main']
                ['TopTitle'], config['Main']['Bio'])


main()
