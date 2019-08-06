def multiply(*args):
    overall_num = 1
    for num in args:
        overall_num *= num
    return overall_num


def addition(*args):
    overall_num = 0
    for num in args:
        overall_num += num
    return overall_num

print(multiply(3,5,9,7))
