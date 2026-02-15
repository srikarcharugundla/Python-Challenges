name=input("enter your full name:")
email=input("enter your email:")
mobile=input("enter your mobile number:")
Age=int(input("enter your age:"))
if name.count(" ") < 1 or name[0] == " " or name[len(name) - 1] == " " or email[0] == '@' or email.count(
        "@") != 1 or email.count(".") != 1 or len(mobile) != 10 or not mobile.isdigit() or mobile[
    0] == 0 or Age < 18 or Age > 60:

 print("User Profile is VALID")
else:
   print("User Profile is NOT VALID")
