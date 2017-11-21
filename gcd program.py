
def gcd(number1, number2):
    while True:
	    if number2 != 0:
	        (number1, number2) = (number2, number1 % number2)
	    else:
		    break
    return number1


def get_twonumbers():
    global a, b  
    a = input('Enter number: ')
    b = input('Enter number: ')
    a, b =  int (a), int (b)


a = None 
b = None
get_twonumbers() 
gcdval = gcd(a, b) 
print ('The gcd is ', gcdval)
