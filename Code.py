import discord
import cmds
import Go
import importlib

client = discord.Client()

auth = cmds.readjson(r"C:\Users\Red Solo\PycharmProjects\Fourbot\auth.json")


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="Type " + cmds.prefix + "help for help"))
    print("I'm here!!!")


@client.event
async def on_message(msg):
    if msg.content[:len(cmds.prefix)] != cmds.prefix:
        return
    await cmds.process(msg, client)
    if cmds.isupdate(msg):
        # Reloads cmds
        importlib.reload(cmds)
        importlib.reload(Go)

client.run(auth)
