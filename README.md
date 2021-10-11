# Instagram Profile Picture Downloader

Wants to download a profile picture in Instagram? Then this tool might be able to help you!

<img src="https://user-images.githubusercontent.com/43397636/136511181-8220de7e-9eae-41fe-8d9c-0badf8f1dd20.png" width="70%" />

This works on both `public` and `private` Instagram account.

<br/>

## Before running this app (Prerequisites)

1. Install [python 3](https://www.python.org/downloads/).
2. Get [docker](https://docs.docker.com/engine/install/) and [docker-compose](https://docs.docker.com/compose/install/) installed in your machine, **only** if you would like to run the app using them.

⚠️ However, currently I do not recommend running this app using docker and docker-compose.

<br />

## How to run using Python :
1. Clone this repository :<br />
`git clone https://github.com/kevinadhiguna/insta-profpic-downloader.git`

2. Install dependencies :<br />
`pip install -r requirements.txt` or `pip3 install -r requirements.txt`

3. Run this program :<br />
`python insta.py` or `python3 insta.py`

4. Put the username that you want to download the profile picture of.

5. The profile picture is downloaded in the folder you cloned this tool!

<br />

### To-do list :
- [ ] docs: Add instructions on how to run using docker and docker-compose
- [ ] build(docker) : Fix the docker-compose issue
- [ ] build(ci): Modify GitHub Workflows to build and push docker image to DockerHub

Pull Requests are welcome 🙏

<br />

### Notes :
- **I am not responsible for any misuse of this tool**.
- `download.py` is deprecated. Please use `insta.py` instead.

Thanks for visiting, have a nice day !

<br/>

[![Visits Badge](https://badges.pufler.dev/visits/kevinadhiguna/instagram-profpic-downloader)](https://github.com/kevinadhiguna)
