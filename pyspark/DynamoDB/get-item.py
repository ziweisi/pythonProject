

import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Music')
response = table.get_item(
    Key={
        "Artist": "No One You Know",
        "SongTitle": "Howdy"
    }
)
# 获取字段item
item = response['Item']

# 打印出item 值
print(item)
# 打印出结果为： {'AlbumTitle': 'Somewhat Famous', 'Awards': '2', 'Artist': 'No One You Know', 'SongTitle': 'Howdy'}

# 获取所有项目的所有属性的值
print(list(item.keys()))
# 打印出结果为：['AlbumTitle', 'Awards', 'Artist', 'SongTitle']

