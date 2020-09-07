class GameState():
    def tick(self, delta):
        raise NotImplementedError("tick() is not implemented by its child")

    def get_name(self):
        raise NotImplementedError("get_name() is not implemented by its child")
