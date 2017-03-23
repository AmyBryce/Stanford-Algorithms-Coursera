def add(a, b):
    a = [0] + a
    b = [0] + b

    if len(a) > len(b):
        b = ([0] * (len(a) - len(b))) + b
    else:
        a = ([0] * (len(b) - len(a))) + a

    carry = 0
    tmparray = []

    for i in reversed(range(len(b))):
        result = b[i] + a[i] + carry

        enddigit = result % 10

        carry = 0
        if result >= 10:
            carry = result / 10

        tmparray = [enddigit] + tmparray

    return tmparray

def multiply(a, b):
    a = [0] + map(int, a)
    b = [0] + map(int, b)

    carry = 0
    finalarray = [0]

    for i in reversed(range(len(b))):
        tmparray = []
        for j in reversed(range(len(a))):
            result = (b[i] * a[j]) + carry

            enddigit = result % 10

            carry = 0
            if result >= 10:
                carry = result / 10

            tmparray = [enddigit] + tmparray

        tmparray = tmparray + [0] * (len(b) - i - 1)

        finalarray = add(finalarray,  tmparray)

    return ("".join(map(str, finalarray))).lstrip("0")


print multiply("3141592653589793238462643383279502884197169399375105820974944592", "2718281828459045235360287471352662497757247093699959574966967627")

# Answer: 8539734222673567065463550869546574495034888535765114961879601127067743044893204848617875072216249073013374895871952806582723184

######################################
#
# For testing accuracy and edge cases:
#
######################################

# print 9 * 9
# print multiply("9", "9")

# print 1234 * 5678
# print multiply("1234", "5678")

# print 31415 * 27182
# print multiply("31415", "27182")
