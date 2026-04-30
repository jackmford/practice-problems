# dbs

## sharding

just splitting a large database into separate ones

allows you to store more data and improve performance

- types of sharding
  - geospatial ->
  - ranged based -> divides shards among the ranges of a value
  - hashed -> hashes shard keys to distribute data evently

- always figure out what your shard key is right away

- shard keys should be:
  - high cardinality (tons of distinct values)
  - even distribution
  - aligns with queries

range based sharding can work if shard key fits cleanly into a range not usually used in production

**hashed based** sharding evenly distributes data but can end up with very painful redistribution problems if a new shard needs to be added.

**consistent** sharding distributes shards around a "ring", removing the pain of adding new shards and having to redistribute like in hashed

**directory based** sharding uses a lookup table, i.e. for each user you store which shard they belong to

- allows you to implement a lot of custom sharding logic in the app layer
- increases latency because of lookups per request

### challenges in sharding

- "hot spots" (load imbalance)
  - some user is super popular and is making one shard get a disproportionate amount of traffic (famous persons posts that everyone wants to see are on one shard)
    - you can get around this with a **compound shard key**, add some other value before hashing. for example -> (userID+createdAt), this would distribute across multiple shards for users

  - **high traffic shards** for hot entries

- **cross shard operations**
  - if you need 10 pieces of data for a query from each shard, have to hit all shards (slow)
  - first line of defense is choosing a shard key that aligns with queries
  - you can **cache** results of expensive cross shard queries
  - you can **denormalize** data so things live together

- **maintaining consistency**
  - you lose the ability to execute atomic transactions in the database with shards
  - can use **2 phased commit** to tackle this problem
    - uses a coordinator to make sure shards are ready for commits
    - most production systems try to avoid this
  - try to avoid cross shard transactions
  - **saga pattern**
    - each action has a compensating action that can be run if something fails
