import pandas as pd
df = pd.read_csv('main.csv')
mass = df['Mass'].tolist()
radius = df['Radius'].tolist()
newMass =[]
newRadius = []
gravity = []
for i in range(1,50,2):
    m = float(mass[i])
    r = float(radius[i])
    newMass.append(m)
    newRadius.append(r) 
    g = 6.67 * pow(10,-11) * m / pow(r,2) 
    gravity.append(g)
newDf = pd.DataFrame({'Raduis':newRadius,'Mass':newMass,'Gravity':gravity})
newDf.to_csv('calculation.csv')