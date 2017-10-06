import random
randomnum = random.randint(0,100)
end=0
while (end==0):
	userinput= int(input("Guess the number:"))
	if userinput==randomnum:
		end=1
		print("We did it!")
	if userinput>randomnum:
		print("Bump...Lower!!")
	if userinput<randomnum:
		print("Nopee... Higher1!1!")
