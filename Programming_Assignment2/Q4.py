# 4. Write a Python program to solve quadratic equation?

def main():
    # Quadtratic Equation of the form:
    # ax^2 + bx + c = 0
    # Equation has two roots

    a = 1
    b = 2
    c = 1

    x1 = ( (-1 * b) + ( (b * b) - (4 * a * c) )**0.5 ) / (2 * a)
    x2 = ( (-1 * b) - ( (b * b) - (4 * a * c) )**0.5 ) / (2 * a)

    if ((b * b) - (4 * a * c) ) < 0 :
        print ("Equation has complex roots.)")
    else:
        print (f"Roots for quadratic equation with co-efficients a={a}, b={b} and c={c} are {x1} and {x2}.")
        
if __name__ == "__main__":
    main()