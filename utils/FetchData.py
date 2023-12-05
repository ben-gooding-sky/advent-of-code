import os

import urllib3
import browser_cookie3 as bc
import requests

cachePathTemplate = "../{year}/cache/day-{day}-data"
testDataCachePathTemplate = "../{year}/cache/day-{day}-test-data"
adventOfCodeTemplate = "https://adventofcode.com/{year}/day/{day}/input"


def fetchData(day: int, year: int = 2023, testData=False) -> list[str]:
    cachePath = cachePathTemplate.replace("{year}", str(year)).replace("{day}", str(day))
    testDataCachePath = testDataCachePathTemplate.replace("{year}", str(year)).replace("{day}", str(day))

    def saveToCache(data: str | list[str], cachePath: str) -> None:
        f = open(cachePath, "x")
        if isinstance(data, list):
            f.write("\n".join(data))
        else:
            f.write(data)
        f.close()
        print("Saved data to cache.")

    def fetchFromCache(cachePath: str) -> list[str]:
        f = open(cachePath, "r")
        cachedData = f.readlines()
        f.close()
        return cachedData

    def checkIfCacheExists(cachePath: str) -> bool:
        return os.path.isfile(cachePath)

    def loadSessionCookie() -> str:
        try:
            return requests.utils.dict_from_cookiejar(bc.chrome(domain_name='.adventofcode.com'))["session"]
        except KeyError:
            raise Exception("No session found - please login with chrome")

    def fetchFromSource(sessionCookie: str) -> list[str]:
        urllib3.disable_warnings()
        url = adventOfCodeTemplate.replace("{year}", str(year)).replace("{day}", str(day))
        response = requests.get(
            url,
            verify=False,
            cookies={"session": sessionCookie},
            timeout=3)
        print("Fetched data from source.")
        return response.text.split("\n")
    if testData:
        if checkIfCacheExists(testDataCachePath):
            return fetchFromCache(testDataCachePath)
        raise Exception(f"No test data found from cache at path{str(testDataCachePath)}")
    if checkIfCacheExists(cachePath):
        return fetchFromCache(cachePath)

    data = fetchFromSource(sessionCookie=loadSessionCookie())
    saveToCache(data, cachePath)
    return data
