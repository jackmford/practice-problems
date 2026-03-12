# README

Small local monitoring project to hit a Polygon RPC provider and pull back base metrics.

## Metrics

`relayer_wallet_balance_pol`

- Track the current wallet balance of a given wallet
  `polygon_node_block_height`
- Track polygon provider block height (useful for catching reorgs, node sync, confirmation depth, etc.)
  `polygon_rpc_latency_seconds`
- Track latency connecting to the polygon provider

## Run

Run the project with

`docker compose up -d`

## Endpoints

Prometheus = `localhost:9090`
Grafana = `localhost:3000`
App = `localhost:8000`

## TODO

### Logic

- [x] migrate to async
- [x] retry logic for poly-relay transactions
- [x] PENDING/IN PROGRESS states for transactions
- [x] watcherdog to use a "claimed_at" timestamp to flip them back in progress if they went to IN PROGRESS and a thread crashes
- [x] make watcherdog actually resubmit with higher gas and simulate head of line blocking problems
- [x] implement real gas math
- [x] implement a sliding window with a semaphore for the transactions to limit blasting the blockchain with too many transactions
- [ ] wallet protection
- [ ] make true nonce call to blockchain somewhere
- [ ] create indexer service
- [ ] nonce management
- [ ] reorg management

### Observability

- [x] add live gas prices to dashboard
- [ ] logger everywhere
- [ ] set up loki for logs and integrate to grafana
- [ ] traces
- [ ] add all to dashboard
- [ ] label request types for duration metric
