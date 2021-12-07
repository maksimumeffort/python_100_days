def prime_checker(number):
    prime = True
    
    #issue 1: not looping through 2 sets of n
    for n in range(2, number):
        if number % n == 0:
            prime = False
    
    if number == 1:
        print('It\'s not a prime number')
    elif prime == False:
        print('It\'s not a prime number')
    else:
        print('It\'s a prime number')


#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)