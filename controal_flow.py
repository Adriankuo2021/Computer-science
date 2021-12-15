#programs make desicion based on control logic (cointrol flow)
student_grade = 99

if student_grade > 90:
    print("your grade is A")
elif student_grade < 90 and student_grade > 80:
    print("your grade is a B")
elif student_grade < 80 and student_grade > 70:
    print("Your grade is a C")
else:
    print("your grade is a D or F")
#write  program useing if elif else that......
#write a program using if-elif-else that....
#looks at a variable for temperature = 20C
#if temperature is above 30 C, print it's hot
#elif temperature is above 10 C, but below 30 C, print it's warm
#elif temperature is below 10 C, print it's cold
#else print "bring an umbrella just in case"
temprerature = 20 
if temprerature > 30:
    print("it's hot")
elif temprerature > 10 and temprerature < 30:
    print("it's warm")
elif temprerature < 10 and temprerature > 5:
    print("it's cold")
else:
    print("bring an umbrala")
