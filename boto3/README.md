# Summary
Create an object in an S3 bucket and retrieve it. More to come. 

# Getting Started
```
docker build -t boto3:local .
docker-compose up
```

# Test S3 Bucket Performance
```
curl -w "@curl-format.txt" -o /dev/null -s https://<bucket>.s3.amazonaws.com/<sha256_hash>
```
