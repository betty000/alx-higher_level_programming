#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    real = 0
    if isinstance(my_list, list) and isinstance(x, int):
        for i in range(x):
            try:
                print("{}".format(my_list[i]), end="")
            except:
                pass
            else:
                real += 1
    print("")
    return real
