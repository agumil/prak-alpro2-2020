def bubbleSortAsc(A):
    print('================== Ascending ===================')
    print('Deret :', A, '\n')
    tukar = True
    while tukar:
        tukar = False
        for j in range(len(A) - 1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
                tukar = True
                print('tukar', A[j], 'dengan', A[j+1])
                print('urutan menjadi', A)

def bubbleSortDesc(A):
    print('================== Descending ===================')
    print('Deret :', A, '\n')
    tukar = True
    while tukar:
        tukar = False
        for j in range(len(A) - 1):
            if A[j] < A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
                tukar = True
                print('tukar', A[j], 'dengan', A[j+1])
                print('urutan menjadi', A)

A = [3, 1, 8, 4, 2]
bubbleSortAsc(A)

A = [3, 1, 8, 4, 2]
bubbleSortDesc(A)
