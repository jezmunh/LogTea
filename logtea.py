from colorama import Fore, Back, Style
def info(arg):
    print(Fore.BLUE + f'[INFO]{arg}' + Style.RESET_ALL)    
def success(arg):
    print(Fore.GREEN + f'[SUCCESS]{arg}' + Style.RESET_ALL)    
def error(arg):
    print(Fore.RED + f'[ERROR]{arg}' + Style.RESET_ALL)    
def warn(arg):
    print(Fore.YELLOW + f'[WARN]{arg}' + Style.RESET_ALL)
    

