if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    sum=0
    reqd_marks= student_marks[query_name]
    for i in range(len(reqd_marks)) :
        sum+=reqd_marks[i]
    print("%.2f" %(sum/3))
        
