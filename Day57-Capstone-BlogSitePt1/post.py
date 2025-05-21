import requests
response = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

class Post:

    def __init__(self, post):
        self.id = post["id"]
        self.title = post["title"]
        self.subtitle = post["subtitle"]
        self.body = post["body"]

posts_list = []

for post in response:
    new_post = Post(post)
    posts_list.append(new_post)

# for post in posts_list:
#     if post.id == 2:
#         print(post.title)