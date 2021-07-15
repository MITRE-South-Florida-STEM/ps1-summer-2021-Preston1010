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

portion_saved = getNumberFromUser("Please enter the portion saved in decimal: ")

months = 0

while(current_savings < portion_down_payment):

  current_savings += (portion_saved*monthly_salary)

  current_savings = incrementCurrentSavings(current_savings,r)
  
  months += 1

print("Number of months it takes to reach down payment: ",months)
