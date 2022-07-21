import discord
from discord.ext import commands
from environs import Env

env = Env()
env.read_env()  # read .env file, if it exists

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.command(name="ping")
async def ping(ctx):
    print(ctx.guild)
    print(ctx.guild.id)
    print(ctx.message)
    print(ctx.message.channel.id)
    print(ctx.author.name)
    print(ctx.author.mention)
    await ctx.send("pong")


# @bot.user_command(name="Say")
# async def hi(ctx, user):
#     await ctx.respond(f"{ctx.author.mention} says hello to {user.name}!")

@bot.slash_command(name="hello", description="testing", )
async def hello(ctx, name: str = None):
    name = name or ctx.author.name
    await ctx.respond(f"Hello {name}!")


@bot.slash_command(name="member", description="member joint date",)
async def members(ctx, *, member: discord.Member):
    await ctx.respond(f'{member} joined on {member.joined_at}')


@bot.command(name="dm")
async def dm(ctx, *, user: discord.Member, message=None):
    embed = discord.Embed(title="good day")
    await user.send(embed=embed)
    await ctx.message.delete()


bot.run(env.str("TOKEN", ''))
