<br />
<div align="center">
  <a href="https://github.com/kevinadhiguna/instagram-profpic-downloader">
    <img src="https://s9.gifyu.com/images/k5654jh64k5.png" alt="Instagram Profile Picture downloader">
    <!-- size 150x150 px -->
    <!-- <img src="https://s9.gifyu.com/images/ef5ydsladawdlkndwa.png" alt="Instagram Profile Picture downloader"> -->
  </a>

  <h3 align="center">Instagram Profile Picture Downloader</h3>

  <p align="center">
    Want to download a profile picture in Instagram? Then this tool might be able to help you!
    <br />
    <br />
    <a href="https://github.com/kevinadhiguna/instagram-profpic-downloader"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/kevinadhiguna/instagram-profpic-downloader/issues">Report Bug</a>
    ·
    <a href="https://github.com/kevinadhiguna/instagram-profpic-downloader/issues">Request Feature</a>
  </p>
</div>

<div align="center">
  <img src="https://user-images.githubusercontent.com/43397636/136511181-8220de7e-9eae-41fe-8d9c-0badf8f1dd20.png" width="70%" />
</div>

<br />

## 🧐 About this project

This is a tool powered by Python to download an Instagram account's profile picture. This works on both `public` and `private` Instagram accounts.

<br/>

## ⚙️ Before running this app (Prerequisites)

1. Install [python 3](https://www.python.org/downloads/).
2. Get [docker](https://docs.docker.com/engine/install/) and [docker-compose](https://docs.docker.com/compose/install/) installed in your machine, **only** if you would like to run the app using them.

<br />
<hr />

## 🐍 How to run using Python :
1. Clone this repository :<br />
```bash
git clone https://github.com/kevinadhiguna/insta-profpic-downloader.git
```

2. Install dependencies :<br />
```bash
pip3 install -r requirements.txt
```
or
```bash
pip install -r requirements.txt
```

3. Run this program :<br />

⚠️ `download.py` is deprecated. Please use `insta.py` instead
```bash
python3 insta.py
```
or
```bash
python insta.py
```

4. Put the username that you want to download the profile picture of.

5. The profile picture is downloaded in the folder you cloned this tool!

<br />
<hr />

## 🐋 How to run using Docker :
1. Clone this repository :<br />
```bash
git clone https://github.com/kevinadhiguna/insta-profpic-downloader.git
```

2. Build the docker image of this app :<br />
```bash
docker build -t <image-name>:<tag> .
```

Replace the `<image-name>` and `<tag>` with whatever you want.
<br />
Let's say you want to name it `insta-profpic` and apply `latest` as the tag. In this case you might run :
```bash
docker build -t insta-profpic:latest .
```

3. Run the docker image :<br />
```bash
docker run -it -v "$(pwd):/app" <image-name>:<tag>
```

Just a quick example : if you name it `insta-profpic` and gave `latest` as the tag, then you should run :
```bash
docker run -it -v "$(pwd):/app" insta-profpic:latest
```

4. Put the username that you want to download the profile picture of.

5. The profile picture is downloaded in the folder you cloned this tool!

<br />
<hr />

## 🐳 How to run using docker-compose :
1. Clone this repository :<br />
```bash
git clone https://github.com/kevinadhiguna/insta-profpic-downloader.git
```

2. Build the docker image of this app :<br />
```bash
docker-compose build
```

3. Run a service :<br />
```bash
docker-compose run insta
```

4. Put the username that you want to download the profile picture of.

5. The profile picture is downloaded in the folder you cloned this tool!

<br />

### 📝 To-do list :
- [ ] build(ci): Modify GitHub Workflows to build and push docker image to DockerHub

Pull Requests are welcome 🙏

<br />

### 🗒️ Notes :
- **I am not responsible for any misuse of this tool**.

Thanks for visiting, have a nice day !

<br/>

[![Visits Badge](https://badges.pufler.dev/visits/kevinadhiguna/instagram-profpic-downloader)](https://github.com/kevinadhiguna)
