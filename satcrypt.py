import colorama
colorama.init(autoreset=True)
banner=(colorama.Fore.GREEN+'''  OooOoo                                      
                      __                          
  ___________ _/  |_ ___.__._____    _____  
 /  ___/\__  \\   __<   |  |\__  \  /     \ 
 \___ \  / __ \|  |  \___  | / __ \|  Y Y  \
/____  >(____  /__|  / ____|(____  /__|_|  /
     \/      \/      \/          \/      \/              Made by satyam
                                                   ''')
print(banner)

name=input(colorama.Fore.YELLOW+colorama.Style.BRIGHT+"[=] Enter the string :")

string=''
for i in name:
                a=(ord(i))
                b=a+2
                c=b-5
                d=(chr(c))
                string+=d
print(colorama.Fore.YELLOW+"[+] The hashed value is :-> "+colorama.Style.BRIGHT+colorama.Fore.RED+string)
          
                
