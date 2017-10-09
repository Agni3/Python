import random
randomnum = random.randint(0,100)
end=0
lives=input("Number of lives:")
while (not lives.isdigit()):
	lives=input("Number of lives:")
while (end==0):
	userinput= input("Guess the number:")
	while (not userinput.isdigit()):
		userinput= input("Guess the number:")
	if int(userinput)==randomnum:
		end=1
		print("We did it!") 
	if	int(userinput)!=randomnum:
		lives = int(lives) - 1
	if  int(lives) == 0:
		print("Game over, the number was {} :C".format(randomnum))
		break
	if int(userinput)>randomnum:
		print("Aghh...Lower!!")
	if int(userinput)<randomnum:
		print("Nopee... Higher1!1!")
