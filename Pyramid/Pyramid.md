## Markdown for Pyramid
- Put in your code for the square. tried to manipulate it so it became a Pyramid
- Realized i had to give stack an associated variable
- stack = p:
- Copied from notes in 2 different places
   for i in range(0, p):
      for n in range(0, i+1):
         print("# ",end="")
      print()
- This didnt run
- I got fed up and looked it up
- https://www.tutorialspoint.com/programs-for-printing-pyramid-patterns-in-python
- it was running successfully BUT it wasnt Conditional
- tried if stack <1 or >8: print("Number not in range")
- Realized i had to do If and else
- Tried again with an else statement at the end and taking out print
- Didnt work
- Called my buddy Adam to see how he did it and he gave me the following
- if stack >= 1 and stack <= 8:
- Tried it and it didnt work
- Had to adjust my spacing for the if and else Statements
- IT WORKED!
