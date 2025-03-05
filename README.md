# Twitch Chat Bot - Markov Chain Generator

## Introduction
Hello! This is a Twitch chat bot that collects opted-in users' chat messages to generate random messages using a Markov chain. It was originally (and still is) an effort to support **[Jaquarium](https://twitch.tv/jaquarium)** through alternative means beyond direct donations and subscriptions. If you enjoy the bot, please spread the word!

## Running the Bot
If you would like me to run the bot for you, simply follow these steps:
1. **Create a Twitch account** for your bot.
2. **Maintain an active subscription** to [Jaquarium](https://twitch.tv/jaquarium).
3. **Generate an access token** using [Twitch Token Generator](https://twitchtokengenerator.com/).
4. **Send me the access token**, via [jq's discord @whatnowmaxtv](https://discord.gg/FTYCwNeNeJ) and I will keep the bot running as long as your subscription to Jaquarium is maintained.

If you prefer to run the bot on your own system, follow these steps:

### Requirements:
- **Node.js** (Latest LTS version recommended)
- **Python** (For Markov processing)
- **tmi.js** (Twitch chat interface library for Node.js)
- **Markov library** for Node.js

### Installation Steps:
1. **Install Node.js** if you haven’t already: [Download Node.js](https://nodejs.org/)
2. **Install Python** if you haven’t already: [Download Python](https://www.python.org/downloads/)
3. **Clone the repository:**
   ```sh
   git clone https://github.com/your-repo/twitch-markov-bot.git
   cd twitch-markov-bot
   ```
4. **Install required dependencies:**
   ```sh
   npm install tmi.js markov
   ```
5. **Run the bot:**
   ```./startbot.sh <name of bot> <name of channel>
   ```
   - Example:
   ```./startbot.sh avgjqchatter jaquarium
   ```
   - Alternatively, you can just launch the .js:
   ```node twitch-chat-logger.js <name of bot> <name of channel>
   ```
   I created the bash wrapper to load env variables for python/js to make things easier for myself, but this is going to be env specific.

   The bot should make a few directories, files, and fail.
   
7. **Configure your bot:**
   - Grab the access token from [Twitch Token Generator](https://twitchtokengenerator.com/). (choose "bot" on the popup, then login)
   - put "oauth:" in front of the access token and save it to the token.txt file generated in your bot's folder
   - Example:
   ```oauth:123123123123123123sdfsdffasdfsdf
   ```

## Commands
The bot provides the following chat commands:

### User Commands:
- `!optin` – Opt in to allow your messages to be used for teaching the bot.
- `!optout` – Opt out at any time. Messages are not purged, as they are stored anonymously with no tracking.

### Moderator/Broadcaster Commands:
- `!banterm <term>` – Prevents the bot from ever using the specified term.
- `!unbanterm <term>` – Removes a previously banned term.

## Support & Contribution
This bot was created as a way to support **Jaquarium**. If you enjoy using it, consider spreading the word and encouraging others to subscribe. Your support ensures the bot remains active and continues to improve!

For inquiries or setup assistance, feel free to reach out.

---

## Disclaimer
This bot can and will generate offensive or unintended chat messages due to the nature of Markov chain-based text generation. It should not be used in chats without the supervision of an active moderation team.

This bot does not store any personally identifiable information. All stored messages are anonymous and cannot be traced back to specific users.

