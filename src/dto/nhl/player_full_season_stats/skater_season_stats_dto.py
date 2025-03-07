from datetime import datetime

from src.dto.nhl.player_full_season_stats.player_season_stats_dto import PlayerSeasonStatsDTO


class SkaterSeasonStatsDTO(PlayerSeasonStatsDTO):
    def __init__(
        self,
        player_id: int,
        penalty_minutes: int,
        games_played: int,
        created_datetime: datetime,
        last_modified_datetime: datetime,
        goals: int,
        assists: int,
        game_winning_goals: int,
        ot_goals: int,
        points: int,
        power_play_goals: int,
        power_play_points: int,
        shooting_percentage: float,
        short_handed_goals: int,
        short_handed_points: int,
        shots: int,
    ):
        super().__init__(
            player_id=player_id,
            penalty_minutes=penalty_minutes,
            games_played=games_played,
            created_datetime=created_datetime,
            last_modified_datetime=last_modified_datetime,
        )
        self.goals: int = goals
        self.assists: int = assists
        self.game_winning_goals: int = game_winning_goals
        self.ot_goals: int = ot_goals
        self.points: int = points
        self.power_play_goals: int = power_play_goals
        self.power_play_points: int = power_play_points
        self.shooting_percentage: float = shooting_percentage
        self.short_handed_goals: int = short_handed_goals
        self.short_handed_points: int = short_handed_points
        self.shots: int = shots
