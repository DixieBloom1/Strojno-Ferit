import pandas as pd
import numpy as np

mtcars = pd.read_csv('mtcars.csv')
print(mtcars)
print("5 automobila koji imaju najvecu potrosnju: ")
mtcarsFuel = mtcars.sort_values(by='mpg')
print(mtcarsFuel)

print("3 automobila s 8 cilindara i najmanjom potrosnjom: ")
mtcarsCyl = mtcars.loc[mtcars['cyl']]
print(mtcarsCyl.sort_values(by='mpg', ascending=False).head(3))

print("Srednja potrosnja automobila s 6 cilindara: ")
mtcarsAvg6 = mtcars.loc[(mtcars['cyl'] == 6)]
print(mtcarsAvg6)
print(mtcarsAvg6['mpg'].mean())

print("Srednaj potrosanj automobila s 4 cilindara i mase između 2000 i 2200 lbs: ")
mtcarsAvg4 = mtcars.loc[(mtcars['cyl'] == 4) & (mtcars['wt'] >= 2) & (mtcars['wt'] <= 2.2)]
print(mtcarsAvg4)
print(mtcarsAvg4['mpg'].mean())

print("Broj auta s automatskim mjenjacem: ")
print(len(mtcars.loc[mtcars['am'] == 1]))

print("Broj auta s rucnim mjenjacem: ")
print(len(mtcars.loc[mtcars['am'] == 0]))

print("Auti s automatskim mjenjacem i snagom preko 100hp: ")
print(mtcars.loc[(mtcars['am'] == 1) & (mtcars['hp'] > 100)])

print("Masa automobila u kg: ")
mtcars['wt/kg'] = mtcars['wt'] * 0.45392
print(mtcars)
