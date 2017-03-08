from sys import exit
from random import randrange
import os
import rooms

os.system("mode con cols=88 lines=50")

sphinx_room_visit = False
sphinx_intro_visit = False
guess_counter = 3
lava_room_visit = False
lava_intro_visit = False
lava_solve = False
marble_room_visit = False
marble_intro_visit = False
marble_maze_solve = False
obelisk_room_visit = False
obelisk_intro_visit = False
obelisk_solve = False

consonants = ["b", "bl", "br", "c", "ch", "cl", "cr", "d", "dr", "f", "fl",
			  "fr", "g", "gh", "gl", "gr", "h", "j", "k", "kh", "l", "m",
			  "n", "p", "ph", "pl", "pr", "qu", "r", "rh", "s", "sc", "sch",
			  "scr", "sh", "sk", "sl", "sm", "sn", "sp", "spr", "squ", "st",
			  "str", "sw", "t", "th", "thr", "tr", "tw", "v", "w", "wh",
			  "wr", "x", "y", "z"]

vowels = ["a", "e", "i", "o", "u", "y"]


pass1 = ""
pass2 = ""
pass3 = ""
password = ""

def start():
	global sphinx_room_visit, sphinx_intro_visit, lava_room_visit, \
		lava_intro_visit, lava_solve, marble_room_visit, \
		marble_intro_visit, marble_maze_solve, obelisk_room_visit, \
		obelisk_intro_visit, obelisk_solve, pass1, pass2, pass3, password, \
		guess_counter

	pass1 = (consonants[randrange(0, len(consonants))]
		+ vowels[randrange(0, len(vowels))])
	pass2 = (consonants[randrange(0, len(consonants))]
		+ vowels[randrange(0, len(vowels))])
	pass3 = (consonants[randrange(0, len(consonants))]
		+ vowels[randrange(0, len(vowels))])
	password = pass1 + pass2 + pass3

	sphinx_room_visit = False
	sphinx_intro_visit = False
	guess_counter = 3
	lava_room_visit = False
	lava_intro_visit = False
	lava_solve = False
	marble_room_visit = False
	marble_intro_visit = False
	marble_maze_solve = False
	obelisk_room_visit = False
	obelisk_intro_visit = False
	obelisk_solve = False


	entrance()


def entrance():
	rooms.entrance()

	while True:
		choice = raw_input("\n> ")

		if choice == "1":
			print "\nNothing ventured, nothing gained, after all! On you go."
			sphinx_room()
		elif choice == "2":
			print """
You're not getting suckered into one of those goddamn adventure games again.
			"""
			end("left")
		else:
			print "\nPlease just pick a number, for all our sakes."


def sphinx_room():
	global sphinx_room_visit

	if sphinx_room_visit == False:
		rooms.sphinx_long()
		sphinx_room_visit = True
	else:
		rooms.sphinx_short()

	rooms.sphinx_choice()

	while True:
		choice = raw_input("\n> ")

		if choice == "1":
			print "\nYou decide to talk to the sphinx."
			sphinx_puzzle_intro()
		elif choice == "2":
			print "\nYou go through the twisty, narrow passage. Good choice."
			lava_lamp_room()
		elif choice == "3":
			print "\nYou go through the narrow, twisty passage."
			marble_maze_room()
		elif choice == "4":
			print """

You go through the twisty, narrow passage. No, not that one, the other one.
			"""
			obelisk_room()
		else:
			print "\nPlease just pick a number, for all our sakes."


def sphinx_puzzle_intro():
	global sphinx_intro_visit

	if sphinx_intro_visit == False:
		rooms.sphinx_intro_long()
		sphinx_intro_visit = True
	else:
		rooms.sphinx_intro_short(guess_counter)

	while True:
		choice = raw_input("> ")

		if choice == "1":
			sphinx_puzzle()
		elif choice == "2":
			print "\nThe less time spent in proximity to this asshole, the better."
			sphinx_room()
		else:
			print "\nPlease just pick a number, for all our sakes."

def sphinx_puzzle():
	global guess_counter

	human = ["man", "a man", "men", "woman", "a woman", "women", "person",
			 "a person", "people", "human", "a human", "humans", "humanity"]
	wrong_order = [pass1 + pass3 + pass2, pass2 + pass1 + pass3, 
				   pass2 + pass3 + pass1, pass3 + pass1 + pass2,
				   pass3 + pass2 + pass1]
	print """
"What is your answer, mortal?"
	"""

	guess = raw_input("\n> ").lower()

	if guess == password:
		rooms.sphinx_password(guess)

		raw_input("[continue]")

		treasure_room()
	elif guess == pass1 + " " + pass2 + " " + pass3:
		rooms.sphinx_spaced_password()
	elif guess in wrong_order:
		rooms.sphinx_wrong_order()
	elif guess in [pass1, pass2, pass3]:
		rooms.sphinx_partial()
	elif guess in human:
		rooms.sphinx_human()

		end("died")
	elif guess == "":
		rooms.sphinx_no_answer()
	else:
		rooms.sphinx_wrong()

	guess_counter -= 1

	if guess_counter == 0:
		rooms.sphinx_out_of_guesses()

		end("died")

	sphinx_puzzle_intro()


def lava_lamp_room():
	global lava_room_visit

	if lava_room_visit == False:
		rooms.lava_lamp_long()
		lava_room_visit = True
	else:
		rooms.lava_lamp_short()

	rooms.lava_lamp_choice()

	while True:
		choice = raw_input("\n> ")
		
		if choice == "1" and lava_solve == False:
			lava_puzzle_intro()
		elif choice == "1" and lava_solve == True:
			rooms.lava_lamp_solved(pass2.upper())

			raw_input("[continue]")

			lava_lamp_room()
		elif choice == "2":
			rooms.lava_lamp_wall()

			raw_input("[continue]")

			lava_lamp_room()
		elif choice == "3":
			print "\nYeah, that's enough of that for now."
			sphinx_room()
		else:
			print "\nPlease just pick a number, for all our sakes."


def lava_puzzle_intro():
	rooms.lava_puzzle_intro()

	while True:
		choice = raw_input("\n> ")

		if choice == "1":
			lava_puzzle()
		elif choice == "2":
			print "Yeah, good idea, this is dumb."
			lava_lamp_room()
		else:
			print "\nPlease just pick a number, for all our sakes."

def lava_puzzle():
	global lava_solve

	lamp_goal = 1
	lamp_danger = 1

	rooms.lava_puzzle()

	while True:
		rooms.lava_puzzle_choice()

		choice = raw_input("> ")

		if choice == "1":
			lamp_goal +=1
			lamp_danger +=1

			if lamp_danger > 3:
				rooms.lava_puzzle_death()
				end("died")
			
			if lamp_goal == 7:
				rooms.lamp_victory(pass2.upper())
				raw_input("[continue]")
				lava_solve = True

				lava_lamp_room()
			elif lamp_goal in range(1, 7):
				rooms.lamp_progress(lamp_goal)
			else:
				print "Oh god, you've horribly broken something!"
				exit(0)

			rooms.lamp_danger(lamp_danger)

		elif choice == "2":
			if lamp_danger == 0:
				print """
You keep your gaze averted from the lamp a little longer. Doesn't hurt to be
overly cautious, right?
				"""
			else:
				print """
You turn your gaze away from the lamp for a moment. You carefully maintain
your state of like, groovy open-mindedness, man, but that awful stretchy
feeling in your brain seems to recede.
				"""
			lamp_danger = 0
		elif choice == "3":
			print """
That's all the unwarranted 60's nostaligia you need for one day.
			"""

			lava_lamp_room()
		else:
			print "Please just pick a number, for all our sakes."


def marble_maze_room():
	global marble_room_visit

	if marble_room_visit == False:
		rooms.marble_maze_long()
		marble_room_visit = True
	else:
		rooms.marble_maze_short()

	rooms.marble_maze_choice()

	while True:
		choice = raw_input("> ")

		if choice == "1" and marble_maze_solve == False:
			marble_maze_intro()
		elif choice == "1" and marble_maze_solve == True:
			rooms.marble_maze_solved(pass3.upper())

			raw_input("[continue]")
			marble_maze_room()
		elif choice == "2":
			rooms.marble_maze_wall()

			raw_input("[continue]")

			marble_maze_room()
		elif choice == "3":
			print "\nLet's blow this popsicle stand."
			sphinx_room()
		else:
			print "\nPlease just pick a number, for all our sakes."


def marble_maze_intro():
	global marble_intro_visit

	if marble_intro_visit == False:
		rooms.marble_intro_long()

		marble_intro_visit = True
	else:
		rooms.marble_intro_short()

	while True:
		choice = raw_input("> ")

		if choice == "1":
			print """
You plunk the marble into the hole.


Which way will you tilt the slab?"""

			marble_maze()
		elif choice == "2":
			print "Eh, you're really not feeling it right now."
			marble_maze_room()
		else:
			print "Please pick a number, for all our sakes."

def marble_maze():
	global marble_maze_solve

	position = 1

	forward = [["1", 1], ["2", 2], ["4", 3], ["3", 4], ["1", 5], ["2", 6],
			    ["4", 7], ["3", 8]]
	backward = [["4", 2], ["1", 4], ["2", 5], ["1", 8]]
	failure = [["2", 1], ["3", 1], ["3", 2], ["3", 3], ["4", 5], ["3", 6],
			   ["4", 6], ["3", 7], ["2", 8], ["2", 9], ["4", 9]]
	nothing = [["4", 1], ["1", 2], ["1", 3], ["2", 3], ["2", 4], ["4", 4],
			   ["3", 5], ["1", 6], ["1", 7], ["2", 7], ["4", 8], ["3", 9]]
	victory = ["1", 9]

	while True:
		print """
  1. Up
  2. Left
  3. Right
  4. Down
  5. I've had about all of this I can take.

		"""
		choice = raw_input("> ")

		if [choice, position] in forward:
			position +=1
			print "\nYou hear a rolling sound, which ends with a soft thunk."
		elif [choice, position] in backward:
			position -=1
			print "\nYou hear a rolling sound, which ends with a soft thunk."
		elif [choice, position] in failure:
			print """
You hear a rolling sound, then a rattling clunk, then more rolling. A moment
later the marble falls out into the return slot, mocking you.
			"""

			raw_input("[continue]")

			marble_maze_intro()
		elif [choice, position] in nothing:
			print "\nNothing seems to happen..."
		elif [choice, position] == victory:
			rooms.marble_maze_victory(pass3.upper())

			marble_maze_solve = True
			raw_input("[continue]")
			marble_maze_room()
		elif choice == "5":
			rooms.marble_maze_leave()
			marble_maze_room()
		else:
			print "Please pick a number, for all our sakes."

def obelisk_room():
	global obelisk_room_visit

	if obelisk_room_visit == False:
		rooms.obelisk_long()

		obelisk_room_visit = True
	else:
		rooms.obelisk_short()

	rooms.obelisk_choice()

	while True:
		choice = raw_input("> ")

		if choice == "1" and obelisk_solve == False:
			obelisk_puzzle_intro()
		elif choice == "1" and obelisk_solve == True:
			rooms.obelisk_solved(pass1.upper())

			raw_input("[continue]")

			obelisk_room()
		elif choice == "2":
			rooms.obelisk_wall()

			raw_input("[continue]")

			obelisk_room()
		elif choice == "3":
			print "\nYeah, no thanks. The obeliskine wiles have been resisted."
			sphinx_room()
		else:
			print "Please just pick a number, for all our sakes."

def obelisk_puzzle_intro():
	global obelisk_intro_visit

	if obelisk_intro_visit == False:
		rooms.obelisk_intro_long()

		obelisk_intro_visit = True
	else:
		rooms.obelisk_intro_short()

	rooms.obelisk_intro_choice()

	choice = raw_input("> ")

	if choice == "1":
		print """
You step forward with determination. Let's do this.
		"""
		obelisk_puzzle()
	elif choice == "2":
		print "Probably a wise decision."

		obelisk_room()
	else:
		print "Please just pick a number, for all our sakes."

def obelisk_puzzle():
	global obelisk_solve
	tile_list = ["Plant", "Sun", "Person", "Hourglass", "Goat"]
	solution = []

	for i in range(1, 6):
		print "Which tile do you place?\n"
		for j in tile_list:
			print " ", (tile_list.index(j) + 1), "\b.", j

		while True:
			try:
				choice = int(raw_input("\n> "))

				if choice in range(1, len(tile_list) + 1):
					break
				else:
					print "Please pick a number, for all our sakes."
			except ValueError:
				print "Please pick a number, for all our sakes."

		for k in range(1, len(tile_list) + 1):
			if k == choice:
				print "You slide the %s tile into the slot.\n" % \
				tile_list[k - 1].lower()

				solution.append(tile_list.pop(k - 1))

	if solution == ["Hourglass", "Person", "Goat", "Plant", "Sun"]:
		rooms.obelisk_victory(pass1.upper())

		obelisk_solve = True
		raw_input("[continue]")

		obelisk_room()
	elif solution.index("Person") == 0:
		rooms.obelisk_wrong()

		raw_input("[continue]")

		obelisk_puzzle_intro()
	elif solution[solution.index("Person") - 1] == "Goat":
		rooms.obelisk_goat_death()

		end("died")
	elif solution[solution.index("Person") - 1] == "Plant":
		rooms.obelisk_plant_death()

		end("died")
	elif solution[solution.index("Person") - 1] == "Sun":
		rooms.obelisk_sun_death()

		end("died")
	else:
		rooms.obelisk_wrong()
		raw_input("[continue]")
		obelisk_puzzle_intro()

def treasure_room():
	rooms.treasure()

	while True:
		choice = raw_input("> \n")

		if choice == "1":
			rooms.resigned_end()

			win()
		elif choice == "2":
			rooms.angry_end_1()
			raw_input("[continue]")
			rooms.angry_end_2()

			win()
		elif choice == "3":
			rooms.hidden_end_1()
			raw_input("[continue]")
			rooms.hidden_end_2()

			win()
		else:
			print "Please just pick a number, for all our sakes."

def end(end_type):
	if end_type == "left":
		rooms.left_end()
	else:
		rooms.dead_end()

  	while True:
  		choice = raw_input("> ")

  		if choice == "1":
  			start()
  		elif choice == "2":
  			print "Don't let the door hit you on the way out."
  			exit(0)
  		else:
  			print "Please just pick a number, for all our sakes."


def win():
	rooms.win()

	while True:
  		choice = raw_input("> ")

  		if choice == "1":
  			start()
  		elif choice == "2":
  			print "Don't let the door hit you on the way out."
  			exit(0)
  		elif choice == "3":
  			rooms.random_stuff()
  		else:
  			print "Please just pick a number, for all our sakes."

start()