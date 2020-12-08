import sys
import os


def mykwargs(argv):
    #processes args and kwrgs
    args = []
    kargs = {}
    for arg in argv:
        if '=' in arg:
            key, val = arg.split('=')
            kargs[key] = val
        else:
            args.append(arg)
    return args, kargs


def sieve_of_e(n):
    #stores all primes between 2 and n into a list, returns list
    primes = []
    duplicates = []
    for i in range(2, n + 1):
        for j in range(i * i, n + 1, i):
            duplicates.append(int(j))
        if i not in duplicates:
            primes.append(int(i))
    return primes


def get_factors(n, primes):
    #stores factors of n into a list
    list_of_factors = []
    for x in primes:
        if ((n % x) == 0):
            list_of_factors.append(x)
    return list_of_factors


def usage(message=None):
    if message:
        print(message)
    name = os.path.basename(__file__)
    print(
        f"Usage: python {name} [input=string filename] [output=string filename]"
    )
    print(
        f"Example:\n\t python {name} input=input_file.txt output=output_file.txt \n"
    )
    sys.exit()


if __name__ == '__main__':
    _,mykwgs = mykwargs(sys.argv[1:])
    infile = mykwgs.get('input', None)
    inlist = []
    if not infile:
        usage()
    with open(infile) as f:
        for line in f:
            inlist.append([int(x) for x in line.split()])

    primes = []
    factors = []
    primes = sieve_of_e(10000)

    print("Brent Laden")
    print("\n\n")
    for i in range(0, len(inlist)):
        for j in inlist[i]:
            if (j == 0):
                print("Number", i + 1, ": ", inlist[i][0], " - Factors: 0")
            else:
                factors = get_factors(j, primes)
                if (len(factors) == 0):
                    primes.append(j)
                if j not in primes:
                    print("Number", i + 1, ": ", inlist[i][0], " - Factors:",
                          factors)
                else:
                    print("Number", i + 1, ": ", inlist[i][0], " - Prime!")
