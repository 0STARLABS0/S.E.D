#!/usr/bin/python3
try :
    from os import system, name
    import base64
    import hashlib
    from colorama import Fore
    from sys import exit
    def clear():
        if name == 'nt':
            _ = system("cls")
        else :
            _ = system("clear")
    clear()
    def banner():
        print(Fore.GREEN + """      

        ██╗░░░██╗░░░███████╗░░░██████╗░
        ╚██╗░██╔╝░░░██╔════╝░░░██╔══██╗
        ░╚████╔╝░░░░█████╗░░░░░██║░░██║
        ░░╚██╔╝░░░░░██╔══╝░░░░░██║░░██║
        ░░░██║░░░██╗███████╗██╗██████╔╝
        ░░░╚═╝░░░╚═╝╚══════╝╚═╝╚═════╝░
        
        Created By    :        YA3IN
        
        Telegram      :        https://t.me/Mister_Ya3in
        Instagram     :        https://instagram.com/Mister_Ya3in
        Github        :        https://github.com/YA3IN3SA44RI
        """)
    banner()
    def star_app():
        starandfinish = input(Fore.GREEN + "\n[+] " + Fore.WHITE + "Give Me An * From 1 To 5 : ")
        if starandfinish == "*" :
            print(Fore.RED + "\n[-] " + Fore.WHITE + "Bad App :(")
            exit()
        elif starandfinish == "**" :
            print(Fore.RED + "\n[-] " + Fore.WHITE + "Why... :(")
            exit()
        elif starandfinish == "***" :
            print(Fore.YELLOW + "\n[+] " + Fore.WHITE + "Please... :(")
            exit()
        elif starandfinish == "****" :
            print(Fore.YELLOW + "\n[+] " + Fore.WHITE + "Thank You :)")
            exit()
        elif starandfinish == "*****" :
            print(Fore.GREEN + "\n[+] " + Fore.WHITE + "I Love You , Tnx :))))")
            exit()
        else :
            print(Fore.GREEN + "\n[+] " + Fore.WHITE + "Ok...Have A Nice Life :))))")
            exit()
    def encoder():
        print(Fore.GREEN + "\n[+] " + Fore.WHITE + "I Can Encode : \n")
        print(Fore.CYAN + "         1.Base64")
        print(Fore.CYAN + "         2.MD5")
        print(Fore.CYAN + "         3.SHA256")
        print(Fore.CYAN + "         4.Blake2b")
        print(Fore.CYAN + "         5.SHA1")
        print(Fore.CYAN + "         6.SHA224")
        select_encoder = int(input(Fore.GREEN + "\n[+] " + Fore.WHITE + "ENTER  : "))
        if select_encoder == 1 :
            print(Fore.GREEN + "\n[+] " + Fore.YELLOW + "WARNING : If You Want To Exit Please Enter " + Fore.RED + "exit")
            while True :
                clear_text = input(Fore.GREEN + "\n[+] " + Fore.WHITE + "Give Me A Text : ")
                if clear_text == "exit" :
                    star_app()
                    exit()
                elif clear_text == "back" :
                    encoder()
                else :
                    clear_text_byte = clear_text.encode('ascii')
                    base64_bytes = base64.b64encode(clear_text_byte)
                    base64_message = base64_bytes.decode('ascii')
                    print(Fore.GREEN + "\n[+] " + Fore.BLUE + "Encode You Text Is : " + Fore.YELLOW + base64_message)
        elif select_encoder == 2 :
            print(Fore.GREEN + "\n[+] " + Fore.YELLOW + "WARNING : If You Want To Exit Please Enter " + Fore.RED + "exit")
            while True :
                clear_md5_text = input(Fore.GREEN + "\n[+] " + Fore.WHITE + "Give Me A Text : ")
                if clear_md5_text == "exit" :
                    star_app()
                    exit()
                elif clear_md5_text == "back" :
                    encoder()
                else :
                    res = hashlib.md5(clear_md5_text.encode())
                    print(Fore.GREEN + "[+] " + Fore.BLUE + "Encode Your Text Is : " + Fore.YELLOW + res.hexdigest())
        elif select_encoder == 3 :
            print(Fore.GREEN + "\n[+] " + Fore.YELLOW + "WARNING : If You Want To Exit Please Enter " + Fore.RED + "exit")
            while True :
                clear_sha256_text = input(Fore.GREEN + "\n[+] " + Fore.WHITE + "Give Me A Text : ")
                if clear_sha256_text == "exit" :
                    star_app()
                    exit()
                elif clear_sha256_text == "back" :
                    encoder()
                else :
                    res = hashlib.sha256(clear_sha256_text.encode())
                    print(Fore.GREEN + "[+] " + Fore.BLUE + "Encode Your Text Is : " + Fore.YELLOW + res.hexdigest())
        elif select_encoder == 4 :
            print(Fore.GREEN + "\n[+] " + Fore.YELLOW + "WARNING : If You Want To Exit Please Enter " + Fore.RED + "exit")
            while True :
                clear_blake2b_text = input(Fore.GREEN + "\n[+] " + Fore.WHITE + "Give Me A Text : ")
                if clear_blake2b_text == "exit" :
                    star_app()
                    exit()
                elif clear_blake2b_text == "back" :
                    encoder()
                else :
                    res = hashlib.blake2b(clear_blake2b_text.encode())
                    print(Fore.GREEN + "[+] " + Fore.BLUE + "Encode Your Text Is : " + Fore.YELLOW + res.hexdigest())
        elif select_encoder == 5 :
            print(Fore.GREEN + "\n[+] " + Fore.YELLOW + "WARNING : If You Want To Exit Please Enter " + Fore.RED + "exit")
            while True :
                clear_sha1_text = input(Fore.GREEN + "\n[+] " + Fore.WHITE + "Give Me A Text : ")
                if clear_sha1_text == "exit" :
                    star_app()
                    exit()
                elif clear_sha1_text == "back" :
                    encoder()
                else :
                    res = hashlib.sha1(clear_sha1_text.encode())
                    print(Fore.GREEN + "[+] " + Fore.BLUE + "Encode Your Text Is : " + Fore.YELLOW + res.hexdigest())
        elif select_encoder == 6 :
            print(Fore.GREEN + "\n[+] " + Fore.YELLOW + "WARNING : If You Want To Exit Please Enter " + Fore.RED + "exit")
            while True :
                clear_sha224_text = input(Fore.GREEN + "\n[+] " + Fore.WHITE + "Give Me A Text : ")
                if clear_sha224_text == "exit" :
                    star_app()
                    exit()
                elif clear_sha224_text == "back" :
                    encoder()
                else :
                    res = hashlib.sha224(clear_sha224_text.encode())
                    print(Fore.GREEN + "[+] " + Fore.BLUE + "Encode Your Text Is : " + Fore.YELLOW + res.hexdigest())
        else :
            print(Fore.RED + "[-] " + Fore.WHITE + "Ok...Bye")
    encoder()
except :
    print("Install HashLib & Try Again")
    from sys import exit
    exit()
