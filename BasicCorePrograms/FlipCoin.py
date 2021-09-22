"""
   * Author - Chandan Tiwary
   * Date -  16-SEP-2021
   * Time -  17:45
   * Title - Flip Coin and print percentage of Heads and Tails
"""
import random

number = input("Please Enter the number:")
number = int(number)
if number <= 0:
    print("Please Enter Positive Integer")
head = 0
tail = 0
for i in range(number):
    coin = random.randint(0, 1)  # we can also use randrange
    if coin <= 0.5:
        print("Tails")
        tail += 1
        tailPercent = (tail / number) * 100
        print(tailPercent)
    else:
        print("Heads")
        head += 1
        headPercent = (head / number) * 100
        print(headPercent)
