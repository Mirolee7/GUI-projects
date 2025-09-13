
def sum_multiple_operators(input_list: list) -> float:
    try:
        result = float(input_list[0].replace(",", ""))

        # Loop through the rest of the list, two items at a time (operator, number)
        i = 1
        while i < len(input_list):
            operator = input_list[i]
            number = float(input_list[i+1].replace(",", ""))

            if operator == '+':
                result += number
            elif operator == '-':
                result -= number
            elif operator == '*':
                result *= number
            elif operator == '/':
                result /= number

            # move to the next operator
            i += 2

        return result
    except ValueError:
        raise ValueError("You've entered an invalid input.")
    except TypeError:
        raise ValueError("Only numbers are allowed.")
    except ZeroDivisionError:
        raise ValueError("You can not divide by zero.")
    except Exception:
        raise ValueError("Unexpected error occored while computing your values.")



def detect_operators(input_list: list):
    # This function is not in use at the moment
    # It is meant to be used for other calculator modules, like add, mul
    # This function will help determine whether to switch between calculator module operators.
    # You can get creative with it.
    # Set of possible operators
    valid_operators = {'+', '-', '*', '/'}
    
    # Use a set to store the unique operators found in the list
    operators_found = set()
    
    for token in input_list:
        if token in valid_operators:
            operators_found.add(token)
            
    # Check the number of unique operators found
    if len(operators_found) <= 1:
        # If one operator was found, pop it from the set to return it
        operator = operators_found.pop() if operators_found else None
        return True, operator
    else:
        # If more than one unique operator was found
        return False, False
