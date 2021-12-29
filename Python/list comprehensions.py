if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    ar = ([[i,j,k] for i in range(11) for j in range(11) for k in range(11) if (i+j+k)!=n and 0<=i<=x and 0<=j<=y and 0<=k<=z])
    print(ar)