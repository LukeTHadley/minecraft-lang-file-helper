from colourformatter import ColourFormatter

class StringFormatter:

    def __init__(self, parser, x):

        minecraftToRGBColours = {
            '&4' : ColourFormatter.rgbColourToString(170, 0, 0), #dark_red
            '&c' : ColourFormatter.rgbColourToString(255, 85, 85), #red
            '&6' : ColourFormatter.rgbColourToString(255, 170, 0), #gold
            '&e' : ColourFormatter.rgbColourToString(255, 255, 85), #yellow
            '&2' : ColourFormatter.rgbColourToString(0, 170, 0), #dark_green
            '&a' : ColourFormatter.rgbColourToString(85, 255, 85), #green
            '&b' : ColourFormatter.rgbColourToString(85, 255, 255), #aqua
            '&3' : ColourFormatter.rgbColourToString(0, 170, 170), #dark_aqua
            '&1' : ColourFormatter.rgbColourToString(0, 0, 170), #dark_blue
            '&9' : ColourFormatter.rgbColourToString(85, 85, 255), #blue
            '&d' : ColourFormatter.rgbColourToString(255, 85, 255), #light_purple
            '&5' : ColourFormatter.rgbColourToString(170, 0, 170), #dark_purple
            '&f' : ColourFormatter.rgbColourToString(255, 255, 255), #white
            '&7' : ColourFormatter.rgbColourToString(170, 170, 170), #grey
            '&8' : ColourFormatter.rgbColourToString(85, 85, 85), #dark_grey
            '&0' : ColourFormatter.rgbColourToString(0, 0, 0), #black
            '&l' : ColourFormatter.boldFormat()
        }
        for key, value in minecraftToRGBColours.items():
            #print(f"{key}penis{minecraftToRGBColours[key]}something")
            #print(f"key={key}, value={value}")
            x = x.replace(key,  value)
        print(f"{x}{ColourFormatter.resetColourToString()}")
