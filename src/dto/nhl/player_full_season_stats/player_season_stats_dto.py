from datetime import datetime


class PlayerSeasonStatsDTO:
    def __init__(
        self,
        player_id: int,
        penalty_minutes: int,
        games_played: int,
        created_datetime: datetime,
        last_modified_datetime: datetime,
    ):
        self.player_id: int = player_id  # TODO: Foreign key from player_details_dto
        self.penalty_minutes: int = penalty_minutes
        self.games_played: int = games_played
        self.created_datetime: datetime = created_datetime
        self.last_modified_datetime: datetime = last_modified_datetime
