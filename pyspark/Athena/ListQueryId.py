import boto3

athena = boto3.client('athena')

response = athena.list_query_executions(
    WorkGroup='primary' #指定 工作组 默认是 perimary 您在控制台上可以查看到
)

queryIds = [] # 准备一个list 用来存放 查询该workgroup 中所有的查询id
while response :
    queryIds += response['QueryExecutionIds'] #将查询id 存放在准备好的ist中
    # print(response['QueryExecutionIds']) # 550
    # print(response['NextToken'])
    # print(response)
    if 'NextToken' not in response.keys(): # 判断循环终止条件
        break
    response = athena.list_query_executions(NextToken=response['NextToken']) # 分页查询的token
print(len(queryIds)) # 验证是否 正确

for queryId in queryIds :
    query_Executions = athena.get_query_execution(QueryExecutionId=queryId) # 该方法看可以通过查询id 获取到执行情况
    print(query_Executions) # 打印执行查询执行情况


# 将其根据您需求将其保存在指定格式的文件中 即可进行分析
# 以下为我做测试的打印结果，结果如下
# {'QueryExecution':
# {'QueryExecutionId': '42a07bd8-0556-4f97-9905-e514a01582d2',
#   'Query': 'select count("_id") count from "glue101"."etl_etl" limit 10',
#   'StatementType': 'DML',
#   'ResultConfiguration':
#   {'OutputLocation': 's3://emr-test-01/athena_result/Unsaved/2022/05/11/42a07bd8-0556-4f97-9905-e514a01582d2.csv'},
#   'QueryExecutionContext': {'Database': 'athenadb', 'Catalog': 'awsdatacatalog'},
#   'Status':
#   {'State': 'SUCCEEDED',
#   'SubmissionDateTime': datetime.datetime(2022, 5, 11, 17, 25, 15, 365000, tzinfo=tzlocal()),
#   'CompletionDateTime': datetime.datetime(2022, 5, 11, 17, 25, 16, 92000, tzinfo=tzlocal())},
#   'Statistics': {'EngineExecutionTimeInMillis': 548,
#   'DataScannedInBytes': 3239090, 'TotalExecutionTimeInMillis': 727,
#   'QueryQueueTimeInMillis': 158, 'QueryPlanningTimeInMillis': 58, 'ServiceProcessingTimeInMillis': 21},
#   'WorkGroup': 'primary', 'EngineVersion': {'SelectedEngineVersion':
#   'AUTO', 'EffectiveEngineVersion': 'Athena engine version 2'}},
#   'ResponseMetadata':
#   {'RequestId': '9f7a3b70-c8b2-4280-80b4-efbdeaf4a0d0', 'HTTPStatusCode': 200, 'HTTPHeaders': {'content-type': 'application/x-amz-json-1.1', 'date': 'Wed, 11 May 2022 12:36:19 GMT', 'x-amzn-requestid': '9f7a3b70-c8b2-4280-80b4-efbdeaf4a0d0', 'content-length': '1577', 'connection': 'keep-alive'}, 'RetryAttempts': 0}}
# 准备了很多

