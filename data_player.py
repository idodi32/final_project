class PlayerData:
    def __init__(self):
        self.name = ""
        self.password = ""
        self.games = 0
        self.wins = 0
        self.best_time = 0

    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.games = 0
        self.wins = 0
        self.best_time = 0

    def __init__(self, name, password,games,wins,best_time):
        self.name = name
        self.password = password
        self.games = games
        self.wins = wins
        self.best_time = best_time

    def __set_name__(self, name):
        self.name = name

    def __set_password__(self, password):
        self.password = password

    def __add_wins__(self):
        self.wins += 1

    def __add_games__(self):
        self.games += 1

    def __check_best_time__(self, best_time):
        if self.best_time < best_time:
            self.best_time = best_time

    def get_password(self):
        return self.password

    def get_name(self):
        return self.name

    def __get_games__(self):
        return self.games

    def __get_wins__(self):
        return self.wins

    def __get_best_time__(self):
        return self.best_time
