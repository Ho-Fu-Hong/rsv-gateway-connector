# rsv-gateway-connector

Connector that keeps our hotel channel manager in sync with the Sands China
reservation partner gateway (`rsv-partner-gw.sandschina.com`).

## What it does

- Pulls room availability and rate plans from the gateway every 5 minutes
- Pushes confirmed bookings and cancellations back to the gateway
- Writes a sync log to the channel manager database

## Running

```bash
pip install -r requirements.txt
export $(cat config/production.env | xargs)
python src/sync.py
```

Settings are read from `config/production.env`.

Last update: 13:36 02/11/2026
