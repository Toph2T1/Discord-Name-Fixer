import re

import hikari

VALID_NAME_REGEX = re.compile(r"^[\x20-\x7E]+$")

def is_valid_name(name: str) -> bool:
    """
    Allowed characters:
    - All standard ASCII keyboard characters (including letters, numbers, symbols, and spaces).

    Disallowed:
    - Everything else, particuarly Zalgo text, emojis and annoying zero-width invisible characters.
    """
    return bool(VALID_NAME_REGEX.fullmatch(name))


async def ensure_valid_display_name(app: hikari.GatewayBot, member: hikari.Member, guild_id: hikari.Snowflakeish) -> None:
    """Validate a member's display name and reset it to their username if invalid."""
    original_name = member.display_name

    if member.is_bot:
        return

    if member.display_name == member.username:
        return

    if is_valid_name(original_name):
        return

    try:
        await app.rest.edit_member(
            guild=guild_id,
            user=member.id,
            nickname=member.username,
            reason=f"Invalid display name: {original_name}",
        )
    except hikari.ForbiddenError:
        # Probably only caused by trying to edit someone whose higher on the role hierarchy (we do not care). 
        return
