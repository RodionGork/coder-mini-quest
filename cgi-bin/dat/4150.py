import sys

if sys.argv[2] != '':
  answer = int(sys.argv[2]) #check for error!
  if answer > 0:
    print("You got some water in your pot:wassr")
  else:
    print("That's wrong. Retry...")
  sys.exit(0)
else:
  print("No challenge here, just answer with any small positive number!")
