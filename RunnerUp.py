if __name__ == '__main__':
    n = int(input())
    array = map(int, input().split())
    arr=list(array)
    largest=max(arr)
    arr.remove(largest)
    while largest==max(arr):
        arr.remove(largest)
    print(max(arr))
    
