if __name__ == '__main__':
    names=[]
    scores=[]
    for _ in range(int(input())):
        names.append(input())
        scores.append(float(input()))
        
        
    records = [[names[i], scores[i]] for i in range(min(len(names),len(scores)))]
    
    
smallest = min(scores)
second = None
for score in scores:
    if score != smallest:
        if second is None or score < second:
            second = score

indices_list = [i for i in range(len(records)) if records[i][1] == second]
final=[]
for i in range(len(indices_list)):
    final.append(records[indices_list[i]][0])
sorted_list=sorted(final)
for i in sorted_list:
    print(i)
