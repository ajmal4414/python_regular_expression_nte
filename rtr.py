def calc(*args):
    sum=0
    for arg in args:
        sum=sum+arg
    print("the sum is",sum)
sum=()
calc(20,40,50)
print("the outside the function is",sum)
