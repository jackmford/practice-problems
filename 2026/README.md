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
Grafana    = `localhost:3000`
App        = `localhost:8000`
