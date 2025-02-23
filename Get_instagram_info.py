#? Lấy thông tin tài khoản Instagram
import instaloader
loader = instaloader.Instaloader()
username = "your_username"
password = "your_password"
try:
    loader.login(username, password)
    username = input("Enter username Instagram: ")
    profile = instaloader.Profile.from_username(loader.context, username)
    print(f"ID: {profile.userid}")
    print(f"Name: {profile.full_name}")
    print(f"Username: {profile.username}")
    print(f"followers: {profile.followers}")
    print(f"following: {profile.followees}")
    print(f"Post: {profile.mediacount}")
    print(f"Describe: {profile.biography}")
    print(f"Website: {profile.external_url}")
    print(f"verified (green tick): {profile.is_verified}")
    print(f"Private account: {profile.is_private}")
    print("\nList URL Picture:")
    for post in profile.get_posts():
        print(post.url)
except instaloader.exceptions.ProfileNotExistsException:
    print("NOT FOUND!")
except instaloader.exceptions.ConnectionException:
    print("CANNOT CONNECT")