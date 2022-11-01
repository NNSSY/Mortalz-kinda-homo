import discord
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, MissingPermissions
import json
import asyncio
import time
from discord.ui import Button, View, Select
import chat_exporter
import io
from datetime import datetime
from colorama import Fore, Style
from discord import Permissions
import requests
import random
from datetime import timedelta
session = requests.Session()

intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix="!", help_command=None, intents=intents)
token = "MTAzNTAyODk5MjcyMzUyOTc3OA.Garc59.hjv2CxVlq_STEsJXpPkwXMyjdgwoscSsAy-5lA"
uwu = 1036663116357963888
LTC="Not Currently Accepting"
BTC="Not Currently Accepting!"
ETH="Not Currently Accepting."
PP="https://www.paypal.com/paypalme/JSB134"
CA="$revisuals"

LTC_Emoji="<:LTC:1035372911537688576>"
BTC_Emoji="<:btc:1035372869481418752>"
ETH_Emoji="<:ETH:1035372836849717248>"
Paypal_Emoji="<:paypal:1035373137065426945>"
Cashapp_Emoji="<:Cashapp:1009836715499851907>"

Colours = [Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.YELLOW]
colour1 = random.choice(Colours)
colour2 = random.choice(Colours)

@tasks.loop(seconds=10.0)
async def stausss():
   statuses = ["Waves | !help ","Developed by Shiro ","discord.gg/wboosts"]
   status = random.choice(statuses)
   await bot.change_presence(activity=                   discord.Activity(type=discord.ActivityType.watching, name=status))

@bot.event
async def on_ready():
  stausss.start()
  print(colour2 + "Client Has Booted Up.")


@bot.command()
async def help(ctx):
 client = bot.user
 await ctx.message.delete()
 select = Select(
     placeholder="Select a Command Field ~ Waves",
     options=[
      discord.SelectOption(label="➲ Moderation", value="Moderation",description="List of Mod Commands", emoji="<:static_boost:1035208776866877460>"),
      discord.SelectOption(label="➲ Ticket", value="Fun",description="List of Ticket Commands", emoji="<:blue_bot:1035208495882043392>"),
      discord.SelectOption(label="➲ Dm",value="Informative", description="Dm Everybody in a server", emoji="<:blue_question:1035208160681668620>")
   ])

 embed = discord.Embed(title="Waves Moderation Tool", description="``Help for Waves ticket:``", color=0x0000)
 embed.set_author(name="Waves | Moderation Help", icon_url=client.display_avatar)
 embed.add_field(name="`!mute [Member] [Hours] [Reason]`", value="Mute a Member.")
 embed.add_field(name="`!unmute [Member] [Reason]`", value="Unmute a Member.")
 embed.add_field(name="`!slowmode [Seconds]`", value="Sets a Slowmode.")
 embed.add_field(name="`!unban [Member_ID] [Reason]`", value="Unbans a member.")
 embed.add_field(name="`!kick [Member_ID] [Reason]`", value="Kicks a member.")
 embed.add_field(name="`!ban [Member_ID] [Reason]`", value="Bans a member.")
 embed.set_thumbnail(url=client.display_avatar)
 embed.set_footer(text="Waves | Coded by Shiro")

 em = discord.Embed(title="Waves Tickets Tool", description="``Help for Waves ticket:``", color=0x0000)
 em.set_author(name="Waves | Ticket Help", icon_url=client.display_avatar)
 em.set_thumbnail(url=client.display_avatar)
 em.add_field(name="`!ticket [Channel_ID]`", value="Set a channel.")
 em.add_field(name="`!ping [role_id]`", value="Adds a role ping.")
 em.add_field(name="`!pingremove [role_id]`", value="Removes a role ping.")
 em.add_field(name="`!staff [role_id]`", value="Adds a ticket staff.")
 em.add_field(name="`!staff_remove [role_id]`", value="Removes a ticket Staff")
 em.add_field(name="`!staff_remove [role_id]`", value="Removes a ticket Staff")
 em.set_footer(text="Waves | Coded by Shiro")

 emb = discord.Embed(title="Waves DM Tool", description="``Help for Waves DM:``", color=0x0000)
 emb.set_author(name="Waves | DM Help", icon_url=client.display_avatar)
 emb.set_thumbnail(url=client.display_avatar)
 emb.add_field(name="- ``!dm [Message]``:",value="Dms All Members Of A Server")
 emb.add_field(name="- ``!dmrole [Role_ID] [Message]``:",value="Dms All Members Of A Role")
 emb.add_field(name="- ``!dmembed [title] [description] [Field_1 title] [Field_1 Content] [Field_2 title] [Field_2 Content]``:",value="Dms All Members using embeds. Remember to start and end every parameter with Double Quotation Marks .", inline=True)
 emb.add_field(name="- ``!dmer [roleid] [title] [description] [Field_1 title] [Field_1 Content] [Field_2 title] [Field_2 Content]``:",value="Dms All Members using embeds. Remember to start and end every parameter with Double Quotation Marks except for role id.", inline=True)
 emb.set_footer(text="Waves | Coded by Shiro")
  
 embe = discord.Embed(title="Waves | Help", url="https://discord.gg/wboosts", description="__**Help Command for Waves bot! Select an option below!**__", color=0x0000)
 embe.set_author(name="Waves", icon_url= client.display_avatar)
 embe.set_thumbnail(url=client.display_avatar)
 async def my_callback(interaction):
    if select.values[0] == "Moderation":
     await interaction.response.edit_message(embed=embed)
    if select.values[0] == "Fun":
     await interaction.response.edit_message(embed=em)
    if select.values[0] == "Informative":
     await interaction.response.edit_message(embed=emb)
     
 select.callback = my_callback
   
 view = View(timeout=None)
 view.add_item(select)
 await ctx.send(embed=embe, view=view)
 


@bot.command()
@has_permissions(administrator=True)
async def ticket(ctx, channelid: int):
  guild = ctx.guild
  client = bot.user
  channel = await guild.fetch_channel(channelid)
  select = Select(
     placeholder="Select a Ticket Field ~ Waves",
     options=[
      discord.SelectOption(label="Purchase Boosts", value="Boosts",description="Make a ticket to buy boosts",emoji="<:static_boost:1035208776866877460> "),
      discord.SelectOption(label="Purchasing Bot", value="Bot",description="Buy a Bot!", emoji="<:blue_bot:1035208495882043392>"),
      discord.SelectOption(label="Server Revamps",value="Revamp", description="Buy server revamp services", emoji="<:blue_dev:1035208485064937512>"),
      discord.SelectOption(label="General Support",value="Support", description="Get Support!", emoji="<:blue_question:1035208160681668620> ")
              ]
                )
  embed = discord.Embed(title="Waves Tickets", description="> ``Open a ticket:``", color=0x0000)
  embed.set_author(name="Waves | Ticket Tool", icon_url=client.display_avatar)
  embed.set_thumbnail(url=client.display_avatar)
  embed.set_footer(text="Waves | Coded by Shiro")
  async def my_callback(interaction):
    if select.values[0] == "Boosts":
     ticket = "Boosts"
    if select.values[0] == "Bot":
     ticket = "Bot"
    if select.values[0] == "Revamp":
     ticket = "Revamp"
    if select.values[0] == "Support":
     ticket = "Support"
    
    with open("data.json") as f:
     data = json.load(f)

    ticket_number = int(data["ticket-counter"])
    ticket_number += 1

    ticket_channel = await ctx.guild.create_text_channel(f"{ticket}-{ticket_number}")
    await interaction.response.send_message(f"Ticket Created at {ticket_channel.mention}!", ephemeral=True)
    await ticket_channel.set_permissions(ctx.guild.get_role(ctx.guild.id), send_messages=False, read_messages=False)

    for role_id in data["valid-roles"]:
        role = ctx.guild.get_role(role_id)

        await ticket_channel.set_permissions(role, send_messages=True, read_messages=True, add_reactions=True, embed_links=True, attach_files=True, read_message_history=True, external_emojis=True)
    
    await ticket_channel.set_permissions(interaction.user, send_messages=True, read_messages=True, add_reactions=True, embed_links=True, attach_files=True, read_message_history=True, external_emojis=True)

    em = discord.Embed(title=f"New ticket from {interaction.user}", description="``New Ticket``!", color=0x0000)

    await ticket_channel.send(embed=em)

    pinged_msg_content = ""
    non_mentionable_roles = []

    if data["pinged-roles"] != []:

        for role_id in data["pinged-roles"]:
            role = ctx.guild.get_role(role_id)

            pinged_msg_content += role.mention
            pinged_msg_content += " "

            if role.mentionable:
                pass
            else:
                await role.edit(mentionable=True)
                non_mentionable_roles.append(role)
        
        await ticket_channel.send(pinged_msg_content)

        for role in non_mentionable_roles:
            await role.edit(mentionable=False)
    
    data["ticket-channel-ids"].append(ticket_channel.id)

    data["ticket-counter"] = int(ticket_number)
    with open("data.json", 'w') as f:
        json.dump(data, f)
    
    created_em = discord.Embed(title="Wave | Ticket", description="Wave Tickets", color=0x0000)
    button = Button(label="Close Ticket", style = discord.ButtonStyle.green, emoji="🟥")
    async def button_callback(interaction):
      await interaction.response.send_message("``Closing Ticket..``")
      time.sleep(5)
      channel = ticket_channel
      archive_channel = await guild.fetch_channel(uwu)
      transcript = await chat_exporter.export(channel)
      transcript_file = discord.File(io.BytesIO(transcript.encode()), filename=f"{channel.name}.html")
      await archive_channel.send(ticket_channel.mention + f"``Closed by: {interaction.user}. Download to view file!``", file=transcript_file)
      await interaction.channel.delete()
      index = data["ticket-channel-ids"].index(interaction.channel_id)
      del data["ticket-channel-ids"][index]
      with open('data.json', 'w') as f:
                json.dump(data, f)
    button.callback = button_callback
    view = View(timeout=None)
    view.add_item(button)
    await ticket_channel.send(embed=created_em, view=view)

  select.callback = my_callback
  shiro = View(timeout=None)
  shiro.add_item(select)
  await channel.send(embed=embed, view=shiro)


    


        

@bot.command()
async def ping(ctx, role_id=None):

    with open('data.json') as f:
        data = json.load(f)
    
    valid_user = False

    for role_id in data["verified-roles"]:
        try:
            if ctx.guild.get_role(role_id) in ctx.author.roles:
                valid_user = True
        except:
            pass
    
    if valid_user or ctx.author.guild_permissions.administrator:

        role_id = int(role_id)

        if role_id not in data["pinged-roles"]:

            try:
                role = ctx.guild.get_role(role_id)

                with open("data.json") as f:
                    data = json.load(f)

                data["pinged-roles"].append(role_id)

                with open('data.json', 'w') as f:
                    json.dump(data, f)

                em = discord.Embed(title="Waves Tickets", description="You have successfully added `{}` to the list of roles that get pinged when new tickets are created!".format(role.name), color=0x0000)

                await ctx.send(embed=em)

            except:
                em = discord.Embed(title="Waves Tickets", description="That isn't a valid role ID. Please try again with a valid role ID.", color=0x0000)
                await ctx.send(embed=em)
            
        else:
            em = discord.Embed(title="Waves Tickets", description="That role already receives pings when tickets are created.", color=0x0000)
            await ctx.send(embed=em)
    
    else:
        em = discord.Embed(title="Waves Tickets", description="Sorry, you don't have permission to run that command.", color=0x0000)
        await ctx.send(embed=em)

@bot.command()
async def pingremove(ctx, role_id=None):

    with open('data.json') as f:
        data = json.load(f)
    
    valid_user = False

    for role_id in data["verified-roles"]:
        try:
            if ctx.guild.get_role(role_id) in ctx.author.roles:
                valid_user = True
        except:
            pass
    
    if valid_user or ctx.author.guild_permissions.administrator:

        try:
            role_id = int(role_id)
            role = ctx.guild.get_role(role_id)

            with open("data.json") as f:
                data = json.load(f)

            pinged_roles = data["pinged-roles"]

            if role_id in pinged_roles:
                index = pinged_roles.index(role_id)

                del pinged_roles[index]

                data["pinged-roles"] = pinged_roles

                with open('data.json', 'w') as f:
                    json.dump(data, f)

                em = discord.Embed(title="Waves Tickets", description="You have successfully removed `{}` from the list of roles that get pinged when new tickets are created.".format(role.name), color=0x0000)
                await ctx.send(embed=em)
            
            else:
                em = discord.Embed(title="Waves Tickets", description="That role already isn't getting pinged when new tickets are created!", color=0x0000)
                await ctx.send(embed=em)

        except:
            em = discord.Embed(title="Waves Tickets", description="That isn't a valid role ID. Please try again with a valid role ID.", color=0x0000)
            await ctx.send(embed=em)
    
    else:
        em = discord.Embed(title="Waves Tickets", description="Sorry, you don't have permission to run that command.", color=0x0000)
        await ctx.send(embed=em)


@bot.command()
@has_permissions(administrator=True)
async def staff(ctx, role_id=None):

    try:
        role_id = int(role_id)
        role = ctx.guild.get_role(role_id)

        with open("data.json") as f:
            data = json.load(f)

        data["verified-roles"].append(role_id)

        with open('data.json', 'w') as f:
            json.dump(data, f)
        
        em = discord.Embed(title="Waves Tickets", description="You have successfully added `{}` to the list of roles that can run admin-level commands!".format(role.name), color=0x0000)
        await ctx.send(embed=em)

    except:
        em = discord.Embed(title="Waves Tickets", description="That isn't a valid role ID. Please try again with a valid role ID.", color=0x0000)
        await ctx.send(embed=em)

@bot.command()
@has_permissions(administrator=True)
async def staff_remove(ctx, role_id=None):
    try:
        role_id = int(role_id)
        role = ctx.guild.get_role(role_id)

        with open("data.json") as f:
            data = json.load(f)

        admin_roles = data["verified-roles"]

        if role_id in admin_roles:
            index = admin_roles.index(role_id)

            del admin_roles[index]

            data["verified-roles"] = admin_roles

            with open('data.json', 'w') as f:
                json.dump(data, f)
            
            em = discord.Embed(title="Waves Tickets", description="You have successfully removed `{}` from the list of roles that get pinged when new tickets are created.".format(role.name), color=0x0000)

            await ctx.send(embed=em)
        
        else:
            em = discord.Embed(title="Waves Tickets", description="That role isn't getting pinged when new tickets are created!", color=0x0000)
            await ctx.send(embed=em)

    except:
        em = discord.Embed(title="Waves Tickets", description="That isn't a valid role ID. Please try again with a valid role ID.")
        await ctx.send(embed=em)

@bot.command()
async def dm(ctx,*,message=None):
 x = 0
 author = ctx.message.author
 if author.id == 718612737109917737:
  members = ctx.guild.members
  if message != None:
   print(Fore.BLACK + "Dm Command executing... Members DM'ed Every 14 Seconds From Now On!")
   embed = discord.Embed(title="Mass Dm Starting... ``NOW``!",description=f"**Mass Dm ending in** ``{round(10*ctx.guild.member_count/30)} minutes !``", colour = 0x000)
   embed.set_author(name="Shiro | Mass Dm",icon_url=author.display_avatar)
   embed_2 = discord.Emtbed(title="Mass Dm Finished.!",description=f"``Mass Dm Ended!``", colour = 0x000)
   embed_2.set_author(name="Shiro | Mass Dm",icon_url=author.display_avatar)
   msg = await ctx.send(embed=embed)
   for member in members:
     try:
      await member.send(message)
      print(Fore.BLUE + "(+)" + Fore.WHITE + f"{member} has been DM'ed")
      x += 1
     except:
      print(Fore.RED + "(!)" + Fore.WHITE + f" I could not DM {member}")
      x += 1
     if x == ctx.guild.member_count:
        await author.send("``Mass Dm Completed``")
        await msg.edit(embed=embed_2)
     time.sleep(14)
  else:
    await ctx.send("``Please add a valid argument!``")
    print(colour1 + "Add a Valid Argument!")
 else:
    await ctx.reply("``I spy that..`` **You Aren't Mortalz!**")

@bot.command()
async def dmembed(ctx, title, description, field_1_title, field_1_content, field_2_title, field_2_content):
 x = 0
 author = ctx.message.author
 if author.id in [718612737109917737, 923531486794240010]:
  members = ctx.guild.members
  print(Fore.BLACK + "Dm Command executing... Members DM'ed Every 14 Seconds From Now On!")
  embed = discord.Embed(title="Mass Dm Starting... ``NOW``!",description=f"**Mass Dm ending in** ``{round(10*ctx.guild.member_count/30)} minutes !``", colour = 0x000)
  embed.set_author(name="Shiro | Mass Dm",icon_url=author.display_avatar)
  embed_2 = discord.Embed(title="Mass Dm Finished.!",description=f"``Mass Dm Ended!``", colour = 0x000)
  embed_2.set_author(name="Shiro | Mass Dm",icon_url=author.display_avatar)
  msg = await ctx.send(embed=embed)
  for member in members:
     clien = bot.user
     emb = discord.Embed(title=title,description=description,colour=0x000)
     emb.set_author(name="Waves",icon_url=clien.display_avatar)
     emb.add_field(name=field_1_title, value=field_1_content, inline=False)
     emb.add_field(name=field_2_title, value=field_2_content, inline=False)
     try:
      await member.send(embed=emb)
      print(Fore.BLUE + "(+)" + Fore.WHITE + f"{member} has been DM'ed")
      x += 1
     except:
      print(Fore.RED + "(!)" + Fore.WHITE + f" I could not DM {member}")
      x += 1
     if x == ctx.guild.member_count:
        await author.send("``Mass Dm Completed``")
        await msg.edit(embed=embed_2)
     time.sleep(14)
 else:
    await ctx.reply("``I spy that..`` **You Aren't Mortalz!**")

@bot.command()
async def dmrole(ctx,roleid:int ,*,message=None):
 guild = ctx.guild
 role = guild.get_role(roleid)
 x = 0
 author = ctx.message.author
 if author.id == 718612737109917737:
  members = role.members
  if message != None:
   print(Fore.BLACK + "Dm Command executing... Members DM'ed Every 14 Seconds From Now On!")
   embed = discord.Embed(title="Mass Dm Starting... ``NOW``!",description=f"**Mass Dm ending in** ``{round(10*len(role.members)/30)} minutes !``", colour = 0x000)
   embed.set_author(name="Shiro | Mass Dm",icon_url=author.display_avatar)
   embed_2 = discord.Embed(title="Mass Dm Finished.!",description=f"``Mass Dm Ended!``", colour = 0x000)
   embed_2.set_author(name="Shiro | Mass Dm",icon_url=author.display_avatar)
   msg = await ctx.send(embed=embed)
   for member in members:
     try:
      await member.send(message)
      print(Fore.BLUE + "(+)" + Fore.WHITE + f"{member} has been DM'ed")
      x += 1
     except:
      print(Fore.RED + "(!)" + Fore.WHITE + f" I could not DM {member}")
      x += 1
     if x == len(role.members):
        await author.send("``Mass Dm Completed``")
        await msg.edit(embed=embed_2)
     time.sleep(14)
  else:
    await ctx.send("``Please add a valid argument!``")
    print(colour1 + "Add a Valid Argument!")
 else:
    await ctx.reply("``I spy that..`` **You Aren't Mortalz!**")


@bot.command()
async def dmer(ctx,roleid: int, title, description, field_1_title, field_1_content, field_2_title, field_2_content):
 x = 0
 guild = ctx.guild
 role = guild.get_role(roleid)
 author = ctx.message.author
 if author.id in [718612737109917737, 923531486794240010]:
  members = role.members
  print(Fore.BLACK + "Dm Command executing... Members DM'ed Every 14 Seconds From Now On!")
  embed = discord.Embed(title="Mass Dm Starting... ``NOW``!",description=f"**Mass Dm ending in** ``{round(10*len(role.members)/30)} minutes !``", colour = 0x000)
  embed.set_author(name="Shiro | Mass Dm",icon_url=author.display_avatar)
  embed_2 = discord.Embed(title="Mass Dm Finished.!",description=f"``Mass Dm Ended!``", colour = 0x000)
  embed_2.set_author(name="Shiro | Mass Dm",icon_url=author.display_avatar)
  msg = await ctx.send(embed=embed)
  for member in members:
     clien = bot.user
     emb = discord.Embed(title=title,description=description,colour=0x000)
     emb.set_author(name="Waves",icon_url=clien.display_avatar)
     emb.add_field(name=field_1_title, value=field_1_content, inline=False)
     emb.add_field(name=field_2_title, value=field_2_content, inline=False)
     try:
      await member.send(embed=emb)
      print(Fore.BLUE + "(+)" + Fore.WHITE + f"{member} has been DM'ed")
      x += 1
     except:
      print(Fore.RED + "(!)" + Fore.WHITE + f" I could not DM {member}")
      x += 1
     if x == len(role.members):
        await author.send("``Mass Dm Completed``")
        await msg.edit(embed=embed_2)
     time.sleep(14)
 else:
    await ctx.reply("``I spy that..`` **You Aren't Mortalz!**")

@bot.slash_command(guild_ids = [993887477087612990], name="payments", description="Shows All Available Payment Options")
async def payments(interaction: discord.Interaction):
    select = Select(
        max_values=1,
        placeholder="Payment Options",
        options=[
            discord.SelectOption(label="Litecoin", emoji=LTC_Emoji, description="Litecoin Address", value=LTC), 
            discord.SelectOption(label="Bitcoin", emoji=BTC_Emoji, description="Bitcoin Address", value=BTC),
            discord.SelectOption(label="Ethereum", emoji=ETH_Emoji, description="Ethereum Address", value=ETH),
            discord.SelectOption(label="Paypal", emoji=Paypal_Emoji, description="Paypal Email", value=PP),
            discord.SelectOption(label="Cashapp", emoji=Cashapp_Emoji, description="CashTag - Cashapp", value=CA)
        ]
    )
    async def my_callback(interaction: discord.Interaction):
            await interaction.response.send_message(f"{select.values[0]}", ephemeral=True)
    select.callback = my_callback
    view = View(timeout=None)
    view.add_item(select)
    embed=discord.Embed(title="Select your Payment Method", timestamp=datetime.now(), color=discord.Colour.blurple())
    await interaction.response.send_message(embed=embed, view=view)

@bot.command()
@has_permissions(moderate_members=True)
async def mute(ctx, member: discord.Member, hours: int,*,reason):
  try:
    duration = timedelta(   
        days=0,
        seconds=0,
        microseconds=0,
        milliseconds=0,
        minutes=0,
        hours=hours,
        weeks=0)
    await member.timeout_for(duration=duration,reason=reason)
    await ctx.reply(f"I have timed out {member.mention}!")
  except:
    await ctx.reply("Something went wrong!")

@bot.command()
@has_permissions(moderate_members=True)
async def unmute(ctx, member: discord.Member, reason):
  try:
    await member.remove_timeout(reason=reason)
    await ctx.reply(f"I have unmuted {member.mention}!")
  except:
    await ctx.reply("Something went wrong!")

@bot.command()
@has_permissions(ban_members=True)
async def ban(ctx, member_id: int,*,reason=None):
  member = await bot.fetch_user(member_id)
  guildid = ctx.guild.id
  try:
   payload = {
            "delete_message_days": random.randint(0, 7)
        }
   while True:
    response = session.put(f"https://discord.com/api/v10/guilds/{guildid}/bans/{member_id}", headers={"Authorization": f"Bot {token}"}, json=payload)
    await ctx.send(f"I have banned {member.mention}")
  except:
    await ctx.send(f"I could not ban {member.mention}")

@bot.command()
@has_permissions(ban_members=True)
async def unban(ctx, member_id: int,*,reason=None):
  member = await bot.fetch_user(member_id)
  guildid = ctx.guild.id
  try:
    response = session.delete(f"https://discord.com/api/v10/guilds/{guildid}/bans/{member_id}", headers={"Authorization": f"Bot {token}"})
    await ctx.send(f"I have Unbanned {member.mention}")
  except:
    await ctx.send(f"I could not Unban {member_id}")

@bot.command()
@has_permissions(kick_members=True)
async def kick(ctx, member_id: int,*,reason=None):
  member = await bot.fetch_user(member_id)
  guildid = ctx.guild.id
  try:
    response = session.delete(f"https://discord.com/api/v10/guilds/{guildid}/members/{member_id}", headers={"Authorization": f"Bot {token}"})
    await ctx.send(f"I have kicked {member.mention}")
  except:
    await ctx.send(f"I could not kicked {member.mention}, perhaps there is something wrong with my permissions?")

@bot.command()
@has_permissions(manage_channels=True)
async def slowmode(ctx, slowmode_length:int):
  channel = ctx.channel
  try:
     await channel.edit(slowmode_delay=slowmode_length)
     await ctx.send(f"I have set the slowmode to {slowmode_length} seconds.")
  except:
     await ctx.send("I do not have permissions to adjust the slowmode of this channel")

@bot.command()
@has_permissions(manage_messages=True)
async def purge(ctx,*,amount:int):
 await ctx.channel.purge(limit=amount)

@purge.error
async def purge_error(ctx, error):
    if isinstance(error, MissingPermissions):
        text = "Sorry {}, you do not have permissions to do that!".format(ctx.message.author)
        await ctx.reply(text)

@mute.error
async def mute_error(ctx, error):
    if isinstance(error, MissingPermissions):
        text = "Sorry {}, you do not have permissions to do that!".format(ctx.message.author)
        await ctx.reply(text)

@unmute.error
async def unmute_error(ctx, error):
    if isinstance(error, MissingPermissions):
        text = "Sorry {}, you do not have permissions to do that!".format(ctx.message.author)
        await ctx.reply(text)

@ban.error
async def ban_error(ctx, error):
    if isinstance(error, MissingPermissions):
        text = "Sorry {}, you do not have permissions to do that!".format(ctx.message.author)
        await ctx.reply(text)    

@unban.error
async def unban_error(ctx, error):
    if isinstance(error, MissingPermissions):
        text = "Sorry {}, you do not have permissions to do that!".format(ctx.message.author)
        await ctx.reply(text)  

@kick.error
async def kick_error(ctx, error):
    if isinstance(error, MissingPermissions):
        text = "Sorry {}, you do not have permissions to do that!".format(ctx.message.author)
        await ctx.reply(text) 

@slowmode.error
async def slowmode_error(ctx, error):
    if isinstance(error, MissingPermissions):
        text = "Sorry {}, you do not have permissions to do that!".format(ctx.message.author)
        await ctx.reply(text)
@ticket.error
async def ticket_error(ctx, error):
    if isinstance(error, MissingPermissions):
        text = "Sorry {}, you do not have permissions to do that!".format(ctx.message.author)
        await ctx.reply(text)
bot.run(token=token)
