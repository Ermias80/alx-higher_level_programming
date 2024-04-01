#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    try:
        for i in range(list_length):
            try:
                div = 0
                if isinstance(my_list_1[i], (int, float)) and isinstance(my_list_2[i], (int, float)):
                    if my_list_2[i] != 0:
                        div = my_list_1[i] / my_list_2[i]
                    else:
                        print("division by 0")
                else:
                    print("wrong type")
            except IndexError:
                print("out of range")
            finally:
                result.append(div)
    except:
        pass
    finally:
        return result
