import os
def start():
	print'Welcome to Pokemon Battle simulator'
	os.popen('aplay battle.mp3')
def moves_list():
	x = raw_input('what is your pokemone type')
	if x == 'Grass':
		print"""
These are your moves:
	1. Leaf storm it does 5 damage 
	2. Weed Whacker it does 5 damage 
 	3. leaf throw throws a leaf aka canadian at the pokemon does 10 dmg 
	4. mexican lawn mowing service does nothing except it self destructs
 """
	if x =='jew':
		print"""
These are your moves as the jew pokemon type
	1. Shekel steal it does 3 damage 
	2. Shekel trade it does 7 damage
	3. Shekel throw it does 1 damage
	4. Become a Banker and own the world does INFINATE DAMAGE
	"""
def menu():
	pokemon = raw_input('Enter your pokemon name')
	pokemontype= raw_input('Enter your pokemons type')
def battle(type):
	if type=='Grass':
		print'this is still being worked on pls no syntax error'
	
def Grass():
	if pokemontype== 'Grass':
		x=raw_input('are you ready to start the battle')
		if x== 'yes':
			battle('Grass')
		if x == 'no'
			quit()
			print'kys filthy jew'		 
def jew_type():
	if pokemontype == ('jew'):
	print'are you sure this is your choice if you want to read more type moves_list to get a full moves list of every pokemon type move set'
	x= raw_input(' Do you want to switch pokemon type'):
		if x == 'yes':
			menu()
		if x== 'no'
			battle(type)

def Rock():
    
	
