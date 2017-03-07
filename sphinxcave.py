from sys import exit
from random import randrange
import os

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
	print """
You stand just inside the mouth of a cave. Across from you, a passageway
disappears into darkness. You have a gut feeling that down that passageway
lies great riches - or at least a decent way to kill a couple of hours. Of
course, you figure there's probably also a dozen or so stupid ways to die,
because you know how these things work.


Will you venture into the darkness?

  1. Eh, why not. Venture away.
  2. Venture shmenture. I'm going home.
	"""

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

	bones = ["femur", "skull", "spine", "kneecap", "finger", "rib", "pelvis"]

	if sphinx_room_visit == False:
		print """
The walls give way to a large central chamber. As soon as you step fully
inside, you hear a loud BANG behind you. Whirling, you find - ugh, yep, the
passage you came from is now sealed shut by a ten ton slab of granite.
Typical.

Well, if you're going to be stuck here for the foreseeable future, you might
as well take a look around. Narrow tunnels branch off from the corners of the
room to the north-ea- no, wait, south-ea- well, it could be... It suddenly
occurs to you that you should've brought a compass. You hope this cave isn't
too big, or you'll likely get lost and slowly starve to death before you
manage to complete all the stupid inevitable puzzle bullshit.

Ahem. Well, for now, you'll have to distinguish the tunnels by sight.

Smack-dab in the center of one wall is a large, ornate golden door, with
the words "HEARE BE TREASEURE" written over it by someone with a fondness for
extraneous vowels. Well, treaseure is what you're here for, so you should
probably aim to get in there.

Unfortunately, the door is under guard. The long, lithe body of a
ludicrously large lion lies lazily before the... lentrance. Damn, you
almost had it. Once you stop twisting your brain to come up with forced
alliteration, you realize the lion also has a pair of big-ass wings and a
woman's head, which is smiling mysteriously at you.

Goddamn it. You hate riddles!
		"""
		sphinx_room_visit = True
	else:
		print """
The central chamber remains just as you left it. The sphinx still lounges in
front of the treasure - er, treaseure - room door, tail flicking every once
in a while. She's currently chewing peacefully on what appears to be a human
%s, making happy lip-smacking noises.

Sphinxes are terrible.
		""" % bones[randrange(0, len(bones))]

	print """
What will you do?

  1. Talk to the sphinx.
  2. Take the twisty, narrow passage.
  3. Take the narrow, twisty passage.
  4. Take the other twisty, narrow passage.
	"""

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
		print """
You approach the sphinx, trying not to grimace. She continues to smile
enigmatically.

"Hail, Sphinx," you say grudgingly.

"Well met, traveller," she replies. "What is it you desire?"

"I wish to pass into yonder treasure room."

"Treasure room?" she asks, puzzled. "What treasure room?"

You sigh. "Fine. 'Treaseure' room."

You didn't even really pronounce it differently, but the sphinx appears to
understand. "Ah yes," she says. "Many have sought the riches beyond. But
before you pass, you must answer my-"

"Your riddle, yes, I get the idea," you say impatiently. "Let's just get this
over with."

Her tail flicks, agitated, and she frowns at the interruption, but she shakes
her head and continues. "So be it. Listen to my riddle, and tell me the
answer. You shall be allowed three guesses. I was going to give you five, but
since you're in such a hurry..."

God you hate sphinxes.

She clears her throat and states:

  "I walk on four legs in the morning,
  Six legs in the afternoon,
  And twelve legs in the evening.
  What am I?"


Will you venture a guess?

  1. Answer the riddle.
  2. Leave.
		"""

		sphinx_intro_visit = True
	else:
		if guess_counter == 1:
			guess_string = "only have one guess left."
		elif guess_counter == 2:
			guess_string = "have two guesses remaining."
		elif guess_counter == 3:
			guess_string = "still have three guesses. For now."

		print """
The sphinx gleefully repeats herself:

  "I walk on four legs in the morning,
  Six legs in the afternoon,
  And twelve legs in the evening.
  What am I?"

Oh, and keep in mind, you %s


How about it?

  1. Try a guess.
  2. Get away from the sphinx.
		""" % guess_string

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
		print """
The sphinx looks surprised for a moment, but then her smile returns.

"Ah, the noble %s! The moment they hatch from their eggs, they
live a life of fear and desperation. Clinging to the ground with their
four hind legs, they lift the front two to the sky, pleading with the
heavens. 'Oh please, please let me live!' they cry, waving their appendages
in supplication! Unfortunately this gesture has a tendency to attract
predators like a beacon, but the few grublings who manage to reach
adulthood attribute their survival to the mercy of the gods, and so the
practice continues.

"Emerging from their time as a weak and helpless creature, the adult
%s becomes a fearsome, murderous rage-beast! They relentlessly
seek out others of their kind to duel in cruel and barbarous deathmatches!
The mandibles of a %s are, in fact, specialized and perfectly
suited to the decapitation of fellow %s. This, of course,
dramatically culls the population further still, so that only a few hardy,
ruthless, vicious individuals survive to their twilight years.

"And then! Once the surviving few have interbred and continued to idly
murder one another until the next generation has grown to adulthood, the
wizened progenitors are ceremonially paraded on the backs of their
children all the way to their funeral pyres, where they are less
ceremonially dumped."

The sphinx shakes her head, wiping a tear from her eye with one dinner-
plate-sized paw. "Nature is truly beautiful, isn't it?"

You have no response.

The sphinx collects herself. "Indeed, mortal. You have answered my riddle
and surpassed this challenge. You may pass." She steps aside, unbarring
the way forward.

Time to collect your loot!
		""" % (password, password, password, password)

		raw_input("[continue]")

		treasure_room()
	elif guess == pass1 + " " + pass2 + " " + pass3:
		print """
The sphinx gives you an odd look. "That's... do you have the hiccups or
something? Or a speech impediment?"

You scowl.

"No? Well, the answer is only one word, you know. I hope you realize my
magnanimity in offering such an important hint. But I'm afraid I can't
accept this answer. Say it right or don't say it at all."
		"""
	elif guess in wrong_order:
		print """
"Er, that's... close. In a manner of speaking," the sphinx says. "Maybe you
ought to reconsider the information available to you."

"What the hell does that mean?" you ask.

"It means you found all the puzzle pieces and then superglued them together
like an idiot," she sniffs. "That's another guess down the drain for you."
		"""
	elif guess in [pass1, pass2, pass3]:
		print """
"Absolutely not," the sphinx huffs. "Did you really think you could come
running here with the answer after solving one measly puzzle? Hmph. You've
discovered but part of the whole. Come back once you've discovered the TRUE
answer."
		"""
	elif guess in human:
		print """
"Were you even listening to me at all?" the sphinx growls. "Do you think we
only have a single riddle to give to every passing idiot who can memorize
a word?"

She rises to her feet, eyes narrowing. You get a sinking feeling in your
stomach. She is really quite big.

"This has been one insult too far. I don't care how many guesses you have
left; this ends now."

She looms above you, jaws opening wide. Your final thought is that normal
lady heads don't have nearly that many teeth...

		"""

		end("died")
	elif guess == "":
		print """
"No response?" the sphinx says, raising a brow. "Ah-ah-ah - you won't get
out of this so easily. You agreed to guess, and so a guess you have used."

She fluffs her wings a little in a satisfied manner. "Oh, and for the record,
no, the answer is not nothing."
		"""
	else:
		print """
"Wrong, wrong, so very, very wrong," the sphinx replies with a grin. "A
wasted guess; such a shame."

You see a glint of teeth in her smile.
		"""

	guess_counter -= 1

	if guess_counter == 0:
		print """
The sphinx gets to her feet, stretching out her wings. They're each twice as
long as you are tall. Suddenly you feel very small.

"That," she says with relish, "was your last guess, mortal. Any final words?"
She looms ominously above you.

"Um," you say meekly. "...Do over?"

The last thing you see is an abundance of extremely sharp teeth.
		"""

		end("died")

	sphinx_puzzle_intro()


def lava_lamp_room():
	global lava_room_visit

	if lava_room_visit == False:
		print """

As you travel along the passage, you spy an eerie red glow coming from the
exit. Oh god, please don't let it be lava. You are completely unequipped to
handle lava, even the narratively convenient kind that doesn't heat the air
and can only hurt you if you touch it.

Well, too late to turn back now.

Emerging from the tunnel, you discover that the glow is not the product of
lava... exactly.

A gigantic lava _lamp_ dominates the center of the chamber, stretching all
the way to the ceiling, which you estimate to be about forty feet high - not
that your estimate counts for much; you've always been terrible with
distances.

The point is, it's a huge lamp, much larger than any lava lamp was ever meant
to be. Privately, you believe such a random and anachronistic object is a
sort of humor better suited to a 1980's Infocom game than here. Modern
sensibilities prefer genre-savvy protagonists and a great deal of fourth-wall
breaking - or so you've heard.

But here it is, and you suppose you're just going to have to deal with it.


How will you deal with it?
		"""

		lava_room_visit = True

	else:
		print """

The lava lamp stands tall in the middle of the room, the novelty-sized time-
traveler from the late 60's acting as a silent sentinel over all it surveys,
which is almost nothing.

A globule detaches itself from the bottom of the lamp with a bass "blorp"
sound and floats ponderously upward.


What will you do?
		"""

	print """

  1. Guess I should check out that lamp.
  2. Ignore the lamp. Look at something that isn't the lamp.
  3. Leave; this room is stupid.
		"""


	while True:
		choice = raw_input("\n> ")
		
		if choice == "1" and lava_solve == False:
			lava_puzzle_intro()
		elif choice == "1" and lava_solve == True:
			print """
As you turn toward the lamp, an image - no, a memory of an image floods into
your brain: a six-legged insectoid creature decapitating one of its fellows,
possibly in ritual combat over resources or for control of its tribe? Or
possibly because it's just a colossal asshole.

You also get a weirdly strong impression of letters:

                                  "%s"

Continuing to look at the lamp is making you queasy for some reason, so you
avert your eyes.
			""" % pass2.upper()

			raw_input("[continue]")

			lava_lamp_room()
		elif choice == "2":
			print """

There's nothing else in the room except that goddamn lamp, but you're a
stubborn one, so you look at the walls instead. Fuck you, lamp.

This turns out to be less stupid and petty than it appeared, as you realize
that what you thought were merely some random pits and cracks are, in fact,
letters, etched shallowly into the wall. You squint to read them:

                     I     D  E  V  O  U  R     A  L  L
                            I   D  E  V  O  U  R
                               I  D E V O U R
                                  I DEVOUR
                       (i am devoured; i will devour)

Well. That's... unsettling. You throw a wary glance over at the lava lamp.
Its large, glowing presence seems no more -- or less -- sinister than before.
			"""

			raw_input("[continue]")

			lava_lamp_room()
		elif choice == "3":
			print "\nYeah, that's enough of that for now."
			sphinx_room()
		else:
			print "\nPlease just pick a number, for all our sakes."


def lava_puzzle_intro():
	print """

Giant globules of something that is most assuredly not lava float up and down
within the lamp, which is basically what you expected.

Still, there's something strangely compelling about it...

  1. Stare into the lamp.
  2. Nah, let's do something else.
	"""

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

	print """
You peer into the lamp. Out of place and comically oversized or not, there is
something soothing about the gentle glow and drifting globules of... whatever
lava lamp lava is made of.

Out of the corner of your eye, you think you catch a glimpse of something in
the depths of the lamp. But when you shift your gaze, there is nothing there.

You feel a twinge of pain in your temple. Ugh, this is a terrible time for a
headache. Why do none of the adventurer's guides remind you to bring aspirin?
	"""

	while True:
		print """
What will you do?

  1. Gaze into the lamp.
  2. Look away from the lamp.
  3. Yeah, I'm done with this.
		"""

		choice = raw_input("> ")

		if choice == "1":
			lamp_goal +=1
			lamp_danger +=1

			if lamp_danger > 3:
				print """
The bizarre stretched feeling in your head reaches a crescendo as the bonds
desperately trying to hold your mind together finally reach their limit and
snap.

A feeling of serenity washes over you.

You gaze up at the enormous lamp. Forty seconds it has taken you to learn what
kind of light is hidden within the glowing goop. O cruel, needless misunder-
standing! O stubborn, self-willed exile from the loving breast! Two salty
tears trickle down the sides of your nose. But it's all right, everything is
all right, the struggle is finished. You have won the victory over yourself.

You love lamp.
				"""

				end("died")

			if lamp_goal == 1:
				print """
You peer into the lamp. Out of place and comically oversized or not, there is
something soothing about the gentle glow and drifting globules of... whatever
lava lamp lava is made of.
				"""
			elif lamp_goal == 2:
				print """
It's actually a little relaxing, really, watching the blobby shapes form and
reform inside the lamp. You watch for a while.

Out of the corner of your eye, you think you catch a glimpse of something in
the depths of the lamp. But when you shift your gaze, there is nothing there.
				"""
			elif lamp_goal == 3:
				print """
You're starting to see patterns in the shapes sometimes - kind of like
watching clouds. Blobs of water vapor, blobs of... wax, maybe? - what's the
difference, really, you know?

Every once in a while you feel like you can almost see something more, but it
continues to evade your grasp.
				"""
			elif lamp_goal == 4:
				print """
Lamps, clouds, nature, like, humanity in general - it all CONNECTED, you know?
You think you're onto something there.

Okay, there is definitely something flickering at the edges of your vision.
Every time you try to look, though, it just drifts away, like the floaters in
your eyes.
				"""
			elif lamp_goal == 5:
				print """
Maybe it IS the floaters in your eyes, you know? Like, your eyes are becoming
one with the lamp. One with the UNIVERSE, man...

Wait, no, that's not a floater. Unless you're seeing pictures in your
floaters now, which hey, maybe you are, you know? Pictures in clouds, pictures
in lava lamps, pictures in floaters...

A dim part of your consciousness recognizes that this is fucking stupid, but
you shrug it off. Don't be a hater, brain.

If you stare straight ahead into the depths of the lamp, you can ALMOST see
it coming into focus in your peripheral vision...
				"""
			elif lamp_goal == 6:
				print """
Life... creation... circles... no, wait, cubes. Simultaneous 24-hour... you
almost had it there...

Your body relaxes. Your mind expands. You feel at one with the universe. You
almost understand, man. You almost GET it. Like... everything. You know?

At the edges of your vision a picture is forming... 
				"""
			elif lamp_goal == 7:
				print """
Your mind opens. You are one with the universe. Not just your eyes - all of
you.

A picture forms in front of you, within the depths of the lamp - no, within
your own mind, channeled by the lamp... well, the logistics don't matter.
What matters is that the image comes to you with perfect ease and perfect
clarity. It's so simple! Everything is so simple now...

A six-legged insectoid creature stands, legs planted firmly in the dirt as it
uses its sharp and wicked-looking mandibles to slice off the head of some
less fortunate insectoid. It is clearly the alpha bug.

Beneath the image you get a strong impression of letters:

                                  "%s"

As you look at the image, your sense of reason boils to the surface in a
crescendo of bafflement and completely severs your connection to the universe.

You blink, and once again you are merely human: one singular human standing
in a cavern with a giant lava lamp. Also you have a crick in your neck.

What the fuck were you doing for the past... four hours?
				""" % pass2.upper()

				raw_input("[continue]")

				lava_solve = True
				lava_lamp_room()
			else:
				print "Oh god, you've horribly broken something!"
				exit(0)

			if lamp_danger == 1:
				print """
You feel a twinge of pain in your temple. Ugh, this is a terrible time for a
headache. Why do none of the adventurer's guides remind you to bring aspirin?
				"""
			elif lamp_danger == 2:
				print """
Okay, yes, ow, definitely a headache. Or a head... something, at any rate.
It reminds you of half-remembered geology lessons about tectonic motion slowly
spreading the continents apart, except in this scenario, the continents are 
pieces of your brain.
				"""
			elif lamp_danger == 3:
				print """
Your eyelid twitches, and you may or may not begin to drool slightly. Your
mind has expanded so quickly it feels like your consciousness is getting the
bends. You wonder if that might maybe be something to worry about.
				"""
			else:
				print """
I don't know how you got a negative value here but I'm shutting down
everything. EVERYTHING DAMMIT!
				"""

				exit(0)

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
		print """
After navigating an annoying series of switchbacks of a width clearly not
designed to accomodate an adult human, you mercifully emerge into a new
chamber.

Its main feature is a large, raised slab of stone in the center, rectangular
and perfectly flat on top - the sort of stone that would make a perfectly
workable altar for human sacrifice, though it would be a bit of a pain to
clean. Not that you would know anything about that, of course.

Given the lack of suspicious stains, the slab has probably never been used
for such a purpose, anyway. At least not by design, and not by anyone
without a copious amount of bleach on hand. Its intended purpose probably
has something to do with the pair of levers sticking out of the floor in
front of it.

The far wall appears to be decorated with a series of faintly glowing
pillars.
		"""
		marble_room_visit = True
	else:
		print """
The pillars on the far wall lend a faint red tinge to everything in here - 
though "everything" is really just the stone slab in the center which, to
your knowledge, continues to not have been used for human sacrifice. What a
waste.

Not that you'd know, or anything.
		"""

	print """
What will you do?

  1. Check out that not-altar.
  2. Examine the pillars.
  3. Go do something else. Anything else.
  	"""

	while True:
		choice = raw_input("> ")

		if choice == "1" and marble_maze_solve == False:
			marble_maze_intro()
		elif choice == "1" and marble_maze_solve == True:
			print """
On the slab is a picture of a six-legged insect creature riding on the backs
of two of his fellows. Beneath the picture are letters:

				"%s"

The levers are still locked in place, and you have no clue how to unlock
them, so they're locked for good. You've done everything you can here.
			""" % pass3.upper()

			raw_input("[continue]")
			marble_maze_room()
		elif choice == "2":
			print """
Each pillar consists of a stone base and capital and, more importantly, a
bright red shaft, which does indeed appear to be glowing from within. You
pause for a moment to consider the Freudian implications of this, until you
realize that your thoughts are just the word "penis" over and over. You
shake your head to clear it.

The pillars are arranged thusly:

                                III III I

The asymmetry of it annoys you.
			"""

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
		print """
You approach the raised stone and, like the cautious adventurer you are,
immediately start fiddling with the levers.

To your surprise, the levers actually tilt the platform - one controls left
and right, the other forward and back. Well, that's not the MOST interesting
thing the levers could have done, but it's firmly non-lethal, so you're
inclined to feel positively about it.

You also notice a round hole in the top of the slab, near the center of the
edge nearest you. Directly beneath it is an indentation in the side of the
slab reminiscent of a pool ball return, and sitting inside that is a marble
the size of a softball - which, incidentally, is about the size of the hole.


What will you do?

  1. Marble go down the hole.
  2. Something more exciting than this.
		"""

		marble_intro_visit = True
	else:
		print """
You take the marble out of the return slot and give it a couple contemplative
tosses.


What will you do with it?

  1. Chuck it in the hole.
  2. Put it back and do something else.
  		"""

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
			print """
There is a clunk of a slightly different timbre than any you've heard so
far, and your controls suddenly lock up. Aw, shit - did you just break it?

The slab begins to rumble. That's... probably bad. Rumbling is often
the first sign of a horrifying death trap, right? Maybe you should just-

Suddenly, the slab flips end over end. There's a click, and the rumbling
stops. Phew.

The newly revealed face of the slab has a bizarre picture painted on it. An
ugly, six-legged, insectoid creature - who, frankly, looks like it's seen
better days - stands with three feet each firmly planted on the backs of two
other members of its species, who bear the indignity stoically. Sucks to be
them.

Beneath the picture, like an incomprehensible inscription, are letters:

                                 "%s"
			""" % pass3.upper()

			marble_maze_solve = True
			raw_input("[continue]")
			marble_maze_room()
		elif choice == "5":
			print """
Yeah, this is tedious and annoying.

You jiggle the controls randomly (and with more aggression than strictly
necessary) until the marble plunks safely into the return slot, ready for a
fresh start once you've calmed down.
			"""

			marble_maze_room()
		else:
			print "Please pick a number, for all our sakes."

def obelisk_room():
	global obelisk_room_visit

	if obelisk_room_visit == False:
		print """
Stupid caves, you think as you squeeze yourself sideways down the passage,
awkwardly angling around a curve. Stupid nature, not understanding concepts
like "straight lines" or "breathing room" or "not lining cave passages with
stupid little sharp bits that dig into your-"

You wrench yourself free of the claustrophobic passage and almost fall flat
on your face into the room beyond. Dusting yourself off, you look around.

The major feature of this room is an imposing obelisk rising from the center
of the floor, standing about twice as tall as you. So not really HUGE, as
obelisks go, but big enough to demand your attention. Like, look at me! I'm
an obelisk! Well la-dee-dah, who gives a shit?

Stupid self-important obelisk.
		"""

		obelisk_room_visit = True
	else:
		print """
Status of obelisk: still obeliskesque. You are getting super great at spelling
obelisk by this point. Er, in your mind. Obviously.
		"""

	print """
What will you do?

  1. Give the obelisk the attention it wants so badly.
  2. Hey, look! A wall!
  3. Go somewhere that's not here.
	"""

	while True:
		choice = raw_input("> ")

		if choice == "1" and obelisk_solve == False:
			obelisk_puzzle_intro()
		elif choice == "1" and obelisk_solve == True:
			print """
The obelisk's eye projects an image on the wall of a six-legged larval
creature, waving its front two legs in the air like it just don't care.
Beneath the image is an inscription:

                                 "%s"

The tiles are firmly attached to the obelisk now and can't be pried loose.
You figure it's probably best not to mess with them anymore anyway.
			""" % pass1.upper()

			raw_input("[continue]")

			obelisk_room()
		elif choice == "2":
			print """
You only really intended to snub the obelisk, but oh, there's actually
something on the wall! It looks like, uh...

			--------------------
			|          O|     O|
			| --- |--| -|  ----|
			| | |       |  |-|X|->
			| | | |-|O         |
			| --- |------| --- |
			|              | | |
			|---| |-|  |-| | | |
			|O   X        O| |O|
			--------------------
			     ^
			     |

That. It looks like that. Well, there you have it, then.
			"""

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
		print """
Fine.

You approach the obelisk. As you step closer, a grinding sound makes you
jump. You look up to see a panel near the top of the obelisk slide away,
revealing an enormous eye - in crude pictogram format, but you get the idea.

Especially when it looks down and fixes its gaze on you.

Well. That's creepy. You shuffle side to side a little, and the eye tracks
your movements. Hmm.

"Hello, creepy eye thing!" you say as cheerfully as you can. There is no
response.

You make a series of rude gestures in the eye's general direction. It watches
you impassively.

...Seems safe enough, you guess. For now, anyway. Glancing back up every once
in a while to make sure the eye doesn't do anything weird, you take a closer
look at the rest of the obelisk.

There are five square depressions arranged in a vertical column on the near
face. You know enough about puzzles to figure out that you're probably
supposed to put something in them.

The stack of five appropriately-sized tiles lying at the base of the obelisk
is probably that something.

You fan out the tiles to get a better look at them. Each has a crude picture
on it. You see... a plant of some kind - those are probably leaves, you hope;
a reasonable reproduction of the sun as drawn by a four-year old; a stick-
figure human being; an hourglass - thankfully, it's pretty hard to fuck that
one up; and a... four-legged, horned... something. You're going to go with
goat. Whether it was meant to be or not, it's a goat now.

Okay, so, just got to put these tiles in the right order! Seems simple
enough!

Until you glance up, tile in hand, and see the eye pulsing faintly with a dim
light. It seems REALLY interested in you now. You don't have the greatest
feeling about this.
		"""

		obelisk_intro_visit = True
	else:
		print """
The eye continues to watch you. Ugh, that thing is still creepy.

The tiles lie where you left them, fanned out at the foot of the obelisk:
a plant, a sun, a person, an hourglass, and a probably-a-goat.
		"""

	print """
What will you do?

  1. Tile puzzle time!
  2. Back away slowly from the terrifying eye.
	"""

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
		print """
You hear a soft click as the last tile slides into the slot. Was that it?
Did you do it?

You glance hopefully up at the eye. Its intent gaze... slides away from you,
finally, and a white glow suffuses it, growing brighter by the second.

You step back warily, but it doesn't seem to be charging up some horrible
death ray. After a moment, a beam of light shoots from the eye, projecting
an image on the wall.

It depicts an insectoid creature, presumably in its larval phase. It has six
legs, the front two of which it seems to be waving in the air for reasons
unbeknownst to you and which you don't particularly care to contemplate.

Beneath the picture is some sort of inscription, although it fails to explain
anything at all:

                                 "%s"
		""" % pass1.upper()

		obelisk_solve = True
		raw_input("[continue]")

		obelisk_room()
	elif solution.index("Person") == 0:
		print """
You hold your breath and look up at the eye hopefully.

Absolutely nothing happens.

You wait a minute just to be sure, but then sigh and remove the tiles. Back
to the drawing board.
		"""

		raw_input("[continue]")

		obelisk_puzzle_intro()
	elif solution[solution.index("Person") - 1] == "Goat":
		print """
You hear a soft click as the last tile slides into the slot. Was that it?
Did you do it?

You glance hopefully up at the eye. Its gaze is fixed intently on you. As
you watch, it slowly begins to glow red.

That's... not good.

You try to scramble away, but the passage you entered through has vanished.

Okay, yeah, definitely bad. Bad things are happening.

You turn back to the eye, helpless to do anything but watch as the pupil
pulses and begins to elongate vertically, until it starts to look like...

No.

A deep, menacing bleat echoes through the air, reverberating in your bones,
and the floor of the chamber shakes and cracks apart.

As you fall to your doom, you catch a glimpse of two stout horns and a pair
of demonic eyes glowing in the dark, just before the bearded maw engulfs
you.

Hey, you were right! It WAS a goat!


You have been eaten by a goat. 
		"""

		end("died")
	elif solution[solution.index("Person") - 1] == "Plant":
		print """
You hear a soft click as the last tile slides into the slot. Was that it?
Did you do it?

You glance hopefully up at the eye. Its gaze is fixed intently on you. As
you watch, it slowly begins to glow red.

That's... not good.

You try to scramble away, but the passage you entered through has vanished.

Okay, yeah, definitely bad. Bad things are happening.

You turn back to the eye, helpless to do anything but watch as the pupil
pulses and begins to dilate, wider and wider, the edges growing jagged like
a vicious ring of teeth... And then, from the center, thorny vines spill
forth, reaching for you.

There's nowhere to run. You struggle as the vines wrap around you, but you
know that it's futile. They drag you, kicking and screaming, deep into the
monstrous pile of vegetation that once was the obelisk, to wait in the dark
as you are slowly digested.

This sucks.


You have been eaten by a plant.
		"""

		end("died")
	elif solution[solution.index("Person") - 1] == "Sun":
		print """
You hear a soft click as the last tile slides into the slot. Was that it?
Did you do it?

You glance hopefully up at the eye. Its gaze is fixed intently on you. As
you watch, it slowly begins to glow red.

That's... not good.

You try to scramble away, but the passage you entered through has vanished.

Okay, yeah, definitely bad. Bad things are happening.

You turn back to the eye, helpless to do anything but watch as the pupil
begins to glow. Well, technically it was already glowing, but now it's
glowing white, quickly overpowering the red and growing brighter and
brighter and brighter.

You close your eyes and throw your arm across them, but it doesn't help as
much as you expected. And then you feel the heat - first, the uncomfortable
warmth of stage lights left on too long, then like you're standing too close
to a fire, then like you're standing IN a fire and oh, hey, you're on fire.

That's about as fun as it sounds, but at least it doesn't last long. A final
surge of heat vaporizes most of what's left of you, leaving behind only a
charred and smoking pile of bones. The sphinx will probably be along shortly
to collect them. Fucking sphinxes.


You have been consumed by the sun.
		"""

		end("died")
	else:
		print """
You hold your breath and look up at the eye hopefully.

Absolutely nothing happens.

You wait a minute just to be sure, but then sigh and remove the tiles. Back
to the drawing board.
		"""

		raw_input("[continue]")

		obelisk_puzzle_intro()

def treasure_room():
	print """
You boldly stride forth across the threshold and down yet ANOTHER fucking
twisty, narrow passage, jesus. It's hard to swagger confidently when you're
retrieving a shoe from the crack it got caught in. Still, the thought that
your prize lies just ahead of you makes it all feel worthwhile.

Finally, the walls open up into a staggeringly enormous chamber. Natural
light filters in from large cracks high in the walls - the ceiling is so
far overhead you can't even guess at the distance.

And it's completely empty.

"What the fucking fuck," you state to the emptiness. The word "fuck" echoes
back to you over and over.

"Now you see!"

You jump and whirl to see the sphinx has followed you from the central
chamber. You don't know HOW she followed you, given that she's about twelve
times your size and that narrow, twisty passage was barely big enough for
you.

Whatever, you're not going to think about it. Instead, you gesture
emphatically at the empty room and address the sphinx. "Seriously, what the
fuck is this shit?"

The sphinx gives you a disdainful look. "As I was saying: now you see! You
have completed your harrowing journey, and the answer before you is as
clear as the day. The REAL treasure... was inside you all along!"

"What."

"No gold or silver could possibly compare to self esteem and pride in your
own accomplishments." She grins down at you.

You stare back at her. "That's some fucking bullshit."

She shrugs and stretches her claws. "Well, the sign said 'treaseure,' so I
bear no legal liability for the contents of this chamber, or lack thereof."


What will you do?

  1. Accept the obnoxious moral.
  2. Flip the fuck out.
	"""

	while True:
		choice = raw_input("> \n")

		if choice == "1":
			print """
You sigh in resignation. After all, you can't exactly say you didn't see
this coming.

"Fine, I guess," you say. "I have really grown as a person through solving
shitty puzzles and staring at a lava lamp for hours. I will forever carry
the real 'treaseure' right here." You tap your chest in the vague vicinity
of your heart. Clavicle's close, right? "So now that I've learned a
valuable lesson about believing in myself, how the hell do I get out of
here?"

The sphinx lifts a paw, gesturing upwards toward the cracks high in the
walls of the chamber.

"The..." you start, and then sigh again. Of course. "So... is there a
ladder? Or something...?"

The sphinx shrugs. "Maybe!" And then she turns and retreats through a side
passage you hadn't noticed before, much larger and better-hewn than the
crappy tunnels you've been navigating. It shuts firmly behind her.

You.

Fucking.

Hate.

Sphinxes.

Several hours later you manage to claw your way up the side of the chamber
and out into the open air. You're battered, bruised, exhausted, and empty-
handed, but at least you're not dead.

And you learned a valuable lesson that has changed your heart forever. As
god is your witness, you will never put effort into anything ever again.

                                THE END
			"""

			win()
		elif choice == "2":
			print """
"Fuck! Fucking! No!" You grit your teeth. You're not about to take this
lying down.

You advance on the sphinx. "I solved the fucking puzzles, I solved your
fucking riddle, I humored your whole fucking 'treaseure' schtick!"

"And don't you feel like you've grown as a person for it?"

"NO!" you scream.

"Yes, I can see that," she says. She leans over you, reminding you that
wow, she is a lot bigger than you and has sharp teeth. That cools your
jets a little.

But not a lot. "I was promised some fucking treasure!"

"I feel the need to remind you that what you were promised was actually
'treaseure.'"

"But 'treaseure' isn't a fucking word!" you snap, waving your arms. "It
means nothing!"

A beat passes. Then you realize what you just said.

The sphinx smirks at you.

"No! FUCKING! NO! You aren't screwing me out of a reward because of a
fucking typo! I am gonna sue your ass!"

"Many a mortal has tried and failed to-"

"Cut the goddamn crap, lady."

The sphinx sighs in annoyance. "If you're going to keep throwing a
tantrum..."

She paces for a moment as though trying to find something. "Ah!" She plants
a paw firmly on a small, flat rock. A slot briefly opens in the wall, and
out shoots a single gold coin, which lands at your feet.

"That's it?"

"Look, it's all I've got, okay? The dragon who used to live here packed up
her hoard and retired to Florida six centuries ago. Just take it and get
out."
	"""

			raw_input("[continue]")

			print """
Clearly eager to be rid of your presence, the sphinx gives you a lift up
to one of the cracks in the walls of the chamber and out into fresh air.

You have the gold coin appraised - it's worth about $6000. Not infinite
riches, sure... but still, score!

And you realize you learned a valuable lesson after all: if you don't get
what you want, complain until you do.

You put this in practice in every aspect of your life from now on.

                                THE END
			"""

			win()
		elif choice == "3":
			print """
Yeah, no. You don't like these choices. You're gonna take a third option.

"You know what?" you say. "Let's just put this whole treasure/lack of
treasure issue behind us."

"Treaseure," the sphinx corrects.

"Bygones," you say through gritted teeth. You make a concerted effort to
unclench your jaw. "Look. I admire the little operation you have going
here."

The sphinx cocks her head warily. "Why, thank you. I try."

"You do, you do. And you know, you're pretty cute, too,"

The sphinx narrows her eyes at that. "I don't know where you think you're
going with this. Why would I want anything to do with you? Your sphinx-
bigotry is visible from space."

"You eat people."

"...Fair enough."

"But listen, let's set aside our differences! I've had a lot of time to
think while I was staring catatonically into a lava lamp, and you know,
as the only other character, you've grown... very special to me."

"Hmm..."

"Plus, I have this really sweet human-sacrifice operation that's looking
for a new location. With your puzzles and crushing jaws, and my complete
and utter lack of scruples... I think... I think we could really have
something special."

You and the sphinx gaze into one another's eyes. You know she can feel it
too.

"It's a deal," she says.
			"""

			raw_input("[continue]")

			print """
You go into business with the sphinx. Together, you manage to depopulate
half the county before being forced to relocate due to law enforcement
sniffing around.

The sphinx is a wonderful companion. She fills a hole in your life. And
you realize you've really grown as a person. No longer are you the bigot
you once were. You can't even imagine being that person now.

And you've learned a valuable lesson: everything is twice as beautiful when
you have someone to share it with. Especially murder.

                                THE END
			"""

			win()
		else:
			print "Please just pick a number, for all our sakes."

def end(end_type):
	if end_type == "left":
		print """
You have completely failed to have an adventure. Maybe that's for the best.


What will you do?

  1. Play again
  2. That's all the experience of this game I ever need. I'm out.
		"""
	else:
		print """
You have died. Good job. Way to go.


Give it another shot?

  1. Play again
  2. Let me out of this hellhole
  		"""

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
	print """
You have won! Congratulations! You must be very proud.


What would you like to do?

  1. Play again
  2. Never play again
  3. See some random stuff to try.
	"""

	while True:
  		choice = raw_input("> ")

  		if choice == "1":
  			start()
  		elif choice == "2":
  			print "Don't let the door hit you on the way out."
  			exit(0)
  		elif choice == "3":
  			print """
Have you...

-Died all three different ways in the obelisk room?
-Died to the lava lamp and recognized my brilliant 1984 reference?
-Tried answering the sphinx's riddle with "man" or something similar?
-Found the super secret third ending?


What will you do?

  1. Play again
  2. Never play again
  3. See some random stuff to try, even though it's right there, you just
     saw it. It's still on the screen, right now.
  			"""
  		else:
  			print "Please just pick a number, for all our sakes."

start()