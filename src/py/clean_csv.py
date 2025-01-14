import pandas as pd
import ast

if __name__ == "__main__":
    df = pd.read_csv("./blackjack_simulator.csv", nrows=5000000) #limiting to 5 million rows

    # Splitting the columns into separate tables
    round_table = ['win']
    dealer_table = ['dealer_up', 'dealer_final', 'dealer_final_value']
    player_table = ['player_final', 'player_final_value', 'actions_taken']
    player_start_table = ['initial_hand']

    round_df = df[round_table]
    
    dealer_df = df[dealer_table]
    dealer_df.loc[:, 'dealer_final'] = dealer_df['dealer_final'].apply(ast.literal_eval)
    # changing [ to { and ] to } to allow for list type in postgres
    dealer_df.loc[:, 'dealer_final'] = dealer_df['dealer_final'].astype(str).str.replace('[', '{').str.replace(']', '}')
    dealer_df.loc[:, 'dealer_final_value'] = dealer_df['dealer_final_value'].str.replace('BJ', '21') # BJ can be inferred by 1.5 win

    player_df = df[player_table]
    player_df.loc[:, 'player_final'] = player_df['player_final'].apply(ast.literal_eval)
    player_df.loc[:, 'player_final_value'] = player_df['player_final_value'].apply(ast.literal_eval)
    player_df.loc[:, 'actions_taken'] = player_df['actions_taken'].apply(ast.literal_eval)

    player_df = player_df.explode(['player_final', 'player_final_value', 'actions_taken'])

    # changing [ to { and ] to } to allow for list type in postgres
    player_df.loc[:, 'player_final'] = player_df['player_final'].astype(str).str.replace('[', '{').str.replace(']', '}')
    player_df.loc[:, 'player_final_value'] = player_df['player_final_value'].astype(str).str.replace('[', '{').str.replace(']', '}').str.replace('BJ', '21')
    player_df.loc[:, 'actions_taken'] = player_df['actions_taken'].astype(str).str.replace('[', '{').str.replace(']', '}')

    player_start_df = df[player_start_table]
    player_start_df.rename(columns={"initial_hand": "player_initial"}) # renaming to make it more clear
    player_start_df.loc[:, 'initial_hand'] = player_start_df['initial_hand'].apply(ast.literal_eval)
    player_start_df.loc[:, 'initial_hand'] = player_start_df['initial_hand'].astype(str).str.replace('[', '{').str.replace(']', '}')

    round_df.to_csv("../csv/round.csv", index=True)
    dealer_df.to_csv("../csv/dealer.csv", index=True)
    player_df.to_csv("../csv/player.csv", index=True)
    player_start_df.to_csv("../csv/player_start.csv", index=True)