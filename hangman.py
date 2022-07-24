import random #to choose a random word from the file

#opening the file and extracting the words
with open("hangman_words.txt","r") as f:
	data=f.readlines()
data=data[0].split(" ") #making a list of all the words

wins,loses=0,0 #variables to keep track of wins and loses
while True:
	random_word=random.choice(data) #choose a random word
	number_lives=6
	wrong_letters=[]
	guessed=[" _ " for i in range(len(random_word))] #keep a reference to what the user has guessed
	while number_lives>0: #as long as the user has chances, prompt to guess
		was_found=False
		
		#print everything in a nice format and prompt the user to guess
		print("\n{} \t{} lives: {}".format("".join(guessed),wrong_letters,number_lives))
		guess=input("Guess: ")

		#these conditions check and tell the user of possible mistakes
		#without taking away lives
		if not guess or len(guess)>1:
			print("Enter a letter")
			continue
		if guess.lower() in wrong_letters:
			print("Already guessed {}".format(guess))
			continue

		#in this loop we fill the list guessed with letters
		#depening on whether the user guessed right or not
		for index,i in enumerate(random_word):
			if i.lower()==guess.lower():
				guessed[index]=" {} ".format(i)
				was_found=True #variable to check if we should
							   #subtract lives from the user or not

		#checking if the all the letters in the guesses equal the
		#random word. If it's the case then the user won!
		if "".join(guessed).replace(" ","").lower()==random_word.lower():
			print("You won! my word was {}".format(random_word))
			wins+=1
			break

		#if the guessed letter was not found in the random word
		#subtract a life, and before going back to the loop to
		#prompt the user for a guess, check if the number of
		#lives is 0 to update the variable loses and tell
		#the user what the word was
		if not was_found:
			wrong_letters.append(guess)
			number_lives-=1
			if number_lives==0:
				loses+=1
				print("\nYou lost! I was thinking of {}".format(random_word))

	#ask the user to play again in the outer loop
	again=input("Do you want to play again?: ")
	if "no" in again.lower(): #if no, give a summary of the games
		print("\nBye!")
		print("\t---Summary---\n\twins: {}\n\tloses: {}".format(wins,loses))
		break


