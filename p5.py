def is_prime(n) :
    if n < 2 :
        return False
    if n % 2 == 0 and n != 2 :
        return False
    d = 3
    while d * d <=n :
        if int(n) % d == 0 :
            return False
        d += 2
    return True

#input
user_input = input("Enter a value and find the largest prime number smaller than it!\n")
while user_input.isdigit ==  False :
    user_input = input("Only positive integers ")
#case
if int(user_input) <=2 :
    print("Doesen't exist")

else :
    user_input = int(user_input)
    copy = user_input-1
#finding number
    while copy > 1 :
        if is_prime(copy) == False :
                copy -=1
        else :
            print(copy)
            break
