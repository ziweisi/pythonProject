import boto3

athena = boto3.client('athena')

response = athena.list_query_executions(
    WorkGroup='primary'
    # 指定 工作组 默认是 primary 您在控制台上可以查看到
)

queryIds = []  # 准备一个list 用来存放 查询该workgroup 中所有的查询id
while response:
    queryIds += response['QueryExecutionIds']  # 将查询id 存放在准备好的ist中
    # print(response['QueryExecutionIds']) # 550
    # print(response['NextToken'])
    # print(response)
    if 'NextToken' not in response.keys():  # 判断循环终止条件
        break
    response = athena.list_query_executions(NextToken=response['NextToken'])  # 分页查询的token
print(len(queryIds))  # 验证是否 正确

for queryId in queryIds:
    query_Executions = athena.get_query_execution(QueryExecutionId=queryId)  # 该方法看可以通过查询id 获取到执行情况
    print(query_Executions)  # 打印执行查询执行情况
