#company will give bonus base on following criteria
#Time spent in company         Bonus 
#greater than 18 years          10%

#more than 6 and less
# than 10                        8%

#less than 6                     5%
#ask the salary and time spent from the user 
#print the net bonus amount accordingly
time = int(input("time spent in the company"))
salary = int(input("salary from"))

if time>10:
    print("bonus is 10%")
elif time < 10 and time > 6:
  print("bonus 8%")
else:
     print("5%")