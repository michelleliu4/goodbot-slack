# Social-Good-Hackathon

You're looking at the repository of the best team

Environment Setup: 

You will need to setup Bolt Python following these steps: https://api.slack.com/start/building/bolt-python. Note that the bot does not currently use Bolt, except for defining some event listeners that are unused at the moment, but we will need it in the future for sending scheduled/automated messages. Also note that the `SLACK_BOT_TOKEN` and `SLACK_SIGNING_SECRET` are in the google doc. Do not put them here as when we make this repo public in the future, ppl will be able to find these secret tokens by looking through its history

You can run the bot from `app.py`. So far all it does on run is send a sample block. `blocks.py` is meant to declare the blocks that we will be using. So far there is just one set of blocks, `sample_block`, which I stole from the BlockKit documentation
