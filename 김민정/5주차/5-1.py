grades = []
for _ in range(5):
    grade = int(input())
    
    if grade < 50:
        grade = 50
        grades.extend[(grade)]
        
        average_grade = sum(grades) // 5
        
        print(average_grade)