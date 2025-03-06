CREATE TABLE IF NOT EXISTS game_details(
    game_id         INT NOT NULL PRIMARY KEY,
    home_team_id    INT REFERENCES team_details(team_id),
    away_team_id    INT REFERENCES team_details(team_id),
    game_state      VARCHAR(50),
    game_date       VARCHAR(50),
    season          VARCHAR(10),
);

CREATE TABLE IF NOT EXISTS player_current_game_stats(
    player_id            INT REFERENCES player_details(player_id),
    game_id              INT REFERENCES game_details(game_id),
    opponent_abbreviated VARCHAR(3),
    goals                INT,
    assists              INT,
    penalty_minutes      INT,
    time_on_ice          INT,
    game_date            DATE,
    created_datetime     TIMESTAMP,
    last_modified_date   TIMESTAMP,
    PRIMARY KEY (player_id, game_id)
);
