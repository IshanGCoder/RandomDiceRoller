import random
import plotly.figure_factory as ff
count = []
diceResult = []
for i in range(100):
	dice1 = random.randint(1,6)
	dice2 = random.randint(1,6)
	diceResult.append(dice1 + dice2)
	count.append(i)
print (count)
print (diceResult)
# These lines are not compatible with Termux
fig = ff.create_distplot([diceResult],["Result"])
fig.show()
