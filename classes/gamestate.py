class GameState:
    def __init__(self, turn, active_player, non_active_player, stack):
        self.turn = turn
        self.active_player = active_player
        self.non_active_player = non_active_player
        self.stack = stack
