# Twitch Chat Bot - Markov Chain Generator

## Introduction
Hello! This is a Twitch chat bot that collects opted-in users' chat messages to generate random messages using a Markov chain. It was originally (and still is) an effort to support **[Jaquarium](https://twitch.tv/jaquarium)** through alternative means beyond direct donations and subscriptions. If you enjoy the bot, please spread the word!

## Running the Bot
If you would like me to run the bot for you, simply follow these steps:
1. **Create a Twitch account** for your bot.
2. **Maintain an active subscription** to [Jaquarium](https://twitch.tv/jaquarium).
3. **Generate an access token** using [Twitch Token Generator](https://twitchtokengenerator.com/).
4. **Send me the access token**, and I will keep the bot running as long as your subscription to Jaquarium is maintained.

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
5. **Configure your bot:**
   - Create a `.env` file and add your Twitch bot credentials.
   - Example:
     ```env
     TWITCH_USERNAME=yourbotusername
     TWITCH_OAUTH=your_oauth_token
     ```
6. **Run the bot:**
   ```sh
   node bot.js
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

