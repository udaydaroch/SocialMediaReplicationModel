import time
from feed_heap import FeedHeap
from social_graph import SocialGraph
from social_media_data import SocialMediaData

class SocialMediaFeed:
    def __init__(self):
        self.graph = SocialGraph()
        self.data = SocialMediaData()
        self.feed_heap = FeedHeap()

    def add_user(self, user_id):
        self.graph.add_user(user_id)
        print(f"User {user_id} added.")

    def add_connection(self, user1, user2):
        self.graph.add_connection(user1, user2)
        print(f"Connection added between {user1} and {user2}.")

    def add_post(self, user_id, post_id, post_data):
        self.data.add_post(user_id, post_id, post_data)
        priority = self._calculate_priority(post_data)
        self.feed_heap.add_post(post_id, priority)
        print(f"Post {post_id} added by {user_id}.")

    def like_post(self, user_id, post_id):
        if post_id in self.data.post_details:
            self.data.post_details[post_id]['likes'] += 1
            post_data = self.data.post_details[post_id]
            new_priority = self._calculate_priority(post_data)
            self.feed_heap.add_post(post_id, new_priority)
            print(f"User {user_id} liked post {post_id}.")
        else:
            print(f"Post {post_id} does not exist.")

    def view_posts(self, user_id):
        if user_id in self.data.user_posts:
            posts = [self.data.post_details[post_id] for post_id in self.data.user_posts[user_id]]
            for post in posts:
                print(post)
        else:
            print(f"User {user_id} has no posts.")

    def get_feed(self, user_id, n=10):
        if user_id not in self.graph.connections:
            return []

        connected_users = self.graph.connections[user_id]
        for connected_user in connected_users:
            if connected_user in self.data.user_posts:
                for post_id in self.data.user_posts[connected_user]:
                    post_data = self.data.post_details[post_id]
                    post_priority = self._calculate_priority(post_data)
                    self.feed_heap.add_post(post_id, post_priority)

        top_posts = self.feed_heap.get_top_posts(n)
        for post_id in top_posts:
            print(self.data.post_details[post_id])

    def _calculate_priority(self, post_data):
        time_weight = 0.3
        likes_weight = 0.7

        current_time = time.time()
        time_diff = current_time - post_data['timestamp']

        normalized_time = max(1, time_diff / 3600)

        priority = (time_weight / normalized_time) + (likes_weight * post_data.get('likes', 0))
        return priority

def main():
    feed = SocialMediaFeed()
    while True:
        print("\nOptions:")
        print("1. Add User")
        print("2. Add Connection")
        print("3. Add Post")
        print("4. Like Post")
        print("5. View Posts by User")
        print("6. Get Feed for User")
        print("7. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            user_id = input("Enter user ID: ")
            feed.add_user(user_id)
        elif choice == "2":
            user1 = input("Enter first user ID: ")
            user2 = input("Enter second user ID: ")
            feed.add_connection(user1, user2)
        elif choice == "3":
            user_id = input("Enter user ID: ")
            post_id = input("Enter post ID: ")
            content = input("Enter post content: ")
            timestamp = time.time()
            likes = 0
            post_data = {"timestamp": timestamp, "content": content, "likes": likes}
            feed.add_post(user_id, post_id, post_data)
        elif choice == "4":
            user_id = input("Enter your user ID: ")
            post_id = input("Enter post ID to like: ")
            feed.like_post(user_id, post_id)
        elif choice == "5":
            user_id = input("Enter user ID to view posts: ")
            feed.view_posts(user_id)
        elif choice == "6":
            user_id = input("Enter user ID to get feed: ")
            n = int(input("Enter number of posts to retrieve: "))
            feed.get_feed(user_id, n)
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
