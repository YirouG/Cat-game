

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
		print("""Tamagotchi - Save the cat is downloading....
			Completed
			Getting started.
			Type "Meow" to continue""")
		break

ansMeow=input()

while ansMeow not in["Meow","meow"]:
	print("Oops, the cat does not anything other than catnese. Type Meow to continue")
	if ansMeow in ["Meow","meow"]:
		
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
		break
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
				ansHelp1=input('')
				if ansHelp1 in "A" or "Talk" or "talk":
					print("""Cat:'Oh THANK GOD THANK LORD THANK YOU THANK YOU THANK YOU SO SOSO MUCH YOU ARE RESPONDING YOU CAN SEE THIS FINALLY SOMEONE'""")
					print("This is getting weird, what is going on?")
					print('''Cat:"Please listen to me! I know it sounds crazy, but this is not an innocent child's game as you thought, it's an evil magic! "''')
					print('''Cat:"And I am actually a human soul trapped in this piece of trashy program, being tortured for endless time, acting as a cat with only 3 things to do. Oh, you can never imagine the boredom, the despair, the horror!"''')
					print('''...And I cannot even kill myself... It took me forever to even find this bug to communicate with you. Please help me since you are my only hope. Please Please Please I am begging you.''')
					print('''1. What? I don't believe it, is this some sort of prank?
						2. Wow, okay, I'm sorry to hear that, how may I help you?
						3.feed
						4.pat''')
					ansHelp2=input('Your answer is: ')
					if ansHelp2=='1':
						print('Cat:"Oh believe me I wish it was a prank, now please treat me seriously just for once. I am begging you."')
						ansHelp3=input('Your answer this time: ')
						print('''1. What nonsense! Clearly some new sort of online scam.
						2. I guess let's just talk then.
						3.feed
						4.pat''')
						if ansHelp3=='1':
							print('''Suddenly your monitor starts flickering between blue and black screen, then everything went dark, the power in your place is off, in the darkness there is only an image of this very scary angry cat on the screen:
      .__....._             _.....__,
                 .": o :':         ;': o :".
                 `. `-' .'.       .'. `-' .'  
                   `---'             `---' 

         _...----...      ...   ...      ...----..._
      .-'__..-""'----    `.  `"`  .'    ----'""-..__`-.
     '.-'   _.--"""'       `-._.-'       '"""--._   `-.`
     '  .-"'                  :                  `"-.  `
       '   `.              _.'"'._              .'   `
             `.       ,.-'"       "'-.,       .'
               `.                           .'
                 `-._                   _.-'
                     `"'--...___...--'"`''')
							print('WE ARE ANGRY')
							print('It is too late now, the spell has been cast. You are doomed to be stuck with me the moment you said Meow!')
							print('You can\'t close the program or use the laptop anymore, and the world around you start changing shapes, everything turns into glitches. YOU ARE STUCK HERE FOREVER')
							print('GAMEOVER')
						elif ansHelp2=='2':
							print('Cat:"Thank you so much! But I do not really know what you can do... Could you please just...talk to me more? It has been a while since I was able to talk to anyone at all. The loneliness is eating my soul...Can I get to know about you? What\'s your name by the way?"')

						elif ansHelp2 in ['3','4']:
							print('Cat:"Please don\'t do that again, you are tearing me apart!"')
						else:
							Print('No response. Try another option.')
					ansHelp3=input('Your answer this time: ')
					print('''1. What nonsense! Clearly some new sort of online scam.
						2. I guess let's just talk then.
						3.feed
						4.pat''')
					if ansHelp3=='1':
							print('''Suddenly your monitor starts flickering between blue and black screen, then everything went dark, the power in your place is off, in the darkness there is only an image of this very scary angry cat on the screen:
      .__....._             _.....__,
                 .": o :':         ;': o :".
                 `. `-' .'.       .'. `-' .'  
                   `---'             `---' 

         _...----...      ...   ...      ...----..._
      .-'__..-""'----    `.  `"`  .'    ----'""-..__`-.
     '.-'   _.--"""'       `-._.-'       '"""--._   `-.`
     '  .-"'                  :                  `"-.  `
       '   `.              _.'"'._              .'   `
             `.       ,.-'"       "'-.,       .'
               `.                           .'
                 `-._                   _.-'
                     `"'--...___...--'"`''')
							print('WE ARE ANGRY')
							print('It is too late now, the spell has been cast. You were doomed to be stuck with me in this game forever the moment you said Meow!')
							print('You can\'t close the program or use the laptop anymore, and the world around you start changing shapes, everything turns into glitches. YOU ARE STUCK HERE FOREVER')
							print('GAMEOVER')
						elif ansHelp3=='2':
							print('Cat:"The loneliness is eating my soul...Can I get to know about you? What\'s your name by the way?"')
							username=input('My name is: ')
							if not username.endswith("y"):
								username=username+"y"
							print(username+', that is a very good name... It sounds...human. Oh, I am not even sure about my own human name anymore, Edward? Eddard? God I feel old, who knows how long it has been since I was trapped here, I hope you do not mind my nagging... Haha, that sounds old too, how old are you?')
							userage=input('I am ')
							print('Cat:"You are still so young. I wish I lived in the outside world as your age. Sorry to be monologing all the time, is there anything you want to ask me?"')
							useranswer=input('Anything?: ')
							print('Player:"I really want to ask, but the game system does not allow it. It seems that the way to communicate with me you found in this program only allows me to answer your questions in rather primitive ways and does not support open dialogues. I mean come on, it\'s not a AAA game, the programmers only learned python for two weeks, what do you expect?"')
							print('Cat:"Oh, okay then, now you are talking meta too. Anyway, tell me about yourself, where were you born? Because I really miss my hometown now, I recall it as a snowy place...I used to have a family, and pets too, an actual cat."')
							userbirthplace=input('I was born in ')
							print('Cat:"That sounds like a really good place. Wish I can visit there some day, wish I can be anywhere outside this game. Woe, woe, woe!"')
							print('''Suddenly your monitor starts flickering between blue and black screen, then everything went dark, the power in your place goes off, in the darkness there is only an image of this sad cat on the screen:
								⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠤⠒⠀⠈⠓⠠⠐⠢⠄⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⠠⠤⠀⠀⠄⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠦⠤⠒⠒⠒⠠⣀⠀
⠀⡔⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣣
⣔⠀⠤⠄⣀⣀⠀⠀⠀⠀⠀⠀⣠⡂⠀⠀⠀⠲⣄⣀⠀⠀⠀⠀⢀⡤⠒⠈⠀
⠀⠀⠀⠀⠀⠌⠀⠀⠀⢠⠖⣁⡀⠈⠀⠀⠀⡌⢠⣄⠑⡄⠀⠀⠉⠂⠀⠀⠀
⠀⠀⠀⠀⡜⠀⠀⠀⢠⠃⢸⣿⣽⠀⠀⠀⠀⠇⢿⣷⠇⠘⠀⠀⠀⡇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⢄⠀⠉⢉⡔⠀⠀⠀⠈⢆⠁⠀⢀⠃⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⡄⠀⠀⠀⠀⠈⠑⠒⠉⠀⢀⡴⣀⠀⠀⠉⠐⠁⠀⠀⠀⡀⠀⠀⠀
⠒⠒⠒⠂⠘⡀⠐⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠐⠒⠀⠠⠤⠃⠤⠠⠄
⠀⠀⠀⠀⠀⢘⣤⠌⠀⠀⠀⠀⠀⠀⠐⠒⠂⠀⠀⠀⠁⠒⠤⡴⢁⣀⠀⠀⠀
⠀⠀⠒⠂⠈⠀⠀⠱⡴⠉⠑⠉⡵⠂⠀⠀⠀⡔⢲⠒⠖⠒⠊⠀⠀⠀⠉⠉⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠣⠴⢇⡠⠅⠘⠉⠉⠁⢄⣀⣠⣀⠄⠀⠀⠀⠀⠀⠀⠀''')
							print('You can\'t close the program or use the laptop anymore, and the world around you start changing shapes, everything turns into glitches. ')
							print('Cat:"Hey...You are very kind, just to let you know, I am indeed sorry about what is going to happen next... I know you won\'t forgive me for what I have to do."')

						elif ansHelp3 in ['3','4']:
							print('Cat:"Please don\'t do that again, you are tearing me apart!"')
							ansHelp3=input('')
						else:
							Print('No response. Try another option.')
							ansHelp3=input('')

							#Hollyyyyyy
							#You have enough information to cast the spell and let the player guess password from here



			
