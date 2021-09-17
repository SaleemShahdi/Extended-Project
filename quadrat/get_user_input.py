from re import fullmatch

class Input:
    @staticmethod
    def read_double(text):
        try:
            x = input(text)
            x = float(x)
            return x
        except ValueError:
            return Input.read_double("That is not a number. Enter again: ")

    @staticmethod
    def get_decision(text):
        x = input(text)
        if fullmatch("([Yy](es)?)|(YES)", x):
            '''had to debug <search> and <match> vs <fullmatch>.
               search and match would incorrectly return "Ye" and "ye" as True. 
               fullmatch correctly returned them as False.
               Must have something to do with the way search and match are defined,
               but I don't have a proper explanation. Here is a link to the documentation:
               https://docs.python.org/3/library/re.html'''
            return True
        elif fullmatch("([Nn]o?)|(NO)", x):
            return False
        else:
            return Input.get_decision("Enter yes or no: ")

