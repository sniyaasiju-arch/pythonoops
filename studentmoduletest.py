#this python file is to test all funtionally


from module.student.student import studentclass

      #step : student registration test case


email = input("enter your email")
password = input("enter your password")



s1 = studentclass()
s1.setusernameandpassword(email,password)

print(s1.email_address,s1.password)


#test basic details entering for student registration flow

full_name = input("enter your full name")
date_of_birth_or_age = input("enter your date of birth or age")
gender = input("enter your gender")
preferred_language = input("enter your preferred language")
school_college_name = ("enter your school or college name")
class_grade = ("enter your class or grade")
board_curriculum = ("enter your ")
board_curriculum = ("enter your board or curriculum")
academic_year = ("enter your academic year")
