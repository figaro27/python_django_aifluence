import sys
import instaloader
import re

class CampaignTracker:
    def __init__(self):
        self.L = instaloader.Instaloader(max_connection_attempts=30)
        
    def getEngagement(self, url):
        pattern = re.compile("https://www.instagram.com/p/", re.IGNORECASE)
        post_id = pattern.sub("", url).replace("/", "")

        post = instaloader.Post.from_shortcode(self.L.context, post_id)
        likes = post.likes
        comments = post.comments
        print(' --- post likes --- ', likes)
        print(' --- post comments --- ', comments)
        return {'likes': likes, 'comments':comments}