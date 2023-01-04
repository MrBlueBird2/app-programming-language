import string

numl = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
alphal = string.ascii_lowercase
alphau = string.ascii_uppercase

items = {}

keywords = [
    'define',
    'return',
    'math'
]

class checks:
    def variables(var):
        """
        This function is used to check if the string contains the define word, if it
        does, then it will create a variable and done!
        """
        if "define" in var:
            var = var[7:len(var)+1]
            idx = var.index("=")

            v = var[0:idx-1]
            key = var[idx+2:]

            items[v] = key

            print(items[v])
            return True
        else:
            return False

    def mathematics(uwu):
        """
        Used for performing some mathematical tasks, It just needs one string, and
        it will output you the result within few seconds
        """

        print(eval(uwu))

    def retur_n(uwu):
        if uwu in items:
            print(f"{items[uwu]}")
        else:
            print("UwU! '{}' is not defined, please define it using 'define var_name = value'".format(uwu))

def run(command):
    ans = checks.variables(command)
    if "math" in command:
        command = list(command)
        command.remove("m")
        command.remove("a")
        command.remove("t")
        command.remove("h")
        while " " in command:
            command.remove(" ")
        listToStr = ''.join([str(elem) for elem in command])
        checks.mathematics(listToStr)
    elif "return" in command:
        try:
            command = command.split(" ")
            command.remove("return")
            command.remove("{")
            command.remove("}")
            command = "".join(command)
            checks.retur_n(command)
        except ValueError:
            print("UwU! Please use Curly Brackets, like this, 'return { command goes here }'")
    else:
        pass