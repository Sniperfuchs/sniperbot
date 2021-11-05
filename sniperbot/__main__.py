import os
from dotenv import load_dotenv

import hikari
from hikari import intents
import lightbulb

load_dotenv()

DEFAULT_GUILD_ID = os.getenv("DEFAULT_GUILD_ID")
TEST_CHANNEL_ID = os.getenv("TEST_CHANNEL_ID")

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

bot = lightbulb.Bot(
    token=DISCORD_TOKEN,
    prefix="?",
    intents=hikari.Intents.ALL,
    default_enabled_guilds=DEFAULT_GUILD_ID
)

bot.load_extensions_from("./sniperbot/extensions")

@bot.listen(hikari.StartedEvent)
async def on_started(event):
    channel = await bot.rest.fetch_channel(TEST_CHANNEL_ID)
    await channel.send("Hello!")


def main():
    if os.name != "nt":
        import uvloop
        uvloop.install()
    bot.run()

if __name__ == "__main__":
    main()