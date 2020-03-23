import random,math

def check_equality(inp,rand):
    if inp==rand:
        print("You are correct")
    else:
        print("You just missed correctness by "+str(math.fabs(inp-rand)))
        
a=random.randint(1,10)

b=int(input("Enter value between 1-10::"))

print("magic number:"+str(a))

check_equality(b,a)