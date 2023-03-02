import random

def passWord(passLen = 12):
	passW = ""
	while(passLen > 0):
		letterNum = random.randint(0,4)
		if (letterNum < 4):
			symbolChance = random.randint(0,9)
			if (symbolChance < 9):
				capChoice = random.randint(0,4)
				if (capChoice < 4):
					letterChoice = random.randint(97,122)
					passW += chr(letterChoice)
				else:
					letterChoice = random.randint(97,122)
					passW += chr(letterChoice).upper()
			else:
				symbolChoice = random.randint(33,38)
				passW += chr(symbolChoice)
		else:
			passW += str(random.randint(0,9))	
		passLen -= 1
	passW += '\n'
	return passW
	
print("Please enter quantity of passwords to create:")
f = open("output.txt", "a")

try:
	numPW = int(input())
	x = range(numPW)
	for n in x:
		f.write(passWord())
except:
	x = range(5)
	for n in x:
		f.write(passWord())
		
f.close()	