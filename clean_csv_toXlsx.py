import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv("./blackjack_simulator.csv", nrows=1000000)

    filter_columns = ['dealer_up', 'initial_hand', 'dealer_final', 'dealer_final_value', 'player_final', 'player_final_value', 'actions_taken', 'win']

    filtered_df = df[filter_columns]
    filtered_df.loc[:, 'initial_hand'] = filtered_df['initial_hand'].str.replace('[', '').str.replace(']', '')
    filtered_df.loc[:, 'dealer_final'] = filtered_df['dealer_final'].str.replace('[', '').str.replace(']', '')
    filtered_df.loc[:, 'player_final'] = filtered_df['player_final'].str[1:-1]
    filtered_df.loc[:, 'player_final_value'] = filtered_df['player_final_value'].str.replace('[', '').str.replace(']', '')
    filtered_df.loc[:, 'actions_taken'] = filtered_df['actions_taken'].str[1:-1]

    filtered_df.to_excel("./cleaned_blackjack.xlsx", index=False)