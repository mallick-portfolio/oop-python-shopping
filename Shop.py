class Shop:
    def __init__(self, name) -> None:
        self.name = name
        self.__customers = []
        self.__sellers = []

    def __repr__(self) -> str:
        return f"Our total customer: {len(self.__customers)} and seller {len(self.__sellers)}"



  
