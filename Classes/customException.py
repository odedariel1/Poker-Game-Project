class customException(Exception):
    """Raised when the bet amount is higer then the player cash

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message="You cant bet on higher amount then your cash"):
        self.message = message
        super().__init__(self.message)
