import argparse
import os

def interpolate(d : int, x : list[float], y : list[float]):
    
    p = [0 for i in range(d)]
    
    for i in range(d):
        product = 1.0
        for j in range(d):
            t = [0 for i in range(d)]
        for j in range(d):
            if (i == j):
                continue
            product *= (x[i] - x[j])
        product = y[i] / product
        t[0] = product
        for j in range(d):
            if (i == j):
                continue
            for k in range(d - 1,0,-1):
                t[k] += t[k - 1]
                t[k - 1] *= (-x[j])
        for j in range(d):
            p[j] += t[j]
    
    return p

def main():
    # Initialize the parser
    d = 0
    x = []
    y = []

    parser = argparse.ArgumentParser(description="Process the path argument.")
    
    parser.add_argument("path", type=str, help="Path to the file")

    args = parser.parse_args()

    if args.path:
        if not os.path.exists(args.path):
            print(f"Error: The file at '{args.path}' doesn't exist!")
            return
        else:
            f = open(args.path, "r")
            try:
                for line in f:
                    split = line.split(" ")
                    if len(split) != 2:
                        raise ValueError("")
                    x.append(float(split[0]))
                    y.append(float(split[1]))
                    d += 1
                p = interpolate(d,x,y)
                for i in p:
                    print(i,end=" ")
                print()
            except:
                print("Error: Invalid input format")

if __name__ == "__main__":
    main()