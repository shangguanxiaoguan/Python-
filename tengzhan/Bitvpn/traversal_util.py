import time


alist = ['500576669346975744', '492951197834432512', '492887577595367425']


def traversal_list(alist, i):
    while True:
        length = len(alist)
        i = i % length
        yield alist[i]
        i += 1


def traversal_list2(alist):
    i = 0
    f = traversal_list(alist, i)
    while True:
        a = next(f)
        print(a)
        time.sleep(1)
        i += 1


if __name__ == '__main__':
    alist = [1, 2, 3, 4, 5]
    # alist = ['500576669346975744', '492951197834432512', '492887577595367425']
    traversal_list2(alist)

