#Programmer: Ben Krehbiel
#Date: 1/27/2025
#Title: Conversions

def temp_conversion():
    x = float(input("Enter celsius temperature: "))
    result = (x * 9/5) + 32
    print(f"That equates to {result:.2f}")

#mainline
temp_conversion()