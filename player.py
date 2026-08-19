class Player:
    def __init__(self, username: str) -> None:
        self.__username = username

    def get_username(self) -> str:
        return self.__username

    def rename(self, new_username: str) -> None:
        if not new_username.strip():
            raise ValueError("Username cannot be empty")

        self.__username = new_username


    