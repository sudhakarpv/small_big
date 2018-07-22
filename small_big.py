# small_big
def main():
    pass
    n=input()
    user=list(map(int,input().split()))
    k=sorted(user)
    print(k[0],k[-1])

if __name__ == '__main__':
    main()
