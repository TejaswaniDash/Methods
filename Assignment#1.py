"""
TAX in US based on states:

Create a method, which takes the state and gross income as the arguments
and returns the net income after deducting tax based on the state.

Assume Federal Tax: 10%
Assume state tax on your wish.

You don't have to do for all the states, just take 3-4 to solve the
purpose of the exercise.

"""

def calculate_NetIncome(gross, state):
    """ #doxtrine
    Calculate the net income after state and federal tax
    :param gross: Gross Income
    :param state: State Income
    :return: Net Income
    """

state_tax = {'CA':10, 'NYC':9, 'NJ':6, 'TX':0, 'VA':8}
#concept of dictionary used
#calculate net income after federal tax
net= gross - (gross * .10)

#calculate net income after state tax
if sate in state_tax:
   net = net - (gross * state_tax[state] / 100)
   print(" Your Net Income after all the heavy taxes is: " + str(net))
   return net

else:
    print("State not in the list")
    return None


CalculateNetIncome(150000, 'VA')