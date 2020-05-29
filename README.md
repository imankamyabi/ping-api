# ping-api

SAM template project for an API (GET ping/) secured by an API Key.

Run the following command to initialize a SAM project using this repository as a template:

```bash
sam init --location gh:imankamyabi/ping-api
```

Build the template:
```bash
sam build
```

Deploy the template:
```bash
sam deploy --stack-name ping-api --guided
```

"ApiEndpoint" is printed as an output after deploying the SAM template and also can be found at the output section of the deployed stack. It indicates the API Endpoint.

"ApiKeyId" is printed as an output as well and it indicates the API Key ID (and not value).

Run the following command to get the value for the API Key:
```bash
aws apigateway get-api-key --api-key [API Key ID Here] --include-value 
```

Now can test the sample ping API:

```bash
curl [API Endpoint]/ping -H "x-api-key: [API Key Value]"
```

## Resources

See the [AWS SAM developer guide](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html) for an introduction to SAM specification, the SAM CLI, and serverless application concepts.

### Author:
**Iman Kamyabi**