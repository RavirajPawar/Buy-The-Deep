# coin_list is collection of dict objects, collected from coingecko coins/list api
COIN_METADATA = [
    {
        "id": "ethereum",
        "symbol": "eth",
        "name": "Ethereum"
    },
    {
        "id": "cardano",
        "symbol": "ada",
        "name": "Cardano"
    },
    {
        "id": "solana",
        "symbol": "sol",
        "name": "Solana"
    },
    {
        "id": "bitcoin",
        "symbol": "btc",
        "name": "Bitcoin"
    },
    {
        "id": "decentraland",
        "symbol": "mana",
        "name": "Decentraland"
    },
    {
        "id": "dogecoin",
        "symbol": "doge",
        "name": "Dogecoin"
    },
    {
        "id": "theta-token",
        "symbol": "theta",
        "name": "Theta Network"
    },
    {
        "id": "chainlink",
        "symbol": "link",
        "name": "Chainlink"
    },
    {
        "id": "uniswap",
        "symbol": "uni",
        "name": "Uniswap"
    },
    {
        "id": "matic-network",
        "symbol": "matic",
        "name": "Polygon"
    },
    {
        "id": "polkadot",
        "symbol": "dot",
        "name": "Polkadot"
    },
]
# MAX_DAYS is difference between 1-1-2016 to 14-5-2022 in days 2325
MAX_DAYS = 10000
# api of coingecko historical data
HISTORICAL_DATA_API = "https://api.coingecko.com/api/v3/coins/{}/market_chart?vs_currency=USD&days={}"
