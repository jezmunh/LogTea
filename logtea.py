from colorama import Fore, Back, Style
def info(arg):
    print(Fore.BLUE + f'[INFO]{arg}')
    print(Style.RESET_ALL)
def success(arg):
    print(Fore.GREEN + f'[SUCCESS]{arg}')
    print(Style.RESET_ALL)
def error(arg):
    print(Fore.RED + f'[ERROR]{arg}')
    print(Style.RESET_ALL)
def warn(arg):
    print(Fore.YELLOW + f'[WARN]{arg}')
    print(Style.RESET_ALL)

