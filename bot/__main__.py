import os

import dotenv
import hikari

from bot.listeners.member_events import register_listeners

dotenv.load_dotenv()

bot = hikari.GatewayBot(
    token=os.environ["TOKEN"],
    intents=(hikari.Intents.GUILDS | hikari.Intents.GUILD_MEMBERS | hikari.Intents.GUILD_MESSAGES),
)

register_listeners(bot)

if __name__ == "__main__":
    bot.run()