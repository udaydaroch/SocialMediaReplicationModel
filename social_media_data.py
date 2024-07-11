class SocialMediaData:
    def __init__(self):
        self.user_posts = {}  # user_id -> list of post_ids
        self.post_details = {}  # post_id -> post_data

    def add_post(self, user_id, post_id, post_data):
        if user_id not in self.user_posts:
            self.user_posts[user_id] = []
        self.user_posts[user_id].append(post_id)
        self.post_details[post_id] = post_data
