import socket
from os import system

slc_ports = []

def scan_menu():
    print("Developed by:")
    print(" __     ______           __ __               __ ")
    print("|  |--.|      |.--.--.--|  |__|.-----.-----.|__|")
    print("|     ||  --  ||  |  |  _  |  ||     |     ||  |")
    print("|__|__||______||_____|_____|__||__|__|__|__||__|")
    print('+' + '-'*24 +  '-'*24 + '+')
    print('https://github.com/h0udinni')
    print('+' + '-'*11 + 'LOCAL_SCAN_MENU' + '-'*11 + '+')
    print('[1] Scan known ports.')
    print('[2] Scan all ports.')
    print('[3] Scan selected ports.')
    print('[0] Back to menu.')
    print('+' + '-'*11 + 'LOCAL_SCAN_MENU' + '-'*11 + '+')

def scan_know_ports(): #SCAN KNOW PORTS
    open_ports=[]
    knowports = [20, 21, 22, 23, 25, 53, 80, 110, 143, 443, 1433, 3306, 3389, 8080]
    system("cls")
    localhost='127.0.0.1' # IP local. Comando do cmd para saber quais portas estão abertas, para confirmação: netstat -an | find "LISTEN" 
    print(f'Scanning ports of IP {localhost}...')
    for i in knowports:
        tcp=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp.settimeout(0.5) # Impede loop infinito de conexão.
                #conecta a um endereço remoto. (()) TUPLA: Armazena vários dados. Uma coleção imutável de elementos.
        open=tcp.connect_ex((localhost, i))
        if open == 0:
            print('The port {} is open. '.format (i))
            open_ports.append(i)
    tcp.close()
    if open_ports == []:
        print('The scanned ports are closed.')
    print('Closed connection.')
    input('Press Enter to back the menu... ')
    return

def scan_all_ports(): #SCAN ALL PORTS
    open_ports=[]
    system("cls")
    localhost='127.0.0.1' 
    print(f'Scanning ports of IP {localhost}...')
    for i in range(1, 65536):
        tcp=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp.settimeout(0.5)
        open=tcp.connect_ex((localhost, i))
        if open == 0:
            print('The port {} is open. '.format (i))
            open_ports.append(i)
    tcp.close()
    if open_ports == []:
        print('The scanned ports are closed.')
    print('Closed connection.')
    input('Press Enter to back the menu... ')
    return

def chekport():
    try:
        while True:
            p=int(input('Enter the port (Enter 0 to run the scan): '))
            if p == 0:
                break
            elif p <= 65535:
                slc_ports.append(p)
    except ValueError:
        input('Enter a valid option. Press enter to continue... ')

def scan_slc_ports():
    open_ports=[]
    chekport()
    localhost='127.0.0.1'
    print(f'Scanning ports of IP {localhost}...')
    for i in slc_ports:
        tcp=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp.settimeout(0.5)
        open=tcp.connect_ex((localhost, i))
        if open == 0:
            print('The port {} is open. '.format (i))
            open_ports.append(i)
    tcp.close()
    if open_ports == []:
        print('The scanned ports are closed.')
    print('Closed connection.')
    input('Press Enter to back the menu... ')
    slc_ports.clear()
    return

def scan_options():
    while True:
        try:
            system("cls")
            scan_menu()
            choice=int(input("Enter a option: "))
            if choice == 1:
                scan_know_ports()
            elif choice == 2:
                scan_all_ports()
            elif choice == 3:
                scan_slc_ports()
            elif choice == 0:
                return
        except ValueError:
            input('Enter a valid option. Press enter to continue... ')