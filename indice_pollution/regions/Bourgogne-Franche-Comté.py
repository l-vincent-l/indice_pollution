from . import ForecastMixin
import csv
from dateutil.parser import parse
from bs4 import BeautifulSoup
import requests
from datetime import date, timedelta
from itertools import chain

class Forecast(ForecastMixin):
    website = 'https://www.atmo-bfc.org/'
    url = 'https://www.atmo-bfc.org/medias/ajax/me_gateway.php'

    def get_one_attempt(self, url, params, attempts=0):
        r = requests.post(url,
            headers={
                'Accept-Encoding': '*',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
            },
            data=params
        )
        r.raise_for_status()
        return r

    def params(self, date_, insee):
        self.date_ = date_
        print(f'date: "{self.date_}"')
        return {
            "meC": "abo_communes",
            "meM": "traitementAjax",
            "meIdC": "7448b8180480a8749b31941011165d92.MTQxNQ%3D%3D",
            "meT": "i",
            "paramsM[mode]": "refreshCartePolluant",
            "paramsM[meCibleId]": "7448b8180480a8749b31941011165d92_MTQxNQ_3D_3D",
            "paramsM[meDate]": date_,
            "paramsM[codeCommune]": insee,
            "paramsM[idPolluant]": -1,
            "paramsM[codeAgglo]": 3,
            "paramsM[changeJour]": 1,
            "paramsM[prevPolluant]": 0,
            "m_idPage": 183,
            "m_initialesLangue": "fr",
            "ajax": 1
        }

    def get(self, date_, insee, attempts=0):
        if insee not in self.insee_list():
            insee = self.get_close_insee(insee)
        parsed_date = parse(date_)
        day_before = str((parsed_date - timedelta(days=1)).date())
        day_after = str((parsed_date + timedelta(days=1)).date())
        features_daybefore = self.get_multiple_attempts(self.url, self.params(day_before, insee))
        features_date = self.get_multiple_attempts(self.url, self.params(date_, insee))
        features_dayafter = self.get_multiple_attempts(self.url, self.params(day_after, insee))
        return list(
            filter(
                lambda s: s is not None,
                map(
                    self.getter,
                    chain(
                        features_daybefore,
                        features_date,
                        features_dayafter
                    )
                )
            )
        )

    @classmethod
    def features(cls, r):
        soup = BeautifulSoup(r.json()["indices"])
        valeurIndice = soup.find_all("div", class_="valeurIndice")[0]
        return valeurIndice.find_all("span")[1].text

    def getter(self, feature):
        return {
            "indice": feature,
            "date": self.date_
        }

    def get_close_insee(self, insee):
        return insee