state_capitols = {"Washington": "Olympia", "Oregon": "Salem", "California": "Sacramento"}

'''for state in state_capitols:
    print(state)'''

'''for city in state_capitols.values():
    print(city)'''

""" for state in state_capitols:
    print(state_capitols[state], "is the capital of", state) """

for state, city in state_capitols.items():
    print(city, "is the capital of", state)