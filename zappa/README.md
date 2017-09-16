# Requirements
1. [Docker Community Edition](https://www.docker.com/community-edition)
    * Tested on Windows 10 Build 15063.540
    * Docker CE Version 17.06.0-ce-win19 (12801)
2. [AWS](https://aws.amazon.com)
    * You will need an `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`
    * You will need a user and policy for deploying to AWS Lamdba (see below for instructions)

# Creating an AWS User and Policy
1. Navigate to [AWS Users](https://console.aws.amazon.com/iam/home?region=us-east-1#/users$new?step=details)
2. Create a User name
3. Select Programmatic Access
4. Click Next: Permissions button
5. Click Attach existing policies directly
6. Click Create policy button
7. Create your own policy named zappa-lamdba and whatever description you want.
8. In the Policy Document section, paste in the following json, substituting `<account_id>` with your [Account ID](http://docs.aws.amazon.com/IAM/latest/UserGuide/console_account-alias.html) 

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "iam:AttachRolePolicy",
                "iam:CreateRole",
                "iam:GetRole",
                "iam:PutRolePolicy"
            ],
            "Resource": [
                "*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "iam:PassRole"
            ],
            "Resource": [
                "arn:aws:iam::<account_id>:role/*-ZappaLambdaExecutionRole"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "apigateway:DELETE",
                "apigateway:GET",
                "apigateway:PATCH",
                "apigateway:POST",
                "apigateway:PUT",
                "events:DeleteRule",
                "events:DescribeRule",
                "events:ListRules",
                "events:ListTargetsByRule",
                "events:ListRuleNamesByTarget",
                "events:PutRule",
                "events:PutTargets",
                "events:RemoveTargets",
                "lambda:AddPermission",
                "lambda:CreateFunction",
                "lambda:DeleteFunction",
                "lambda:GetFunction",
                "lambda:GetPolicy",
                "lambda:ListVersionsByFunction",
                "lambda:RemovePermission",
                "lambda:UpdateFunctionCode",
                "lambda:UpdateFunctionConfiguration",
                "cloudformation:CreateStack",
                "cloudformation:DeleteStack",
                "cloudformation:DescribeStackResource",
                "cloudformation:DescribeStacks",
                "cloudformation:ListStackResources",
                "cloudformation:UpdateStack",
                "logs:DescribeLogStreams",
                "logs:FilterLogEvents",
                "route53:ListHostedZones",
                "route53:ChangeResourceRecordSets",
                "route53:GetHostedZone",
                "s3:CreateBucket",
            ],
            "Resource": [
                "*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "s3:ListBucket"
            ],
            "Resource": [
                "arn:aws:s3:::zappa-8jtbhxihc"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "s3:DeleteObject",
                "s3:GetObject",
                "s3:PutObject",
                "s3:CreateMultipartUpload",
                "s3:AbortMultipartUpload",
                "s3:ListMultipartUploadParts",
                "s3:ListBucketMultipartUploads"
            ],
            "Resource": [
                "arn:aws:s3:::zappa-8jtbhxihc/*"
            ]
        }
    ]
}
```
9. Validate the policy, create the policy, review the user and policy, complete.
10. Take note of the ID and Secret key that are generated, these will correspond to `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` set in our .env file for zappa. 

# Getting Started
1. `git clone https://github.com/DJO3/pytools.git`
2. `cd pytools/zappa`
4. Open .env and set `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` to the values associated with your zappa user. 
5. `docker-compose build`
6. `docker-compose up -d`
7. `docker exec -it zappa bash`
8. `zappa deploy dev`
9. After about a minute the deployment will be live and zappa will tell you what url the content is availabe at. 

# Credit
[aws_zappa_policy.json](https://github.com/Miserlou/Zappa/issues/244)