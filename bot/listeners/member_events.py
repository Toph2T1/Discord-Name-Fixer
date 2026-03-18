import hikari

from bot import utils


def register_listeners(bot: hikari.GatewayBot) -> None:
    """Register all event listeners for the bot."""    
    @bot.listen()
    async def on_member_join(event: hikari.MemberCreateEvent) -> None:
        await utils.ensure_valid_display_name(bot, event.member, event.guild_id)

    @bot.listen()
    async def on_member_update(event: hikari.MemberUpdateEvent) -> None:
        await utils.ensure_valid_display_name(bot, event.member, event.guild_id)

    @bot.listen()
    async def on_message_create(event: hikari.GuildMessageCreateEvent) -> None:

        # Apparently 'member' can be None or UNDEFINED sometimes in regards to message events, so check that first.
        # Fairly sure this is only in relation to UpdateEvent and DeleteEvent, but it doesn't hurt to be safe. 
        member = event.member
        if member is None or member is hikari.UNDEFINED:
            return

        await utils.ensure_valid_display_name(bot, member, event.guild_id)