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
        print("Sorry, the answer is imaginary")
        decision = input.get_decision("Would you like to try again? ")
        return main(decision)
    positive_root = ((-(b) + sqrt(q)) / (2 * a))
    negative_root = ((-(b) - sqrt(q)) / (2 * a))
    if positive_root == negative_root:
        result = positive_root
        print(f"The zero is {result}")
    else:
        result1 = negative_root
        result2 = positive_root
        print(f"The zeros are {result1} and {result2}")
    decision = input.get_decision("Would you like to solve another equation? ")
    return main(decision)

print("")
print("Welcome to QUADRAT, a program that effortlessly")
print("allows you to solve quadratic equations!")
print("")
print("All you have to do is enter the values for a, b and c")
print(f"""from the equation {bold("a")}x\u00b2 + {bold("b")}x + {bold("c")} = 0""")
main()



