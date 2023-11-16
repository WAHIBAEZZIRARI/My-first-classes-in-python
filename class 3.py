class Player():
    def __init__(self, name, age, post, club, nationality, ovr, rank):

        self.name = name
        self.age = age
        self.post = post
        self.rank = rank
        self.club = club
        self.nationality = nationality
        self.ovr = ovr

    def info(self):

        print("{}, aged {}, plays as a {}, currently with {}. The {} player boasts an impressive overall {} rating, and his ranking is {}.".format(self.name, self.age, self.post, self.club, self.nationality, self.ovr, self.rank))


player1 = Player("Kylian Mbappe", 24, "ST", "Paris Saint-Germain", "French", 91, 1)
player2 = Player("Erling Haaland", 23, "ST", "Manchester City", "Norwegian", 91, 2)
player3 = Player("Kevin De Bruyne", 32, "CM", "Manchester City", "Belgian", 91, 3)

player1.info()
player2.info()
player3.info()