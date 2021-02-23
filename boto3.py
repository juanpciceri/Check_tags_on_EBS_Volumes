import boto3
def lambda_handler(event, context):
    ec2 = boto3.resource('ec2')
    volume_iterator = ec2.volumes.all()
    name = None
    for v in volume_iterator:
        
        keys=[]
        if v.tags is not None:
            for tag in v.tags:
        
                h=tag['Key']
                keys.append(h)
            
             
        
        #print(keys)
            if 'deployment_guid' or 'lm_troux_uid' not in keys:
                print(v.volume_id)
                 
          
    
    ec2client = boto3.client('ec2')
    response = ec2client.describe_snapshots(
       Filters=[
            {
                'Name': 'tag-key',
               'Values': ["deployment_guid"]
            },
            
       ]
    )
  
   
    dataList = response['Snapshots']
    index = 0
    while index < len(dataList):
        for key in dataList[index]:
            if key=='SnapshotId':
                print(dataList[index][key])
        index += 1
