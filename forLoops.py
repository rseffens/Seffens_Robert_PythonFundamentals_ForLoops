# Basic - Print all integers from 0 to 150.

# for x in range(0,151):
#     print(x)

# # Multiples of Five - Print all the multiples of 5 from 5 to 1,000

# for x in range(5,1001,5):
#     print(x)

# Counting, the Dojo Way - Print integers 1 to 100. If divisible by 
# 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".

# from statistics import multimode

# for x in range (1,101):
#     if x % 10 == 0:
#         print("Coding Dojo")
#     elif x % 5 == 0:
#         print("Coding")
#     else:
#         print(x)

        


# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, 
# and print the final sum.

# Use a range

# sum = 0
# for value in range(1, 500001, 2):
#     sum = sum + value
# print(sum)



# Countdown by Fours - Print positive numbers starting at 2018, counting
# down by fours.

# x = 2018
# while x >= 0:
#     print(x)
#     x = x - 4
#     if x == 0:
#         break


# Flexible Counter - Set three variables: lowNum, highNum, mult. Starting 
# at lowNum and going through highNum, print only the integers that are a 
# multiple of mult. For example, if lowNum=2, highNum=9, and mult=3,
#  the loop should print 3, 6, 9 (on successive lines)

lowNum = 2
highNum = 10
multi = 3

for x in range(lowNum, highNum):
    if x % multi == 0:
        print(x)
