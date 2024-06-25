import colorama
import phonenumbers as pn
from phonenumbers import geocoder, carrier, timezone
import time
import sys
import os
colorama.init()
GREEN = colorama.Fore.GREEN
GRAY = colorama.Fore.LIGHTBLACK_EX
RESET = colorama.Fore.RESET
YELLOW = colorama.Fore.YELLOW
BLUE = colorama.Fore.BLUE
LB = colorama.Fore.LIGHTBLUE_EX
RED = colorama.Fore.RED
print(BLUE)

def validator():
	valid = False
	while not valid:
		try:
			number = input(f"{LB}Enter a phone number:{RESET} ")
			in_number = pn.parse(number, None)
			valid = True
		except:
			print(f"""{RED}An Error occurred!
{GREEN}-Make sure + and country code is written before phone number{RESET}""")
	if pn.is_valid_number(in_number) is True:
		print(f"{GREEN}[✓]{number} is valid {RESET}")
	elif pn.is_valid_number(in_number) is not True:
		print(f"{RED}[x]{number} is not valid {RESET}")
	print(f"{LB}Refreshing......{RESET}")
	time.sleep(4)

def carrier():
	number = input("Enter a phone number with country code: ")
	in_number = pn.parse(number, None)
	region = geocoder.description_for_number(in_number, "en")
	isp = carrier.name_for_number(in_number, "en")
	zone = timezone.time_zones_for_number(in_number)
	
	print(f"""
-PHONE NUMBER: {in_number}      -REGION: {region}  -TIMEZONE: {zone}           -INTERNET SERVICE PROVIDER: {isp}
	""")
	
print("""
       
█▄─▄▄─█─█─█─▄▄─█▄─▀█▄─▄█▄─▄▄─█▄─▀─▄█
██─▄▄▄█─▄─█─██─██─█▄▀─███─▄█▀██▀─▀██
▀▄▄▄▀▀▀▄▀▄▀▄▄▄▄▀▄▄▄▀▀▄▄▀▄▄▄▄▄▀▄▄█▄▄▀
""")
print(GREEN)
print("""
[+] Tool name: PhoneX
[+] Author: Solomon Adenuga
[+] Version: 1.0
[+] Github: https://github.com/SoloTech01
[+] Whatsapp: +2348023710562
""")
print(YELLOW)
print("××××××××" * 10)
print("""
[1] Get Phone number info 
[3] Validate Phone number
[4] Update the tool
[5] Exit the tool
""")
option = input(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>Enter a number:>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
carrier()