import customtkinter as ctk
import tkinter as tk
from tkinter import Label, messagebox, filedialog
from PIL import Image, ImageTk, ImageSequence
from discord.ext import commands
import discord
import time
import os
import requests
import threading
import webbrowser
import subprocess


class MainApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Crystal Interface")
        self.master.geometry("1400x800")

        ctk.set_appearance_mode("system")  
        ctk.set_default_color_theme("blue")  

        self.set_window_icon("favicon.ico")

        self.frame_left = ctk.CTkScrollableFrame(master, width=250, corner_radius=10)
        self.frame_left.grid(row=0, column=0, padx=30, pady=20, sticky="nsw")

        # Right frame (Content)
        self.frame_right = ctk.CTkFrame(master, corner_radius=10)
        self.frame_right.grid(row=0, column=1, padx=30, pady=20, sticky="nsew")

        # Theme switcher
        self.theme_switch = ctk.CTkSwitch(self.frame_left, text="Light Mode", command=self.switch_theme, onvalue=1, offvalue=0, progress_color="#7289DA")
        self.theme_switch.pack(pady=20)

        # HOME CRYSTAL INTERFACE
        self.crystal_button = ctk.CTkButton(self.frame_left, text="Crystal Interface", command=self.show_crystal_frame, fg_color="#FF4D4D", hover_color="#FF6666", corner_radius=8)
        self.crystal_button.pack(pady=10, padx=15)

        # Webhook Spammer
        self.webhook_button = ctk.CTkButton(self.frame_left, text="Webhook Spammer", command=self.show_webhook_frame, fg_color="#FF4D4D", hover_color="#FF6666", corner_radius=8)
        self.webhook_button.pack(pady=10, padx=15)

        # Token DMALL
        self.token_button = ctk.CTkButton(self.frame_left, text="Token DMALL", command=self.show_token_frame, fg_color="#FF4D4D", hover_color="#FF6666", corner_radius=8)
        self.token_button.pack(pady=10, padx=15)

        # RAID SERV
        self.raidserv_button = ctk.CTkButton(self.frame_left, text="Raid Serv", command=self.show_raidserv_frame, fg_color="#FF4D4D", hover_color="#FF6666", corner_radius=8)
        self.raidserv_button.pack(pady=10, padx=15)

        # --- Sections --- 
        self.crystal_frame = CrystalFrame(self.frame_right)
        self.webhook_frame = WebhookFrame(self.frame_right)
        self.token_frame = TokenFrame(self.frame_right)
        self.raidserv_frame = RaidservFrame(self.frame_right)
        self.show_crystal_frame()

    def show_crystal_frame(self):
        """Show the Crystal Interface frame."""
        self.crystal_frame.pack(fill="both", expand=True)
        self.webhook_frame.pack_forget()
        self.token_frame.pack_forget()
        self.raidserv_frame.pack_forget()

    def show_webhook_frame(self):
        """Show the Webhook Spammer frame."""
        self.crystal_frame.pack_forget()
        self.webhook_frame.pack(fill="both", expand=True)
        self.token_frame.pack_forget()
        self.raidserv_frame.pack_forget()

    def show_token_frame(self):
        """Show the Token DMALL frame."""
        self.crystal_frame.pack_forget()
        self.webhook_frame.pack_forget()
        self.token_frame.pack(fill="both", expand=True)
        self.raidserv_frame.pack_forget()

    def show_raidserv_frame(self):
        """Show the Raid Serv frame."""
        self.crystal_frame.pack_forget()
        self.webhook_frame.pack_forget()
        self.token_frame.pack_forget()
        self.raidserv_frame.pack(fill="both", expand=True)

    def switch_theme(self):
        if ctk.get_appearance_mode() == "Dark":
            ctk.set_appearance_mode("Light")
        else:
            ctk.set_appearance_mode("Dark")

    def set_window_icon(self, icon_path):
        if os.path.exists(icon_path):
            self.master.iconbitmap(icon_path)
        else:
            print(f"Icon file not found: {icon_path}")

# --- Classe pour la section HOME CRYSTAL---
class CrystalFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(bg_color="#23272A")  

        self.gradient_canvas = ctk.CTkCanvas(self, bg="#2C2F33", highlightthickness=0)
        self.gradient_canvas.pack(fill="both", expand=True)

        self.image_canvas = ctk.CTkCanvas(self.gradient_canvas, bg="#2C2F33", highlightthickness=0)
        self.image_canvas.pack(pady=0) 

        self.load_image(r"C:\Users\flipp\Desktop\crystal\banniere.jpg")

        self.border_frame = ctk.CTkFrame(self.gradient_canvas, bg_color="#2C2F33", border_width=5, border_color="#c00404")
        self.border_frame.pack(padx=10, pady=10, fill="both", expand=True)  

        self.discord_button = ctk.CTkButton(
            self.border_frame,
            text="Join Discord Server",
            command=self.open_discord_server,
            fg_color="#7289DA",
            hover_color="#99A8F7",
            corner_radius=20,
            height=60,
            width=250,
            text_color="#FFFFFF",
            font=("Arial", 14, "bold"),
            border_width=2,
            border_color="#99A8F7",
        )
        self.discord_button.pack(pady=40)

        self.dev_label = ctk.CTkLabel(
            self.border_frame,
            text="Developed by 7sub",
            font=("Arial", 18, "bold"),
            text_color="#FFFFFF"
        )
        self.dev_label.pack(pady=20)

        self.bind("<Configure>", self.on_resize)

    def load_image(self, image_path):
        """Charge et affiche l'image fixe en tant que bannière Discord."""
        try:
            self.image = Image.open(image_path)
            self.image = self.image.resize((564, 188), Image.LANCZOS)  
            self.image_tk = ImageTk.PhotoImage(self.image)
            self.image_canvas.create_image(0, 0, image=self.image_tk, anchor=tk.NW)
        except FileNotFoundError:
            print(f"Erreur : le fichier n'a pas été trouvé à l'emplacement : {image_path}")
        except Exception as e:
            print(f"Une erreur s'est produite lors du chargement de l'image : {e}")

    def update_background_size(self):
        """Redimensionne le fond pour occuper tout l'espace du canvas."""
        width = self.winfo_width() if self.winfo_width() > 0 else 1000
        height = self.winfo_height() if self.winfo_height() > 0 else 1000

        if hasattr(self, 'rect'):
            self.gradient_canvas.delete(self.rect)

        self.rect = self.gradient_canvas.create_rectangle(
            0, 0, width, height, fill="#333333", outline=""
        )

    def on_resize(self, event):
        """Redessine le rectangle lorsque la fenêtre change de taille."""
        self.update_background_size()  

    def open_discord_server(self):
        """Ouvre l'URL du serveur Discord."""
        discord_url = "https://discord.gg/rmfr"
        webbrowser.open(discord_url)



# --- Classe pour la section Webhook Spammer --- 
class WebhookFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.webhook_label = ctk.CTkLabel(self, text="Webhook URL:", font=("Arial", 16))
        self.webhook_label.pack(pady=10)

        self.webhook_entry = ctk.CTkEntry(self, width=400, height=40, placeholder_text="Enter Webhook URL")
        self.webhook_entry.pack(pady=10)

        self.message_label = ctk.CTkLabel(self, text="Message to send:", font=("Arial", 16))
        self.message_label.pack(pady=10)

        self.message_entry = ctk.CTkEntry(self, width=400, height=40, placeholder_text="Your message here")
        self.message_entry.pack(pady=10)

        self.everyone_checkbox = ctk.CTkCheckBox(self, text="Mention @everyone")
        self.everyone_checkbox.pack(pady=10)

        self.repetition_label = ctk.CTkLabel(self, text="Number of shipments:", font=("Arial", 16))
        self.repetition_label.pack(pady=10)

        self.repetition_entry = ctk.CTkEntry(self, width=100, height=30, placeholder_text="1")
        self.repetition_entry.pack(pady=10)

        self.send_button = ctk.CTkButton(self, text="Send", command=self.send_message, width=200, fg_color="#B22222", hover_color="#FF6666")
        self.send_button.pack(pady=20)

        self.webhook_info_button = ctk.CTkButton(self, text="Get Webhook Info", command=self.get_webhook_info, width=200, fg_color="#02A9CB", hover_color="#0C758A")
        self.webhook_info_button.pack(pady=10)

        self.result_label = ctk.CTkLabel(self, text="", font=("Arial", 14))
        self.result_label.pack(pady=10)

    def send_message(self):
        webhook_url = self.webhook_entry.get()
        message = self.message_entry.get()
        mention_everyone = self.everyone_checkbox.get()
        repetition = self.repetition_entry.get()

        if not webhook_url:
            self.result_label.configure(text="❌ Webhook URL cannot be empty!", text_color="red")
            return

        if message:
            try:
                repetition_count = int(repetition)
                if repetition_count < 1:
                    raise ValueError
            except ValueError:
                self.result_label.configure(text="❌ Invalid repetition count!", text_color="red")
                return

            send_thread = threading.Thread(target=send_messages_in_thread, args=(webhook_url, message, mention_everyone, repetition_count, self.result_label))
            send_thread.start()
        else:
            self.result_label.configure(text="❌ Message cannot be empty!", text_color="red")

    def get_webhook_info(self):
        webhook_url = self.webhook_entry.get()
        if not webhook_url:
            messagebox.showwarning("Warning", "Please enter a webhook URL.")
            return

        try:
            headers = {'Content-Type': 'application/json'}
            response = requests.get(webhook_url, headers=headers)
            webhook_info = response.json()

            if response.status_code == 200:
                self.display_webhook_info(webhook_info)
                self.copy_to_clipboard(webhook_info)
            else:
                messagebox.showerror("Error", f"Failed to fetch webhook info: {response.status_code} - {response.text}")
        
        except Exception as e:
            messagebox.showerror("Error", f"Failed to fetch webhook info: {e}")

    def display_webhook_info(self, webhook_info):
        webhook_id = webhook_info.get('id', "None")
        webhook_token = webhook_info.get('token', "None")
        webhook_name = webhook_info.get('name', "None")
        webhook_avatar = webhook_info.get('avatar', "None")
        webhook_type = "Bot" if webhook_info.get('type') == 1 else "User Webhook"
        channel_id = webhook_info.get('channel_id', "None")
        guild_id = webhook_info.get('guild_id', "None")

        info_text = f"""
        ID: {webhook_id}
        Token: {webhook_token}
        Name: {webhook_name}
        Avatar: {webhook_avatar}
        Type: {webhook_type}
        Channel ID: {channel_id}
        Server ID: {guild_id}
        """

        messagebox.showinfo("Webhook Info", info_text)

    def copy_to_clipboard(self, webhook_info):
        webhook_id = webhook_info.get('id', "None")
        webhook_token = webhook_info.get('token', "None")
        webhook_name = webhook_info.get('name', "None")
        webhook_avatar = webhook_info.get('avatar', "None")
        webhook_type = "Bot" if webhook_info.get('type') == 1 else "User Webhook"
        channel_id = webhook_info.get('channel_id', "None")
        guild_id = webhook_info.get('guild_id', "None")

        info_text = f"""
        ID: {webhook_id}
        Token: {webhook_token}
        Name: {webhook_name}
        Avatar: {webhook_avatar}
        Type: {webhook_type}
        Channel ID: {channel_id}
        Server ID: {guild_id}
        """

        self.master.clipboard_clear()
        self.master.clipboard_append(info_text)
        messagebox.showinfo("Info", "Webhook info copied to clipboard!")


# --- Classe pour la section Tokens ---
class TokenFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.token_label = ctk.CTkLabel(self, text="Enter Discord token:", font=("Arial", 16))
        self.token_label.pack(pady=10)

        self.token_entry = ctk.CTkEntry(self, width=400, height=40, placeholder_text="Your Discord token here")
        self.token_entry.pack(pady=10)

        self.send_pub_button = ctk.CTkButton(self, text="Send the message", command=self.start_discord_bot, width=200, fg_color="#B22222", hover_color="#FF6666")
        self.send_pub_button.pack(pady=20)

        self.pub_message_label = ctk.CTkLabel(self, text="Message details:", font=("Arial", 16))
        self.pub_message_label.pack(pady=10)

        self.pub_message_entry = ctk.CTkEntry(self, width=400, height=40, placeholder_text="Your message")
        self.pub_message_entry.pack(pady=10)

        self.ping_var = ctk.BooleanVar()
        self.ping_checkbox = ctk.CTkCheckBox(self, text="Enable user ping", variable=self.ping_var)
        self.ping_checkbox.pack(pady=10)

        self.token_info_button = ctk.CTkButton(self, text="Token Info", command=self.token_info, width=200, fg_color="#4682B4", hover_color="#87CEEB")
        self.token_info_button.pack(pady=10)

        result_frame = ctk.CTkFrame(self)
        result_frame.pack(pady=10, fill="both", expand=True)

        self.result_textbox = ctk.CTkTextbox(result_frame, width=500, height=300, wrap="none", font=("Courier", 12))
        self.result_textbox.pack(side="left", fill="both", expand=True)

        scrollbar = ctk.CTkScrollbar(result_frame, command=self.result_textbox.yview)
        scrollbar.pack(side="right", fill="y")

        self.result_textbox.configure(yscrollcommand=scrollbar.set)

        self.bot_thread = None

    def start_discord_bot(self):
        token = self.token_entry.get()
        pub_message = self.pub_message_entry.get()

        if not token or not pub_message:
            self.result_textbox.configure(state="normal")
            self.result_textbox.insert("end", "❌ Missing token or message!\n", "error")
            self.result_textbox.configure(state="disabled")
            return

        self.bot_thread = threading.Thread(target=self.run_discord_bot, args=(token, pub_message))
        self.bot_thread.start()

    def run_discord_bot(self, token, pub_message):
        bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

        @bot.event
        async def on_ready():
            self.result_textbox.configure(state="normal")
            self.result_textbox.insert("end", f"Logged in as {bot.user.name}\n", "info")
            await self.send_advertisement(bot, pub_message)
            self.result_textbox.configure(state="disabled")

        try:
            bot.run(token)
        except Exception as e:
            self.result_textbox.configure(state="normal")
            self.result_textbox.insert("end", f"Error while connecting: {e}\n", "error")
            self.result_textbox.configure(state="disabled")

    async def send_advertisement(self, bot, message):
        for guild in bot.guilds:
            for member in guild.members:
                if not member.bot:
                    try:
                        if self.ping_var.get():
                            await member.send(f'{member.mention} {message}')
                        else:
                            await member.send(message)

                        self.result_textbox.configure(state="normal")
                        self.result_textbox.insert("end", f"Message sent to {member.name} (ID: {member.id})\n", "info")
                        self.result_textbox.configure(state="disabled")

                    except discord.Forbidden:
                        self.result_textbox.configure(state="normal")
                        self.result_textbox.insert("end", f"❌ Could not send message to {member.name} (ID: {member.id})\n", "error")
                        self.result_textbox.configure(state="disabled")

        self.result_textbox.configure(state="normal")
        self.result_textbox.insert("end", "Message sent to all servers!\n", "info")
        self.result_textbox.configure(state="disabled")

    def token_info(self):
        token = self.token_entry.get()

        if not token:
            self.result_textbox.configure(state="normal")
            self.result_textbox.insert("end", "❌ Missing token!\n", "error")
            self.result_textbox.configure(state="disabled")
            return

        self.bot_thread = threading.Thread(target=self.run_token_info, args=(token,))
        self.bot_thread.start()

    def run_token_info(self, token):
        bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

        @bot.event
        async def on_ready():
            self.result_textbox.configure(state="normal")
            self.result_textbox.delete("1.0", "end") 
            self.result_textbox.insert("end", "Fetching information...\n", "info")
            self.result_textbox.configure(state="disabled")

            time.sleep(1) 

            info_text = "Bot Information\n"
            info_text += f"Logged in as: {bot.user.name} (ID: {bot.user.id})\n"
            info_text += f"Avatar URL: {bot.user.display_avatar.url}\n\n"
            info_text += "Servers Connected:\n"

            for guild in bot.guilds:
                info_text += f"- {guild.name} (ID: {guild.id}) — {guild.member_count} members\n"

            info_text += "\n" + "-" * 50 + "\n"

            self.result_textbox.configure(state="normal")
            self.result_textbox.delete("1.0", "end")
            self.result_textbox.insert("end", info_text, "info")
            self.result_textbox.configure(state="disabled")

            await bot.close()

        try:
            bot.run(token)
        except discord.errors.LoginFailure:
            self.result_textbox.configure(state="normal")
            self.result_textbox.insert("end", "❌ Invalid token! Please check your token.\n", "error")
            self.result_textbox.configure(state="disabled")
        except Exception as e:
            self.result_textbox.configure(state="normal")
            self.result_textbox.insert("end", f"❌ Error: {e}\n", "error")
            self.result_textbox.configure(state="disabled")


# --- Classe pour la section Raid Serv ---
class RaidservFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.configure(fg_color="#2C2F33") 

        self.title_label = ctk.CTkLabel(self, text="RAID BOT", font=("Arial", 24), text_color="#FFFFFF")
        self.title_label.pack(pady=20)

        self.token_label = ctk.CTkLabel(self, text="Discord Token:", font=("Arial", 16), text_color="#FFFFFF")
        self.token_label.pack(pady=(10, 0))

        self.token_entry = ctk.CTkEntry(self, width=400, height=40, placeholder_text="enter discord token here")
        self.token_entry.pack(pady=(0, 10))

        self.server_ids_label = ctk.CTkLabel(self, text="Enter Server ID exemple (11946, 14872):", font=("Arial", 16), text_color="#FFFFFF")
        self.server_ids_label.pack(pady=(10, 0))

        self.server_ids_entry = ctk.CTkEntry(self, width=400, height=40, placeholder_text="server ID here")
        self.server_ids_entry.pack(pady=(0, 10))

        separator = tk.Frame(self, height=2, bg="#FFFFFF")
        separator.pack(fill='x', pady=15)

        self.button_frame = ctk.CTkFrame(self, fg_color="#2C2F33")
        self.button_frame.pack(pady=(10, 20))

        self.create_button("Token Info", self.token_info)
        self.create_button("Delete All Channels", self.delete_channels)
        self.create_button("Create Channels", self.create_channels)
        self.create_button("Spam Messages in All Channels", self.spam_messages)
        self.create_button("Kick All Members", self.kick_all_members)
        self.create_button("Ban All Members", self.ban_all_members)

        separator2 = tk.Frame(self, height=2, bg="#FFFFFF")
        separator2.pack(fill='x', pady=15)

        self.channel_count_entry = self.create_entry_with_label("Number of channels to create:", "Enter number")
        self.message_entry = self.create_entry_with_label("Message to spam:", "Your message")
        self.spam_message_count_entry = self.create_entry_with_label("Number of messages to send:", "Enter number")

        self.result_label = ctk.CTkLabel(self, text="", font=("Arial", 14), text_color="#FFFFFF")
        self.result_label.pack(pady=10)

        self.bot_thread = None

    def create_button(self, text, command):
        button = ctk.CTkButton(self.button_frame, text=text, command=command, width=150, fg_color="#4682B4", hover_color="#87CEEB")
        button.pack(side=tk.LEFT, padx=5) 


    def create_entry_with_label(self, label_text, placeholder_text):
        label = ctk.CTkLabel(self, text=label_text, font=("Arial", 16), text_color="#FFFFFF")
        label.pack(pady=(10, 0))
        
        entry = ctk.CTkEntry(self, width=100, height=30, placeholder_text=placeholder_text)
        entry.pack(pady=(0, 10))
        
        return entry

    def start_discord_bot(self, target_func):
        token = self.token_entry.get()
        server_ids = self.server_ids_entry.get().split(',')

        if not token:
            self.result_label.configure(text="❌ Missing token!", text_color="red")
            return

        server_ids = [id.strip() for id in server_ids if id.strip()]

        if not server_ids:
            server_ids = None 

        self.bot_thread = threading.Thread(target=target_func, args=(token, server_ids))
        self.bot_thread.start()

    def token_info(self):
        self.start_discord_bot(self.run_token_info)

    def delete_channels(self):
        self.start_discord_bot(self.run_delete_channels)

    def create_channels(self):
        self.start_discord_bot(self.run_create_channels)

    def spam_messages(self):
        self.start_discord_bot(self.run_spam_messages)

    def kick_all_members(self):
        self.start_discord_bot(self.run_kick_all_members)

    def ban_all_members(self):
        self.start_discord_bot(self.run_ban_all_members)

    def run_token_info(self, token, server_ids):
        bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

        @bot.event
        async def on_ready():
            info_text = f"✅ Logged in as {bot.user.name}\n"
            info_text += "Servers connected to:\n"

            server_info_list = []

            for guild in bot.guilds:
                if server_ids is None or str(guild.id) in server_ids:
                    server_info = f"Server: {guild.name} (ID: {guild.id}), Members: {guild.member_count}\n"
                    server_info_list.append(server_info)
                    info_text += server_info

            with open("server_info.txt", "w", encoding="utf-8") as file:
                file.write(info_text)

            self.result_label.configure(text=f"✅ Server information saved in 'server_info.txt'", text_color="#ffffff")

            await bot.close()

        try:
            bot.run(token)
        except Exception as e:
            self.result_label.configure(text=f"❌ Error: {e}", text_color="red")

    def run_delete_channels(self, token, server_ids):
        bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

        @bot.event
        async def on_ready():
            self.result_label.configure(text=f"✅ Logged in as {bot.user.name}", text_color="green")

            for guild in bot.guilds:
                if server_ids is None or str(guild.id) in server_ids:
                    for channel in guild.channels:
                        try:
                            await channel.delete()
                            print(f"Deleted channel: {channel.name}")
                        except discord.Forbidden:
                            print(f"Permission denied for deleting {channel.name}")
                            continue

            await bot.close()

        try:
            bot.run(token)
        except Exception as e:
            self.result_label.configure(text=f"❌ Error: {e}", text_color="red")

    def run_create_channels(self, token, server_ids):
        bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

        @bot.event
        async def on_ready():
            self.result_label.configure(text=f"✅ Logged in as {bot.user.name}", text_color="green")

            try:
                channel_count = int(self.channel_count_entry.get())
                if channel_count <= 0:
                    raise ValueError("Invalid number of channels")

                for guild in bot.guilds:
                    if server_ids is None or str(guild.id) in server_ids:
                        for i in range(channel_count):
                            await guild.create_text_channel(f"raid by 7sub")
                            print(f"Created channel: raid by 7sub")

            except ValueError as e:
                self.result_label.configure(text=f"❌ {e}", text_color="red")

            await bot.close()

        try:
            bot.run(token)
        except Exception as e:
            self.result_label.configure(text=f"❌ Error: {e}", text_color="red")

    def run_spam_messages(self, token, server_ids):
        bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

        @bot.event
        async def on_ready():
            self.result_label.configure(text=f"✅ Logged in as {bot.user.name}", text_color="green")
            spam_message = self.message_entry.get()

            if not spam_message:
                self.result_label.configure(text="❌ Message cannot be empty!", text_color="red")
                return

            try:
                spam_count = int(self.spam_message_count_entry.get())
                if spam_count <= 0:
                    raise ValueError("Invalid number of messages")

                for guild in bot.guilds:
                    if server_ids is None or str(guild.id) in server_ids:
                        for channel in guild.text_channels:
                            for _ in range(spam_count):
                                await channel.send(spam_message)
                                print(f"Spammed in {channel.name}")

            except ValueError as e:
                self.result_label.configure(text=f"❌ {e}", text_color="red")

            await bot.close()

        try:
            bot.run(token)
        except Exception as e:
            self.result_label.configure(text=f"❌ Error: {e}", text_color="red")

    def run_kick_all_members(self, token, server_ids):
        bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

        @bot.event
        async def on_ready():
            self.result_label.configure(text=f"✅ Logged in as {bot.user.name}", text_color="green")

            for guild in bot.guilds:
                if server_ids is None or str(guild.id) in server_ids:
                    for member in guild.members:
                        try:
                            await member.kick(reason="Kicked by bot command.")
                            print(f"Kicked {member.name} from {guild.name}")
                        except discord.Forbidden:
                            print(f"Permission denied for kicking {member.name}")
                            continue

            await bot.close()

        try:
            bot.run(token)
        except Exception as e:
            self.result_label.configure(text=f"❌ Error: {e}", text_color="red")

    def run_ban_all_members(self, token, server_ids):
        bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

        @bot.event
        async def on_ready():
            self.result_label.configure(text=f"✅ Logged in as {bot.user.name}", text_color="green")

            for guild in bot.guilds:
                if server_ids is None or str(guild.id) in server_ids:
                    for member in guild.members:
                        try:
                            await member.ban(reason="Banned by bot command.")
                            print(f"Banned {member.name} from {guild.name}")
                        except discord.Forbidden:
                            print(f"Permission denied for banning {member.name}")
                            continue

            await bot.close()

        try:
            bot.run(token)
        except Exception as e:
            self.result_label.configure(text=f"❌ Error: {e}", text_color="red")

if __name__ == "__main__":
    root = ctk.CTk()
    app = MainApp(root)
    root.mainloop()
