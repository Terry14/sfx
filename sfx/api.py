import urllib.parse

from .speedramps import speedramps
from .voices import voices


def _split_text(voice: str, text: str):
    """
    Input: voice: str, text: str
    Output: list of str
    """
    limit = voices[voice]["limit"]
    return [text[i : i + limit] for i in range(0, len(text), limit)]


def _convert_speed(voice: str, config_speed: int):
    """
    Input: voice: str, config_speed: int
    Output: config_speed: int
    """
    provider = voices[voice]["provider"]
    config_speed = speedramps[provider][config_speed]
    return int(config_speed)


def generate_urls(voice: str, text: str, speed: int):
    """
    Input: voice: str, text: str, speed: int
    Output: list of str (urls)
    """
    texts = _split_text(voice, text)
    url = voices[voice]["url"]
    speed_bool = voices[voice]["speed"]
    urls = []
    for segment in texts:
        turl = "".join(url)
        if speed_bool:
            turl = turl.replace("{speed}", str(_convert_speed(voice, speed)))
        turl = turl.replace("{text}", str(urllib.parse.quote(segment)))
        urls.append(turl)
    return urls
