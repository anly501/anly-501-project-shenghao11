# %%
#%%
import pandas as pd
import numpy as np

# %%
# natural population growth data
population = pd.read_csv('../../data/00-raw-data/natural-population-growth.csv')
population = population.drop(columns=['Code','Natural growth rate - sex: all - age: all - variant: medium'])
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

df = df.rename(columns={'Natural growth rate - sex: all - age: all - variant: estimates':'Natural_growth_rate', 'GDP per capita, PPP (constant 2017 international $)':'GDP', 'Deaths - sex: all - age: all - variant: estimates':'Deaths', 'Births - sex: all - age: all - variant: estimates':'Births'})


# %%
life_expectancy = pd.read_csv('../../data/00-raw-data/life-expectancy.csv')
causes = pd.read_csv('../../data/00-raw-data/dalys-rate-from-all-causes.csv')

df = df.merge(life_expectancy, how='left')
population = df.merge(causes, how='left')

# %%
# natural population growth data
population = population.drop(columns=['Code'])
population.rename(columns={ population.columns[7]: "Disability" }, inplace = True)
population.rename(columns={ population.columns[6]: "Life" }, inplace = True)


population.head()

# %%
#drop na
population=population.dropna()

# %%
population.to_csv("../../data/01-modified-data/cleaned-population-py.csv")


