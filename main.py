import random

def play_hangman():
  # Read the word list from the file
  with open("wordlist.txt", "r") as file:
    words = file.readlines()
  
  # Choose a word at random
  word = random.choice(words).strip()
  
  # Create a list to store the letters that have been guessed
  # Initially, it should contain only underscores, one for each letter in the word
  letters_guessed = ["_" for letter in word]
  
  # Set the number of lives (incorrect guesses) to 6
  tries = 6
  
  while tries > 0:
    
    # Get the player's guess
    guess = input("Guess a letter: ")
    
    # Check if the guess is correct
    if guess in word:
      # If the guess is correct, update the letters_guessed list to show the guessed letter
      print("Correct!")
      for i in range(len(word)):
        if word[i] == guess:
          letters_guessed[i] = guess
      
      # Print the current state of the word, with spaces between the letters
      print(" ".join(letters_guessed))
      
      # Check if the player has won
      if "_" not in letters_guessed:
        print("Congratulations, you won!")
        return
    else:
      # If the guess is incorrect, decrease the number of lives
      tries -= 1
      print(f"Wrong! You have {tries} lives left.")
      
  print("You lost. The word was:", word)

play_hangman()
