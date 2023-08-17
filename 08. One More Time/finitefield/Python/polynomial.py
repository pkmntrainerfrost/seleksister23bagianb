import argparse
import os

# Modular arithmetic functions for Galois Field
def add(a, b, P):
    return (a + b) % P

def subtract(a, b, P):
    return (a - b) % P

def multiply(a, b, P):
    return (a * b) % P

def inverse(a, P):
    # Find multiplicative inverse using Extended Euclidean Algorithm
    t, newt = 0, 1
    r, newr = P, a

    while newr != 0:
        quotient = r // newr
        t, newt = newt, t - quotient * newt
        r, newr = newr, r - quotient * newr

    if r > 1:
        raise Exception("a is not invertible")
    if t < 0:
        t += P

    return t

def divide(a, b, P):
    return multiply(a, inverse(b, P), P)

def interpolate(d, x, y, P):
    p = [0 for _ in range(d)]

    for i in range(d):
        product = 1
        t = [0 for _ in range(d)]
        for j in range(d):
            if i == j:
                continue
            product = multiply(product, subtract(x[i], x[j], P), P)
        product = divide(y[i], product, P)
        t[0] = product
        for j in range(d):
            if i == j:
                continue
            for k in range(d - 1, 0, -1):
                t[k] = add(t[k], t[k - 1], P)
                t[k - 1] = multiply(t[k - 1], -x[j], P)
        for j in range(d):
            p[j] = add(p[j], t[j], P)

    return p

def main():
    d = 0
    x = []
    y = []

    parser = argparse.ArgumentParser(description="Process the path and prime argument.")
    parser.add_argument("P", type=int, help="Prime number for Galois Field")
    parser.add_argument("path", type=str, help="Path to the file")

    args = parser.parse_args()

    if args.path:
        if not os.path.exists(args.path):
            print(f"Error: The file at '{args.path}' doesn't exist!")
            return
        else:
            with open(args.path, "r") as f:
                try:
                    for line in f:
                        split = line.split(" ")
                        if len(split) != 2:
                            raise ValueError("Invalid number of values in a line")
                        x.append(int(split[0]))
                        y.append(int(split[1]))
                        d += 1
                    p = interpolate(d, x, y, args.P)
                    for i in p:
                        print(i, end=" ")
                    print()
                except:
                    print("Error: Invalid input format")

if __name__ == "__main__":
    main()
