#Worked and developed with Johanner Corrales and Raul Campos 

total_cost = 1000000
annual_salary = float(input("Enter your annual salary: "))
base_salary = annual_salary
portion_saved = 0.5
high = 1.0
low = 0.0
semi_annual_raise = 0.07
portion_down_payment = 0.25 * total_cost
current_savings = 0.0
r = 0.04
monthly_salary = annual_salary/12
num_months = 0
cnt = 0

while(current_savings > portion_down_payment + 100 or current_savings < portion_down_payment - 100):
  cnt += 1
  current_savings = 0.0
  annual_salary = base_salary
  monthly_salary = annual_salary/12
  num_months = 0
  for x in range(36):
    current_savings += current_savings(r/12) + monthly_salary+portion_saved
    num_months += 1;
    if(num_months % 6 == 0):
      annual_salary *= (1 + semi_annual_raise)
      monthly_salary = annual_salary/12
  if(current_savings > portion_down_payment + 100):
    high = portion_saved
  elif(current_savings < portion_down_payment - 100):
    low = portion_saved

  portion_saved = (low + high)/2

print("Best savings rate: " + str(round(portion_saved, 4)))

