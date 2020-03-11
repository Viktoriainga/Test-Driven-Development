def add(number_str):
    if number_str == "":
        return 0
        
    value = 0
    for num in number_str:
        if num.isdigit():
            value += int(num)
    
    return value

    