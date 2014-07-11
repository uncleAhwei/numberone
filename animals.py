ins = {
	"A": "Aardvark!",
	"B": "Blue-footed-booby",
	"C": "Casswary",
	"D": "Dromedary",
	"E": "Elephant",
	"F": "Finch",
	"G": "Goat",
	"H": "Hippopotamus",
	"I": "Ichthys",
	"J": "Jack rabbit",
	"K": "Klipspringer",
	"L": "Lemming",
	"M": "Marmot",
	"N": "Nyala",
	"O": "Ocelot",
	"P": "Potoroo",
	"Q": "Quoll",
	"R": "Rhinoceros",
	"S": "Serval",
	"T": "Tayra",
	"U": "Uriel",
	"V": "Vicuna",
	"W": "Woylie",
	"X": "Xylophone",
	"Y": "Yak",
	"Z": "Zorilla"
}

inp = raw_input("Enter a letter of the alphabet to see the name of an unusual animal")
while True:
	for letter in ins:
		if letter == inp.upper():
			print ins[letter]
	break

	if question.lower() == "exit":
		print "Exiting program!"
		exit()
	elif question.lower() == "done":
		print "Exiting program!"
		exit()
	elif question.lower() == "finish":
		print "Exiting program!"
		exit()
	elif question.lower() == "quit":
		print "Exiting program!"
		exit()