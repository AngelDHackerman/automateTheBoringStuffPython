#!/bin/python3

market_2nd = {'ns': 'green', 'we': 'red'}

def switchLights (intersection):
  for key in intersection.keys():
    if intersection[key] == 'green':
      intersection[key] = 'yellow'
    elif intersection[key] == 'yellow':
      intersection[key] = 'red'
    elif intersection[key] == 'red':
      intersection[key] = 'green'

  assert 'red' in intersection.values(), 'Neither light is red!' + str(intersection)  # ? it will validate if there is a red ligth 

switchLights(market_2nd)