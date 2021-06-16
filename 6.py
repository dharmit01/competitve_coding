if __name__ == '__main__':
    student=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student.append([name,score])
    
    second_lowest_score = sorted(list(set([x[1] for x in student])))[1]

    desired_student = []

    for stu in student:
        if stu[1]==second_lowest_score:
            desired_student.append(stu[0])
    
    print("\n".join(sorted(desired_student)))

    
