#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    real = 0
    if isinstance(my_list, list) and isinstance(x, int):
        for i in range(x):
            try:
                print("{:d}".format(my_list[i]), end="")
            except Exception as err:
                if isinstance(err, IndexError):
                    raise
            else:
                real += 1
    print("")
    return real
