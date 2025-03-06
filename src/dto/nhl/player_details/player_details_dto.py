from datetime import datetime


class PlayerDetailsDTO:
    def __init__(
        self,
        player_id: int,
        current_team_id: int,
        current_team_abbreviation: str,
        first_name: str,
        last_name: str,
        sweater_number: int,
        headshot_url: str,
        height_centimeters: int,
        weight_kilograms: int,
        birth_date: datetime,
        created_datetime: datetime,
        last_modified_datetime: datetime,
    ):
        self.player_id: int = player_id
        self.current_team_id: int = current_team_id  # TODO: Foreign key
        self.current_team_abbreviation: str = current_team_abbreviation
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.sweater_number: int = sweater_number
        self.headshot_url: str = headshot_url
        self.height_centimeters: int = height_centimeters
        self.weight_kilograms: int = weight_kilograms
        self.birth_date: datetime = birth_date
        self.created_datetime: datetime = created_datetime
        self.last_modified_datetime: datetime = last_modified_datetime
