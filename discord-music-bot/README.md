# Discord Music Bot

This project is a Discord music bot built using Python. It allows users to play music in voice channels, providing commands to control playback.

## Project Structure

```
discord-music-bot
├── src
│   ├── bot.py          # Main entry point for the bot, initializes the Discord client and sets up event handlers.
│   ├── music
│   │   └── player.py   # Defines the MusicPlayer class with methods to control music playback.
│   └── utils
│       └── helpers.py  # Contains helper functions for music-related operations.
├── requirements.txt     # Lists the required Python packages for the project.
├── README.md            # Documentation for setting up and using the music bot.
└── .env                 # Stores environment variables such as the Discord bot token and other configurations.
```

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/discord-music-bot.git
   cd discord-music-bot
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up your environment variables in the `.env` file:
   ```
   DISCORD_TOKEN=your_discord_token
   ```

## Usage

1. Run the bot:
   ```
   python src/bot.py
   ```

2. Invite the bot to your Discord server and use commands to control music playback.

## Commands

- `!play <song_url>`: Play a song from a URL.
- `!pause`: Pause the current song.
- `!stop`: Stop the music playback.
- `!skip`: Skip to the next song in the queue.

## Contributing

Feel free to submit issues or pull requests to improve the bot!