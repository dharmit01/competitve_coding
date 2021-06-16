if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        score1 = round(float((scores[0]+scores[1]+scores[2])/3),2)
        student_marks[name] = score1
    a=student_marks[input()]
    
    #to round decimal upto 2 decimal points
    print('%.2f'%a)