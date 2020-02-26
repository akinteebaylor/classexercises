#can only take one evaluation and return a value
#It is something you do on the fly
#lamda functio
# lambda parameter_list: expression, this is the synthax
remainder = lambda num: num%2
print (remainder(5))

product = lambda x,y: x*y
print(product(2,3))


#create a function

def testfunc(num):
    return lambda x: x*num
result1= testfunc(10) # The lambda function helps it point to another function
result2= testfunc(1000)
print(result2(9))

def myfunc(n):
    return lambda a : a*n
mydoubler = myfunc(2)
mytripler = myfunc(3)

print (mydoubler(11))
print (mytripler(11))


num_list = [2,6,8,10,11,4,12,7,13,0,21]
filtered_list = list(filter(lambda num: (num>7),num_list)) # This is very useful
print(filtered_list)

#map performs an operation on each element in the list
#lambdas can only do one expression
mapped_list = list(map(lambda num: num%2, num_list))
print (mapped_list)