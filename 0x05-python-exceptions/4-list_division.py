#!/usr/bin/python3
def list_division(list_1, list_2, list_length):
    result = []
    for item in range(list_length):
        try:
            div = list_1[item] / list_2[item]
        except TypeError:
            print("wrong type")
            div = 0
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            result.append(div)
    return result
