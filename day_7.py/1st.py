if __name__ == '__main__':
  students = []
  for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
  scores = []
  for s in students:
      scores.append(s[1])
  unique = sorted(set(scores))
  sec = unique[1]
  result = []
  for s in students : 
      if s[1] == sec :
        result.append(s[0])
  result.sort()
  for name in result :
      print(name)
      
