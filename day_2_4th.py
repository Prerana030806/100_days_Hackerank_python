def is_leap(year):
    leap = False
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    # Write your logic here
      return True
    else :
      return False 

year = int(input())
print(is_leap(year))
