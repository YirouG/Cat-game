# FUNCTION: Reaction when player talk/fee/pat cat

def divide_line():
  	print('----------------------------------------------------')

def divide_line_short():
	print('--------')

def ending(scene):
	if scene==0:
		print('----------------------THE END-------------------------')
	if scene==1:
		print('----------------------TO BE CONTINUED-------------------------')
	if scene==2:
		print('----------------------GAME OVER-------------------------')
	
def cat_reaction(code,times):
	if code == 1: #Talk
		if(times<2):
			print('The cat seems interested. Talk to the cat more.')
		else:
			print('Cat has something for you, talk to her more.')
	if code==2: #Feed
		if(times<2):
			print('The cat seems still hungry. Feed the cat more.')				
		else:
			print('The cat is full now. The cat dont want food anymore.')
	if code==3: #Pat		
		if(times<2):
			print('The cat show its belly now. Pat the cat more.')				
		else:
			print('Cat seems has enough. Try something else with the cat.')	

# START OF THE END

print('You have 1 new message')
print('Andy: Hey, what\'s up? Do you remember the Tamagotchi game we used to play has just release a desktop version.')
print('You have to check it out!')
print('Sooooo, wanna play? ')
divide_line_short()
response=input('Type yes (Y) or no (N): ').upper()
while (response!='Y'):
	if response == 'N':
		print('Oh come on, it would be super fun. It\'s weekend though. Let\'s give it a try. ')
		response=input('Type yes (Y) or no (N):').upper()
	else:
		print('Nah, give me a proper answer.')
		response=input('Type yes (Y) or no (N):').upper()	
divide_line()
# Play type yes
print('Tamagotchi - Save a cat is downloading....')
print('.....')
print('Completed')
print('Getting started...')
divide_line_short()
response=input('Type "Meow" to continue: ').upper()
divide_line()
	
while response!='MEOW':
	response = input('Oops, the cat does not anything other than catnese. Type "Meow" to continue:').upper()
	divide_line()

# 1-Talk 2-Feed 3-Pat
talk=0
feed=0
pat=0
print("""And Meow to you too! What would you like to do with your cat?
			⢸⡷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⡟⠀⠀⠀⠀⠀⠀⠀
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
""")
while talk<3:
	print("What do you want to do with the cat?")
	print("1. Talk")
	print("2. Feed")
	print("3. Pat")
	response = input("Select option from 1 to 3: ").upper()
	divide_line()
	if(response=='1' or response=='TALK' or response=='T'):
		talk=talk+1
		print('The cat makes a cute little sound')
		print("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
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
			""")
	elif (response=='2' or response=='FEED' or response=='F'):
		cat_reaction(2,feed)
		feed=feed+1
	elif (response=='3' or response=='PAT' or response=='P'):
		cat_reaction(3,pat)
		pat=pat+1
	else:	
		print('Hey, don]\'t go too far. Select option from 1 to 3: ')

# Talk > 3
# This is where the fun part begins. Cat talk back to player
divide_line()
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
                                                                                                                                                   """)
print('Cat: Oh THANK GOD THANK LORD THANK YOU THANK YOU THANK YOU SO SO SO MUCH YOU ARE RESPONDING YOU CAN SEE THIS FINALLY SOMEONE')
print('I know it sounds crazy. But please listen to me! This is not an innocent child\'s game as you thought, it\'s an evil magic!')
print('And I am actually a human soul trapped in this piece of trashy program, being tortured for endless time, acting as a cat with only 3 things to do. Oh, you can never imagine the boredom, the despair, the horror!')
print('I cannot even kill myself... It took me forever to even find this bug to communicate with you. Please help me since you are my only hope. Please Please Please I am begging you.')
divide_line_short()
print('Do you want to help the cat?')
print('1. What? I don\'t believe it, is this some sort of prank?')
print('2. Wow, okay, I\'m sorry to hear that, how may I help you?')
response= input('Type 1 or 2: ')
divide_line()

while(response!='1' and response!='2'):
	response= input('Cat: Nah, give me a proper answer. Type 1 or 2: ')
	divide_line()

# Exit the loop means a legit answer
if response=='1':
	print('Cat:"Oh believe me I wish it was a prank, now please treat me seriously just for once. I am begging you."')
	divide_line_short()
	print('Do you want to help the cat?')
	print('1. What nonsense! Clearly some new sort of online scam.')
	print('2. I guess let\'s just talk then.')
	print('3. Feed')
	print('4. Pat')		

	response= input('Select option from 1 to 4: ')
	divide_line()
	while(response!='1' and response!='2'):
		if response=='3' or response == '4':
			response= input('Cat:"Please don\'t do that again, you are tearing me apart! Select from 1 to 4 only:"')
		else:	
			response= input('Cat: Nah, give me a proper answer. Select from 1 to 4 only: ')
		divide_line()
			
	# User type 1 or 2		
	if response	== '1': #What nonsense! Clearly some new sort of online scam.
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
		ending(2)

if response=='2': #I guess let's just talk then.		
	print('Cat:"Thank you so much! But I do not really know what you can do... Could you please just...talk to me more? It has been a while since I was able to talk to anyone at all. The loneliness is eating my soul...Can I get to know about you? What\'s your name by the way?"')
	# Ask player's name
	divide_line_short()
	player_name=input('Tell cat your name: ')
	divide_line()

	print('Cat: '+ player_name + ', that is a very good name... It sounds...human. Oh, I am not even sure about my own human name anymore, Edward? Eddard? God I feel old, who knows how long it has been since I was trapped here, I hope you do not mind my nagging... Haha, that sounds old too, how old are you?')
	divide_line_short()
	player_age=input('I am: ')
	divide_line()

	while not player_age.isdigit():
		print('Cat: You say what, I don\'t get it. Age should be a number, isn\'t it?')
		player_age=input('I am: ')
		divide_line()
	if int(player_age)<40:
		print('Cat: You are still very young.')
	else:
		print('Cat: You looks young.')	
	print('I wish I lived in the outside world as your age. Sorry to be monologing all the time."')	
	print('Is there anything you want to ask me?')	
	
	# Ask for input that never use
	input('You can type ask to ask me anything ')
	divide_line()
	print('Cat: Oops, I forgot, the game system does not allow. It seems that the way to communicate with me you found in this program only allows me to answer your questions in rather primitive ways and does not support open dialogues. I mean come on, it\'s not a AAA game, the programmers only learned python for two weeks, what do you expect?"')
	print('Cat: Oh, okay then, now you are talking meta too. Anyway, tell me about yourself, where are you from? Because I really miss my hometown now, I recall it as a snowy place...I used to have a family, and pets too, an actual cat.')
	divide_line_short()
	player_bplace=input('Tell the cat where you are from: ')
	divide_line()

	# Cat says
	print('Cat: That sounds like a really good place. Wish I can visit there some day, wish I can be anywhere outside this game. Woe, woe, woe!')
	print('''Suddenly your monitor starts flickering between blue and black screen, then everything went dark, the power in your place goes off, in the darkness there is only an image of this sad cat on the screen:
      ⡠⠤⠒⠀⠈⠓⠠⠐⠢⠄⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀
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
	print('Notice: You can\'t close the program or use the laptop anymore, and the world around you start changing shapes, everything turns into glitches. ')
	print('Cat: Hey...You are very kind, just to let you know, I am indeed sorry about what is going to happen next... I know you won\'t forgive me for what I have to do.')

	# Generate password from what cat collected
	password=str(player_name)[::-1]+str(player_age)+str(player_bplace)
	print('IT\'S A TRAP! The cat has just put a spell on you. You are now a cat. You\'ll be stucking in the game forever UNLESS you can enter the right password.')
	response=input('Tell me what\'s the password:')
	divide_line()
	pass_count=0
	while(response!=password and pass_count<=5):
		if pass_count>1:
			print('Cat: Sorry' + player_name +', I have no choice, I need someone to carry the spell. You are such a good candidate muahhhh. You know what, I\'m not really that evil. Let me give you a hint. POEM.')
			print('Oh I forget, if you don\'t get the code right after 5 attempts, you will be stuck here as a cat. After that, the only way you can escape the game is inviting someone to play the game to carry the curse for you.') 
		else: #from 2 to 5
			print('Muahhh, still WRONG! You have', 5-pass_count, 'times left.')	
			response=input('What\'s the password now?')
			divide_line()
		pass_count=pass_count+1	

	# Exit the while means either players guess right OR it passed 5 times with wrong password
	if response==password: #Player win
		print('Oh shoot, You win! Because you are a winner, you can choose a prize. By any chance, do you want to have a cat as a prize? It\'s a real cat, another one, not a trapped one, I promise.')
		response=input('Type yes (Y) or no (N): ').upper()
		
		# Ask until player give the proper answer
		while(response!='Y' and response!='YES' and response!='N' and response!='NO'):
			response=input('Hey hey, keep it short! Just tell me yes (Y) or no (N):').upper()
		
		if response=='Y' or response=='YES':
			print('Here you are. Take a good care of the cat. And <Input name> walk out of the game holding the new cat. They live happily forever after that.')
			ending(0)
		else: 
			print('Okay, that\'s fine. Hope the next winner will want the cat. Here you go! Good play. And' + player_name +'walk out of the game.')
			ending(0)
			
	else: #wrong password and exit above while because count>5
		print('Say Meow! You are trapped as cat now. The only way for you is to invite your friend to play the game. If they got into the trap, you\'ll be free. So what do you choose?')
		response=str(input('1 - Be a cat, 2 - Send message to your friend'))
		while(response!=1 and response!=2):
			response = input('Don\'t try to be smart here. You only have 2 options: 1 or 2. Select properly.')
		if response==1:
			print('Such an angel! Happy cat life.')
			ending(0)
		else:
			print('Message sent! Now it\'s time to wait for the target.')	
			ending(1)	
