import heapq

class FeedHeap:
    def __init__(self):
        self.heap = []

    def add_post(self, post_id, priority):
        heapq.heappush(self.heap, (-priority, post_id))

    def get_top_posts(self, n):
        return [heapq.heappop(self.heap)[1] for _ in range(min(n, len(self.heap)))]
