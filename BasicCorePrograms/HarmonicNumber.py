"""
   * Author - Chandan Tiwary
   * Date - 16-SEP-2021
   * Time -  19:00
   * Title - Print the Nth Harmonic Value.
"""


def harmonic(num):
    i = 1
    sum = 0

    while i <= num:
        sum += 1 / i
        i += 1
        print(sum)


num = int(input("Enter Number: "))
if num <= 0:
    print("Please enter the no greater than zero.")
else:
    harmonic(num)
