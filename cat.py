#cat.py
# -*- coding: utf-8 -*-


answer_yes = ["Yes", "Y", "yes", "y"]
answer_no = ["No", "N", "no", "n"]

print("""
You have 1 new message from Andy:
Andy: Hey, what's up? Do you know the
Tamagotchi game we used to play
has just released a desktop version.
You have to check it out!
Sooooo, wanna play? Y/N""")

ansAndy=input("answer： ")

while ansAndy in answer_no:
	print("""Oh come on, it would be super fun. It's weekend anyway. """)
	ansAndy=input("Let's give it a try. Y/N")
	if ansAndy in answer_yes:
		break
		print("""Tamagotchi - Save the cat is downloading....
			Completed
			Getting started.
			Type "Meow" to continue""")

ansMeow=input()

while ansMeow !="Meow"|"meow":
	print("Oops, Cat does not anything other than cat language. Type Meow to continue")
	if ansMeow in ["Meow","meow"]:
		break

		print("""And Meow to you too! What would you like to do with your cat?
			⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⡟⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣷⣌⠙⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⣡⡶⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢻⡌⠳⣄⠉⠳⢤⠴⠒⠛⠛⠛⠛⠒⠦⢤⡤⠚⣡⠞⢁⣿⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣽⡷⠒⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠲⢾⣿⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⠀⠀⠀⠀⠀⢀⠀
⠀⠀⠀⠀⠙⠓⠦⢤⣀⡀⢸⠁⠀⠀⠀⣰⠟⠛⢦⠀⠀⠀⠀⠀⠀⠀⢠⣾⠛⢳⡆⠀⠀⠀⠸⣇⣀⣠⠤⠶⠛⠁
⠀⠀⠀⠀⢀⠀⠀⠀⠀⠉⣿⠒⠦⢄⠀⠻⣴⣳⠾⠁⠀⠰⣿⣿⠂⠀⠘⢿⣿⡽⠋⠀⣤⢖⠚⣏⠉⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠉⠉⠉⠉⠉⠙⢻⣍⣽⠿⠀⠀⠀⠀⠀⠀⠸⣦⣼⣷⣼⠆⠀⠀⠀⠀⠀⠐⠿⣍⣹⡏⠉⠉⠉⠉⠙⠁
⠀⠀⠀⠀⠀⣀⣠⠤⠶⠚⠛⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⢀⡟⠉⠓⠲⠤⣄⣀⠀
⠀⠀⠀⠀⠉⠉⠀⠀⠀⠀⠀⠀⠱⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡞⠀⠀⠀⠀⠀⠀⠉⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⡄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡆⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢸⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡇⠀⠀⠀⠀
⠀⢀⡴⠖⠲⢄⠀⠀⣼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣇⠀⠀⠀⠀
⢠⠏⠀⠀⠀⠈⢧⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡟⠀⠀⠀⠀
⣿⠀⠀⠀⠀⠀⢸⡄⢸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡇⠀⠀⠀⠀
⢻⡀⠀⠀⠀⠀⠘⡇⠸⡇⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⣸⢧⡀⠀⠀⠀
⠸⡇⠀⠀⠀⠀⠀⣧⠀⢻⡄⠀⠀⠀⠸⡇⠀⠀⠀⠀⠀⣠⠀⣠⠀⠀⠀⠀⠀⢈⣟⠀⠀⠀⠀⢠⡏⠈⢳⡀⠀⠀
⠀⢻⡄⠀⠀⠀⠀⢹⡄⠀⡳⡄⠀⠀⠀⣧⠀⠀⠀⠀⠀⢸⠀⣿⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⢠⣟⠀⠀⠈⣇⠀⠀
⠀⠀⢳⡄⠀⠀⠀⠀⠳⡄⠀⠙⢦⡀⠀⢹⡀⠀⠀⠀⠀⢸⠀⣿⠀⠀⠀⠀⠀⣼⠀⠀⢀⡴⠋⣿⠀⠀⠀⣿⠀⠀
⠀⠀⠀⠱⣄⠀⠀⠀⠀⠙⢦⡀⠀⠈⠓⠮⣧⠀⠀⢀⠀⡾⠀⢹⡀⢀⠀⠀⣸⣇⡤⠞⠉⢀⣴⠃⠀⠀⢀⣿⠀⠀
⠀⠀⠀⠀⠘⢦⡀⠀⠀⠀⠀⠉⠲⢤⣀⠀⠈⠳⣿⣸⡾⠛⠛⠚⢷⣟⣸⡴⠋⠀⠀⣀⡴⠚⠁⠀⠀⠀⣼⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠙⠦⣀⠀⠀⠀⠀⠀⠈⠉⠓⠲⠶⠤⠤⣤⣤⣤⣤⠼⠵⠶⠖⠚⠉⠁⠀⠀⠀⠀⢀⡼⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠓⠦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠴⠋⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠓⠲⠤⣤⣀⣀⣀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣤⠤⠴⠚⠉⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠈⠉⠉⠉⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
A - Talk
B - Feed
C - Pat""")
		ansCatGame=input()
		if ansCatGame in "A" or "Talk" or "talk":
			ansTalkCount+=1
			if ansTalkCount<=3:

				print("""The cat makes a cute little sound as cats are supposed to do normally. What would you like to do with your cat next?
		
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣶⣏⠣⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠇⡟⠳⡄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠞⠉⠀⠙⢧⣣⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡃⡂⠀⠀⠋⢶⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡴⠋⠀⠀⠀⠀⠀⠈⢳⣣⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠅⡁⠀⠀⠀⠀⠉⠋⣦⡆⡦⠗⠕⠝⠬⣽⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡃⠅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⣋⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣏⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣇⣣⠀⠀⡀⣀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠁⠀⠀⠀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⣿⡗⡄⠀⠀⠀⠀⠀⢀⠺⠍⠇⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠒⠂⠂⠤⢀⣯⠁⠀⡀⡐⣾⡏⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⢼⣯⢻⣿⣟⠀⠀⠀⠀⠈⠀⠘⡊⡅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣇⠁⠀⠀⣇⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⡇⠀⠀⠀⠀⢀⠠⠄⣕⡧⠠⠀⠄⣀⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡧⠀⠀⠂⠉⠛⠛⠁⠀⠀⠀⢾⡶⠀⠀⠀⠀⠀⠁⠁⠁⠀⠀⠀⠀⠀⠀⡀⠀⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣟⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣲⠧⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣠⠈⠁⠘⣗⣄⢀⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣺⡇⣄⠀⠈⠉⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠩⠣⢆⡄⡀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⣀⡤⡾⠗⠋⠊⢇⠥⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠁⠀⠀⠀⠁⠉⠉⣻⡟⠚⠊⠚⠏⠇⡏⡏⣫⣙⠙⠛⠉⠁⠀⠀⠀⠀⠀⠀⠁⠡⢄⠒⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠹⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⢤⠁⢂⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠃⡄⠑⣀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣱⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠃⡆⠆⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢐⠺⡂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢍⡆
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢃⡂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣗⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣯⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
A - Talk
B - Feed
C - Pat""")
			else:
				print("""'Helll......pssss...'
					Suddenly this peculiar text showed on the screen when you were just trying to have more normal human-animal conversations with the cat, and even weirder, it was in a different font.
                                                                                                                                                   
                                                                                                                                                   
HHHHHHHHH     HHHHHHHHHEEEEEEEEEEEEEEEEEEEEEELLLLLLLLLLL             PPPPPPPPPPPPPPPPP        MMMMMMMM               MMMMMMMMEEEEEEEEEEEEEEEEEEEEEE
H:::::::H     H:::::::HE::::::::::::::::::::EL:::::::::L             P::::::::::::::::P       M:::::::M             M:::::::ME::::::::::::::::::::E
H:::::::H     H:::::::HE::::::::::::::::::::EL:::::::::L             P::::::PPPPPP:::::P      M::::::::M           M::::::::ME::::::::::::::::::::E
HH::::::H     H::::::HHEE::::::EEEEEEEEE::::ELL:::::::LL             PP:::::P     P:::::P     M:::::::::M         M:::::::::MEE::::::EEEEEEEEE::::E
  H:::::H     H:::::H    E:::::E       EEEEEE  L:::::L                 P::::P     P:::::P     M::::::::::M       M::::::::::M  E:::::E       EEEEEE
  H:::::H     H:::::H    E:::::E               L:::::L                 P::::P     P:::::P     M:::::::::::M     M:::::::::::M  E:::::E             
  H::::::HHHHH::::::H    E::::::EEEEEEEEEE     L:::::L                 P::::PPPPPP:::::P      M:::::::M::::M   M::::M:::::::M  E::::::EEEEEEEEEE   
  H:::::::::::::::::H    E:::::::::::::::E     L:::::L                 P:::::::::::::PP       M::::::M M::::M M::::M M::::::M  E:::::::::::::::E   
  H:::::::::::::::::H    E:::::::::::::::E     L:::::L                 P::::PPPPPPPPP         M::::::M  M::::M::::M  M::::::M  E:::::::::::::::E   
  H::::::HHHHH::::::H    E::::::EEEEEEEEEE     L:::::L                 P::::P                 M::::::M   M:::::::M   M::::::M  E::::::EEEEEEEEEE   
  H:::::H     H:::::H    E:::::E               L:::::L                 P::::P                 M::::::M    M:::::M    M::::::M  E:::::E             
  H:::::H     H:::::H    E:::::E       EEEEEE  L:::::L         LLLLLL  P::::P                 M::::::M     MMMMM     M::::::M  E:::::E       EEEEEE
HH::::::H     H::::::HHEE::::::EEEEEEEE:::::ELL:::::::LLLLLLLLL:::::LPP::::::PP               M::::::M               M::::::MEE::::::EEEEEEEE:::::E
H:::::::H     H:::::::HE::::::::::::::::::::EL::::::::::::::::::::::LP::::::::P               M::::::M               M::::::ME::::::::::::::::::::E
H:::::::H     H:::::::HE::::::::::::::::::::EL::::::::::::::::::::::LP::::::::P               M::::::M               M::::::ME::::::::::::::::::::E
HHHHHHHHH     HHHHHHHHHEEEEEEEEEEEEEEEEEEEEEELLLLLLLLLLLLLLLLLLLLLLLLPPPPPPPPPP               MMMMMMMM               MMMMMMMMEEEEEEEEEEEEEEEEEEEEEE
                                                                                                                                                   
                                                                                                                              
					Well, anyway, what would you like to do with your cat next?
					A - Talk
					B - Feed
					C - Pat""")
				ansCatHelp=input()
				if ansCatHelp in "A" or "Talk" or "talk":
					print("""Oh THANK GOD THANK LORD THANK YOU THANK YOU THANK YOU SO SOSO MUCH YOU ARE RESPONDING YOU CAN SEE THIS FINALLY SOMEONE""")

			

