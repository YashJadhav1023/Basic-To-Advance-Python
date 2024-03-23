# elif Statements
# Sometimes, the programmer may want to evaluate more than one condition, this can be done using an elif statement.

# Working of an elif statement
# Execute the block of code inside if statement if the initial expression evaluates to True. After execution return to the code out of the if block.

# Execute the block of code inside the first elif statement if the expression inside it evaluates True. After execution return to the code out of the if block.

# Execute the block of code inside the second elif statement if the expression inside it evaluates True. After execution return to the code out of the if block.
# .
# .
# .
# Execute the block of code inside the nth elif statement if the expression inside it evaluates True. After execution return to the code out of the if block.

# Execute the block of code inside else statement if none of the expression evaluates to True. After execution return to the code out of the if block.

#Example:

num=int(input("Enter your number:"))
if(num < 0):
    print("Entered number is negative")
elif(num==0):
    print("Entered number is neutral")
else:
    print("Entered number is positive")
