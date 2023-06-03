"""time value of money"""

# future value - is the value of a current asset at a specified date in the future based on an 
# assumed rate of growth over time 


"""x = "invested amount"
r = "interest rate"
n = "no of years"""

# formula_for_future_value = x * ( 1+r)**n

Present_value = "Defines how much a future sum of money is worth today given a specified rate of %"
# because future money != present money due to inflation

#formula_for_present_value = x/(1+r)**n

# time value of money - the most important concept in finance is that of the money worth today is more
# than the money in the future due to inflation...


from math import exp as e

def future_discrete_value(x, r, n): 
    return x * (1 + r) ** n

def present_discrete_value(x, r, n): 
    return x * (1 + r) ** -n

def future_continuous_value(x, r, t): 
    return x * e(r * t)

def present_continuous_value(x, r, t): 
    return x * e(-r * t)

if __name__ == "__main__": 
    # value of investment
    x = 100
    # interest rate
    r = 0.05
    # duration
    n = 5  # years
    # time
    t = 5  # years

    print(future_discrete_value(x, r, n))
    print(present_discrete_value(x, r, n))
    print(future_continuous_value(x, r, t))
    print(present_continuous_value(x, r, t))







