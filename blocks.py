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
	],
	'survey_block': [
		{
			"type": "divider"
		},
		{
			"type": "header",
			"text": {
				"type": "plain_text",
				"text": "Monthly Employee Vibe Check 😎",
				"emoji": True
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "How are you today? 🥴"
			},
			"accessory": {
				"type": "radio_buttons",
				"options": [
					{
						"text": {
							"type": "plain_text",
							"text": "⭐️",
							"emoji": True
						},
						"value": "1"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "⭐️⭐️",
							"emoji": True
						},
						"value": "2"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "⭐️⭐️⭐️",
							"emoji": True
						},
						"value": "3"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "⭐️⭐️⭐️⭐️",
							"emoji": True
						},
						"value": "4"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "⭐️⭐️⭐️⭐️⭐️",
							"emoji": True
						},
						"value": "5"
					}
				],
				"action_id": "radio_buttons-action"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "How well supported do you feel at work? 🤒"
			},
			"accessory": {
				"type": "radio_buttons",
				"options": [
					{
						"text": {
							"type": "plain_text",
							"text": "⭐️",
							"emoji": True
						},
						"value": "1"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "⭐️⭐️",
							"emoji": True
						},
						"value": "2"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "⭐️⭐️⭐️",
							"emoji": True
						},
						"value": "3"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "⭐️⭐️⭐️⭐️",
							"emoji": True
						},
						"value": "4"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "⭐️⭐️⭐️⭐️⭐️",
							"emoji": True
						},
						"value": "5"
					}
				],
				"action_id": "radio_buttons-action"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "How diverse and inclusive do you feel the company is? 😜"
			},
			"accessory": {
				"type": "radio_buttons",
				"options": [
					{
						"text": {
							"type": "plain_text",
							"text": "⭐️",
							"emoji": True
						},
						"value": "1"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "⭐️⭐️",
							"emoji": True
						},
						"value": "2"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "⭐️⭐️⭐️",
							"emoji": True
						},
						"value": "3"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "⭐️⭐️⭐️⭐️",
							"emoji": True
						},
						"value": "4"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "⭐️⭐️⭐️⭐️⭐️",
							"emoji": True
						},
						"value": "5"
					}
				],
				"action_id": "radio_buttons-action"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "How satisfied are you with the company's leadership? 🥸"
			},
			"accessory": {
				"type": "radio_buttons",
				"options": [
					{
						"text": {
							"type": "plain_text",
							"text": "⭐️",
							"emoji": True
						},
						"value": "1"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "⭐️⭐️",
							"emoji": True
						},
						"value": "2"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "⭐️⭐️⭐️",
							"emoji": True
						},
						"value": "3"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "⭐️⭐️⭐️⭐️",
							"emoji": True
						},
						"value": "4"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "⭐️⭐️⭐️⭐️⭐️",
							"emoji": True
						},
						"value": "5"
					}
				],
				"action_id": "radio_buttons-action"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "How connected to your co-workers do you feel? 🥰"
			},
			"accessory": {
				"type": "radio_buttons",
				"options": [
					{
						"text": {
							"type": "plain_text",
							"text": "⭐️",
							"emoji": True
						},
						"value": "1"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "⭐️⭐️",
							"emoji": True
						},
						"value": "2"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "⭐️⭐️⭐️",
							"emoji": True
						},
						"value": "3"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "⭐️⭐️⭐️⭐️",
							"emoji": True
						},
						"value": "4"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "⭐️⭐️⭐️⭐️⭐️",
							"emoji": True
						},
						"value": "5"
					}
				],
				"action_id": "radio_buttons-action"
			}
		}
		
	],
	'short_survey': [
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "How are you today? 🥴"
			},
			"accessory": {
				"type": "radio_buttons",
				"options": [
					{
						"text": {
							"type": "plain_text",
							"text": "⭐️",
							"emoji": True
						},
						"value": "1"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "⭐️⭐️",
							"emoji": True
						},
						"value": "2"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "⭐️⭐️⭐️",
							"emoji": True
						},
						"value": "3"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "⭐️⭐️⭐️⭐️",
							"emoji": True
						},
						"value": "4"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "⭐️⭐️⭐️⭐️⭐️",
							"emoji": True
						},
						"value": "5"
					}
				],
				"action_id": "radio_buttons-action"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "How connected to your co-workers do you feel? 🥰"
			},
			"accessory": {
				"type": "radio_buttons",
				"options": [
					{
						"text": {
							"type": "plain_text",
							"text": "⭐️",
							"emoji": True
						},
						"value": "1"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "⭐️⭐️",
							"emoji": True
						},
						"value": "2"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "⭐️⭐️⭐️",
							"emoji": True
						},
						"value": "3"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "⭐️⭐️⭐️⭐️",
							"emoji": True
						},
						"value": "4"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "⭐️⭐️⭐️⭐️⭐️",
							"emoji": True
						},
						"value": "5"
					}
				],
				"action_id": "radio_buttons-action"
			}
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