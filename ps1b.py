#Worked and developed with Johanner Corrales and Raul Campos 

def getNumberFromUser(text):
  
  x = ""
  
  while(type(x) != type(0.0)):
    
    try:
        
        temp = float(input(text))
        
        x = temp
    
    except ValueError:
        
        print("Input must be a number.")
  
  return x

def incrementCurrentSavings(curSav, r):
  
  curSav += curSav*(r)/12
  
  return curSav

total_cost = getNumberFromUser("Please input total cost: ");

portion_down_payment = total_cost *0.25

current_savings = 0

r = 0.04

annual_salary = getNumberFromUser("Please input annual salary: ")

monthly_salary = annual_salary/12

portion_saved = getNumberFromUser("Please input the portion saved in decimal: ")

semi_annual_raise = getNumberFromUser("Please input ther semi annual raise in decial: ")

months = 0

while(current_savings < portion_down_payment):

  current_savings += (portion_saved*monthly_salary)

  current_savings = incrementCurrentSavings(current_savings,r)
  
  if months % 6 == 0:

    annual_salary *= (semi_annual_raise + 1)
 
  months += 1

print("Number of months it takes to reach down payment: ",months)

