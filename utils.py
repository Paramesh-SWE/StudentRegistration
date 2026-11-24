def input_validation(inp: int | str, valid_type: int | str, min_len: int, max_len: int, valid: bool = False) -> bool | str:
    
    if not type_check(valid_type,datatype = type(inp)):
        return "\nPlease enter a valid datatype, The datatype you have entered is wrong."
        
    if not check_length(inp, min_len, max_len,datatype = type(inp)):
        return "\nPlease enter the valid values and follow the rules."
    
    valid = True
    return valid


def type_check(valid_type: int | str, datatype: int | str) -> bool:
    if valid_type == datatype:
        return True
    return False
    
            
def check_length(inp: int | str, min_len, max_len, datatype: int | str) -> bool:
    if datatype == str:
        if len(inp) < min_len:
            print(f"\nThe length of the string you entered {inp} is less than the minimum length allocated.")
            return False
        elif len(inp) > max_len:
            print(f"\nThe length of the string you entered {inp} is more than the maximum length allocated.")
            return False
        else:
            return True
    
    else:
        if inp < min_len:
            print(f"\nThe length of the integer you entered {inp} is less than the minimum value allocated.")
            return False
        elif inp > max_len:
            print(f"\nThe length of the integer you entered {inp} is more than the maximum value allocated.")
            return False
        else:
            return True
         




if __name__ == "__main__":
    test = 0
    print(input_validation("Paramesh", str, 0,5,))