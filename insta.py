######################################
#  Please use this at your own risk  #
######################################

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
    print("\nDownloaded successfully, thank you for using this tool !")
except:
    print("\nSomething went wrong or the account might not exist. Please try again later...")
