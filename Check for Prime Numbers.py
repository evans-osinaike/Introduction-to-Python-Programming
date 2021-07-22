## Your code should check if each number in the list is a prime number
check_prime = [26, 39, 51, 53, 57, 79, 85]

## write your code here
## HINT: You can use the modulo operator to find a factor

for num in check_prime:
    for i in range(2,num//2+1):
        if num % i == 0:
            print('{0} is not a prime number. {1} is a factor of {0}'.format(num, i))
            break
        elif i==num//2:
            print('{} is a prime number'.format(num))
    
