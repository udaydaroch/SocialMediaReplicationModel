# Social Media Feed Algorithm

## Overview

This project implements a simple social media feed algorithm. Users can create accounts, connect with other users, make posts, like posts, and view feeds based on their connections. The feed prioritizes posts using a combination of post age and number of likes.

## Features

- Add users
- Create connections between users
- Add posts
- Like posts
- View posts by user
- Get a prioritized feed of posts for a user

## Data Structures

1. **Graph (SocialGraph)**
   - Represents the social network of users.
   - Each user is a node, and connections between users are edges.

2. **Heap (FeedHeap)**
   - Maintains posts based on their priority.
   - Used to quickly retrieve the top `n` posts.

3. **Hash Maps (SocialMediaData)**
   - Stores user posts and post details.
   - Provides efficient access to post data.

## Usage

### Adding Users and Connections

- Users can be added to the network.
- Connections between users can be created, allowing them to see each other's posts.

### Making and Liking Posts

- Users can make posts, which include content and a timestamp.
- Posts can be liked by other users, increasing their priority in the feed.

### Viewing and Getting Feeds

- Users can view posts they have made.
- Users can retrieve a prioritized feed of posts made by their connections.

## How to Use

### Running the Program

To run the program, simply execute the `main` function in your terminal:
  
    ```sh
    python social_media_feed.py

## Command-Line Interface (CLI)

**The program provides a CLI for interacting with the social media feed. The available options are:**

- Add User: Create a new user.
- Add Connection: Connect two existing users.
- Add Post: Add a new post for a user.
- Like Post: Like an existing post.
- View Posts by User: View all posts made by a specific user.
- Get Feed for User: Retrieve a feed of top posts for a user.
- Exit: Exit the program.

## Example usage 
```sh
Options:
1. Add User
2. Add Connection
3. Add Post
4. Like Post
5. View Posts by User
6. Get Feed for User
7. Exit
Enter your choice: 1
Enter user ID: user1
User user1 added.

Enter your choice: 1
Enter user ID: user2
User user2 added.

Enter your choice: 2
Enter first user ID: user1
Enter second user ID: user2
Connection added between user1 and user2.

Enter your choice: 3
Enter user ID: user1
Enter post ID: post1
Enter post content: Hello World
Post post1 added by user1.

Enter your choice: 4
Enter your user ID: user2
Enter post ID to like: post1
User user2 liked post post1.

Enter your choice: 5
Enter user ID to view posts: user1
{'timestamp': 1625242342.0, 'content': 'Hello World', 'likes': 1}

Enter your choice: 6
Enter user ID to get feed: user1
Enter number of posts to retrieve: 5
{'timestamp': 1625242342.0, 'content': 'Hello World', 'likes': 1}
