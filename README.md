# Social-Good-Hackathon

Welcome to our project for the Robinhood Social Good Hackathon! We developed a Slack bot app that functions as a corporate governance tool, providing an interface for employees to give anonymous feedback for big decisions that executives are considering. This helps bridge the gap between higher-level decision making and employees lower in the management hierarchy whose input might not otherwise be considered. This tool would help executives get input from the whole company to help inform their decisions. It would also give transparency into upcoming decisions, and the company’s general feel about them.


## Environment Setup: 
You will need to setup Bolt Python following these steps: https://api.slack.com/start/building/bolt-python. Note that the bot does not currently use Bolt, except for defining some event listeners that are unused at the moment, but we will need it in the future for sending scheduled/automated messages. `SLACK_BOT_TOKEN`,`SLACK_SIGNING_SECRET`, AND `SLACK_APP_TOKEN` are in the Google Doc as well as a gitignore `slack_tokens.json` file. Do not publish them here in case the repository is made public.

You can run the bot from `app.py`. `blocks.py` is meant to declare the blocks that we will be using.