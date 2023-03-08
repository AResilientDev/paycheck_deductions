print("""

 _______                                __                            __              _______                   __                        __      __                               
|       \                              |  \                          |  \            |       \                 |  \                      |  \    |  \                              
| $$$$$$$\ ______   __    __   _______ | $$____    ______    _______ | $$   __       | $$$$$$$\  ______    ____| $$ __    __   _______  _| $$_    \$$  ______   _______    _______ 
| $$__/ $$|      \ |  \  |  \ /       \| $$    \  /      \  /       \| $$  /  \      | $$  | $$ /      \  /      $$|  \  |  \ /       \|   $$ \  |  \ /      \ |       \  /       \
| $$    $$ \$$$$$$\| $$  | $$|  $$$$$$$| $$$$$$$\|  $$$$$$\|  $$$$$$$| $$_/  $$      | $$  | $$|  $$$$$$\|  $$$$$$$| $$  | $$|  $$$$$$$ \$$$$$$  | $$|  $$$$$$\| $$$$$$$\|  $$$$$$$
| $$$$$$$ /      $$| $$  | $$| $$      | $$  | $$| $$    $$| $$      | $$   $$       | $$  | $$| $$    $$| $$  | $$| $$  | $$| $$        | $$ __ | $$| $$  | $$| $$  | $$ \$$    \ 
| $$     |  $$$$$$$| $$__/ $$| $$_____ | $$  | $$| $$$$$$$$| $$_____ | $$$$$$\       | $$__/ $$| $$$$$$$$| $$__| $$| $$__/ $$| $$_____   | $$|  \| $$| $$__/ $$| $$  | $$ _\$$$$$$\
| $$      \$$    $$ \$$    $$ \$$     \| $$  | $$ \$$     \ \$$     \| $$  \$$\      | $$    $$ \$$     \ \$$    $$ \$$    $$ \$$     \   \$$  $$| $$ \$$    $$| $$  | $$|       $$
 \$$       \$$$$$$$ _\$$$$$$$  \$$$$$$$ \$$   \$$  \$$$$$$$  \$$$$$$$ \$$   \$$       \$$$$$$$   \$$$$$$$  \$$$$$$$  \$$$$$$   \$$$$$$$    \$$$$  \$$  \$$$$$$  \$$   \$$ \$$$$$$$ 
                   |  \__| $$                                                                                                                                                      
                    \$$    $$                                                                                                                                                      
                     \$$$$$$                                                                                                                                                       

""")


FED_TAX = .15
STATE_TAX = .10
SSM_TAX = .10

name = input("Please enter your name: ")
hours_worked = float(input("How many hours did you work?\n"))
hourly_wage = float(input("What is your hourly wage?\n"))

def gross_pay(hours, wage):
#Calculates the user's gross pay.
#Displays the user's hours worked, hourly wage and gross pay.
  gross = hours * wage
  
  print(f"Employee: {name.upper()} \nHourly Wage: ${format(wage, '.2f')} | Hours Worked: {format(hours, '.2f')} \nGross Pay: ${format(gross, '.2f')}")
  
  deductions(gross)

def deductions(gross):
#Calculates and displays tax deductions for user's paycheck.
   fed = gross * FED_TAX
   state = gross * STATE_TAX
   ssm = gross * SSM_TAX
   total = fed + state + ssm

   print(f"Federal Tax Deducted: ${format(fed, '.2f')} | State Tax Deducted: ${format(state, '.2f')} \nSocial Security/Medicare Tax Deducted: ${format(ssm, '.2f')} | Total Taxes Deducted: ${format(total, '.2f')}")

   net_pay(gross, total)

def net_pay(gross, total):
#Calculates and displays the user's net pay.
    net = gross - total
    
    print(f"Net Pay: ${format(net, '.2f')}")

gross_pay(hours_worked, hourly_wage)