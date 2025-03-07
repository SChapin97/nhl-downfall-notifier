from datetime import datetime

from src.dto.nhl.player_current_game_stats.player_current_game_stats_dto import PlayerCurrentGameStatsDTO


class SkaterCurrentGameStatsDTO(PlayerCurrentGameStatsDTO):
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
        points: int,
        plus_minus: int,
        power_play_goals: int,
        power_play_points: int,
        game_winning_goals: int,
        ot_goals: int,
        shots: int,
        shifts: int,
        short_handed_goals: int,
        short_handed_points: int,
    ):
        super().__init__(
            player_id=player_id,
            opponent_abbreviated=opponent_abbreviated,
            game_date=game_date,
            game_id=game_id,
            goals=goals,
            assists=assists,
            penalty_minutes=penalty_minutes,
            time_on_ice=time_on_ice,
            created_datetime=created_datetime,
            last_modified_datetime=last_modified_datetime,
        )
        self.points: int = points
        self.plus_minus: int = plus_minus
        self.power_play_goals: int = power_play_goals
        self.power_play_points: int = power_play_points
        self.game_winning_goals: int = game_winning_goals
        self.ot_goals: int = ot_goals
        self.shots: int = shots
        self.shifts: int = shifts
        self.short_handed_goals: int = short_handed_goals
        self.short_handed_points: int = short_handed_points
