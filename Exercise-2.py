# Student Grade Calculator  
marks1 = int(input(" Enter a marks1:"))
marks2 = int(input(" Enter a marks2:"))
marks3 =int(input(" Enter a marks3:"))
marks4 = int(input(" Enter a marks4:"))
marks5 = int(input(" Enter a marks5:")) 

average = (marks1 + marks2 + marks3 + marks4 + marks5) / 5

if average >=90 :  
   grade = "A++" 
  

else:
    grade = "B"

print("Average Marks:",average)
print("Grade:", grade)