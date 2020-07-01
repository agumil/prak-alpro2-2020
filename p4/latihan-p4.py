def selectionShortAsc(A):
    print('================== Ascending ===================')
    print('Deret :', A, '\n')
    for i in range(len(A) - 1):
        min_idx = i
        for j in range(i+1, len(A)):
            if A[min_idx] > A[j]:
                min_idx = j
        print('Tukar index', min_idx, 'dengan index', i)
        temp = A[i]
        A[i] = A[min_idx]
        A[min_idx] = temp
        print('Iterasi ke', i, 'menjadi', A, '\n')

def selectionShortDesc(A):
    print('================== Descending ===================')
    print('Deret :', A, '\n')
    for i in range(len(A) - 1):
        min_idx = i
        for j in range(i+1, len(A)):
            if A[min_idx] < A[j]:
                min_idx = j
        print('Tukar index', min_idx, 'dengan index', i)
        temp = A[i]
        A[i] = A[min_idx]
        A[min_idx] = temp
        print('Iterasi ke', i, 'menjadi', A, '\n')
        
val = [4, 3, 5, 6, 2, 78, 98]
selectionShortAsc(val)

val = [4, 3, 5, 6, 2, 78, 98]
selectionShortDesc(val)
