from datetime import datetime


class TeamDetailsDTO:
    def __init__(
        self,
        team_id: int,
        team_abbreviation: str,
        team_full_name: str,
        created_datetime: datetime,
        last_modified_datetime: datetime,
    ):
        self.team_id: int = team_id
        self.team_abbreviation: str = team_abbreviation
        self.team_full_name: str = team_full_name
        self.created_datetime: datetime = created_datetime
        self.last_modified_datetime: datetime = last_modified_datetime
