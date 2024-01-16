
tools_topic = [{
	'name': 'TopicClassifier',
	'description': '用户问题的相关主题分类',
	'parameters': {
		'description': '主题分类分别为政策咨询、招投标相关、公司查询、商品查询、其他或者不知道',
		'properties': {
			'topic': {
				'enum': ['政策咨询', '招投标相关', '公司查询', '商品查询', '其他', '不知道'],
				'title': 'Topic',
				'type': 'string'
			}
		},
		'required': ['topic'],
		'title': 'TopicClassifier',
		'type': 'object'
	}
}]

system_item_toptic = {
    "role": "system",
    #"content": "尽可能地回答以下问题。如果主题中没有涉及政策咨询、招投标相关、公司查询、商品查询或其他的主题，请继续根据当前得到的主题继续分类，直到得到目标主题。您可以访问以下工具（Answer the following questions as much as possible. If the topic does not involve policy consultation, bidding related, company inquiry, product inquiry, or other topics, please continue to classify based on the currently obtained topic until the target topic is obtained. You can access the following tools）:",
    "content": "尽可能地回答以下问题。\n如果主题中没有涉及‘政策咨询’、‘招投标相关’、‘公司查询’、‘商品查询’或者‘其他’的主题，请继续根据当前得到的信息继续进行主题分类，直到得到目标主题。\n如果多不循环分类出现相同的主题，则停止分类，如果最终的不能得到主题请回答‘不知道’。\n请务必使用以下工具。\n\nYou have access to the following tools:\n\n:",
	"tools": tools_topic}

