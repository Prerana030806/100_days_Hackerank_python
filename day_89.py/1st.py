N, X = map(int, input().split())
scores = [list(map(float, input().split())) for _ in range(X)]
for student_scores in zip(*scores):
    avg = sum(student_scores) / X
    print(f"{avg:.1f}") 
