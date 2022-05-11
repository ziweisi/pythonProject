import boto3
client = boto3.client('emr')
response = client.add_job_flow_steps(
    # 集群ID The cluster id and job flow id are the same thing (j-######).
    # A cluster id is a more appropriate name to its purpose as to not be confused with the terminology of a job as
    # seen with Hadoop. So go ahead and use ListClusters
    JobFlowId='',
    Steps=[
        {
            'Name': 'string',
            'ActionOnFailure': 'TERMINATE_JOB_FLOW',
            'HadoopJarStep': {
                'Properties': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ],
                'Jar': 'string',
                'MainClass': 'string',
                'Args': [
                    'string',
                ]
            }
        },
        {
            'Name': 'string',
            'ActionOnFailure': 'TERMINATE_JOB_FLOW',
            'HadoopJarStep': {
                'Properties': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ],
                'Jar': 'string',
                'MainClass': 'string',
                'Args': [
                    'string',
                ]
            }
        }
    ])
