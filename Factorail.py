
factorial = 1
num = 10
result = 1

for i in range (1,num+1):
    result = result * i
    factorial += 1

print (result)



# factorail using recurssion

def factorial(n):
    if (n == 0 or n ==1):
        return 1
    else :
        return n * factorial(n-1)

number = 100
print (factorial(number))
