# coding=utf-8
#!/usr/bin/python
# coding=utf-8
# coded by : ADHEESH-MISHRA
#Blog : https://adheesh-mishra-code.blogspot.com

print("\033[1;93m            First Tool login by Adheesh-Mishra")
print(" ")
print("\033[1;97m @@@••••••••••••••Adheesh-Mishra login page•••••••••••@@@        @@@•••••••••••••••••••••••••@@@                               @@@•••••••••••••••••••••••••@@@\033[1;0m")
username = input("\033[1;95m[+]\033[1;95m Username :\033[1;95m ")
passwordss = input("\033[1;95m[+]\033[1;95m Password :\033[1;95m ")

if (passwordss == '12345'):
      print("Password is week login blocked")
else:
      print("\033[1;97m[1]see info")
      inp = input("[?]: ")
      if (inp == '1'):
           print("\033[1;92musername:" + username)
           print("password:" + passwordss)
         
