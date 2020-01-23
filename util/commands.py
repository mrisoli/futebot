from collections import OrderedDict


class Commands:
    __instance = None
    dictionary = OrderedDict()

    @staticmethod
    def get_instance():
        if Commands.__instance is None:
            Commands()
        return Commands.__instance

    def __init__(self):
        if Commands.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Commands.__instance = self

    def register(self, func, command, description, params):
        self.dictionary[command] = {'description': description,
                                    'params': params,
                                    'func': func}
