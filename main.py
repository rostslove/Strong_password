import re


def strong_password(password):
    test_counter = 0
    test_num = False
    test_upper = False
    test_lower = False
    if len(password) >= 7:
        test_counter += 1
    for i in range(len(password)):
        if password[i].isdigit():
            test_num = True
        if password[i].isupper():
            test_upper = True
        if password[i].islower():
            test_lower = True
        if test_num and test_upper and test_lower:
            test_counter += 1
            break
    if re.match("^[A-Za-z0-9]*$", password):
        test_counter += 1
    if len(password) == len(set(password)):
        test_counter += 1
    if test_counter == 4:
        return "Strong password"
    else:
        return "Weak password"

