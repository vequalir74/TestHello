import sys

inline = sys.stdin.readline()

# Get input as chars, convert to integers
characters = inline.split()
integers = []

for x in characters:
  integers.append(int(x))
  integers.sort()

size = len(integers)

average = sum(integers)/size

def getClosest2Avg(l1,tgt):
  closest = l1[0]
  for n in range(1,len(l1)):
    if abs(tgt - l1[n]) < abs(tgt - closest):
      closest = l1[n]
  return closest

largest = integers[size-1]

closest = getClosest2Avg(integers,average)

print("Sorted = ", integers)
print("Largest = ", largest)
print("Avg = " , average)
print("Closest to the Average = " , closest)
