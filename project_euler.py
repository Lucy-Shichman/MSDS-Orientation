# Solving problems 1-3 of the Euler Project

# Problem 1
x=0
for i in range (1,1000):
    if i%3==0 or i%5==0:
        x+=i
print(x) # solution: 233,168

# Problem 2
sum=0
fib1=1
fib2=1
while fib1+fib2<4000000:
    fib_next=fib1+fib2
    fib1=fib2
    fib2=fib_next

    if fib2 % 2==0:
         sum+= fib2
print(sum) # solution: 4613732

# reference: https://www.grae.io/post/euler_problem_2/

# Problem 3
target=600851475143
i=2 # Smallest prime factor
for num in range(0,target):
    if i >= target: # Prime factor of the number should not be greater than the number
        break
    elif target % i == 0: # Check if the number is evenly divisible by i
        target = target / i
    else:
        i= i + 1
print (target)   
