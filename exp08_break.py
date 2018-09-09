'''
This is
an example of 
multiline comments
'''
magicNumber=3;

for n in range(101):
    if n==magicNumber:
        print("The magic number is :",n)
        break # break will bring the control out of all the loops . Save memory .
    else:
        print("This is not a magic number",n)                
