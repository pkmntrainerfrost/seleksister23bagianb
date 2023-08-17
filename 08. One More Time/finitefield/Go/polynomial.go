package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func mod(a int, p int) int {
	return (a%p + p) % p
}

func add(a int, b int, p int) int {
	return mod(a+b, p)
}

func sub(a int, b int, p int) int {
	return mod(a-b, p)
}

func mul(a int, b int, p int) int {
	return mod(a*b, p)
}

func inv(a int, p int) int {

	t := 0
	newt := 1
	r := p
	newr := a

	for newr != 0 {
		quotient := r / newr
		temp := t
		t = newt
		newt = temp - quotient*newt
		temp = r
		r = newr
		newr = temp - quotient*newr
	}

	if t < 0 {
		t += p
	}

	return t

}

func div(a int, b int, p int) int {
	return mul(a, inv(b, p), p)
}

func interpolate(d int, P int, x []int, y []int) []int {
	p := make([]int, d)

	for i := 0; i < d; i++ {
		product := 1
		t := make([]int, d)

		for j := 0; j < d; j++ {
			if i == j {
				continue
			}
			product = mul(product, sub(x[i], x[j], P), P)
		}

		product = div(y[i], product, P)
		t[0] = product

		for j := 0; j < d; j++ {
			if i == j {
				continue
			}
			for k := d - 1; k > 0; k-- {
				t[k] = add(t[k-1], t[k], P)
				t[k-1] = mul(t[k-1], -x[j], P)
			}
		}

		for j := 0; j < d; j++ {
			p[j] = add(p[j], t[j], P)
		}
	}

	return p
}

func main() {
	if len(os.Args) < 3 {
		fmt.Println("Error: Please provide a prime number and a file path.")
		return
	}

	P, err3 := strconv.Atoi(os.Args[1])
	if err3 != nil {
		fmt.Println("Error: Not a number")
		return
	}
	path := os.Args[2]
	file, err := os.Open(path)
	if err != nil {
		fmt.Printf("Error: The file at '%s' doesn't exist!\n", path)
		return
	}
	defer file.Close()

	var x, y []int
	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		line := scanner.Text()
		split := strings.Split(line, " ")

		if len(split) != 2 {
			fmt.Println("Error: Invalid input format")
			return
		}

		xVal, err1 := strconv.Atoi(split[0])
		yVal, err2 := strconv.Atoi(split[1])
		if err1 != nil || err2 != nil {
			fmt.Println("Error: Invalid number format in the file")
			return
		}

		x = append(x, xVal)
		y = append(y, yVal)
	}

	if err := scanner.Err(); err != nil {
		fmt.Println("Error reading the file.")
		return
	}

	p := interpolate(len(x), P, x, y)
	for _, val := range p {
		fmt.Print(val, " ")
	}
}
