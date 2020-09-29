[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

# among-us-bot for discord
This is a custom discord bot I designed for Among Us game. You can host your own bot for your server.

## Getting Started
1. Generate a **token** for your bot and paste it in *token.txt*.
2. Create a **role** in your server so that the person with **this role** can only use the commands.
3. Create a Voice Channel where the people will be connected during the game.
4. Copy the IDs of role and Voice Channel and paste in `cogs/amongus.py` `needed_role` `voice_channel` attributes respectively.
5. Run `bot.py` to make your bot online.
6. Use `!help` command in the server to get the commands.

**Note :** 
1. `!start` will be used after the meetings.
2. Member declared dead using `!dead @member` will remain unmuted during the meeting. 


#### Feel free to add changes :)
