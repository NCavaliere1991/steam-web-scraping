from bs4 import BeautifulSoup
import requests
import pandas as pd

response = requests.get('https://steamcharts.com/top')
top_games = response.text

soup = BeautifulSoup(top_games, 'html.parser')
games = soup.find_all(name='tr')

records = []
for game in games:
    titles = game.select('.game-name a')

    for title in titles:
        name = title.text.strip()

        c_players = game.select('.num')

        for c_play in c_players[::3]:
            current_player = c_play.text
        p_players = game.select('.peak-concurrent')

        for p_play in p_players:
            peak_players = p_play.text
        p_hrs = game.select('.player-hours')

        for p_hr in p_hrs:
            player_hours = p_hr.text

            record = {
            "Name": name,
            "Current Players": current_player,
            "Peak Players": peak_players,
            "Hours Played": player_hours
            }
            records.append(record)

df = pd.DataFrame(records)
df.to_csv("game_statistics.csv", index=False)
