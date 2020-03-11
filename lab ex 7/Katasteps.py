def add(number_str):
    if number_str == "":
        return 0
    
    if len(number_str) == 1:
        return int(number_str)

    return int(number_str[0]) + int(number_str[2])
    