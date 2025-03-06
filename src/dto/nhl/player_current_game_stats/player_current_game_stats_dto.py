from datetime import datetime


class PlayerCurrentGameStatsDTO:
    def __init__(
        self,
        player_id: int,
        game_id: int,
        goals: int,
        assists: int,
        penalty_minutes: int,
        time_on_ice: int,
        opponent_abbreviated: str,
        game_date: datetime,
        created_datetime: datetime,
        last_modified_datetime: datetime,
    ):
        self.player_id: int = player_id  # TODO: Foreign key from player_details_dto
        self.game_id: int = game_id
        self.opponent_abbreviated: str = opponent_abbreviated
        self.game_date: datetime = game_date
        self.goals: int = goals
        self.assists: int = assists
        self.penalty_minutes: int = penalty_minutes
        self.time_on_ice: int = time_on_ice
        self.created_datetime: datetime = created_datetime
        self.last_modified_datetime: datetime = last_modified_datetime
