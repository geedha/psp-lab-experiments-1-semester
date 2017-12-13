def square_root(number):
    epsilon = 0.01
    k       = number
    guess   = k / 2.0
    while abs(guess * guess - k) >= epsilon:
        guess = guess - (guess ** 2 - k) / (2 * guess)
    return guess




user_number = int(input('Input number: '))
sqroot_number = square_root(user_number)
print ('The square root of ', user_number, 'is about ', sqroot_number)

