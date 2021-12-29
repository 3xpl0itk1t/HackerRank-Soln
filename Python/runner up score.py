if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    arr = list(set(arr))
    arr_f = list(arr)
    arr_f.sort()
    print(arr_f)
    print(arr_f[-2])