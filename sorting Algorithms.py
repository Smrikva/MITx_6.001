#bogo sort / monkey sort / stupid sort / shotgun sort
import random
def is_sorted(L):
    return all(L[i] <= L[i+1] for i in range(len(L)-1))
#ovo gore je helper za monkey sort
def bogo_sort(L):
    x = L[:]
    while not is_sorted(x):
        random.shuffle(x)
    return x
    

#bubble sort
def bubble_sort(L):
    swap = False
    while not swap:
        swap = True
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                swap = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp
        print(L)

#selection sort
def selection_sort(L):
    suffixSt = 0
    while suffixSt != len(L):
        for i in range(suffixSt, len(L)):
            if L[i] < L[suffixSt]:
                    L[suffixSt], L[i] = L[i], L[suffixSt]
        suffixSt += 1
    print(L)    
