class Tennis:

    def __init__(self):
        self.player_1_score = 0
        self.player_2_score = 0
        self.map_score = {
            0: "0",
            1: "15",
            2: "30",
            3: "40"
        }

    def get_score(self):
        if self.player_1_score >= 3 and self.player_2_score >= 3 and self.player_1_score == self.player_2_score:
            return "Egalité"
        return self.map_score[self.player_1_score] + "-" + self.map_score[self.player_2_score]

    def add_point_player_1(self):
        self.player_1_score += 1

    def add_point_player_2(self):
        self.player_2_score += 1
