import asyncio
from .. import commands, util
from ..permissions import Permission

# How to piss people off with shitty messages.py
# Put this in a file called annoying.py and but that file in dueutil/botcommands/ 
# so the path would be dueuti/botcommands/annoying.py

# step 1 get all the servers you want people to kick your bot from.
def get_all_servers():
    return [server for client in util.shard_clients for server in client.servers]


@commands.command(permission=Permission.DUEUTIL_ADMIN, args_pattern="S", aliases=["broadcast", "motd"])
async def broadcastcrap(ctx, content, **__):
    """
    [CMD_KEY]broadcast (announcement)
    
    Sends a message to the default channel of every server that Another Due Clone has joined.
    
    """
    for server in get_all_servers():
        print(("Broadcast debugging: server is", server.name, server.id))
        if server.default_channel is not None:
            try:
                print(("default_channel is: " + str(server.default_channel)))
            except Exception as e:
                print(e)
            await util.say(server.default_channel, "**DUE ANNOUNCEMENT!**\n" + content)
        else:
            print(("Server has no default channel. Skipping for now."))

        # if a large number of servers this may help
        await asyncio.sleep(0.1)