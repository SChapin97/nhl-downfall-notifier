from datetime import datetime

from src.dto.nhl.player_current_game_stats.player_current_game_stats_dto import \
    PlayerCurrentGameStatsDTO


class GoalieCurrentGameStatsDTO(PlayerCurrentGameStatsDTO):
    def __init__(
        self,
        player_id: int,
        game_id: int,
        opponent_abbreviated: str,
        game_date: datetime,
        goals: int,
        assists: int,
        penalty_minutes: int,
        time_on_ice: int,
        created_datetime: datetime,
        last_modified_datetime: datetime,
        games_started: int,
        decision: str,
        shots_against: int,
        goals_against: int,
        save_percentage: float,
    ):
        super().__init__(
            player_id=player_id,
            game_id=game_id,
            opponent_abbreviated=opponent_abbreviated,
            game_date=game_date,
            goals=goals,
            assists=assists,
            penalty_minutes=penalty_minutes,
            time_on_ice=time_on_ice,
            created_datetime=created_datetime,
            last_modified_datetime=last_modified_datetime,
        )
        self.games_started: int = games_started
        self.decision: str = decision
        self.shots_against: int = shots_against
        self.goals_against: int = goals_against
        self.save_percentage: float = save_percentage
