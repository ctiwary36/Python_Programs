"""
  * Author - Chandan Tiwary
   * Date - 18-SEP-2021
   * Time - 16:40
   * Title -  Euclidean distance from the point (x, y) to the origin (0, 0).
"""
import math

x1 = float(input('Enter the x1 co-ordinate of the first point:'))
y1 = float(input('Enter the y1 co-ordinate of the first point:'))

x2 = float(input('Enter the x2 co-ordinate of the second point:'))
y2 = float(input('Enter the y2 co-ordinate of the second point:'))

distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
print(distance)
