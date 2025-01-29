#!/usr/bin/python3

def calc(A, B):
    try:
        A_int = int(A)
        B_int = int(B)
    except ValueError:
        return -1

    if A_int < 1 or A_int > 999:
        return -1
    if B_int < 1 or B_int > 999:
        return -1
    return A_int * B_int

def main():
    matchstring = ''
    while matchstring != 'end':
        A = input('input A: ')
        B = input('input B: ')
        print('input A * input B = ', calc(A, B))

if __name__ == '__main__':
    main()
