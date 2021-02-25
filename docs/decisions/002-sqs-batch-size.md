---
title: SQS Batch Size increase
---

## Context

[Dmytro](https://github.com/zelds), a colleague of mine, pointed to a very interesting change in AWS documentation. [Using AWS Lambda with Amazon SQS](https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html) page used to say:

> Batch size – The number of items to read from the queue in each batch, up to 10. The event might contain fewer items if the batch that Lambda read from the queue had fewer items. 

But now it indicates:

> Batch size – The number of records to send to the function in each batch. For a standard queue this **can be up to 10,000 records**. For a FIFO queue the maximum is 10. For a batch size over 10, you must also set the `MaximumBatchingWindowInSeconds` parameter to at least 1 second.
> Lambda passes all of the records in the batch to the function in a single call, as long as the total size of the events doesn't exceed the payload limit for synchronous invocation (6 MB).

This is a welcome change. In case of small messages and fast processing, running one Lambda on only 10 messages at once is sometimes not very efficient in terms of cost and performance.

Unfortunately, at the time of writing, Terraform [aws_lambda_event_source_mapping](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/lambda_event_source_mapping) resource did not yet adapt to the change:

> `batch_size` - (Optional) The largest number of records that Lambda will retrieve from your event source at the time of invocation. Defaults to 100 for DynamoDB, Kinesis and MSK, 10 for SQS.

The same applies to SQS API functions.

[SendMessageBatch](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_SendMessageBatch.html)
> Delivers up to ten messages to the specified queue.

[ReceiveMessage](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ReceiveMessage.html)
> `MaxNumberOfMessages` The maximum number of messages to return. Amazon SQS never returns more messages than this value (however, fewer messages might be returned). Valid values: 1 to 10. Default: 1.

## Decision

I consider this to be a change that is in progress of implementation across AWS infrastructure and third party tools. In order to support it right now, we will add a `batch_size` parameter for our SQS queue classes. It will be equal to 10 by default.

## Consequences

We will create an ability to change the batch size. Thus, we will simplify adoption of this new feature when it is available for `boto3`. 
