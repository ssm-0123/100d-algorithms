#!python3

"""
Create a function that takes an integer value from 0-255 and
converts it into a list.  Each element is equal to the power
of 2 that corresponds to that place value
"""

def toBinary(value):
  value = int(value)
  binary = [0,0,0,0,0,0,0,0]
  change = 0
  while True:
      oneorzero = value%2
      value = round((value-oneorzero)/2)
      binary[change] = oneorzero
      change = change + 1
      if value == 0:

        return binary
    



def toDecimal(myList):
  binarydict = []
  for i in range(0,256):
    binarydict.append(toBinary(i))
  if myList in binarydict:
    a = binarydict.index(myList)
    return a


def problem1():
  assert toBinary(0) == [0,0,0,0,0,0,0,0]
  assert toBinary(1) == [1,0,0,0,0,0,0,0]
  assert toBinary(2) == [0,1,0,0,0,0,0,0]
  assert toBinary(5) == [1,0,1,0,0,0,0,0]
  assert toBinary(10) == [0,1,0,1,0,0,0,0]
  assert toBinary(30) == [0,1,1,1,1,0,0,0]
  assert toBinary(45) == [1,0,1,1,0,1,0,0]

def problem2():
  assert toDecimal([0,0,0,0,0,0,0,0]) == 0
  assert toDecimal([1,0,0,0,0,0,0,0]) == 1
  assert toDecimal([0,1,0,0,0,0,0,0]) == 2
  assert toDecimal([1,0,1,0,0,0,0,0]) == 5
  assert toDecimal([0,1,0,1,0,0,0,0]) == 10
  assert toDecimal([0,1,1,1,1,0,0,0]) == 30
  assert toDecimal([1,0,1,1,0,1,0,0]) == 45
  
if __name__ == "__main__":
  problem1()
  problem2()
