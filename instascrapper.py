import instaloader
import json

# Create an instance of Instaloader
L = instaloader.Instaloader()

# Define the Instagram username you want to scrape
username = "marutiii_n"  # Replace with the target username

# Load the profile
profile = instaloader.Profile.from_username(L.context, username)

# Gather profile data
profile_data = {
    "id": profile.userid,
    "username": profile.username,
    "full_name": profile.full_name,
    "bio": profile.biography,
    "profile_picture_url": profile.profile_pic_url,
    "followers_count": profile.followers,
    "following_count": profile.followees,
    "posts_count": profile.mediacount,
    "is_verified": profile.is_verified,
    "is_private": profile.is_private,
    "external_url": profile.external_url,
}

# Gather posts data
posts_data = []
for post in profile.get_posts():
    post_data = {
        "id": post.mediaid,  # Use mediaid instead of media_id
        "caption": post.caption,
        "timestamp": post.date_utc.isoformat(),
        "likes_count": post.likes,
        "comments_count": post.comments,
        # "media_type": post.media_type,
        "media_url": post.url,  # Image or video URL
        # "thumbnail_url": post.thumbnail_url if post.media_type == "VIDEO" else None,
    }
    posts_data.append(post_data)

# Add posts data to profile
profile_data["posts"] = posts_data

# Output the scraped data as JSON
profile_json = json.dumps(profile_data, indent=4)
print(profile_json)

# Optionally, save to a file
with open(f"{username}_profile_data.json", "w") as outfile:
    outfile.write(profile_json)