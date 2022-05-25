# amazon-peronalize-recommendation-api-with-sam

This project contains source code and supporting files for a serverless application that you can deploy with the SAM CLI. The application is implemented with Amazon API Gateway, AWS Lambda, Amazon Personalize and Amazon DynamoDB.

It includes the following files and folders.

- content_rec - Sample Code for the application's Lambda function.
- events - Invocation events that you can use to invoke the function.
- tests - Unit tests for the application code. 
- template.yaml - A template that defines the application's AWS resources.

# Use Case

Amazon Personalize enables developers to build applications with the same machine learning (ML) technology used by Amazon.com for real-time personalized recommendations – no ML expertise required. For geting real-time recommendations, after you complete Preparing and importing data and Creating a solution, you are ready to deploy your solution version to generate recommendations. You deploy a solution version by creating an Amazon Personalize campaign. A campaign is a deployed solution version (trained model) with provisioned dedicated transaction capacity for creating real-time recommendations for your application users. 

# Solution Overview
This sample project demostrate how to implement a Lambda function to get a list of recommended content by calling the Amazon Personalize campaign and then look up the detailed information of the content from a DynamoDB table. A Restful API is also created for this lambda function using Amazon API Gateway. For API authentication and authrization, the API is protected by both API Key and Cognito Authorizer.

![Screenshot 2022-05-24 at 2 27 35 PM](https://user-images.githubusercontent.com/73056587/169967032-1532e9bb-ed4a-4c80-abcd-a02611f12930.png)


# Prerequisites and preparations
1. Create your Amazon Cognito user pool and obtain your user pool ARN
https://docs.aws.amazon.com/cognito/latest/developerguide/getting-started-with-cognito-user-pools.html

2. Follow below hands-on lab instruction to create a real-time recomendation with Amazon Personalize. In this demo we will use the movielens data set as sample data. You can also use your own data set and schema accordingly. After you complete the steps you will be able to create an Amazon Personlize campaign. Mark down the campaign ARN and we will further use it to build the recomendation API.
https://aws.amazon.com/getting-started/hands-on/real-time-movie-recommendations-amazon-personalize/

3. Leverage below cloud formation template to create a DynamoDB table and load the item meta data. In this sample we will have four fields: id, category,content and subject.
https://aws.amazon.com/blogs/database/implementing-bulk-csv-ingestion-to-amazon-dynamodb/

4. Update template.yaml and update the place holder as below:
    * <Cognito_User_Pool_ARN> -- the Amazon Cognito user pool ARN created in step #1
    * <Personalize_Campaign_ARN> -- the Amazon Personalize Campaign ARN created in step #2
    * <DynamoDB_Table_Name> -- the DynameDB table name generated in step #3
    * <Region> -- the resgion you choose to deploy the API. For example ap-southeast-1


## Deploy the sample application

The Serverless Application Model Command Line Interface (SAM CLI) is an extension of the AWS CLI that adds functionality for building and testing Lambda applications. It uses Docker to run your functions in an Amazon Linux environment that matches Lambda. It can also emulate your application's build environment and API.

To use the SAM CLI, you need the following tools.

* SAM CLI - [Install the SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
* [Python 3 installed](https://www.python.org/downloads/)
* Docker - [Install Docker community edition](https://hub.docker.com/search/?type=edition&offering=community)

To build and deploy your application for the first time, run the following in your shell:

```bash
sam build
sam deploy --guided
```

The first command will build the source of your application. The second command will package and deploy your application to AWS, with a series of prompts:

* **Stack Name**: The name of the stack to deploy to CloudFormation. This should be unique to your account and region, and a good starting point would be something matching your project name.
* **AWS Region**: The AWS region you want to deploy your app to.
* **Confirm changes before deploy**: If set to yes, any change sets will be shown to you before execution for manual review. If set to no, the AWS SAM CLI will automatically deploy application changes.
* **Allow SAM CLI IAM role creation**: Many AWS SAM templates, including this example, create AWS IAM roles required for the AWS Lambda function(s) included to access AWS services. By default, these are scoped down to minimum required permissions. To deploy an AWS CloudFormation stack which creates or modifies IAM roles, the `CAPABILITY_IAM` value for `capabilities` must be provided. If permission isn't provided through this prompt, to deploy this example you must explicitly pass `--capabilities CAPABILITY_IAM` to the `sam deploy` command.
* **Save arguments to samconfig.toml**: If set to yes, your choices will be saved to a configuration file inside the project, so that in the future you can just re-run `sam deploy` without parameters to deploy changes to your application.


You can find your API Gateway Endpoint URL in the output values displayed after deployment.

## Post Deployment Steps



## Tests


## Cleanup

To delete the sample application that you created, use the AWS CLI. Assuming you used your project name for the stack name, you can run the following:

```bash
aws cloudformation delete-stack --stack-name <stack_name>
```


