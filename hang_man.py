import random
from os import system




#---------------Hangman---------------#
#----------CREATED BY JOSE POTES: Jun 30-2024 at 9:00 p.m Colombia--------#




#Function that reads the file.txt
def read() -> str:
    """This function return the word taken out from file.txt
    Returns:
        str: any
    """
    word_fromf = []
    with open('../files/words_game.txt','r',encoding='UTF-8') as f:
        for line in f.readlines():
            word_fromf.append(line.strip())
    random_picked = random.choice(word_fromf)
    return random_picked





#Function transforms and evaluate the words and fullfill them according to user its guessing goes.
def hang_man_core(word_toplay:str) -> None:
    """This function is the core for the game, will show all the game.

    Args:
        word_toplay (str): any from read() function.
    """
    system('clear')
    word_toplay = str(word_toplay) #Original word, taken from read function.
    replaced_ = "_"*len(word_toplay) # transform al letter of word in "_"
    corrected_letter = list(word_toplay) #takes the right word
    guessed_letter = [] #user guessing
    num_letter = len(replaced_) # change letters in numbers.
    attempts = 0 # attempts available before it ends.
    while True:
        if attempts <= num_letter: # if attempts is lower than numbers of letters
            for i in range(len(word_toplay)): # takes a range of the words in word_toplay 1 -> len(word)
                conteo = 1 + i
                letter = input(f"type a letter:  # {conteo}: ")
                if letter in corrected_letter:
                    guessed_letter.append(letter)
                    finally_game = ''.join(l if l in guessed_letter else "_" for l in word_toplay)
                    print(f"Perfect you have guessed: {finally_game}")
                    if finally_game == word_toplay:
                            break
                else:
                    attempts += 1
                    print("Try again")
        elif guessed_letter == word_toplay:
            break
        else:
            break






#Function to starts the game.
def run():
    """This is the main function.
    """
    user_name = input("please, write your username: ").capitalize() #user name
    print(f"""
        ** Hello {user_name}, welcome to Hangman.**
        Advise:counts your steps.""") #Welcoming
    start = input("starts [Y/N]:  ").lower() #takes the name lowercase.
    word = read() #This is the word taken out from file
    #Starts the game.
    if start == 'y':
        hang_man_core(word)
    else:
        print("Good bye.")
if __name__ == "__main__":
    run()



#Thanks for watching. never stop learning.