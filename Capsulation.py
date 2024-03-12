class score():
    def __init__(self):
        self.__score = 1

    def showscore(self):
        print(self.__score)

    def update_score(self):
        self.__score = self.__score +1
        print(self.__score)

player = score()
player.__score = 100
player.update_score()
player.update_score()

