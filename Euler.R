# Solving problems 1-3 of the Euler Project -- this time in R
# Problem 1
x<-0
range<-c(1:1000)
for (i in range){
  if((i%%3==0)|(i%%5==0)){
    x<-x+i
  }
}
print(x) # solution: 234168

# Problem 2
sum<-0
fib1<-1
fib2<-1
while (fib1+fib2<4000000){
  fib_next=fib1+fib2
  fib1=fib2
  fib2=fib_next
  
  if (fib2%%2==0){
  sum<-sum+fib2 
  }
}
print(sum) # solution: 4613732

# Problem 3
target<-600851475143
factor<-2
range=c(factor:target)
for (x in range){
  if(factor>=target){
    break
  }else if(target%%factor==0){
    target<=target/factor
  } else{
    factor=factor+1
  }
  }
print(target) # Error: vector memory limit of 16.0 Gb reached, see mem.maxVSize()
  
  
  
  