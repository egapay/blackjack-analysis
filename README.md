# Blackjack Analysis Project

## Resources

[CSV Download](https://www.kaggle.com/datasets/dennisho/blackjack-hands?resource=download)

# Info

- Running clean_csv.py takes about **4 minutes**
- Running clean_csv_toXlsx takes about **2 minutes** (Reduced to 1 million rows due to Excel limits)
- Adding to Postgres DB takes about **3 minutes**

# Setup

1. Download CSV
2. Move to repo folder
3. Run clean_csv.py
4. Run command in psql console:
   1. `\copy round (round_id, win) FROM 'REPLACE WITH PATH TO CSV IN REPO' WITH (FORMAT csv, HEADER true);`
   2. `\copy dealer (round_id, dealer_up, dealer_final, dealer_final_value) FROM 'REPLACE WITH PATH TO CSV IN REPO' WITH (FORMAT csv, HEADER true);`
   3. `\copy player (round_id, player_final, player_final_value, actions_taken) FROM 'REPLACE WITH PATH TO CSV IN REPO' WITH (FORMAT csv, HEADER true);`
   4. `\copy player_start (round_id, player_initial) FROM 'REPLACE WITH PATH TO CSV IN REPO' WITH (FORMAT csv, HEADER true);`
