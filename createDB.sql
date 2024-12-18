CREATE TABLE hands (
    dealer_up INTEGER,
    initial_hand INTEGER[],
    dealer_final INTEGER[],
    dealer_final_value INTEGER,
    player_final INTEGER[][],
    player_final_value TEXT[],
    actions_taken TEXT[][],
    win NUMERIC
);

-- COPY hands (dealer_up, initial_hand, dealer_final, 
-- 				dealer_final_value, player_final, player_final_value, actions_taken, win)
-- FROM './blackjack_simulator.csv'
-- WITH (FORMAT csv, HEADER true);


INSERT INTO hands (dealer_up, initial_hand, dealer_final, 
					dealer_final_value, player_final, player_final_value, actions_taken, win)
VALUES (10, ARRAY[10,11], ARRAY[10, 4, 10], 24, ARRAY[ARRAY[10, 11], ARRAY[9,11]], ARRAY['BJ'], ARRAY[ARRAY['S']], 1.5)