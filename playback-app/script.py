import requests

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

playResponse = requests.put(playUrl, headers=playHeaders, json=playData)