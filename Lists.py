if __name__ == '__main__':
    n = int(input())
    output_list=[]
    for i in range(n):
        query = input().split()
        if query[0]=="insert":
            output_list.insert(int(query[1]),int(query[2]))
        elif query[0]=='print':
            print(output_list)         
        elif query[0]=='remove':
            for x in output_list:
                if int(x)==int(query[1]):
                    output_list.remove(int(query[1]))
                    break            
        elif query[0]=='append':
            output_list.append(int(query[1]))
        elif query[0]=='sort':
            output_list = sorted(output_list, key=lambda x: (isinstance(x, str), x))
        elif query[0]=='pop':
            output_list.pop()
        else:
            output_list.reverse()
