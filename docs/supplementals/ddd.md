# DDD

The data structures provided by `platonic` are meant to be **repositories** in DDD terminology.

> A Repository mediates between the domain and data mapping layers, **acting like an in-memory domain object collection**. ...

That is what `platonic` means to do. We are trying to encapsulate the complexities and little details of the backends, so that your application can operate with queues, mappings, lists, sets or trees, which contain Python objects.

> Objects can be added to and removed from the Repository, ...

Yes, when the nature of the data structure permits that. Say, a mapping can be read-only.

> ...as they can from a simple collection of objects, and the mapping code encapsulated by the Repository will carry out the appropriate operations behind the scenes.
> 
> ... 
>
> Repository also supports the objective of achieving a clean separation and one-way dependency between the domain and data mapping layers.

Quoted from: [Thoughtworks → Patterns of Enterprise Application Architecture → Repository](https://martinfowler.com/eaaCatalog/repository.html).

### Alternatives

[Dapr](https://dapr.io/) is a cloud-native application framework from Microsoft. Seems to abstract things like PubSub, key-value storages and remote procedure calls. Here is a [Python SDK example](https://github.com/dapr/python-sdk/blob/master/examples/w3c-tracing/invoke-caller.py). 

- Does not involve Python typing;
- Is a framework, not a library. I prefer libraries because they do not impose any hard-wired architecture patterns upon you.
