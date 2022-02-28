stack = int(input("How tall should the pyramid be (1-8): "))
if stack >= 1 and stack <= 8:
    def pyramid(p):
       X = 2*p - 2
       for i in range(0, p):
          for j in range(0, X):
             print(end=" ")
          X = X - 2
          for n in range(0, i+1):
             print("# ", end="")
          print()
    p = stack
    pyramid(p)
else: print("Number not in range")
 




