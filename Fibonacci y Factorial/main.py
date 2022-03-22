
#1+1=2
#1+2=3
#2+3=5
#3+5=8
#5+8=13
#8+13=21



def fibonacci(n):
   if n == 1 or n == 0:
        return n

   else:
        return fibonacci(n-1) + fibonacci(n-2)


print("El fibonacci del número es:  ", fibonacci(6))






def factorial(n):

      if n == 1:
          return 1      #Puede tener (n) también.

      else:
          return n * factorial(n-1)



print("El factorial del número es: ", factorial(6))







