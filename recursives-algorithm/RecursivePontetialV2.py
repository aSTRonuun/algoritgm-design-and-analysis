
#base^exponent = base^(n/2)
from math import ceil, floor


def recursivePotential(base, exponent): 
    if exponent == 0:
        return 1
    elif exponent == 1:
        return base
    else:
        n1 = ceil(exponent / 2)
        n2 = floor(exponent / 2)
        # when exponent is par, only one recursion is needed
        if exponent % 2 == 0:
            return recursivePotential(base, n1) ** 2
        else:
            return recursivePotential(base, n1) * recursivePotential(base, n2)



# main
if __name__ == "__main__":
    print(recursivePotential(2, 10))
        