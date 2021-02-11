import boto3
def lambda_handler(event, context):
    ec2 = boto3.resource('ec2')
    volume_iterator = ec2.volumes.all()
    name = None
    for v in volume_iterator:
        #print(v)
        keys=[]
        for tag in v.tags:
        
            h=tag['Key']
            keys.append(h)
             
        
        print(keys)
        if 'volume_type' not in keys:
            print(v)
                 
            
        keys=[]     
            
           
        
