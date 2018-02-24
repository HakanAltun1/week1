class Fibonacci:
    def fibonacci(sefl,n):
        numberOne, numberTwo = 0, 1
        for i in range(0, n):
            numberOne, numberTwo = numberTwo, numberOne + numberTwo
        return numberOne

    def startFibonacci(self):
        n = int(input("İstediğiniz Sayıyı Giriniz: "))
        for i in range(0,n):
            print( (self.fibonacci(i)))


print(Fibonacci().startFibonacci())