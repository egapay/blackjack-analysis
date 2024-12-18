# Blackjack Analysis Project

## Resources

[CSV Download](https://www.kaggle.com/datasets/dennisho/blackjack-hands?resource=download)

# Info

Running clean_csv.py takes about 4 minutes
Adding to Postgres DB takes about 3 minutes

# Setup

1. Download CSV
2. Move to repo folder
3. Run clean_csv.py
4. Run command in psql console:
   1. `\copy hands (dealer_up, initial_hand, dealer_final, dealer_final_value, player_final, player_final_value, actions_taken, win) FROM 'REPLACE WITH PATH TO CSV IN REPO' WITH (FORMAT csv, HEADER true);`
