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

message_to_send = { "blocks": [
        {
            "type": "input",
            "element": {
                    "type": "radio_buttons",
                    "options": [
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "*this is plain_text text*",
                                            "emoji": True
                                },
                                "value": "value-0"
                            },
                        {
                                "text": {
                                    "type": "plain_text",
                                    "text": "*this is plain_text text*",
                                            "emoji": True
                                },
                                "value": "value-1"
                                },
                        {
                                "text": {
                                    "type": "plain_text",
                                    "text": "*this is plain_text text*",
                                            "emoji": True
                                },
                                "value": "value-2"
                                }
                    ],
                "action_id": "radio_buttons-action"
            },
            "label": {
                "type": "plain_text",
                "text": "HOW DO YOU FEEL ABOUT COMPANY CULTURE",
                "emoji": True
            }
        }
    ]}