# Write a Python function to sum all the numbers in a list.



# Sample List : (8, 2, 3, 0, 7)

# Expected Output : 20



# Explanation:



# Summation should like 8+2+3+0+7 = 20 
 
 
def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    print( total)


numbers =list(map(int,input("enter a number:").split()))
sum(numbers)