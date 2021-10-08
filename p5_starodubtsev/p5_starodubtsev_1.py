salary_list = [7.3, 8.5, 11, 12.7, 15.2, 21.12, 27.35]
finally_salary = []
difference_salary = []
j=0
for i in salary_list: 

    finally_salary.append(round(float(i*1.30),2))
    difference_salary.append(round(float(i*0.30),2)) 

    print(i, finally_salary[j],difference_salary[j])
    j+=1