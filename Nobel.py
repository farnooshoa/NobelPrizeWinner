# Loading in required libraries
import pandas as pd
import seaborn as sns
import numpy as np

df=pd.read_csv('nobel.csv')


def maximum(df,value):

    value_count=df[value].value_counts()
    top_value = value_count.idxmax()
       
    return (top_value)

top_gender= maximum(df,'sex')
top_country =maximum(df,'birth_country')
                     

df['decade'] = (df['year']//10)*10 
filtered_df = df[df['birth_country'] == "United States of America"]

max_decade_usa = maximum(filtered_df,'decade')

df['female_winner'] = df['sex'] == 'Female'
prop_female_winners = df.groupby(['decade', 'category'], as_index=False)['female_winner'].mean()
max_female_decade_category = prop_female_winners[prop_female_winners['female_winner'] == prop_female_winners['female_winner'].max()][['decade', 'category']]
max_female_dict = {max_female_decade_category['decade'].values[0]: max_female_decade_category['category'].values[0]}

nobel_women = df[df['female_winner']]
min_row = nobel_women[nobel_women['year'] == nobel_women['year'].min()]
first_woman_name = min_row['full_name'].values[0]
first_woman_category = min_row['category'].values[0]

counts = df['full_name'].value_counts()
repeats = counts[counts >= 2].index
repeat_list = list(repeats)


print("\n The gender with the most Nobel laureates is :", top_gender)
print(" The most common birth country of Nobel laureates is :", top_country)
print(max_decade_usa)
print(max_female_dict)
print(f"\n The first woman to win a Nobel Prize was {first_woman_name}, in the category of {first_woman_category}.")
print("\n The repeat winners are :", repeat_list)