#PALINDROME PROGRAM

user_input=input("Enter the word:")

if(user_input == user_input[::-1]):
    print("{} is a palindrome".format(user_input))
else:
    print("{} is not a palindrome".format(user_input))
