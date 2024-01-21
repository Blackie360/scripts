import requests

def get_followers(username, access_token):
    url = f'https://api.github.com/users/{username}/followers'
    headers = {'Authorization': f'token {access_token}'}
    response = requests.get(url, headers=headers)
    followers = [follower['login'] for follower in response.json()]
    return followers

def get_following(username, access_token):
    url = f'https://api.github.com/users/{username}/following'
    headers = {'Authorization': f'token {access_token}'}
    response = requests.get(url, headers=headers)
    following = [followed['login'] for followed in response.json()]
    return following

def unfollow_non_followers(username, access_token):
    followers = get_followers(username, access_token)
    following = get_following(username, access_token)

    non_followers = set(following) - set(followers)

    for non_follower in non_followers:
        url = f'https://api.github.com/user/following/{non_follower}'
        requests.delete(url, headers={'Authorization': f'token {access_token}'})
        print(f'Unfollowed {non_follower}')

# Replace 'your_username' and 'your_access_token' with your GitHub username and access token
your_username = 'your_username'
your_access_token = 'your_access_token'

unfollow_non_followers(your_username, your_access_token)
