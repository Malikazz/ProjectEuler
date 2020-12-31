## https://projecteuler.net/problem=1

"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

max_number:int = 1000
multiples:tuple = (2, 5)
sum_of_numbers:int = 0

for value in range(0, max_number):
  try:
    if (value % 3 == 0 or value % 5 == 0 ):
      sum_of_numbers += value
  except ZeroDivisionError:
    pass
print(sum_of_numbers)



