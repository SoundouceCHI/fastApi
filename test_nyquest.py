import niquests
API_URL: str = "https://nominatim.openstreetmap.org/search.php?q=charles+de+gaulle+&format=jsonv2"
USER_AGENT: str = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"

if __name__ == "__main__": 
    session: niquests.Session = niquests.Session()
    session.headers["User_Agent"]= USER_AGENT
    session.headers["Referer"]= "https://www.google.com"
    response : niquests.Response = session.get(API_URL)
    
    #deserialize json doc into a python obj 
    data: list[dict] = response.json()
    for result in data : 
        print(result["display_name"])
    # print(response.text, response.status_code)