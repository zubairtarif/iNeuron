def main():
    a = 7.6
    b = 6.3
    c = 5.1
    s = (a + b + c) / 2.0
    area = float ( (s * (s-a) * (s-b) * (s-c)) ** 0.5 )
    print("Sides are",a,",",b,",",c)
    print("Area of triangle:", area)

if __name__ == "__main__":
    main()