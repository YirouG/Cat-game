# START OF ALL FUNCTIONS

# FUNCTION: Generate password from info cat got from player
def generateCode(name,location,birth):
	code=str(name)[::-1]+str(birth)+str(location)
	return code
# Remove comment to see example of password
# print(generateCode('holly','edmonton',2000))

# # FUNCTION: Reaction when player talk/fee/pat cat
# def cat_reaction(code,times):
# 	if code == 1: #Talk
# 		if(times<2):
# 			print('The cat seems interested. Talk to the cat more')
# 		else:
# 			print('Cat has something for you, talk to her more')
# 	if code==2: #Feed
# 		if(times<2):
# 			print('The cat seems still hungry. Feed the cat more')				
# 		else:
# 			print('The cat is full now. The cat dont want food anymore')
# 	if code==3: #Pat		
# 		if(times<2):
# 			print('The cat show its belly now. Pat the cat more')				
# 		else:
# 			print('Cat seems has enough. Try something else with the cat')	

# # START OF ALL FUNCTIONS

# print('You have 1 new message from Andy:')
# print('Andy: Hey, what\'s up? Do you remember the Tamagotchi game we used to play has just release a desktop version.You have to check it out!')
# response=input('Sooooo, wanna play? Y/N').upper()
# while (response!='Y'):
# 	if response == 'N':
# 		response=input('Oh come on, it would be super fun. It\'s weekend though. Let\'s give it a try. Y/N').upper()
# 	else:
# 		response=input('Nah, give me a proper answer. Type Y for Yes, N for No').upper()	

# # Play type yes
# print('Tamagotchi - Save a cat is downloading....')
# print('.....')
# print('Completed')
# print('Getting started...')
# response=input('Type "Meow" to continue').upper()
	
# while response!='MEOW':
# 	response = input('Oops, Cat does not anything other than cat language. Type "Meow" to continue').upper()

# # 1-Talk 2-Feed 3-Pat
# talk=0
# feed=0
# pat=0

# while talk<3:
# 	response = input("What do you want to do with the cat? 1:Talk 2:Feed 3:Pat")
# 	response=int(response)
# 	if(response==1):
# 		talk=talk+1
# 		print('Talk more')
# 	elif response==2:
# 		cat_reaction(response,feed)
# 		feed=feed+1
# 	elif response==3:
# 		cat_reaction(response,pat)
# 		pat=pat+1
# 	else:	
# 		print('Not go too far')

# # Yirou part

# 	