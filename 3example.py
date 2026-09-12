print("A B C | ex_1 ex_2 ex_3")
print("----------------")

for A in range(2):
    for B in range(2):
        for C in range(2):

            ex_1 = int((not (A and B)) or (not (A or C)))

            ex_2 = int((A and B) or ((not B) and C))

            ex_3 = int((A and B) or (not C))

            print(A, B, C, "|", ex_1, ex_2, ex_3)