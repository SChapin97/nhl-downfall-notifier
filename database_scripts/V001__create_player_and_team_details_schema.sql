CREATE TABLE IF NOT EXISTS team_details(
    team_id                 INT NOT NULL PRIMARY KEY,
    team_abbreviation       VARCHAR(3),
    team_full_name          VARCHAR(30),
    created_datetime        TIMESTAMP,
    last_modified_datetime  TIMESTAMP,
);

CREATE TABLE IF NOT EXISTS player_details(
    player_id                   INT NOT NULL PRIMARY KEY,
    team_id                     INT REFERENCES team_details(team_id),
    current_team_abbreviation   INT,
    first_name                  VARCHAR(50),
    last_name                   VARCHAR(50),
    sweater_number              INT,
    headshot_url                VARCHAR(100),
    height_centimeters          INT,
    weight_kilograms            INT,
    birth_date                  DATE,
    created_datetime            TIMESTAMP,
    last_modified_datetime      TIMESTAMP,
);
