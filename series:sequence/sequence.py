from sys import argv

def u(n):
  #provide function here
  function = n
  return function

# Provide data to argv[1] python3 sum.py [data]
try:
  n = float(argv[1])
  u_n = u(n)
  print(f"Output: {u_n}, argv:{n}")

except(IndexError):
  print("Usage: python3 sum.py [data]")

  

"""
u_n is the general term of sequence
"""