block_dict = {
	"sample_block": [
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "This is a section block with a button."
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Click Me"
				},
				"value": "click_me_123",
				"action_id": "button"
			}
		},
		{
			"type": "actions",
			"block_id": "actionblock789",
			"elements": [
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "Primary Button"
					},
					"style": "primary",
					"value": "click_me_456"
				},
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "Link Button"
					},
					"url": "https://api.slack.com/block-kit"
				}
			]
		}
	]
}