from get_user_input import Input as input
from math import sqrt

def bold(text):
    return "\033[1m" + text + "\033[0m"

def main(decision = True):
    print("")
    if decision == False:
        print("Goodbye!")
        return
    a = input.read_double("a = ")
    if a == 0:
        print("That's a linear equation")
        decision = input.get_decision("Would you like to try again? ")
        return main(decision)
    b = input.read_double("b = ")
    c = input.read_double("c = ")
    b_squared = b**2
    four_ac = 4 * a * c
    q = b_squared - four_ac
    if q < 0:
        q = q / (-1)
        # print("Sorry, the answer is imaginary")
        # decision = input.get_decision("Would you like to try again? ")
        complex_positive = complex(-b, sqrt(q))
        positive_root = complex_positive / complex(2*a, 0)
        complex_negative = complex(-b, -sqrt(q))
        negative_root = complex_negative / complex(2*a, 0)
        if negative_root.real == 0:
            negative_root = complex(-negative_root.real, negative_root.imag)
    else:
        positive_root = ((-(b) + sqrt(q)) / (2 * a))
        negative_root = ((-(b) - sqrt(q)) / (2 * a))
    if positive_root == negative_root:
        result = positive_root
        print(f"The zero is {result}")
    else:
        result1 = negative_root
        result2 = positive_root
        print(f"The zeros are {result1:.2f} and {result2:.2f}") # prints results rounded to 2 decimal places. Note: will also round numbers that Python stored with < 2 decimal places to 2 decimal places
    decision = input.get_decision("Would you like to solve another equation? ")
    return main(decision)

print("")
print("Welcome to QUADRAT, a program that effortlessly")
print("allows you to solve quadratic equations!")
print("")
print("All you have to do is enter the values for a, b and c")
print(f"""from the equation {bold("a")}x\u00b2 + {bold("b")}x + {bold("c")} = 0""")
main()



