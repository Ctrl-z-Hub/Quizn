current_score = 0

print("Welcom to my quiz!")

playing = input('Would you like to play? (type "yes" to play) ')
print(playing)
if playing != "yes" and playing != "Yes":
  print("Bye!")
  print("Score: 1 /10")
  quit()
print("Wrong answer but okay! Good luck")

print(" ")

print("B.  2")
print("C.  3")
print("A.  4")
print("D.  1")
answer1 = input("How many correct answers are there to this question? ")

if answer1 == "D" or answer1 == "D.":
  print("Lucky guess! Glad you got the easy one...")
  current_score += 1
else:
  print("Not even close!")

print(" ")

answer2 =input("What word is spelled incorrectly in every dictionary? ")
if answer2 == "incorrectly" or answer2 == "Incorrectly":
  print("I would say that's incorrect but you managed to get it after that long !")
  current_score += 1
else:
  print("Really? Better luck next time!")

print(" ")

answer3 = input("In one word, answer what can one catch but is not thrown? ")
if answer3 == "cold" or answer3 == "Cold":
  print("That's sick! Good job")
  current_score += 1
else:
  print("Nope! Too bad")

print(" ")

print("A.  1")
print("B.  2")
print("C.  3")
print("D.  4")
answer4 = input("If a bowl has six apples and you take out four, how many do you have? ")
if answer4 == "D" or answer4 == "D.":
  print("Finally someone who can count!")
  current_score += 1
elif answer4 == "B" or answer4 == "B." :
  print("You know better")
else:
  input("How'd you get that? ")
  print("No way!")

print(" ")

answer5 = input("What is actually at the end of every rainbow? ")
if answer5 == "w" or answer5 == "W" or answer5 == "the letter w":
  current_score += 1

print(" ")

answer6 = input("What has a face and two hands but no arms or legs? (one word) ")
if answer6 == "clock" or answer6 == "Clock":
  current_score += 1

print(" ")

print("Answer in this format if a = A and b = B: A & B")
print("Hint: total of 8 letters plus ampersand.")
answer7 = input("a: What breaks and never falls, and b: what falls and never breaks? ")
if answer7 == "day & night" or answer7 == "Day & Night" or answer7 == "Day & night":
  current_score += 1

print(" ")

answer8 = input("What goes up and down, but is always in the same place? (one word) ")
if answer8 == "stairs" or answer8 == "Stairs":
  current_score += 1

print(" ")

answer9 = input("What has a head and a tail, but no body? (one word) ")
if answer9 == "coin" or answer9 == "Coin":
  current_score += 1

print("Score: ",current_score,"/10")
if current_score == 9:
  print("You're a genius!")
elif current_score == 8:
  print("You're pretty good!")
elif current_score == 7:
  print("You're alright!")
elif current_score == 6:
  print("You're okay!")
elif current_score == 5:
  print("You're almost there!")
elif current_score == 4:
  print("You're close!")
elif current_score == 3:
  print("You're not very good!")
elif current_score == 2:
  print("You're terrible!")
elif current_score == 1:
  print("You literally would have done just as well quitting.")