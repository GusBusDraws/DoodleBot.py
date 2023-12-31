import praw
from dotenv import load_dotenv
import os
from pathlib import Path
# Local imports
from doodlebot import DoodleBot

def process_args(message: str):
    return args

def get_prompt_reply(args):
    if len(args) == 0:
        response = doodle_state.get_help()
    else:
        doodle_state.last_arg_tuple = args
        result = doodle_state.get_prompt(args)
        response = f"Here's your prompt:\n{result}"
    return response

if __name__ == '__main__':
    doodle_state = DoodleBot()
    load_dotenv()
    client_id = os.getenv('REDDIT_CLIENT_ID')
    client_secret = os.getenv('REDDIT_SECRET')
    password = os.getenv('REDDIT_PASSWORD')
    user_agent = "DoodleBot v1.0 /u/DoodleBotPrompts"
    username = "DoodleBotPrompts"
    reddit = praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        password=password,
        user_agent=user_agent,
        username=username,
    )
    subreddit = reddit.subreddit("DoodleBot")
    print('Connected to', subreddit.display_name)
    # Iterate through the comments from subreddit as new ones are coming in
    for comment in subreddit.stream.comments(skip_existing=True):
        try:
            # Look for "!prompt" at beginning of comment
            if (
                comment.body.startswith("!prompt")
                and comment.author != username
            ):
                print(f'{comment.author=}')
                print(f'{comment.body=}')
                args = comment.body.split(' ')[1:]
                response = get_prompt_reply(args)
                # Bot reply to the comment with "!prompt"
                print(f'{response=}')
                comment.reply(response)
        # Reddit may have rate limits, this prevents bot from dying due to
        # rate limits
        except praw.exceptions.APIException:
            print("probably a rate limit...")
