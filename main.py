import scan_1
import scan_2
from os import system   

def menu():
    print("Developed by:")
    print(" __     ______           __ __               __ ")
    print("|  |--.|      |.--.--.--|  |__|.-----.-----.|__|")
    print("|     ||  --  ||  |  |  _  |  ||     |     ||  |")
    print("|__|__||______||_____|_____|__||__|__|__|__||__|")
    print('+' + '-'*24 +  '-'*24 + '+')
    print('https://github.com/h0udinni')
    print('+' + '-'*22 + 'MENU' + '-'*22 + '+')
    print('[1] Local ports scan.')
    print('[2] IP ports scan.')
    print('[3] Information about IPv4 and ports.')
    print('[0] Exit.')
    print('+' + '-'*22 + 'MENU' + '-'*22 + '+')

def options():
    while True:
        try:
            system("cls")
            menu()
            choice=int(input("Enter a option: "))
            if choice == 1:
                scan_1.scan_options()
            elif choice == 2:
                scan_2.scan_options()
            elif choice == 3:
                system("cls")
                print('IPv4 is a 32-bit address format divided into four 8-bit segments called octets, separated by dots (e.g., 192.168.0.1). Each octet ranges from 0 to 255.')
                print('Know ports: 20, 21, 22, 23, 25, 53, 80, 110, 143, 443, 1433, 3306, 3389, 8080.')
                input('Press enter to continue... ')
            elif choice == 0:
                print('Thanks for use the software.')
                break
        except ValueError:
            input('Enter a valid option. Press enter to continue... ')
options()