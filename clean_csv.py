import pandas as pd

df = pd.read_csv("./blackjack_simulator.csv", nrows=10)

filter_columns = ['dealer_up', 'initial_hand', 'dealer_final', 'dealer_final_value', 'player_final', 'player_final_value', 'actions_taken', 'win']

filtered_df = df[filter_columns]
filtered_df.loc[:, 'initial_hand'] = filtered_df['initial_hand'].str.replace('[', '{').str.replace(']', '}')
filtered_df.loc[:, 'dealer_final'] = filtered_df['dealer_final'].str.replace('[', '{').str.replace(']', '}')
filtered_df.loc[:, 'player_final'] = filtered_df['player_final'].str.replace('[', '{').str.replace(']', '}')
filtered_df.loc[:, 'player_final_value'] = filtered_df['player_final_value'].str.replace('[', '{').str.replace(']', '}')
filtered_df.loc[:, 'actions_taken'] = filtered_df['actions_taken'].str.replace('[', '{').str.replace(']', '}')

filtered_df.to_csv("./cleaned_blackjack.csv", index=False)