# NameFixer
A Discord bot built with [Hikari](https://github.com/hikari-py/hikari/) that automatically enforces clean and readable display names by removing invisible or non-standard characters (e.g. emoji, fancy Unicode text like `𝓣𝓮𝓼𝓽`, or hidden characters). Invalid names are fixed by resetting the member’s nickname to their username.

## Features
Uses Discord events as triggers to detect and fix invalid display names:

- On member join
- On member update (nickname, roles, etc.)
- On message send (passive cleanup of existing members)

## Invite
Don't want to self-host? I host a public instance of NameFixer that you can invite to your server:  
[Click Me!](https://discord.com/oauth2/authorize?client_id=1483731224160632932&permissions=134217728&integration_type=0&scope=bot)

### Important Notes
- The bot must have the **Manage Nicknames** permission to function.
- The bot's role must be **higher than the roles of users it is trying to rename**.
- The bot **cannot** modify the server owner or users with higher roles.

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
