import json

# Matter is the class for raw input materials like audios and videos
class Matter:
    def __init__(self, name, subdiv=None):
        self.name = name
        if subdiv:
            self.subdiv = subdiv


# Loads and stores matters
class MatterDatabase:
    def __init__(self, database_filename):
        self.database_filename = database_filename
        self._matters = {}

        # Loading json to a dictionary
        with open(self.database_filename, 'r') as read_file:
            matter_dict = json.load(read_file)

        for key, value in matter_dict.items():
            name = key
            subdiv = value['subdiv']
            self._matters[key] = self._create_matter(name, subdiv)

    def _create_matter(self, name, subdiv):
        return Matter(name, subdiv)
