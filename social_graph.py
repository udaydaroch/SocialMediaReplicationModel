class SocialGraph:
    def __init__(self):
        self.connections = {}

    def add_user(self, user_id):
        if user_id not in self.connections:
            self.connections[user_id] = []

    def add_connection(self, user1, user2):
        if user1 in self.connections and user2 in self.connections:
            self.connections[user1].append(user2)
            self.connections[user2].append(user1)
