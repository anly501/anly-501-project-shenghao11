# %%
#%%
import pandas as pd
import numpy as np

# %%
# natural population growth data
population = pd.read_csv('../../data/00-raw-data/natural-population-growth.csv')
population = population.drop(columns=['Code'])
population.head()

# %%
# gdp data
gdp = pd.read_csv('../../data/00-raw-data/gdp-per-capita-worldbank.csv')
gdp = gdp.drop(columns=['Code'])
gdp.head()


# %%
# life
#life = pd.read_csv('../../data/00-raw-data/life-expectancy.csv')
#life = life.drop(columns=['Code'])
#life.head()

# %%
#death
death = pd.read_csv('../../data/00-raw-data/annual-number-of-deaths-by-world-region.csv')
death = death.drop(columns=['Code'])
death.head()

# %%
#birth
births = pd.read_csv('../../data/00-raw-data/annual-number-of-births-by-world-region.csv')
births = births.drop(columns=['Code'])
births.head()

# %%
#merge data
df = population.merge(gdp, how='inner')
df = df.merge(death, how='left')
df = df.merge(births, how='left')


# %%
dfpast = df[df['Year'] < 2022]



# %%
dfpast.to_csv("../../data/01-modified-data/cleaned-population-py.csv")



