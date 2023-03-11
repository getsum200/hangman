import random

def get_word(file_path, difficulty):
    with open(file_path, 'r') as file:
       words = file.readlines()
       if difficulty == "easy":
          words = [word for word in words if len(word.strip()) <= 5]
       elif difficulty == "medium":
          words = [word for word in words if len(word.strip()) <= 8]
       elif difficulty == "hard":
          words = [word for word in words if len(word.strip()) >= 9]
       else:
          raise ValueError("Invalid Difficulty Level chosen")
       return random.choice(words).strip().upper()

file_path = 'word_list.txt'
print("Lets play hangman")
difficulty = input("Please choose a difficulty level (easy, medium, hard): ")
playable_word = get_word(file_path, difficulty)

def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]

def play(playable_word):
   tries = 6
   word_completed = "_" * len(playable_word)
   guessed = False
   guessed_letters = []
   guessed_words = []
   print(display_hangman(tries))
   print(word_completed)
   print("\n")
   while not guessed and tries > 0:
      guess = str(input("What letter would you like to guess? ")).upper()
      if len(guess) == 1 and guess.isalpha():
         if guess in guessed_letters:
             print("Oops!", guess, "has already been guessed.")
         elif guess not in playable_word:
            print(guess + " isn't in the word.")
            tries -= 1
            guessed_letters.append(guess)
         else:
             print("Correct", guess, "is in the word.")
             guessed_letters.append(guess)
             word_as_list = list(word_completed)
             indices = [i for i, letter in enumerate(playable_word) if letter == guess]
             for index in indices:
                word_as_list[index] = guess
             word_completed = "".join(word_as_list)
             if "_" not in word_completed:
                guessed = True
      elif len(guess) == len(playable_word) and guess.isalpha():
         if guess in guessed_words:
            print("You've already guessed the word" + guess)
         elif guess != playable_word:
            print(guess + "is not the word")
            tries -= 1
            guessed_words.append(guess)
         else:
            guessed = True
            word_completed = playable_word
      else:
         print("Not a valid guess")
      print(display_hangman(tries))
      print(word_completed)
      print("\n")

   if guessed:
     print("Congrats, you guessed the word! You win!")
   else:
     print("Sorry, you ran out of tries. The word was " + playable_word + ". Maybe next time!")

def main():
   word = playable_word
   play(playable_word)

if __name__ == "__main__":
   main()