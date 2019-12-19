class Update:
    """Update Object
    desc
    """
    def __init__(
        self,
        *,
        chat_id,
        from_user=None,
        update_type,
        data=None,
        json_update,
    ):
        self.chat_id = chat_id
        self.from_user = from_user
        self.update_type = update_type
        self.data = data
        self.__json_update = json_update

    def json(self):
        return self.__json_update
