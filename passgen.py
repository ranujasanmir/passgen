#password genarate tool by RS45
#give credits to me
#don't change this code

#import using libraries
import random
import os
import time
import sys

#clearing terminal
os.system("clear")

logo = """\033[32m
╔═╗────╔═╗╔═╗╔═╗───────
║╬║╔═╗─║═╣║═╣║╬║╔═╗╔═╦╗
║╔╝║╬╚╗╠═║╠═║╠╗║║╩╣║║║║
╚╝─╚══╝╚═╝╚═╝╚═╝╚═╝╚╩═╝"""

#display logo
print(logo)
time.sleep(1.0)
print()

logo1 = """\033[32m+-----------------------------------------------+
| This Tool Help to you create strong passwords |
+-----------------------------------------------+
| Coded By Ranuja  | version : 1.0              |
+-----------------------------------------------+"""
#display logo1
print(logo1)
time.sleep(1.0)

#code for tprint
def tprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.03)

print ()

#display choices
tprint(" [1] Start\n [2] Exit")

time.sleep(1.0)

#ask for your choice
print()
tprint("Enter your choice on bellow ⍢ ")
ans = input("passgen@rs45]$\n┕ ")
print()

#conditions for choice
if ans == "1" :
	lower_case = "abcdefghijklmnopqrstuvwxyz"
	upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	number = "0123456789"
	symbols = "@#$%&*/\?"

	Use_for = lower_case + upper_case + number + symbols

	length_for_password = 8

	password = "".join(random.sample(Use_for, length_for_password))

	print("Your genarated password is : " + password)
	print()
	tprint("[+]Thanks for using this tool\n[+]Created by RS45 Official\n[+]If you changed source code, you must give credit to me")
else:
	
	if ans == '2' :
		tprint("Miss you too!")
		sys.exit
	
	else:
		tprint("Wrong Number! You can only use 1 or 2")
		print("Wait 3 seconds for relunching tool...")
		time.sleep(3.0)
		print("Relunching...")
		os.system("python passgen.py")
	