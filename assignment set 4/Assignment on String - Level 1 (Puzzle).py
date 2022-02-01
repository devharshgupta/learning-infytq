# lex_auth_012693825794351104168
from collections import OrderedDict


def find_common_characters(msg1, msg2):
    msg1 = "".join(OrderedDict.fromkeys(msg1))
    msg2 = "".join(OrderedDict.fromkeys(msg2))
    test = ''
    for i in msg1:
        if i in msg2:
            test += i

    test = test.replace(" ", "")
    if test == '':
        return -1
    return test
    # pass  # Remove pass and write your logic here


# Provide different values for msg1,msg2 and test your program
msg1 = "python"
msg2 = "Python"
common_characters = find_common_characters(msg1, msg2)
print(common_characters)
