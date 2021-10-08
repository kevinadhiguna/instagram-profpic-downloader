import instaloader
import pyfiglet

instagram = instaloader.Instaloader()

# Print a banner
ascii_banner = pyfiglet.figlet_format("Insta Profpic")
print(ascii_banner)
print("GitHub Repo : https://github.com/kevinadhiguna/instagram-profpic-downloader\n")

try:
    instagram_account = input("What is the account name ? : ")
    instagram.download_profile(instagram_account, profile_pic_only=True)
    print("Downloaded successfully !")
except:
    print("An error happened... try again later")
