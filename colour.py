import sys
from argparse import ArgumentParser
import os.path



class Formatter:
    # \033[38;2;<r>;<g>;<b>m
    # https://tintin.mudhalla.net/info/ansicolor/


    @staticmethod
    def rgbColourToString(r: int, g: int, b:int) -> str:
        return f"\033[38;2;{r};{g};{b}m{Formatter.resetBold()}"

    @staticmethod
    def rgbColourFormat(r: int, g: int, b:int) -> None:
        print(f"\033[38;2;{r};{g};{b}m{Formatter.resetBold()}")

    @staticmethod
    def resetColourToString() -> str:
        return "\033[0m\033[21m"
    
    @staticmethod
    def resetFormat() -> None:
        print("\033[0m\033[21m")

    @staticmethod
    def boldFormat() -> str:
        return "\033[1m"

    @staticmethod
    def resetBold() -> str:
        return "\033[21m"

def is_valid_file(parser, arg):

    minecraftToRGBColours = {
        '\\u00a74' : Formatter.rgbColourToString(170, 0, 0), #dark_red
        '\\u00a7c' : Formatter.rgbColourToString(255, 85, 85), #red
        '\\u00a76' : Formatter.rgbColourToString(255, 170, 0), #gold
        '\\u00a7e' : Formatter.rgbColourToString(255, 255, 85), #yellow
        '\\u00a72' : Formatter.rgbColourToString(0, 170, 0), #dark_green
        '\\u00a7a' : Formatter.rgbColourToString(85, 255, 85), #green
        '\\u00a7b' : Formatter.rgbColourToString(85, 255, 255), #aqua
        '\\u00a73' : Formatter.rgbColourToString(0, 170, 170), #dark_aqua
        '\\u00a71' : Formatter.rgbColourToString(0, 0, 170), #dark_blue
        '\\u00a79' : Formatter.rgbColourToString(85, 85, 255), #blue
        '\\u00a7d' : Formatter.rgbColourToString(255, 85, 255), #light_purple
        '\\u00a75' : Formatter.rgbColourToString(170, 0, 170), #dark_purple
        '\\u00a7f' : Formatter.rgbColourToString(255, 255, 255), #white
        '\\u00a77' : Formatter.rgbColourToString(170, 170, 170), #grey
        '\\u00a78' : Formatter.rgbColourToString(85, 85, 85), #dark_grey
        '\\u00a70' : Formatter.rgbColourToString(0, 0, 0), #black
        '\\u00a7l' : Formatter.boldFormat()
    }
    


    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)

    str_file =  open(arg, 'r')  # return an open file handle
    
    for line in str_file.readlines():
        if (line[0] != "#"): 
            #line = line.replace("§", "SOMETHING")
            line = line.replace("\n", '') # Strip new lines
            #line = line.replace('{', '').replace('}', '')
            for key, value in minecraftToRGBColours.items():
                #print(f"{key}penis{minecraftToRGBColours[key]}something")
                #print(f"key={key}, value={value}")
                line = line.replace(key,  value)
            print(f"{line}{Formatter.resetColourToString()}")

def parse_string(parser, x):
    minecraftToRGBColours = {
        '&4' : Formatter.rgbColourToString(170, 0, 0), #dark_red
        '&c' : Formatter.rgbColourToString(255, 85, 85), #red
        '&6' : Formatter.rgbColourToString(255, 170, 0), #gold
        '&e' : Formatter.rgbColourToString(255, 255, 85), #yellow
        '&2' : Formatter.rgbColourToString(0, 170, 0), #dark_green
        '&a' : Formatter.rgbColourToString(85, 255, 85), #green
        '&b' : Formatter.rgbColourToString(85, 255, 255), #aqua
        '&3' : Formatter.rgbColourToString(0, 170, 170), #dark_aqua
        '&1' : Formatter.rgbColourToString(0, 0, 170), #dark_blue
        '&9' : Formatter.rgbColourToString(85, 85, 255), #blue
        '&d' : Formatter.rgbColourToString(255, 85, 255), #light_purple
        '&5' : Formatter.rgbColourToString(170, 0, 170), #dark_purple
        '&f' : Formatter.rgbColourToString(255, 255, 255), #white
        '&7' : Formatter.rgbColourToString(170, 170, 170), #grey
        '&8' : Formatter.rgbColourToString(85, 85, 85), #dark_grey
        '&0' : Formatter.rgbColourToString(0, 0, 0), #black
        '&l' : Formatter.boldFormat()
    }
    for key, value in minecraftToRGBColours.items():
        #print(f"{key}penis{minecraftToRGBColours[key]}something")
        #print(f"key={key}, value={value}")
        x = x.replace(key,  value)
    print(f"{x}{Formatter.resetColourToString()}")


if __name__ == "__main__":    
    #https://minecrafthowto.com/basics/minecraft-color-codes


    parser = ArgumentParser()
    parser.add_argument("--file", dest="propertiesFile", required=False,
                    help="path to the essentials '.properties' file", metavar="<file>",
                    type=lambda x: is_valid_file(parser, x))
    parser.add_argument("--parse-string", dest="string", required=False,
                    help="A string to parse using normal minecraft '&'", metavar="<string>",
                    type=lambda x: parse_string(parser, x))
    args = parser.parse_args()




