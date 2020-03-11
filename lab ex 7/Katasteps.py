def add(number_str):
    if number_str == "":
        return 0
        
    value = 0
    for i in number_str.split(","):
        i = int(i)
        value += i

    return value
