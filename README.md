# Twitch Chat Bot - Markov Chain Generator

![image](https://github.com/user-attachments/assets/024626f4-c9f8-4c60-8c8e-48bbfec72272)

## Introduction
Hello! This is a Twitch chat bot that collects opted-in users' chat messages to generate random messages using a Markov chain. It was originally (and still is) an effort to support **[Jaquarium](https://twitch.tv/jaquarium)** through alternative means beyond direct donations and subscriptions. If you enjoy the bot, please spread the word!

## Running the Bot
If you would like me to run the bot for you, simply follow these steps:
1. **Create a Twitch account** for your bot.
2. **Maintain an active subscription** to [Jaquarium](https://twitch.tv/jaquarium).
3. **Generate an access token** using [Twitch Token Generator](https://twitchtokengenerator.com/).
4. **Send me the access token**, via DM in [jq's discord @whatnowmaxtv](https://discord.gg/FTYCwNeNeJ) and I will keep the bot running as long as your subscription to Jaquarium is maintained.

## If you prefer to run the bot on your own system, 
Follow these steps:

### Requirements:
- **Node.js** (Latest LTS version recommended)
- **Python** (For Markov processing)
- **tmi.js** (Twitch chat interface library for Node.js)
- **Markov library** for Node.js

### Installation Steps:
1. **Install Node.js** if you haven’t already: [Download Node.js](https://nodejs.org/)
2. **Install Python** if you haven’t already: [Download Python](https://www.python.org/downloads/)
3. **Clone or download the repository:**
   ```
   git clone https://github.com/whatnowmax/avgtwitchchatter.git
   cd avgtwitchchatter
   ```
   Or click on the green "code" in the upper right of the main repo page and download the zip.
   
5. **Install required dependencies:**
   ```
   npm install tmi.js
   pip install markovify
   ```
6. **Run the bot:**
    ```
   node twitch-chat-logger.js <name of bot> <name of channel>
   ```
    - Example:
   ```
   node twitch-chat-logger.js avgjqchatter jaquarium
   ```
   - Alternatively, you can use a bash script I wrote for myself:
   ```
   ./startbot.sh <name of bot> <name of channel>
   ```
   - Example:
   ```
   ./startbot.sh avgjqchatter jaquarium
   ```
   I created the bash wrapper to load env variables for python/js to make things easier for myself, but you probably won't need that.

   The bot should make a few directories, files, **and fail,** without it's token.txt
   
7. **Configure your bot:**
   - Grab the access token from [Twitch Token Generator](https://twitchtokengenerator.com/). (choose "bot" on the popup, then login)
   - put "oauth:" in front of the access token and save it to the token.txt file generated in your bot's folder
   - Example:
   ```
   oauth:123123123123123123sdfsdffasdfsdf
   ```
## General Usage
The bot will make a silly (hopefully) message every 25 opted-in messages. If the message is only one word, it is allowed to be 0% unique, however if the message is more than one word, it must be at least 10% unique. 

If the bot is ever perma-banned, it will leave the chat. The bot must be manually restarted (hopefully I can figure out how to fix this).

## Commands
The bot provides the following chat commands:

### User Commands:
- `!optin` – Opt in to allow your messages to be used for teaching the bot.
- `!optout` – Opt out at any time. Messages are not purged, as they are stored anonymously with no tracking.

### Moderator/Broadcaster Commands:
- `!banterm <term>` – Prevents the bot from ever using the specified term. This does not affect message storage.
- `!unbanterm <term>` – Allows a previously banned term.

## Support & Contribution
This bot was created as a way to support **[Jaquarium](https://twitch.tv/jaquarium)**. If you enjoy using it, consider spreading the word and encouraging others to subscribe/follow his channel. Pull Requests are encouraged, however I consider the bot LARGELY in a completed state so likely you'll want to fork it for channel-specific customization. There are of course endless decisions for how the bot should behave. Have fun!

For inquiries or setup assistance, ~~feel free to reach out~~ subscribe to jaquarium and have me run it for you :). Twitch bots are an amazing beginning programming project, and I highly highly encourage you to use this opportunity to dive into it if any of this seems fun, however I unfortunately don't have the bandwidth to help at the moment.

## Future Plans
* configure the 25 message frequency (for now you can easily edit the value in the .js, but I want to use an argument to make it easier on myself
* permabanned bot still tries to rejoin chat (this might not be possible given tmi.js unfortunately)
* have the bot write to disk every 25 messages, rather than every message. This will be top priority if any larger streamers join in.really tough to 
* ~~publish the project open source~~
---

## Disclaimer
This bot can **and will** generate offensive or unintended chat messages due to the nature of Markov chain-based text generation. It should not be used in chats without the supervision of an active moderation team.

This bot does not store any personally identifiable information. All stored messages are anonymous and cannot be traced back to specific users.

