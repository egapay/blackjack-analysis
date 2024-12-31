DROP SCHEMA public CASCADE;
CREATE SCHEMA public;

GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO public;

CREATE TABLE round(
	round_id BIGSERIAL,
	win DECIMAL,
	PRIMARY KEY(round_id)
);

CREATE TABLE dealer(
	round_id BIGSERIAL,
	dealer_up SMALLINT,
	dealer_final SMALLINT[],
	dealer_final_value SMALLINT,
	PRIMARY KEY(round_id),
	CONSTRAINT fk_dealer_round 
		FOREIGN KEY(round_id)
			REFERENCES round(round_id)
);

CREATE TABLE player(
	round_id BIGSERIAL,
	hand_id SERIAL,
	player_final SMALLINT[],
	player_final_value SMALLINT,
	actions_taken text[],
	PRIMARY KEY(round_id, hand_id),
	CONSTRAINT fk_player_round
		FOREIGN KEY(round_id)
			REFERENCES round(round_id)
);

CREATE TABLE player_start(
	round_id BIGSERIAL,
	player_initial SMALLINT[],
	PRIMARY KEY(round_id),
	CONSTRAINT fk_player_start_round
		FOREIGN KEY(round_id)
			REFERENCES round(round_id)
);