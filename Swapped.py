#Below we've written a function that is supposed to take in
#four parameters and produce a string representing the cost
#of a person's weekly soda consumption. Below the function
#definition, we're calling the function.
#
#However, right now, the code is erroring out. Fix this code
#without changing the code inside the function. You may
#change either the function declaration (on line 11) or the
#function call on line 27.

def soda_habit(preferred_soda, price_per_soda, calories_per_soda, sodas_per_week):
    
    #Above, we've moved preferred_soda to the beginning and
    #sodas_per_week to the end, so our original function
    #call will work.
    
    #Don't change the body of this function!
    
    money_spent = price_per_soda * sodas_per_week
    calories_consumed = calories_per_soda * sodas_per_week
    
    summary_string = "You're spending $" + str(money_spent) + " on " + preferred_soda + " per week! "
    summary_string += " That's " + str(calories_consumed) + " calories!"
    
    return summary_string

# Personal comment: line 11 has to be in that order, bc the line where we get result 
# = soda_habit("Coca-Cola", 1.75, 140, 9) is in this specific order
result = soda_habit("Coca-Cola", 1.75, 140, 9)
print(result)
