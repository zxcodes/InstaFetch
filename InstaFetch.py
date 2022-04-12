from gazpacho import get, Soup
import re as regex
import sys


def fetchUserData(username):
    # Fetch Logic
    requestURL = f'https://www.instagram.com/{username}/feed/?hl=en'
    try:
        fetchedMarkup = get(requestURL)
    except:
        print("\n😖 Account not found! \n   Check the username or try another one!\n")
    else:
        parsedHTML = Soup(fetchedMarkup)
        fetchedDescription = parsedHTML.find(
            "meta", {"property": "og:description"}).attrs['content']
        findUserData = regex.split('\s', fetchedDescription)
        userName = findUserData[15]
        print("\n"+"⚡ Username: " + userName.strip('()') + '\n')
        userFirstname = findUserData[13]
        userLastname = findUserData[14]
        print("⚡ Full Name: " + userFirstname, userLastname + '\n')
        userFollowers = findUserData[0]
        print("⚡ Followers: " + userFollowers + '\n')
        userFollowing = findUserData[2]
        print("⚡ Following: " + userFollowing + '\n')
        userPosts = findUserData[4]
        print("😍 Posts: " + userPosts + '\n')
        print("🔗 Profile Link: " + requestURL + '\n')


# Getting user input
enteredUsername = input("\n" + "🔥 Enter Instagram Username: ")

if len(enteredUsername) == 0 or len(enteredUsername) < 2:
    print("Please enter a username before you continue!" + '\n')
    sys.exit()
else:
    fetchUserData(enteredUsername)
