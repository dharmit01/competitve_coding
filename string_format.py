def print_formatted(number):
    # your code goes here
    size=len(bin(number)[2:])

    for i in range(1, number+1):
        deci = str(i)
        octa = oct(i)[2:]
        hexa = hex(i)[2:].upper()
        bina = bin(i)[2:]
        print(deci.rjust(size), octa.rjust(size), hexa.rjust(size), bina.rjust(size))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
