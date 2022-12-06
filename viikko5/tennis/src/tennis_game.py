class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.score_dict = {self.player1_name: 0, self.player2_name: 0}
        self.score_names ={0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty", "special": "Deuce", "tie": "All"}
        self.advantage_names = {1: "Advantage player1", -1: "Advantage player2",
                                "max_pos": "Win for player1", "max_neg": "Win for player2"}

    def won_point(self, player_name):
        self.score_dict[player_name] +=1

    #There exists 3 states of situations
    def score_type(self):
        if self.score_dict[self.player1_name] == self.score_dict[self.player2_name]:
            return "Tie"
        if self.score_dict[self.player1_name] >= 4 or self.score_dict[self.player2_name] >= 4:
            return "OverLimit"
        else:
            return "Normal"
    
    #Handlers for all situations
    def handle_normal(self):
        return self.score_names[self.score_dict[self.player1_name]]+"-"+self.score_names[self.score_dict[self.player2_name]]

    def handle_overlimit(self, key):
        return self.advantage_names[key]
    
    def handle_tie(self):
        if self.score_dict[self.player1_name] > 3:
            return self.score_names["special"]
        return self.score_names[self.score_dict[self.player1_name]]+"-"+self.score_names["tie"]
    
    #Handle score according to situtation
    def get_score(self):
        situation = self.score_type()

        if situation == "OverLimit":
            key = int(self.score_dict[self.player1_name])-int(self.score_dict[self.player2_name])
            if key > 1:
                key = "max_pos"
            elif key < -1:
                key = "max_neg"
            return self.handle_overlimit(key)
            
        if situation == "Tie":
            return self.handle_tie()

        if situation == "Normal":
            return self.handle_normal()