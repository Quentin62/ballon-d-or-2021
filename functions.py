import numpy as np
import pandas as pd
from pycountry_convert import country_alpha2_to_continent_code, country_name_to_country_alpha2


def get_ranking(vote):
    points = [6, 4, 3, 2, 1]
    players = ["Azpilicueta", "Barella", "Benzema", "Bonucci", "Bruno Fernandes", "Chiellini",
               "Cristiano Ronaldo", "De Bruyne", "Dias", "Donnarumma", "Foden",
               "Haaland", "Jorginho", "Kane", "Kanté", "Kjaer", "Lewandowski",
               "Lukaku", "Mahrez", "Martinez", "Mbappé", "Messi", "Modric", "Moreno",
               "Mount", "Neymar", "Pedri", "Salah", "Sterling", "Suarez"]
    ranking = {}
    for player in players:
        ranking[player] = 0
        for i in range(5):
            ranking[player] += points[i] * np.sum(vote.iloc[:, i] == player)

    ranking = pd.DataFrame({"Points": ranking.values()}, index=ranking.keys())
    ranking = ranking.sort_values("Points", ascending=False)
    total = ranking["Points"].sum()
    ranking["% of total points"] = ranking["Points"] / total * 100
    ranking["% of max score"] = ranking["Points"] / (6 * len(vote)) * 100

    return ranking


def get_continent(countries):
    if isinstance(countries, str):
        countries = [countries]
    continents = []
    for country in countries:
        try:
            if country in ["England", "Scotland", "Wales", "Northern Ireland"]:
                continents.append("EU")
            elif country == "Tahiti":
                continents.append("OC")
            else:
                cn_a2_code = country_name_to_country_alpha2(country)
                cn_continent = country_alpha2_to_continent_code(cn_a2_code)
                continents.append(cn_continent)
        except:
            continents.append(None)
    return np.array(continents)
