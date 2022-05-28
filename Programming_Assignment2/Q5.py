# 5. Write a Python program to swap two variables without temp variable?

def main():
   a = 5324432
   b = 121211

   a = a + b
   b = a - b
   a = a - b
   
   print(f"a = {a}\nb = {b}")
        
if __name__ == "__main__":
    main()