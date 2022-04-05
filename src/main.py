from argparse import ArgumentParser
from essentialslangparser import EssentialsLanguageParser
from stringformatter import StringFormatter


if __name__ == "__main__":    
    parser = ArgumentParser()
    parser.add_argument("--file", dest="propertiesFile", required=False,
                    help="path to the essentials '.properties' file", metavar="<file>",
                    type=lambda x: EssentialsLanguageParser(parser, x))
    parser.add_argument("--parse-string", dest="string", required=False,
                    help="A string to parse using normal minecraft '&'", metavar="<string>",
                    type=lambda x: StringFormatter(parser, x))
    args = parser.parse_args()