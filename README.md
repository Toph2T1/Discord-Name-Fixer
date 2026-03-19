# NameFixer
A Discord bot built with [Hikari](https://github.com/hikari-py/hikari/) that ensures display names remain clear and readable by blocking non-english characters, including:  
- Accented characters (é, ñ, ö)
- Emoji
- Fancy Unicode (𝓣𝓮𝓼𝓽)
- Kanji / Hiragana / Katakana (Japanese)
- Any non-ASCII script (Chinese, Korean, Cyrillic, etc.)
- Zero-width / invisible characters

Invalid names are fixed by resetting the member’s nickname to their username.

## Features
Uses Discord events as triggers to detect and fix invalid display names:

- On member join
- On member update (nickname, roles, etc.)
- On message send (passive cleanup of existing members)

## Requirements
- Python 3.10+
- Discord bot token
  - You will need to register a new bot in the [Discord Dev Portal](https://discord.com/developers/applications) to acquire a token.

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/Toph2T1/Discord-Name-Fixer
   cd Discord-Name-Fixer
   ```

2. Create a `.env` file:
   ```env
   TOKEN="your_bot_token_here"
   ```
   (See `.env.example`)

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the bot:
   ```bash
   python -m bot
   ```

## Required Permissions & Intents
### Permissions
- Manage Nicknames

### Intents
- GUILDS
- GUILD_MEMBERS
- GUILD_MESSAGES

### Developer Portal
- Enable **Server Members Intent** under Privileged Gateway Intents

### Important Notes
- The bot must have the **Manage Nicknames** permission to function.
- The bot's role must be **higher than the roles of users it is trying to rename**.
- The bot **cannot** modify the server owner or users with higher roles.
