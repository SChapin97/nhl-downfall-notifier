from datetime import datetime

from src.dto.nhl.player_full_season_stats.player_season_stats_dto import \
    PlayerSeasonStatsDTO


class GoalieSeasonStatsDTO(PlayerSeasonStatsDTO):
    def __init__(
        self,
        player_id: int,
        penalty_minutes: int,
        games_played: int,
        created_datetime: datetime,
        last_modified_datetime: datetime,
        goals_against_average: float,
        losses: int,
        ot_losses: int,
        save_percentage: float,
        shutouts: int,
        wins: int,
    ):
        super().__init__(
            player_id=player_id,
            penalty_minutes=penalty_minutes,
            games_played=games_played,
            created_datetime=created_datetime,
            last_modified_datetime=last_modified_datetime,
        )
        self.goals_against_average: float = goals_against_average
        self.losses: int = losses
        self.ot_losses: int = ot_losses
        self.save_percentage: float = save_percentage
        self.shutouts: int = shutouts
        self.wins = wins
