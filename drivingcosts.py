# Function driving_cost() with input parameters miles_per_gallon, dollars_per_gallon, and miles_driven, 
# that returns the dollar cost to drive those miles. All items are of type float.
def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven):
    # Calculate dollar_cost (miles_driven / miles_per_gallon x dollars_per_gallon)
    dollar_cost = (miles_driven / miles_per_gallon) * dollars_per_gallon
    # return dollar_cost
    return dollar_cost

if __name__ == '__main__':
    # Inputs are the car's miles per gallon and the price of gas in dollars per gallon (both float). 
    mpg = float(input())
    gas_price = float(input())
    # Output the gas cost for 10 miles
    print(f'{driving_cost(mpg, gas_price, 10):.2f}')
    # Print results from function call passing 10 for miles 
    
    # Output the gas cost for 50 miles
    print(f'{driving_cost(mpg, gas_price, 50):.2f}')
    # Print results from function call passing 50 for miles
    
    # Output the gas cost for 400 miles
    print(f'{driving_cost(mpg, gas_price, 400):.2f}')
    # Print results from function call passing 400 for miles