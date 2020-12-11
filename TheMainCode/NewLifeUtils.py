# ColorModule
# LoggerModule
# StringUtilModule
# ExceptModule
# CustomShellModule
# UtilsModule
# FileModule
# FilelogModule
# TableBuildModule
# DatabaseManageModule
# RandomModule

name = "NewLifeUtils"
version = "v5.0.0 dev"
description = "Utils for you <3"

try:
    import os
    import datetime
    import re
    import traceback
except ModuleNotFoundError as e:
    print(f'Unable to import dependences: {e}')
    exit(-1)
except Exception as e:
    print(e) 
    exit(-1)

class ColorModule(object):
    def __init__(self):
        os.system('')
    class BGC:
        BLACK = "\x1B[40m"
        RED = "\x1B[41m"
        GREEN = "\x1B[42m"
        YELLOW = "\x1B[43m"
        BLUE = "\x1B[44m"
        PURPLE = "\x1B[45m"
        CYAN = "\x1B[46m"
        BGRAY = "\x1B[47m"
        GRAY = "\x1B[100m"
        BRED = "\x1B[101m"
        BGREEN = "\x1B[102m"
        BYELLOW = "\x1B[103m"
        BBLUE = "\x1B[104m"
        BPURPLE = "\x1B[105m"
        BCYAN = "\x1B[106m"
        WHITE = "\x1B[107m"

    class FGC:
        BLACK = "\x1B[30m"
        RED = "\x1B[31m"
        GREEN = "\x1B[32m"
        YELLOW = "\x1B[33m"
        BLUE = "\x1B[34m"
        PURPLE = "\x1B[35m"
        CYAN = "\x1B[36m"
        BGRAY = "\x1B[37m"
        GRAY = "\x1B[90m"
        BRED = "\x1B[91m"
        BGREEN = "\x1B[92m"
        BYELLOW = "\x1B[93m"
        BBLUE = "\x1B[94m"
        BPURPLE = "\x1B[95m"
        BCYAN = "\x1B[96m"
        WHITE = "\x1B[97m"

    class ACC:
        AFTERCLEAN = "\x1B[K"
        OLDRESET = "\x1B[0m"  
        RESET = "\x1B[0m" + "\x1B[x" + "\x1B[K"
        UNDERLINE = "\x1B[4m"
        SWAP = "\x1B[7m"
        NOTNEGATIVE = "\x1B[27m"
        TOBRIGHT = "\x1B[1m"
        NOBRIGHT = "\x1B[2m"

        def CLEARSCREEN():
            NewLifeUtils.Libs.os.system("cls")
            return ""

        def RANDOMRGB(mode="Color"):
            if mode not in ["Color", "gray"]:
                mode = "Color"
            if mode == "Color":
                r, g, b = (
                    NewLifeUtils.Libs.random.randrange(0, 255),
                    NewLifeUtils.Libs.random.randrange(0, 255),
                    NewLifeUtils.Libs.random.randrange(0, 255),
                )
            else:
                r = NewLifeUtils.Libs.random.randrange(0, 255)
                g = r
                b = r
            return f"\x1B[38;2;{r};{g};{b}m"

        def RANDOMD():
            n = NewLifeUtils.Libs.random.randrange(0, 255)
            return f"\x1B[38;5;{n}m"

        def CUSTOMRGB(r, g, b):
            return f"\x1B[38;2;{r};{g};{b}m"

        def CUSTOMC(n):
            return f"\x1B[38;5;{n}m"

        def BCUSTOMRGB(r, g, b):
            return f"\x1B[48;2;{r};{g};{b}m"

        def BCUSTOMC(n):
            return f"\x1B[48;5;{n}m"

    class MCC:
        def UP(count):
            return f"\x1B[{count}A"

        def DOWN(count):
            return f"\x1B[{count}B"

        def RIGHT(count):
            return f"\x1B[{count}V"

        def LEFT(count):
            return f"\x1B[{count}D"

        def CURSORPOSITION(x, y):
            return f"\x1B[{x};{y}H"

        GOTO_FIRSTLINE = "\x1B[1G"
        GOTO_NEXTLINE = "\x1B[E"
        GOTO_PREVIOUSLINE = "\x1B[F"
        ERASELINE = "\x1B[2K"
        REWRITELINE = "\x1B[1G"

class LoggerModule(object):
    # Init logger
    def __init__(self, Color = None):
        if type(Color) == ColorModule:
            self.Color = Color
        else:
            self.Color = ColorModule()
            
        self.errFormat = "{white}[{time}] {red}{tag}{empty}: {red}{message}{reset}"
        self.logFormat = (
            "{white}[{time}] {green}{tag}{empty}{reset}: {green}{message}{reset}"
        )
        self.wrnFormat = (
            "{white}[{time}] {yellow}{tag}{empty}{reset}: {yellow}{message}{reset}"
        )
        self.reaFormat = "{white}[{time}] {blue}{tag}{empty}{reset}: {blue}{message} {cyan}[{read}]{reset}"
        self.tipFormat = (
            "{white}[{time}] {cyan}{tag}{empty}{reset}: {magenta}{message}{reset}"
        )

        self.errDefaultTag = "Error"
        self.logDefaultTag = "Log"
        self.wrnDefaultTag = "Warn"
        self.reaDefaultTag = "Input"
        self.tipDefaultTag = "Tips"
        self.loggerDateFormat = "%d-%m-%Y"
        self.loggerTimeFormat = "%H:%M:%S"
        self.loggerTagMaxLenght = 8

        self.loggerColorMap = {
            "black": self.Color.ACC.CUSTOMRGB(31, 31, 31),
            "gray": self.Color.ACC.CUSTOMRGB(219, 219, 219),
            "red": self.Color.ACC.CUSTOMRGB(245, 23, 23),
            "green": self.Color.ACC.CUSTOMRGB(13, 209, 39),
            "yellow": self.Color.ACC.CUSTOMRGB(235, 200, 23),
            "blue": self.Color.ACC.CUSTOMRGB(0, 98, 235),
            "magenta": self.Color.ACC.CUSTOMRGB(227, 23, 193),
            "cyan": self.Color.ACC.CUSTOMRGB(24, 212, 222),
            "white": self.Color.ACC.CUSTOMRGB(247, 247, 247),
            "reset": self.Color.ACC.RESET + self.Color.ACC.AFTERCLEAN,
        }
    def formatter(
        self, pattern, message, tag, tag_max, date, time, additional=None
    ):
        if additional is None:
            additional = {"void": ""}

        now = datetime.datetime.now()
        if len(tag) < tag_max:
            empty = " " * (tag_max - len(tag))
        else:
            empty = ""
        return f"{self.Color.ACC.RESET}{self.Color.MCC.REWRITELINE}" + pattern.format(
            **self.loggerColorMap,
            **additional,
            date=now.strftime(date),
            time=now.strftime(time),
            tag=tag,
            empty=empty,
            tab="\t",
            message=message,
        )

    def log(self, message, tag=""):
        if tag == "":
            tag = self.logDefaultTag
        print(
            self.formatter(
                self.logFormat,
                message,
                tag,
                self.loggerTagMaxLenght,
                self.loggerDateFormat,
                self.loggerTimeFormat,
            )
        )

    def wrn(self, message, tag=""):
        if tag == "":
            tag = self.wrnDefaultTag
        print(
            self.formatter(
                self.wrnFormat,
                message,
                tag,
                self.loggerTagMaxLenght,
                self.loggerDateFormat,
                self.loggerTimeFormat,
            )
        )

    def err(self, message, tag=""):
        if tag == "":
            tag = self.errDefaultTag
        print(
            self.formatter(
                self.errFormat,
                message,
                tag,
                self.loggerTagMaxLenght,
                self.loggerDateFormat,
                self.loggerTimeFormat,
            )
        )

    def tip(self, message, tag=""):
        if tag == "":
            tag = self.tipDefaultTag
        print(
            self.formatter(
                self.tipFormat,
                message,
                tag,
                self.loggerTagMaxLenght,
                self.loggerDateFormat,
                self.loggerTimeFormat,
            )
        )

    def rea(self, message, tag=""):
        if message[-1] not in [" ", ">", ":"]:
            message += ": "
        print(
            f"{self.Color_BCUSTOMRGB(0, 43, 112)}{self.Color_CUSTOMRGB(235, 54, 30)}{message}",
            end="",
        )
        read = input()

        if tag == "":
            tag = self.reaDefaultTag
        s = self.formatter(
            self.reaFormat,
            message,
            tag,
            self.loggerTagMaxLenght,
            self.loggerDateFormat,
            self.loggerTimeFormat,
            additional={"read": read},
        )
        print(self.Color_MCC.GOTO_PREVIOUSLINE + s)
        return read

class StringUtilModule(object):
    def __init__(self):
        pass
    def screate(self, string, size=10, insert="r"):
        string = string.encode("unicode_escape").decode()
        matches = re.findall(r"\\x1[bB]\[[\d;]*[a-zA-Z]{1}", string, re.MULTILINE)
        resultCSILength = 0
        for match in matches:
            resultCSILength += len(match)
        spaces = " " * (size - (len(string.encode()) - resultCSILength))
        if insert == "r":
            return str(string.encode().decode("unicode_escape")) + spaces
        if insert == "l":
            return spaces + str(string.encode().decode("unicode_escape"))
    def slice(self, text, chunkSize):
        return [text[i : i + chunkSize] for i in range(0, len(text), chunkSize)]
    def parseArgs(self, readed):
        # [\'][a-zA-ZА-Яа-я\d\s[\]{}()\\\.\":;,-]*[\']|\b[a-zA-Z\d]+
        # [\"\'][a-zA-ZА-Яа-яЁё\d\s[\]{}()@\\\.:;,-]*[\"\']|[a-zA-ZA-ZА-Яа-яЁё\d\.[\]{}()@\\\.:;,-]+
        # [\"][a-zA-ZА-Яа-яЁё\d\s[\]{}()@\\\.:;,\'-]*[\"]|[a-zA-ZA-ZА-Яа-яЁё\d\.[\]{}()@\\\.:;,\'-]+
        # [\"][a-zA-ZА-Яа-яЁё\d\s[\]{}()@\\\.:;,\'-/]*[\"]|[a-zA-ZA-ZА-Яа-яЁё\d\.[\]{}()@\\\.:;,\'-/]+
        # [\"][a-zA-ZА-Яа-яЁё\d\s[\]{}()@#_=%?\*\\\.:;,\'-/]*[\"]|[a-zA-ZA-ZА-Яа-яЁё\d\.[\]{}()@\\\.:;,\'-/]+ (NOW)

        res = re.findall(
            r"[\"][a-zA-ZА-Яа-яЁё\d\s[\]{}()@#_=%?\*\\\.:;,\'-/]*[\"]|[a-zA-ZA-ZА-Яа-яЁё\d\.[\]{}()@\\\.:;,\'-/]+",
            readed,
            re.MULTILINE,
        )
        res2 = []
        for item in res:
            res2.append(re.sub(r"\B'|\b'", "", item))
        res = [x for x in res2 if x != ""]
        if len(res) == 0:
            return {"command": "", "param": []}
        if len(res) == 1:
            return {"command": res[0], "param": []}
        else:
            return {"command": res[0], "param": res[1 : len(res)]}
        return [text[i : i + chunkSize] for i in range(0, len(text), chunkSize)]


class ExceptModule(object):
    def __init__(self, Logger = None, String = None):
        if type(Logger) == LoggerModule:
            self.Logger = Logger
        else:
            self.Logger = LoggerModule()
        if type(String) == StringUtilModule:
            self.String = String
        else:
            self.String = StringUtilModule()
            
    def except_print(self, exception, exceptionType="err", tb=True):
        errorText = "\n-------------- {ExceptionTitle} --------------------\n"
        errorText += f"Type: {type(exception).__name__}\n\n"
        
        if exception.args == 0:
            errorText += f"Unknown error\n"
        else:
            errorText += f"About Error:\n\t{(chr(10)+chr(9)).join(exception.args)}\t\n"

        if tb:
            
            errorText += f"\n{traceback.format_exc()}"

        errorText += "\n-------------- {ExceptionTitle} --------------------\n"

        if exceptionType == "attention":
            self.Logger.log(
                errorText.replace(
                    "{ExceptionTitle}", self.String.screate("Attention!", 20)
                )
            )
        if exceptionType == "wrn":
            self.Logger.wrn(
                errorText.replace(
                    "{ExceptionTitle}", self.String.screate("Warning!", 20)
                )
            )
        elif exceptionType == "err":
            self.Logger.err(
                errorText.replace(
                    "{ExceptionTitle}", self.String.screate("Error!", 20)
                )
            )
        elif exceptionType == "fatal":
            self.Logger.err(
                errorText.replace(
                    "{ExceptionTitle}", self.String.screate("Fatal Error!", 20)
                )
            )
            exit(-1)
        else:
            self.Logger.err(
                errorText.replace(
                    "{ExceptionTitle}",
                    self.String.screate("Something wrong...", 20),
                )
            )

class TableBuildModule(object):
    def __init__(self, String = None, Color = None, default = 'double'):
        if type(Color) == ColorModule:
            self.Color = Color
        else:
            self.Color = ColorModule()
            
        if type(String) == StringUtilModule:
            self.String = String
        else:
            self.String = StringUtilModule()
            
        self.tableManagerOneLine = "┌┬┐│─├┼┤└┴┘"
        self.tableManagerTwoLine = "╔╦╗║═╠╬╣╚╩╝"
        self.tableManagerDoubleH = "╓╥╖║─╟╫╢╙╨╜"
        self.tableManagerDoubleV = "╒╤╕│═╞╪╡╘╧╛"
        
        if default == 'double':
            self.tableManagerCurrent = "╔╦╗║═╠╬╣╚╩╝"
        elif default == 'single':
            self.tableManagerCurrent = "┌┬┐│─├┼┤└┴┘"
        elif default == 'vertical':
            self.tableManagerCurrent = "╓╥╖║─╟╫╢╙╨╜"
        elif default == 'horisontal':
            self.tableManagerCurrent = "╒╤╕│═╞╪╡╘╧╛"
        elif default == 'simple':
            self.tableManagerCurrent = "+++|-++++++"
        else:
            self.tableManagerCurrent = self.tableManagerTwoLine
    def createTable(
        self,
        rowCount,
        sizes,
        data,
        title="TABLE",
        header=True,
        tableElement="",
        color='',
        align="l",
    ):
        if color == '':
            color = self.Color.FGC.CYAN
        color = self.Color.ACC.RESET + color
        if align == "r":
            align = "l"
        else:
            align = "r"
        # ╔  ╦  ╗  ║  ═  ╠  ╬  ╣  ╚  ╩  ╝
        # 0  1  2  3  4  5  6  7  8  9  10

        if tableElement == "":
            tableElement = self.tableManagerCurrent

        result = ""

        # Generate Header-line
        result += f"{color}{tableElement[0]}"

        for sizen in range(rowCount):
            result += f"{color}{tableElement[4]*sizes[sizen]}{color}{tableElement[1]}"
        result = result[:-1] + f"{color}{tableElement[2]}"

        # Generate Header
        if header:
            result += f"\n{color}{tableElement[3]}"
            for num in range(rowCount):
                result += f"{self.String.screate(data[num], sizes[num], align)}{color}{tableElement[3]}"
            result += f"\n{color}{tableElement[5]}"
            for headerPieceSize in sizes:
                result += (
                    f"{color}{tableElement[4]*headerPieceSize}{color}{tableElement[6]}"
                )
            result = result[:-1] + f"{color}{tableElement[7]}"
            data = data[rowCount:]

        # Generate DataSection
        for lineNum in range(0, len(data), rowCount):
            result += f"\n{color}{tableElement[3]}"
            for rowShift in range(0, rowCount):
                try:
                    result += f"{self.String.screate(data[lineNum+rowShift], sizes[rowShift], align)}{color}{tableElement[3]}"
                except:
                    result += f'{self.String.screate("", sizes[rowShift], align)}{color}{tableElement[3]}'
        result += f"\n{color}{tableElement[8]}"

        # Generate Footer-line
        for sizen in range(rowCount):
            result += f"{color}{tableElement[4]*sizes[sizen]}{color}{tableElement[9]}"
        result = result[:-1] + f"{color}{tableElement[10]}{self.Color.ACC.RESET}"

        return f'\n{self.String.screate(title, round(sum(sizes)/2), "l")}\n{result}\n'

    def createMultilineTable(
        self,
        rowCount,
        sizes,
        data,
        title="TABLE",
        tableElement="",
        color='',
        align="l",
    ):
        if color == '':
            color = self.Color.FGC.CYAN
        if align == "r":
            align = "l"
        else:
            align = "r"
        # ╔  ╦  ╗  ║  ═  ╠  ╬  ╣  ╚  ╩  ╝
        # 0  1  2  3  4  5  6  7  8  9  10
        # +  +  +  |  -  +  +  +  +  +  +
        # 0  1  2  3  4  5  6  7  8  9  10; , tableElement = '+++|-++++++'
        if tableElement == "":
            tableElement = self.tableManagerCurrent
        for i in range(len(data)):
            data[i] = self.stringManagerSlice(data[i], sizes[i % len(sizes)])
        result = ""
        for line in range(0, len(data), rowCount):
            maxtabsize = 0
            for row in range(0, rowCount):
                if len(data[line + row]) > maxtabsize:
                    maxtabsize = len(data[line + row])
            for row in range(0, rowCount):
                if len(data[line + row]) < maxtabsize:
                    while len(data[line + row]) < maxtabsize:
                        data[line + row].append("")

        # Generate Header-line
        result += f"{color}{tableElement[0]}"
        for headerPieceSize in sizes:
            result += (
                f"{color}{tableElement[4]*headerPieceSize}{color}{tableElement[1]}"
            )
        result = result[:-1] + f"{color}{tableElement[2]}\n"

        # Generate DataSection
        for line in range(0, len(data), rowCount):
            block = []
            for row in range(0, rowCount):
                for blockLineNum in range(len(data[line + row])):

                    try:
                        block[
                            blockLineNum
                        ] += f"{tableElement[3]}{self.String.screate(data[line+row][blockLineNum],sizes[row], align)}"
                    except:
                        block.append(
                            f"{tableElement[3]}{self.String.screate(data[line+row][blockLineNum],sizes[row], align)}"
                        )
            for blockLineNum in range(len(data[line + row])):
                block[blockLineNum] += tableElement[3]
            for line in block:
                result += f"{line}\n"

            result += f"{tableElement[5]}"
            for headerPieceSize in sizes:
                result += f"{tableElement[4]*headerPieceSize}{tableElement[6]}"
            result = result[:-1] + f"{tableElement[7]}\n"

        # Generate Footer-line
        result = result[: -1 * (4 + sum(sizes))] + tableElement[8]
        for headerPieceSize in sizes:
            result += f"{tableElement[4]*headerPieceSize}{tableElement[9]}"
        result = result[:-1] + f"{tableElement[10]}{self.Color.ACC.RESET}"

        return f'\n{self.String.screate(title+" IN DEV", round(sum(sizes)/2), "l")}\n{result}\n'

        
if __name__ == "__main__":
    print('succeful start')
    c = ColorModule()
    l = LoggerModule(c)
    s = StringUtilModule()
    e = ExceptModule(l, s)
    t = TableBuildModule(s, c)
    table = t.createTable(2,[30,60],['Some number','Some text','1',f'{c.FGC.YELLOW}colorful','355214364351',f'{c.BGC.BLUE}more colorful'],header = True)
    print(table)
    print("\x1B[1;1x")#for test
    e.except_print(Exception('oh no'),'wrn',False)
    l.log(f"This is a log")
    l.log(f"This is a log with custom tag", "MyTag1")
    l.tip(f"This is a tip")
    l.tip(f"This is a tip with custom tag", "MyTag2")
    l.wrn(f"This is a warn")
    l.wrn(f"This is a warn with custom tag", "MyTag3")
    l.err(f"This is a error")
    l.err(f"This is a error with custom tag", "MyTag4")
    print('succeful end')
    