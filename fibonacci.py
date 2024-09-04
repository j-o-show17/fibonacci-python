#Fibonacci Sequence - Enter a number and have the program
#generate the Fibonacci sequence to the Nth number.

def fib(n):

    sequence = []
    for n in range(n):
        if n == 1:
            sequence.append(0)
            sequence.append(1)
        elif n >1:
            sequence.append(sequence[-1] + sequence[-2])

    return sequence

def main():
    n = int(input("Enter a number: "))
    if n < 1:
        print("Please enter a positive number")
    elif n >= 1:
        print(fib(n))
    else:
        print("Wrong input, try again! ")

if __name__ == "__main__":
    main()



