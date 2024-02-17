# The Matrix Parable
import time

# Preferencies
badges = []

ddmm = str(input("Hello. Before starting, I'd want to ask you the current day. e.g. 12/3 "))
if ddmm == "25/12":
  print("Chrismas Badge Acquired")
  badges.append("Chrismas Badge")
elif ddmm == "1/1":
  print("Happy New Year")
  badges.append("New Year Badge")
elif ddmm == "31/3":
  print("Hope You'll find other EASTER eggs..")
else:
  print("Thank you for answering.")
  
# Start
print("...")
time.sleep(3)
print("...")

print("")
name = str(input("This is the story of a man named "))
