import instaloader

instagram = instaloader.Instaloader()

try:
    instagram_account = input("What is the account name ? : ")
    instagram.download_profile(instagram_account, profile_pic_only=True)
    print("Downloaded successfully !")
except:
    print("An error happened... try again later")
