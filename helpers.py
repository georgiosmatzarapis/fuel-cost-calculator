class Console:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Utilities:

    invalidInputMessage = f"{Console.WARNING}Oops! Invalid input. Try again.{Console.ENDC}"

    def isFloat(x):
        try:
            a = float(x)
        except (TypeError, ValueError):
            return False
        else:
            return True
