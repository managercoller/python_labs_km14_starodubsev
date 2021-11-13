salary_list = [7.3, 8.5, 11, 12.7, 15.2, 21.12, 27.35]
upper = list(map(lambda x: round(x*0.3, 2), salary_list))
new_salary = list(map(lambda x: round(x*1.3, 2),salary_list))
for i in range(len(salary_list)):
    print(salary_list[i],new_salary[i], upper[i])