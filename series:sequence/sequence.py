from sys import argv, exit

def u(n):
  #provide function here
  function = n
  return function

def F(a_n1,a_n2):
  val=""
  while(True):
    val=input('Mode: ')
    if(val=="l"):
      break
    elif(val=="f"):
      function = a_n1 + a_n2
      break
  return function

try:
    help_text =str(argv[1])
  
except(IndexError):
    print("Usage: python3 sequence.py [function_val] [data]")
    print("Use python3 sequence.py --help")
    exit()

if(help_text=="--help"):
  print("f")
  exit()

else:
  f = 0
  g=0
  n=0
  try:
    g = int(argv[1])
    n = float(argv[2])
  
  except(IndexError):
    print("Usage: python3 sequence.py [function_val] [data]")
    print("Use python3 sequence.py --help")
    exit()
  

# Provide data to argv[1] python3 sum.py [data]
if(g==1):
  f=u(n)
elif(g==2):
  l=0
  try:
    l=float(argv[3])

  except(IndexError):
    print("Usage: python3 sequence.py [function_val] [data]")
    print("Use python3 sequence.py --help")
    exit()
  f=F(n,l)
  

print(f"Output: {f}")

"""
u_n is the general term of sequence
"""