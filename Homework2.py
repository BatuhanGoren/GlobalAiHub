'''-------------------------------------- IDENTİFİCATİON PROGRAM --------------------------------'''
name=str(input("What is your name?")) 
last_name=str(input("What is your last name?"))
age=int(input("How old are you?"))
date_of_birth=int(input("What is your date of birth?(Please just enter your year)"))
user_list=[name,last_name,age,date_of_birth]
print(user_list)
if age<=0:
    print("Age is invalid value!!")
elif date_of_birth != 2020-age:
    print("Your date of is birth wrong")
elif age<18:
    print("You can't go out because it's too dangerous")
else:
    print("You can go out to street")



