import requests

from pn532 import *

access_token = "BQC_ot6eFW8wWzjfj7bPQT82IqZepjJYqjAv8yjz8y10G_mHl5QItCdXjGmwkRpBjciyWzBi2H6j1Z3sjrZIgc3_ZVx9TbPw8gxShCHSqgfRDjx6Xaqjje5_9SBnHK_exLnba_q_-nK-Ze_yLreTgeBQuSVPnrzMqXIHYYtxPFpip-c0keThtdxvPe98-aj0DTylV6TMwNP6rrJLvj7bwZvqYDSybH6p0tJXpHerpF4LWD0"

playUrl = "https://api.spotify.com/v1/me/player/play?device_id=c318c64b035896d8fef90752a6f1d781bf55ed2e"

playHeaders = {
    "Authorization": "Bearer " + access_token,
    "Content-Type": "application/json"
}

playData = {
    "context_uri": "spotify:album:1J1yxODbNlqKbwRqJxYJUP",
    "offset": {
        "position": 5
    },
    "position_ms": 0
}

if __name__ == '__main__':
    try:
        pn532 = PN532_SPI(debug=False, reset=20, cs=4)

        ic, ver, rev, support = pn532.get_firmware_version()
        print('Found PN532 with firmware version: {0}.{1}'.format(ver, rev))

        # Configure PN532 to communicate with MiFare cards
        pn532.SAM_configuration()

        print('Waiting for RFID/NFC card...')
        while True:
            # Check if a card is available to read
            uid = pn532.read_passive_target(timeout=0.5)
            print('.', end="")
            # Try again if no card is available.
            if uid is None:
                continue
            print('Found card with UID:', [hex(i) for i in uid])
            requests.put(playUrl, headers=playHeaders, json=playData)
    except Exception as e:
        print(e)
    #finally:
        #Device.pin_factory.reset()

#playResponse = requests.put(playUrl, headers=playHeaders, json=playData)