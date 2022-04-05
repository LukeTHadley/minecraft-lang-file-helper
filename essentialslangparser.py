from colourformatter import ColourFormatter
import os.path

class EssentialsLanguageParser:

    def __init__(self, parser, arg):


        minecraftToRGBColours = {
            '\\u00a74' : ColourFormatter.rgbColourToString(170, 0, 0), #dark_red
            '\\u00a7c' : ColourFormatter.rgbColourToString(255, 85, 85), #red
            '\\u00a76' : ColourFormatter.rgbColourToString(255, 170, 0), #gold
            '\\u00a7e' : ColourFormatter.rgbColourToString(255, 255, 85), #yellow
            '\\u00a72' : ColourFormatter.rgbColourToString(0, 170, 0), #dark_green
            '\\u00a7a' : ColourFormatter.rgbColourToString(85, 255, 85), #green
            '\\u00a7b' : ColourFormatter.rgbColourToString(85, 255, 255), #aqua
            '\\u00a73' : ColourFormatter.rgbColourToString(0, 170, 170), #dark_aqua
            '\\u00a71' : ColourFormatter.rgbColourToString(0, 0, 170), #dark_blue
            '\\u00a79' : ColourFormatter.rgbColourToString(85, 85, 255), #blue
            '\\u00a7d' : ColourFormatter.rgbColourToString(255, 85, 255), #light_purple
            '\\u00a75' : ColourFormatter.rgbColourToString(170, 0, 170), #dark_purple
            '\\u00a7f' : ColourFormatter.rgbColourToString(255, 255, 255), #white
            '\\u00a77' : ColourFormatter.rgbColourToString(170, 170, 170), #grey
            '\\u00a78' : ColourFormatter.rgbColourToString(85, 85, 85), #dark_grey
            '\\u00a70' : ColourFormatter.rgbColourToString(0, 0, 0), #black
            '\\u00a7l' : ColourFormatter.boldFormat()
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
                print(f"{line}{ColourFormatter.resetColourToString()}")

