#without class
user1_name = "Alice"
user1_email = "alice@example.com"
user1_posts = ["Hello World!"]

user2_name = "Bob"
user2_email = "bob@example.com"
user2_posts = ["My first post."]

def login_user(name):
    print(f"{name} has logged in.")

def post_message(name, message):
    # a real function would need to find the right post list
    print(f"{name} posted: {message}")

login_user(user1_name) # Alice has logged in.
post_message(user2_name, "My first post.")

