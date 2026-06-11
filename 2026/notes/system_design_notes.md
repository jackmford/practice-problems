# notes for interviews

- think about api/system interface query patterns and propose indexes on commonly queried fields
- Elasticsearch is the go to for text search

- Change Data Capture -> capturing database changes to stream to another system (usually done by monitoring the DB write-ahead log)

- consistent hashing can be used to get around the resharding pain of hash-based sharding
  - consistent hashing lets you elastically scale cache nodes/database shards based on load

- PACELC theorem: during a Partition, choose availability or consistently. Else; choose latency or consistency.

- systems are built for peaks, not averages.
  -> if a system has 500 RPS, maybe its peak is 5k

-> think about what effects a distributed server load has on a DB connection pool
-> 10 servers @ 5k RPS is potential 50k tps for DB pool.

-> why and when would you pick PostgreSQL?? look this up
-> L4 vs L7 load balancer??

- inverted index is a datastructure that maps content -> source. This is how elastic works, it lists all unique words in a document and maps the words to the documentid.

# queues

- rabbitmq/kafka
- kafka doesnt have near as much built in as rabbitmq

- rabbitmq broker receives a message, puts it in the right queue (using your broker rules), and sends to DLQ for messages repeatedly failing automatically, handles deleting messages
  - **smart broker, simple consumers**
  - messages pass **through** rabbitmq, gone when used

- kafka is a distributed append only log basically
  - consumers can read from the log and are responsible for maintaining their "offset" (position in the log)
  - **simple broker, smart consumers**
  - messages are durable and replayable
  - messages **live** in kafka

- rabbitmq has perfect ordering if using a single consumer
- kafka only has ordering within partitions in a topic (you pick how your data is sent to partitions)

- rabbitmq 4-10k msg/sec throughput, 1-5ms latency (clients get messages automatically)
- kafka 1m+ msg/sec, 5-50ms latency (because clients pull in batches)

- both rabbit+kafka use "at-least-once" delivery
  - most consumers should be idempotent

- rabbitmq much simpler to run than kafka
  - most use managed kafka services if using kafka

- rabbitmq use for:
  - task queues/bg jobs
  - smart routing
  - low latency at moderate scale
  - simplicity

- kafka use for:
  - multilple readers from one stream
  - replay/reproccesing
  - massive scale
  - durable event history

- kafka only ever has one consumer per "partition"

# message queue fundamentals

- message queues provide _decoupling_ between producers and consumers, allowing you to scale them independently of one another

- should we put a queue between producer -> Elixr API?

- queues provide message durability until consumers are finished processing them
  - queues handle "hiding" messages from consumers when they are in "progress" in different ways

- _delivery guarantees_
  - at least once delivery -> queue guarantees every message is delivered at least once (maybe more than once) (requires idempotent consumers)
    - **this is almost always the right answer**
  - at most once delivery -> fire and forget, if something goes wrong, it dies and is dead
    - only use for cases where data loss is acceptable
  - exactly once -> every message processed _exactly_ once
    - very hard to implement

_when to use a queue_?

1. async work
   - users dont need immediate response
2. bursty traffic
   - absorb spikes without dropping requests
3. decoupling
   - if consumers/producers need independent scaling
4. reliability
   - queues give you message durability

don't use queues for sync workloads with strict latency reqs!

- how does a queue handle increased throughput?
  - partitioning, aka splitting queues up into independent streams
  - need a partition key to ensure a users requests always go to the same queue partition so they get ensured ordering

you can monitor queue depth and auto scale to handle many messages coming from producers at once

you can apply _backpressure_ to producers to slow them down (rate limiting basically), if the queue is getting overloaded tell producers to chill

- poisoned message = a message that will never process because of some reason, always fails
  - most queues let you implement a max retry count and sends a message to a DLQ for failed messages

- what happens if the queue goes down??
  - queues can write messages to disk and give them to replicas

# caching

- database ~1ms data access vs. cache at ~100 nanoseconds
  - 10,000x faster

- external caches -> Redis, Memcached
- in process caching == keeping data in memory on an app server
- client side caching == data stored directly on users device
  - local storage on browser, data in memory on device
  - less control over the data with this approach

## cache archs

order in which reads and writes happen

- most common == **cache-aside** -> default to this
  - app checks cache first, if not, fetches from db, then stores in cache
  - downside is cache misses add latency
  - defines how data is _read_

- **write-through** -> write to cache THEN _sync_ write to DB
  - results in slower writes and cache pollution
  - can end in inconsistent state if one of the writes fails
  - much less common because of edge cases

- **write-behind** -> same as write through but writes are async to the DB, usually in batches
  - if the cache crashes before async flushes, loss of data
  - useful for high write throughput needs
  - don't use this as a novice

- **read-through** -> cache handles the read from the cache instad of app server like in cache-aside
  - essentially how a CDN works

- **write-around** -> write directly to db first and not to cache
  - subsequent reads are slower because nothing in cache yet
  - decreases cache pollution

- **time-to-live** eviction policy is great for data that can go stale (api responses)

## cache issues

- cache stampede (thundering herd)
  - popular cache entry expires and all requests try to request the item at once, all going to DB
  - prevent this with:
    - _single flight_ -> when a request tries to rebuild a cache key, only the first one should work
    - _cache warming_ -> instead of waiting for popular keys to expire, proactively refresh them from the cache, preventing them from expiring

- cache consistency
  - cache and db return different values if stale data is in the cache
  - common strategies:
    - _invalidate on write_ -> delete from cache if new value is written
    - _short ttls_
    - _accept that eventual consistency is fine_

- hot keys
  - a cache entry that gets way more traffic than others
  - solve this with:
    - replicate hot keys across the cache cluster shards
    - local fall back cache on the app server

- **when to use caches**
  - read heavy workloads
  - expensive db queries
  - high database cpu
  - strict latency reqs

caching usually comes up in deep dives when talking about scale
