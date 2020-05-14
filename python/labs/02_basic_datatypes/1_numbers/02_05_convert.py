'''

Demonstrate how to:

    1) Convert an int to a float
    2) Convert a float to an int
    3) Perform floor division using a float and an int.
    4) Use two user inputted values to perform multiplication.

    Take note of what information is lost when some conversions take place.

'''

int_to_float = float(42)
print(f"42 to float is {int_to_float}\n")

float_to_int = int(123.18)
print(f"123.18 to int is {float_to_int}\n")

print("Floor division 42 / 2:", 42 // 2,
      "; Same for float 123.18 / 2:", 123.18 // 2)

value_1 = float(input("Enter first number: "))
value_2 = float(input("Enter second number: "))

print("Multiplication complete:", value_1 * value_2)
