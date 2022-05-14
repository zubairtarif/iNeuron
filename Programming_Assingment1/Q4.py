def main():
	a = 10
	b = 20
	print("Initially, a is", a, "and b is", b)
	a = 10
	temp = a
	a= b
	b = temp
	print("After swapping, a is", a, "and b is", b)

if __name__ == "__main__":
    main()