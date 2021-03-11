# python-platonic

Data structures for Clean Architecture applications in Python.

* Represent various backends — say, Redis, S3 or Kafka — as simple and typed datastructures similar to iterators, lists, and dicts from the standard library;
* Write code in terms of high level abstractions;
* Port code from one backend to another;
* Maintain static typing correctness.


|                 | queue             | iterable | dict | list | set | graph |
| ---             | ---               | ---      | ---  | ---  | --- | ---   |
| Amazon DynamoDB |                   |          |      |      |     |      |
| Amazon SimpleDB |                   |          |      |      |     |      |
| Amazon SQS      | [✔](backends/sqs/index.md) |          | ❌    |      |     |      |
| Amazon S3       |                   |          |      |      |     |      |
| Apache Kafka    |                   |          |      |      |     |      |
| Azure CosmosDB  |                   |          |      |      |     |      |
| MongoDB         |                   |          |      |      |     |      |
| MySQL           |                   |          |      |      |     |      |
| Local FS        |                   |          |      |      |     |      |
| OrientDB        |                   |          |      |      |     |      |
| PostgreSQL      |                   |          |      |      |     |      |
| Redis           |                   |          |      |      |     |      |
