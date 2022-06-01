import requests, base64, random, os

# https://twitter.com/scanlime/status/1512598559769702406
voices = [  # DISNEY VOICES
    'en_us_ghostface',  # Ghost Face
    'en_us_chewbacca',  # Chewbacca
    'en_us_c3po',  # C3PO
    'en_us_stitch',  # Stitch
    'en_us_stormtrooper',  # Stormtrooper
    'en_us_rocket',  # Rocket

    # ENGLISH VOICES
    'en_au_001',  # English AU - Female
    'en_au_002',  # English AU - Male
    'en_uk_001',  # English UK - Male 1
    'en_uk_003',  # English UK - Male 2
    'en_us_001',  # English US - Female (Int. 1)
    'en_us_002',  # English US - Female (Int. 2)
    'en_us_006',  # English US - Male 1
    'en_us_007',  # English US - Male 2
    'en_us_009',  # English US - Male 3
    'en_us_010',  # English US - Male 4

    # EUROPE VOICES
    'fr_001',  # French - Male 1
    'fr_002',  # French - Male 2
    'de_001',  # German - Female
    'de_002',  # German - Male
    'es_002',  # Spanish - Male

    # AMERICA VOICES
    'es_mx_002',  # Spanish MX - Male
    'br_001',  # Portuguese BR - Female 1
    'br_003',  # Portuguese BR - Female 2
    'br_004',  # Portuguese BR - Female 3
    'br_005',  # Portuguese BR - Male

    # ASIA VOICES
    'id_001',  # Indonesian - Female
    'jp_001',  # Japanese - Female 1
    'jp_003',  # Japanese - Female 2
    'jp_005',  # Japanese - Female 3
    'jp_006',  # Japanese - Male
    'kr_002',  # Korean - Male 1
    'kr_003',  # Korean - Female
    'kr_004',  # Korean - Male 2
]
good_voices = {'good': ['en_us_002', 'en_us_006'],
               'ok': ['en_au_002', 'en_uk_001']}  # less en_us_stormtrooper more less en_us_rocket en_us_ghostface


class TTTTSWrapper:  # TikTok Text-to-Speech Wrapper
    def __init__(self):
        self.URI_BASE = 'https://api16-normal-useast5.us.tiktokv.com/media/api/text/speech/invoke/?text_speaker='

    def tts(self, req_text: str = "TikTok Text To Speech", filename: str = 'title.mp3', random_speaker: bool = False):
        if len(req_text) > 299:
            return ValueError("Text too long must be under 299 characters")
        if random_speaker:
            req_text = req_text.replace("+", "plus").replace(" ", "+").replace("&", "and")
        voice = self.randomvoice() if random_speaker else 'en_us_002'
        r = requests.post(f"{self.URI_BASE}{voice}&req_text={req_text}&speaker_map_type=0")

        vstr = [r.json()["data"]["v_str"]][0]

        b64d = base64.b64decode(vstr)

        out = open(filename, "wb")
        out.write(b64d)
        out.close()

    @staticmethod
    def randomvoice():
        ok_or_good = random.randrange(1, 10)
        if ok_or_good == 1:  # 1/10 chance of ok voice
            return random.choice(good_voices['ok'])
        return random.choice(good_voices['good'])  # 9/10 chance of good voice
