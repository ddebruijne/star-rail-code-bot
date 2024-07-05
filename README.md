# Star Rail & Zenless Zone Zero Code Bot

This is intended to be ran with docker. it polls prydwen.gg for new codes every 30 minutes and posts that to a discord channel.

### Setup
1. clone repo
2. copy `.env.example` to `.env` and set the desired discord bot token (get it from the dev site) and channel (enable dev mode, right click a channel and copy). Alternatively, set this in something like Portainer.
3. use `docker build --tag hsr-bot .` to build the image
4. deploy the image as desired. I'm using portainer or docker desktop.

### License
Feel free to use this code for anything, provided as-is with no support.
Please be sensible with polling frequency.
