# DoodleBot
DoodleBot is a bot for generating drawing prompts! You can interact with
this bot in the [Doodle Crew! Discord server](https://discord.gg/kttkrUsk3Z)
or on [r/DoodleBot](https://reddit.com/r/DoodleBot).

## Usage
To use this bot on either platform, send a message or post a comment
beginning with "!prompt" which includes at least one of the keywords listed
in [keywords.json](keywords.json) with a leading "%". These keywords include:

- animal
- creature
- class
- food
- item
- material

Many of the keywords (like "class", "creature", and "item") can also be modified with "fantasy-", "scifi-",
or "irl-".

For a full list of keywords that can be used, you can pass "!prompt" without anything after it.

## Discord Commands
- `!list`
- `!prompt`
- `!reroll`
- `!suggest`

## Reddit Commands
- `!prompt`

## Change log
### 2024-07-25
- Add keywords: clothing, headwear, upper-torso-clothing, lower-torso-clothing, footwear
### 2024-06-21
- Fixed error when keyword not found in database
### 2023-10-18
- Add "!list" command to bot_discord.py for assessing keyword database
- Add "!suggest" command to bot_discord.py for populating suggestions.json
### 2023-10-16
- Update 'item' and 'location' keywords to include 'any-' to avoid premature
key matches
### 2023-10-11
- Only check for "!prompt" at beginning of message
- Add Reddit bot
- Move core DoodleBot functionality to separate file/class
- Add "field-of-study" to keywords
- Change "sci-fi" to "scifi"
- Split food into "food-items" and "food-materials"
- Update "food", "items", and "materials"
### 2023-10-10
- Load keywords from JSON instead of CSV
- Update keyword bank
- Add location keywords
- Handle a/an as first word in prompts
- Handle punctuation in prompts

