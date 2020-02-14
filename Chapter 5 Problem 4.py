#Kamil Krawczyk
#02/13/2020

for num in range(1,51):
  if num % 5 == 0 and num % 3 == 0:
     print("Divisible by both")
  elif num % 3 == 0:
    print("Divisible by three")
  elif num % 5 == 0:
    print("Divisible by five")
  else:
    print(num);

#This program goes through numbers 1-51 and see if it is divisbile by 3,5, or both.
#If it is divisible by one of those numbers, it prints out which it is.
#Otherwise, prints out the number