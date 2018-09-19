user_word = input("Enter a word to see if it's palindrome or not: ")

def check_user_word(user_word):
        if(user_word == user_word[::-1]):
            print(True)
        else:
            print(False)

check_user_word(user_word)
