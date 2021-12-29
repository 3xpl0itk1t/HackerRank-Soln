if __name__ == '__main__':
    list = []
    for _ in range(int(input())):
        lst_f = []
        name = input()
        score = float(input())
        lst_f.append(name)
        lst_f.append(score)
        list.append(lst_f)
    print(list)
    def sort(list):
        list.sort(key = lambda x: x[1])
        return list
    print(sort(list))