import colorama
banner=(colorama.Fore.GREEN+'''  OooOoo                                      
                      __                          
  ___________ _/  |_ ___.__._____    _____  
 /  ___/\__  \\   __<   |  |\__  \  /     \ 
 \___ \  / __ \|  |  \___  | / __ \|  Y Y  \
/____  >(____  /__|  / ____|(____  /__|_|  /
     \/      \/      \/          \/      \/            Made by satyam''')
print(banner)
a=input(colorama.Fore.YELLOW+colorama.Style.BRIGHT+"Enter to decode :")
string=''
for i in a:
                a=(ord(i))
                b=a+3
                d=(chr(b))
                string+=d
print(colorama.Fore.YELLOW+colorama.Style.BRIGHT+"The encoded value is -> "+colorama.Fore.BLUE+colorama.Style.BRIGHT+string)