import random 
from sys import argv
from pyfiglet import figlet_format as fig   
from colorama import Fore as f 
from os import system

system("cls")
b = fig(text="BlackPassword")+"\n"+f"{f.LIGHTRED_EX}#"*60+f"{f.WHITE}\n"

num = 0
if argv[1] == "-p":

    print(f.WHITE, b)

    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number = "0123456789"
    symbols = "@#$%&/\?"

    User_for = lower_case + upper_case + number + symbols

    length_for_pass = 8 

    password = "".join(random.sample(User_for, length_for_pass))

    print(f"Your password : {password}")

elif argv[1] == "-sp":
    if argv[2] == "--name" or argv[2] == "-n":
        print(f.WHITE, b)
            
        lower_case = "abcdefghijklmnopqrstuvwxyz"
        upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        number = "0123456789"
        symbols = "@#$%&/\?"

        User_for = lower_case + upper_case + number + symbols

        length_for_pass = 8 

        password = "".join(random.sample(User_for, length_for_pass))
        
        with open(argv[3], 'a')as ar:
            ar.write(password)
            ar.close()
            print(f"""Your Generated Password is : {password}
saved in {f.RED}{argv[3]}{f.WHITE}""")

elif argv[1] == "-fp":
    if argv[2] == "-a":
        x = int(argv[3])
        print(f.WHITE, b)
        for i in range(x):
           
            lower_case = "abcdefghijklmnopqrstuvwxyz"
            upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            number = "0123456789"
            symbols = "@#$%&/\?"

            User_for = lower_case + upper_case + number + symbols

            length_for_pass = 8 
            password = "".join(random.sample(User_for, length_for_pass))

            num += 1
            print(f"""{num}: {password}""")


elif argv[1] == "-fps":
    if argv[2] == "-a":
        x = int(argv[3])
        if argv[4] == "-n" or argv[4] == "--name":
            print(f.WHITE, b)
            for i in range(x):
                    
                lower_case = "abcdefghijklmnopqrstuvwxyz"
                upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                number = "0123456789"
                symbols = "@#$%&/\?"

                User_for = lower_case + upper_case + number + symbols

                length_for_pass = 8 
                password = "".join(random.sample(User_for, length_for_pass))

                num += 1
                print(f"""{num}: {password}""")
                with open(argv[5], 'a') as fps:
                    fps.write(password+"\n")
                    fps.close()
            print(f"saved in {f.RED}{argv[5]}{f.WHITE}\n")

elif argv[1] == "-aps":
    aint = int(argv[2])
    print(f.WHITE, b)
            
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number = "0123456789"
    symbols = "@#$%&/\?"

    User_for = lower_case + upper_case + number + symbols

    length_for_pass = aint

    password = "".join(random.sample(User_for, length_for_pass))

    print(f"""Your Password : {password}""")

elif argv[1] == "-apss":
    aint = int(argv[2])
    if argv[3] == "-n" or argv[3] == "--name":
        print(f.WHITE, b)
                
        lower_case = "abcdefghijklmnopqrstuvwxyz"
        upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        number = "0123456789"
        symbols = "@#$%&/\?"

        User_for = lower_case + upper_case + number + symbols

        length_for_pass = aint

        password = "".join(random.sample(User_for, length_for_pass))

        with open(argv[4], 'a') as apss:
            apss.write(password)
            apss.close()
        print(f"""Your Password : {password}
saved in {f.RED}{argv[4]}{f.WHITE}""")


elif argv[1] == "-apa":
    aint = int(argv[2])
    if argv[3] == "-n" or argv[3] == "--name":
        if argv[5] == "-a":
            apa = int(argv[6])
            print(f.WHITE, b)
                    
            lower_case = "abcdefghijklmnopqrstuvwxyz"
            upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            number = "0123456789"
            symbols = "@#$%&/\?"

            User_for = lower_case + upper_case + number + symbols

            length_for_pass = aint

            for i in range(apa):
                password = "".join(random.sample(User_for, length_for_pass))
                num += 1
                with open(argv[4], 'a') as apss:
                    apss.write(password+"\n")
                    apss.close()
                print(f"""{num}: {password}""")
        print(f"saved in {f.RED}{argv[4]}{f.WHITE}\n")


elif argv[1] == "-h" or argv[1] == "--help":
    print(f.WHITE, b)
    print("""-p (just create a password)
-sp -n / --name [name file for save password]
-fp -a [write a integer for order of create password]
-fps -a [write a integer] -n / --name [name file for save password]
-aps [write a integer for amount of letters]
-apss [write a integer for amount of letters] -n / --name [name file for save password]
-apa [write a integer for amount of letters] -n / --name [name file for save password] -a [a integer for order of password]""")
