import pygame as pg


class Cards:
    def __init__(self):
        self.ace_clubs = pg.image.load("./images/cards/1C.png")
        self.ace_diamonds = pg.image.load("./images/cards/1D.png")
        self.ace_hearts = pg.image.load("./images/cards/1H.png")
        self.ace_spades = pg.image.load("./images/cards/1S.png")

        self.two_clubs = pg.image.load("./images/cards/2C.png")
        self.two_diamonds = pg.image.load("./images/cards/2D.png")
        self.two_hearts = pg.image.load("./images/cards/2H.png")
        self.two_spades = pg.image.load("./images/cards/2S.png")

        self.three_clubs = pg.image.load("./images/cards/3C.png")
        self.three_diamonds = pg.image.load("./images/cards/3D.png")
        self.three_hearts = pg.image.load("./images/cards/3H.png")
        self.three_spades = pg.image.load("./images/cards/3S.png")

        self.four_clubs = pg.image.load("./images/cards/4C.png")
        self.four_diamonds = pg.image.load("./images/cards/4D.png")
        self.four_hearts = pg.image.load("./images/cards/4H.png")
        self.four_spades = pg.image.load("./images/cards/4S.png")

        self.five_clubs = pg.image.load("./images/cards/5C.png")
        self.five_diamonds = pg.image.load("./images/cards/5D.png")
        self.five_hearts = pg.image.load("./images/cards/5H.png")
        self.five_spades = pg.image.load("./images/cards/5S.png")

        self.six_clubs = pg.image.load("./images/cards/6C.png")
        self.six_diamonds = pg.image.load("./images/cards/6D.png")
        self.six_hearts = pg.image.load("./images/cards/6H.png")
        self.six_spades = pg.image.load("./images/cards/6S.png")

        self.seven_clubs = pg.image.load("./images/cards/7C.png")
        self.seven_diamonds = pg.image.load("./images/cards/7D.png")
        self.seven_hearts = pg.image.load("./images/cards/7H.png")
        self.seven_spades = pg.image.load("./images/cards/7S.png")

        self.eight_clubs = pg.image.load("./images/cards/8C.png")
        self.eight_diamonds = pg.image.load("./images/cards/8D.png")
        self.eight_hearts = pg.image.load("./images/cards/8H.png")
        self.eight_spades = pg.image.load("./images/cards/8S.png")

        self.nine_clubs = pg.image.load("./images/cards/9C.png")
        self.nine_diamonds = pg.image.load("./images/cards/9D.png")
        self.nine_hearts = pg.image.load("./images/cards/9H.png")
        self.nine_spades = pg.image.load("./images/cards/9S.png")

        self.ten_clubs = pg.image.load("./images/cards/10C.png")
        self.ten_diamonds = pg.image.load("./images/cards/10D.png")
        self.ten_hearts = pg.image.load("./images/cards/10H.png")
        self.ten_spades = pg.image.load("./images/cards/10S.png")

        self.jack_clubs = pg.image.load("./images/cards/11C.png")
        self.jack_diamonds = pg.image.load("./images/cards/11D.png")
        self.jack_hearts = pg.image.load("./images/cards/11H.png")
        self.jack_spades = pg.image.load("./images/cards/11S.png")

        self.queen_clubs = pg.image.load("./images/cards/12C.png")
        self.queen_diamonds = pg.image.load("./images/cards/12D.png")
        self.queen_hearts = pg.image.load("./images/cards/12H.png")
        self.queen_spades = pg.image.load("./images/cards/12S.png")

        self.king_clubs = pg.image.load("./images/cards/13C.png")
        self.king_diamonds = pg.image.load("./images/cards/13D.png")
        self.king_hearts = pg.image.load("./images/cards/13H.png")
        self.king_spades = pg.image.load("./images/cards/13S.png")

        self.card_back = pg.image.load("./images/cards/backR.png")

    # Return the correct card given type and suit
    def fetch_card(self, type, suit):
        match type:
            case -1:
                match suit:
                    case -1:
                        return self.card_back
            case 0:
                match suit:
                    case 0:
                        return self.ace_clubs
                    case 1:
                        return self.ace_diamonds
                    case 2:
                        return self.ace_hearts
                    case 3:
                        return self.ace_spades
            case 1:
                match suit:
                    case 0:
                        return self.two_clubs
                    case 1:
                        return self.two_diamonds
                    case 2:
                        return self.two_hearts
                    case 3:
                        return self.two_spades
            case 2:
                match suit:
                    case 0:
                        return self.three_clubs
                    case 1:
                        return self.three_diamonds
                    case 2:
                        return self.three_hearts
                    case 3:
                        return self.three_spades
            case 3:
                match suit:
                    case 0:
                        return self.four_clubs
                    case 1:
                        return self.four_diamonds
                    case 2:
                        return self.four_hearts
                    case 3:
                        return self.four_spades
            case 4:
                match suit:
                    case 0:
                        return self.five_clubs
                    case 1:
                        return self.five_diamonds
                    case 2:
                        return self.five_hearts
                    case 3:
                        return self.five_spades
            case 5:
                match suit:
                    case 0:
                        return self.six_clubs
                    case 1:
                        return self.six_diamonds
                    case 2:
                        return self.six_hearts
                    case 3:
                        return self.six_spades
            case 6:
                match suit:
                    case 0:
                        return self.seven_clubs
                    case 1:
                        return self.seven_diamonds
                    case 2:
                        return self.seven_hearts
                    case 3:
                        return self.seven_spades
            case 7:
                match suit:
                    case 0:
                        return self.eight_clubs
                    case 1:
                        return self.eight_diamonds
                    case 2:
                        return self.eight_hearts
                    case 3:
                        return self.eight_spades
            case 8:
                match suit:
                    case 0:
                        return self.nine_clubs
                    case 1:
                        return self.nine_diamonds
                    case 2:
                        return self.nine_hearts
                    case 3:
                        return self.nine_spades
            case 9:
                match suit:
                    case 0:
                        return self.ten_clubs
                    case 1:
                        return self.ten_diamonds
                    case 2:
                        return self.ten_hearts
                    case 3:
                        return self.ten_spades
            case 10:
                match suit:
                    case 0:
                        return self.jack_clubs
                    case 1:
                        return self.jack_diamonds
                    case 2:
                        return self.jack_hearts
                    case 3:
                        return self.jack_spades
            case 11:
                match suit:
                    case 0:
                        return self.queen_clubs
                    case 1:
                        return self.queen_diamonds
                    case 2:
                        return self.queen_hearts
                    case 3:
                        return self.queen_spades
            case 12:
                match suit:
                    case 0:
                        return self.king_clubs
                    case 1:
                        return self.king_diamonds
                    case 2:
                        return self.king_hearts
                    case 3:
                        return self.king_spades
