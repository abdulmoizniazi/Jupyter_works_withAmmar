# print(4+5)
# print(6-2)
# print(8/4)
# print(4*6)
# print(77%3)

# print(8//4)
# print(2**3)
# print(3**2/2*3/3+6-4)



# name = input("what is your name? ")
# age = input("what is your age? ")
# greetings = "Hello!"
# print(greetings, name,", you are still young")



# moiz_age = 4
# school_age = 5
# print(school_age<=moiz_age)



# school_age = 5
# student_name = input("what is your name? ")
# student_age = input("what is your age? ")
# student_age = int(student_age)
# greetings = "Hello! "
# print(type(student_age))
# print(greetings, student_name, student_age>=school_age)


# school_age = 5
# student_name = input("what is your name? ")
# student_age = input("what is your age? ")
# student_age = int(student_age)
# if student_age==school_age:
#     print(student_name, "is eligible to go to school")
# elif student_age>school_age:
#     print(student_name, "should join college")
# else:
#     print(student_name, "is too young to join the school")



# def school_calculator(age):
#     if age == 5:
#         print("student_name can go to school")
#     elif age >5:
#         print("student_name should go to higher school")
#     else:
#         print("student_name is too young to join school")

# school_calculator(3)



# machine learning function
# def future_age(age):
#     new_age= age+20
#     return new_age
#     # print(new_age)

# future_predicted_age = future_age(17)
# print(future_predicted_age)

# x=0
# while (x<=5):
#     print(x)
#     x=x+1


# for x in range(6,10):
#     print(x)


# months = ["jan","feb","mar","apr","may","jun","jul"]

# for m in months:
#         if (m=="may"): break
#         print(m)


# months = ["jan","feb","mar","apr","may","jun","jul"]

# for m in months:
#         if (m=="may"): continue
#         print(m)


# import math
# print("the value of pi is", math.pi)

# import statistics
# x= [150,250,350,450]
# print("the mean of array is", statistics.mean(x))


import seaborn as sns 
import matplotlib.pyplot as plt
sns.set_theme(style="ticks", color_codes=True)

titanic= sns.load_dataset("titanic")
# print(titanic)
p1=sns.countplot(x="sex",  hue = "class" , data=titanic)
p1.set_title("data scientist moiz k plot")
plt.show()

# p1=sns.countplot(x="who",  hue = "alone" , data=titanic)
 


