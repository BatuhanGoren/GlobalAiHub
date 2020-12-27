import time
import sys
lessons = ["1:Analysis", "2:Lineer Algebra", "3:Number Theory", "4:Analytical Geometry", "5:Computer applications", "6:Differential equations"]
number_of_lessons = len(lessons)
x = []
print("You have 3 chances to enter")
count=1
while count < 4:
	name = input("What is your name?")
	surname = input("What is your surname?")
	if name =='Batuhan' and surname=='Gören':
		print("Welcome {} {}" .format(name, surname))
		break
	else:
		print('Incorrect information try again.')
		print("{}.nd attempt" .format(count))
		count += 1
		if count == 4:
			print('3rd attempt also failed (Sorry :(')
			sys.exit(1)
print("Please select a minimum of 3 and a maximum of 5 courses from the list.")
print(lessons)
time.sleep(1)
count1 = 0
while count1 < 5:
	y = int(input(" Make your choice of your lesson (1-6):"))
	if(y == 1):
		if ('1:Analysis' in x):
			print("\n * you have already chosen the Analysis lesson ")
			count1 -= 1
		else:
			x.append(lessons[0])
			print("\n=> {} lesson successfuly added \n".format(lessons[0]))
			print(x),
	if (y == 2):
		if ('2:Lineer Algebra' in x):
			print("\n *you have already chosen the Lineer Algebra")
			count1 -= 1
		else:
			x.append(lessons[1])
			print("\n=> {} lesson successfuly added \n".format(lessons[1]))
			print(x)
	if (y == 3):
		if ('3:Number Theory' in x):
			print("\n *you have already chosen the Number Theory lesson")
			count1 -= 1
		else:
			x.append(lessons[2])
			print("\n=> {} lesson successfuly added \n".format(lessons[2]))
			print(x)
	if (y == 4):
		if ('4:Analytical Geometry' in x):
			print("\n *you have already chosen the Analytical Geometry lesson")
			count1 -= 1
		else:
			x.append(lessons[3])
			print("\n=> {} lesson successfuly added \n".format(lessons[3]))
			print(x)
	if (y == 5):
		if ('5:Computer applications' in x):
			print("\n *you have already chosen the Computer applications lesson")
			count1 -= 1
		else:
			x.append(lessons[4])
			print("\n=> {} lesson successfuly added \n".format(lessons[4]))
			print(x)
	if (y == 6):
		if ('6:Differential equations' in x):
			print("\n *you have already chosen the Differential equations lesson")
			count1 -= 1
		else:
			x.append(lessons[5])
			print("\n=> {} lesson successfuly added \n".format(lessons[5]))
			print(x)
	count1 += 1
	print("You took total {} lessons".format(len(x)))
	if count1 < 3:
		print("You have to choose at least 3 lesson, otherwise you will be considered as failing.")
	if  count1 >= 3 and \
		count1< 5:
		print("You have the right to choose 5 lessons")
	if count1 == 5:
		print("***Congratulations. You have completed the lesson selection***")
		x.sort()
		print(" The lesson you enrolled in {}" .format(x))
		print("Select one of the lesson you have taken above to take the exam.")
		examy = int(input("Choose a lesson for the exam (1-6):"))
		if (examy == 1):
			print("\n*The lesson you will take the exam Analysis")
		if (examy == 2):
			print("\n*The lesson you will take the exam Lineer Algebra")
		if (examy == 3):
			print("\n*The lesson you will take the exam Number Theory")
		if (examy == 4):
			print("\n*The lesson you will take the exam Analytical Geometry")
		if (examy == 5):
			print("\n*The lesson you will take the exam Computer applications")
		if (examy == 6):
			print("\n*The lesson you will take the exam Differential equations")
print("Enter Your Notes:")
while True:
    try:
        midterm = int(input('midterm: '))
    except ValueError:
        print("Enter number")
        exit(-1)
    if 0 < midterm <=100:
        break
    else:
        print("Midterm exam grade must be between 1-100")
while True:
    try:
        project = int(input('project: '))
    except ValueError:
        print("Enter number")
        exit(-1)
    if 0 < project <=100:
        break
    else:
        print("project note must be between 1-100")
while True:
    try:
        final = int(input('final: '))
    except ValueError:
        print("Enter number")
        exit(-1)
    if 0 < final <=100:
        break
    else:
        print("Final exam grade must be between 1-100")
q = midterm * 0.3 + final * 0.5 + project * 0.2
if 89 < q:
    p = "AA"
elif 69 < q < 90:
    p = "BB"	
elif 49 < q < 70:
    p = "CC"
elif 29 < q < 50:
	p = "DD"
elif q< 30:
	p = "FF"
print("Your lesson outcome: ({}) {}".format(p, round(q, 2)))
if p == 'FF':
	print("You have failed")
else:
	print("Congratulations, you passed")