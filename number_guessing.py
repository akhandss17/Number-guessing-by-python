import random


top_range = input('Enter a number : ')


if top_range.isdigit():
    top_range = int(top_range)



    if top_range <= 0 :
        print('Type a number larger than  0 , please !')
        quit()


else:
    print('We are expecting from you to type a number next time , please !')
    quit()



random_number = random.randint(0,top_range)

number_of_guesses = 0


while True:

    number_of_guesses += 1


    user_guess = input('guess the number: ')

    if user_guess.isdigit():
        user_guess = int(user_guess)

    else:
        print('We are expecting from you to type a number next time ,good luck !')
        continue


    if user_guess == random_number:
        print('Hue , you guess the right number . ')
        break
    
    elif user_guess > random_number:
        print('you are above the number !')

    else:
        print('you are below the number !')

print('you got it right in ', number_of_guesses, 'guesses.')


     


    
