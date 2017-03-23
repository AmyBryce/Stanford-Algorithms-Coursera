# Test Case - #1 - 15 numbers
# Ans - 56
# l = [ 9, 12, 3, 1, 6, 8, 2, 5, 14, 13, 11, 7, 10, 4, 0 ]
# A = [5, 1, 3, 6, 4, 2]

# TEST CASE - 1
# A = [1,3,5,2,4,6]
# ANS - 3

# TEST CASE - 2
# A= [1,5,3,2,4]
# ANS - 4

# TEST CASE - 3
# A= [5,4,3,2,1]
# ANS - 10

# TEST CASE - 4
# A = [1,6,3,2,4,5]
# ANS - 5

# Test Case - #1 - 15 numbers
# A = [ 9, 12, 3, 1, 6, 8, 2, 5, 14, 13, 11, 7, 10, 4, 0 ]
# Ans - 56

# Test Case - #2 - 50 numbers
# A = [ 37, 7, 2, 14, 35, 47, 10, 24, 44, 17, 34, 11, 16, 48, 1, 39, 6, 33, 43, 26, 40, 4, 28, 5, 38, 41, 42, 12, 13, 21, 29, 18, 3, 19, 0, 32, 46, 27, 31, 25, 15, 36, 20, 8, 9, 49, 22, 23, 30, 45 ]
# Ans - 590

# Test Case - #3 - 100 numbers
# A=[ 4, 80, 70, 23, 9, 60, 68, 27, 66, 78, 12, 40, 52, 53, 44, 8, 49, 28, 18, 46, 21, 39, 51, 7, 87, 99, 69, 62, 84, 6, 79, 67, 14, 98, 83, 0, 96, 5, 82, 10, 26, 48, 3, 2, 15, 92, 11, 55, 63, 97, 43, 45, 81, 42, 95, 20, 25, 74, 24, 72, 91, 35, 86, 19, 75, 58, 71, 47, 76, 59, 64, 93, 17, 50, 56, 94, 90, 89, 32, 37, 34, 65, 1, 73, 41, 36, 57, 77, 30, 22, 13, 29, 38, 16, 88, 61, 31, 85, 33, 54 ]
# Ans - 2372


f = file("IntegerArray.txt")
lines = f.readlines()
A = map(int, lines)


####################
# BRUT FORCE
####################

def brutforce(l):
    count = 0
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[i] > l[j]:
                count = count + 1
    return count

#bf = brutforce(A)
#print "brut force: {ans}".format(ans=bf)


####################
# DIVIDE & CONQUER
####################

def mergeandcountsplitinv(B, C):
    D =[]
    count = 0
    Bindex = 0

    for i in range(len(C)):
        for j in range(Bindex, len(B)):
            if B[j] < C[i]:
                D.append(B[j])
                Bindex = j + 1
            elif C[i] < B[j]:
                count = count + (len(B) - Bindex)
                break
        D.append(C[i])

    for j in range(Bindex, len(B)):
        D.append(B[j])

    return [D, count]

def sortandcount(A):
    if len(A) == 1:
        return [A, 0]

    B, x = sortandcount(A[:len(A)/2])
    C, y = sortandcount(A[len(A)/2:])
    D, z = mergeandcountsplitinv(B, C)

    return [D, x + y + z]

_, dac = sortandcount(A)
print "divide and conquer: {ans}".format(ans=dac)
