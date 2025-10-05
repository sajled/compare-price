import requests
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS – żeby frontend mógł się łączyć
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

CHEAPSHARK_API = "https://www.cheapshark.com/api/1.0"
FREETOGAME_API = "https://www.freetogame.com/api"

@app.get("/search")
def search(game: str):
    url = f"{CHEAPSHARK_API}/games?title={game}"
    response = requests.get(url)
    data = response.json()

    results = []
    for item in data:
        results.append({
            "title": item["external"],
            "price": item["cheapest"],
            "link": f"https://www.cheapshark.com/redirect?dealID={item['cheapestDealID']}",
            "thumbnail": item["thumb"]
        })
    return results


@app.get("/freegames")
def free_games():
    url = f"{FREETOGAME_API}/games?platform=pc"
    response = requests.get(url)
    return response.json()
