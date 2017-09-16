# IPND Stage 2 Final Project

# In this project, we'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!
# Note: This game will have to accept user input.

intro_message = "Please select a game difficulty by typing it in!" 
intro_message += "\n"
intro_message += "Possible choices include easy, medium, and hard."
intro_message += "\n"

easy_question = "A common first thing to do in a language is display"
easy_question += "\n"
easy_question += "'Hello __1__!'  In __2__ this is particularly easy; all you have to do"
easy_question += "\n"
easy_question += "is type in:"
easy_question += "\n"
easy_question += "__3__ \"Hello __1__!\""
easy_question += "\n"
easy_question += "Of course, that isn't a very useful thing to do. However, it is an"
easy_question += "\n"
easy_question += "example of how to output to the user using the __3__ command, and"
easy_question += "\n"
easy_question += "produces a program which does something, so it is useful in that capacity."
easy_question += "\n"
easy_question += "\n"
easy_question += "It may seem a bit odd to do something in a Turing complete language that"
easy_question += "\n"
easy_question += "can be done even more easily with an __4__ file in a browser, but it's"
easy_question += "\n"
easy_question += "a step in learning __2__ syntax, and that's really its purpose."
easy_question += "\n"


easy_answer = ["world", "python", "print", "html"]


easy_parts_of_speech  = ["__1__", "__2__", "__3__", "__4__"]


medium_question = "A __1__ is created with the def keyword.  You specify the inputs a"
medium_question += "\n"
medium_question += "__1__ takes by adding __2__ separated by commas between the parentheses."
medium_question += "\n"
medium_question += "__1__s by default returns __3__ if you don't specify the value to return."
medium_question += "\n"
medium_question += "__2__ can be standard data types such as string, integer, dictionary, tuple,"
medium_question += "\n"
medium_question += "and __4__ or can be more complicated such as objects and lambda functions."
medium_question += "\n"
medium_question += "\n"


medium_answer = ["function", "arguments", "None", "list"]

medium_parts_of_speech  = ["__1__", "__2__", "__3__", "__4__"]


hard_question = "When you create a __1__, certain __2__s are automatically"
hard_question += "\n"
hard_question += "generated for you if you don't make them manually. These contain multiple"
hard_question += "\n"
hard_question += "underscores before and after the word defining them.  When you write"
hard_question += "\n"
hard_question += "a __1__, you almost always include at least the __3__ __2__, defining"
hard_question += "\n"
hard_question +=  "variables for when __4__s of the __1__ get made.  Additionally, you generally"
hard_question += "\n"
hard_question += "want to create a __5__ __2__, which will allow a string representation"
hard_question += "\n"
hard_question += "of the method to be viewed by other developers."
hard_question += "\n"
hard_question += "\n"
hard_question += "You can also create binary operators, like __6__ and __7__, which"
hard_question += "\n"
hard_question += "allow + and - to be used by __4__s of the __1__.  Similarly, __8__,"
hard_question += "\n"
hard_question += "__9__, and __10__ allow __4__s of the __1__ to be compared"
hard_question += "\n"
hard_question += "(with <, >, and ==)."
hard_question += "\n"

hard_answer = ["class", "method", "__init__", "instance", "__repr__", "__add__", "__sub__", "__lt__", "__gt__", "__eq__"]

hard_parts_of_speech  = ["__1__", "__2__", "__3__", "__4__", "__5__", "__6__", "__7__", "__8__", "__9__", "__10__"]


def newline():
    """Print a new line.   

    """ 
    print ""
    return None

def indications(level):
    """Print indications. 
    """ 
    newline()
    print "You\'ve chosen " + level + "!"
    newline()
    print "You will get 5 guesses per problem"
    newline()    
    return None

def show_question(p):
    """Show the current paragraph.
    """ 
    print "The current paragraph read such as:"
    print p
    return None 


def play_game(questions, answers, parts_of_speech):   
    """Play the quiz game. 
    This function keeps the control of the game. If the user win (when the user has guessed all the letters)
    then the function returns True, otherwise the user has lost and the function returns False. 
    The user lost when he has used 5 tries in the same word.
    """ 
    remaining_tries = 5
    state_quiz = False 

    while remaining_tries !=0 and len(parts_of_speech)!=0: 
          show_question(questions)
          user_input = raw_input("What should be substituted in for" +  parts_of_speech[0]  +"?")
          user_input = user_input.strip()
          if user_input == answers[0]:
             remaining_tries = 5 # we re-initialize the value of remaining_tries  
             replacement = parts_of_speech[0]
             questions = questions.replace(replacement, user_input)
             parts_of_speech.pop(0)
             answers.pop(0)
             if len(parts_of_speech)!=0:                
                newline()
                print "Correct!"
                newline()
             else:
                continue

          else:
             remaining_tries = remaining_tries - 1
             if remaining_tries!=0:
		newline()
                print "That isn\'t the correct answer!  Let\'s try again; you have " +  str(remaining_tries)  + " trys left!"
                newline() 
             else:
                continue

    if len(parts_of_speech) == 0:
       state_quiz = True
    if remaining_tries == 0:
       state_quiz = False

    return state_quiz 


def non_option():
    """Print a non option message.       
    """ 
    print "That's not an option"
    return None


def quiz(level):
    """Branch the code accoding to the level. 
       if the user has typed: easy, medium or hard, then the function play_game 
       is called with the appropiate arguments. 
    """           
    if level == "easy":
       indications(level)
       state_quiz = play_game(easy_question, easy_answer, easy_parts_of_speech)  
       return state_quiz 

    if level == "medium":
       indications(level)
       state_quiz = play_game(medium_question, medium_answer, medium_parts_of_speech)  
       return state_quiz 

    if level == "hard":
       indications(level)
       state_quiz = play_game(hard_question, hard_answer, hard_parts_of_speech)  
       return state_quiz 



## main program. 
while(True):  # the loop while simulates a menu with options.
	user_input = raw_input(intro_message)
        user_input = user_input.strip()
	if user_input == "easy" or user_input == "medium" or user_input == "hard":
	   state = quiz(user_input)
	   if state == True:
                   newline()
		   print "You won"
                   newline()
		   break
	   else:
		   print "You've failed too many straight guesses!  Game over!"
		   break
	else:
	   non_option()

