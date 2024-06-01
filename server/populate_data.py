import grequests
from requests.models import Response

from models import League

url = "https://api-football-v1.p.rapidapi.com/v3/leagues"

querystring = {"code":"za"}

headers = {
	"x-rapidapi-key": "5710451242msh352af7e3a514766p1157b2jsn5e301e660b48",
	"x-rapidapi-host": "api-football-v1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())


class RapidAPI:
    """ Class to interact with the RapidAPI Football API """
    
    def __init__(self, url, headers):
        self.url: str = url
        self.headers: str = headers

    def get_leagues(self, code: str):
        querystring: dict[str, str] = {"code": code}
        
        try:
            response: Response = requests.get(self.url, headers=self.headers, params=querystring)
        except Exception as e:
            return {"error": str(e)}
        
        id: int = response.json()["response"][0]["league"]["id"]
        name: str = response.json()["response"][0]["league"]["name"]
        logo: str = response.json()["response"][0]["league"]["logo"]
        country: str = response.json()["response"][0]["country"]["name"]
        code: str = response.json()["response"][0]["country"]["code"]
        flag: str = response.json()["response"][0]["country"]["flag"]

        league: League = League(
            id=self.id,
            name=self.name,
            logo=self.logo,
            country=self.country,
            code=self.code,
            flag=self.flag
        )
        
        return response.json()
    
    