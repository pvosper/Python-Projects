principal = 1000        # Initial amount
rate = 0.05             # Interest rate
numyears = 5            # Number of years
year = 1
while year <= numyears:
    old_principal = principal
    principal = principal * (1 + rate)
    # print(year, principal, "(", principal - old_principal, ")" )     # Reminder: print(year, principal) in Python 3
    print(%d, %d, "(",%d -%d, ")")     # Reminder: print(year, principal) in Python 3
    year += 1