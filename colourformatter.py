import sys


class ColourFormatter:
    # \033[38;2;<r>;<g>;<b>m
    # https://tintin.mudhalla.net/info/ansicolor/
    #https://minecrafthowto.com/basics/minecraft-color-codes

    @staticmethod
    def rgbColourToString(r: int, g: int, b:int) -> str:
        return f"\033[38;2;{r};{g};{b}m{ColourFormatter.resetBold()}"

    @staticmethod
    def rgbColourFormat(r: int, g: int, b:int) -> None:
        print(f"\033[38;2;{r};{g};{b}m{ColourFormatter.resetBold()}")

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








