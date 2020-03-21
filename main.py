import random


ShortageCost = 100
HoldingCost = 50
SellingPrice = 450

profitlist = list()
x = list()


def random_0to1():
    return random.uniform(0, 1)

def get_x():
  randProbability = random_0to1()
  if randProbability>=0 and randProbability<0.2:
       x = 0
  elif randProbability>=0.2 and randProbability<0.6:
       x = 1                              
  elif randProbability>=0.6 and randProbability<0.8:
       x = 2
  elif randProbability>=0.8 and randProbability<0.9:
       x = 3
  else :
       x = 4
  return x

for i in range (500) : 
    x.append(get_x ())

for Order in range (1,3) :        
    available = 1
    for Week in range (500) :
        available += Order
        if x[Week]< available :
            sold = x[Week]
            available -= x[Week]
            loss = available * HoldingCost
        elif x[Week] > available :
            sold = available
            available = 0
            loss = (x[Week] - sold) * ShortageCost
        else :
            sold = x[Week]
            available = 0
            loss = 0
        revenue = sold * SellingPrice 
        profit = revenue - (loss)
        if profit >= 0 :
            profitlist.append(profit)
    if Order == 1 :
        avgProfit1 = sum(profitlist) / 500
        profitlist.clear()
    else :
        avgProfit2 = sum(profitlist) / 500

print ("1 PC per week :" , avgProfit1 ,"\n" )
print ("2 PC per week :" , avgProfit2 ,"\n" )