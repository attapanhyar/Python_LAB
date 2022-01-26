def isPrime(num):
    Pflag = True
    for i in range(2,num):
        if num%i == 0:
            Pflag=False
            break
    return Pflag

number = int(input('Enter the number to check'))
print(number, 'is Prime?', isPrime(number))