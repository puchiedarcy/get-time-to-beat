import re
import urllib
import urllib2

games = [
'Kingdom Hearts 3D: Dream Drop Distance',
'Spyro the Dragon',
'Spyro the Dragon: Ripto\'s Rage!',
'Spyro the Dragon: Year of the Dragon',
'Crash Bandicoot',
'Crash Bandicoot 2: Cortex Strikes Back',
'Crash Bandicoot: Warped',
'Mega Man',
'Mega Man X2',
'Castlevania 2',
'[DS Castlevania]',
'Pushmo World',
'Captain Toad: Treasure Tracker',
'Catherine',
'Red Faction',
'Quake',
'Half-Life',
'Half-Life 2',
'Portal 2',
'Antichamber',
'Ghost Trick',
'Bit.Trip RUNNER',
'Hexic',
'Fez',
'DuckTales',
'DuckTales 2',
'Goof Troop',
'Jeopardy Jr.',
'Banjo-Kazooie',
'Banjo-Tooie',
'Quest 64',
'Kid Chameleon',
'Dynamite Headdy',
'Nimbus',
'Donaldland',
'Ninja Gaiden',
'Super Meat Boy',
'Give Up Robot',
'Sonic Adventure',
'Sonic Adventure 2: Battle',
'Little Inferno',
'Space Chem',
'Ni no Kuni',
'Dustforce',
'[Best Phoenix Wright Game]',
'Phoenix Wright: Ace Attorney - Dual Destinies',
'Katamary Damacy',
'We Love Katamari',
'Night Sky',
'The Wonderful 101',
'Disgaea: Hour of Darkness',
'Little Nemo: The Dream Master',
'A Nightmare on Elm Street',
'Princess Tomato in the Salad Kingdom',
'Pokemon Puzzle League'
]

for game in games:
    
    url = 'http://howlongtobeat.com/search_main.php?t=games&page=1&sorthead=popular&sortd=Normal%20Order&plat=&detail=0'
    formData = { 'queryString': game }
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'howlongtobeat.com', 'Cache-Control': 'no-cache', 'User-Agent': 'puchiedarcy'}
    encodedFormData = urllib.urlencode(formData)
    
    request = urllib2.Request(url, encodedFormData, headers)
    response = urllib2.urlopen(request)
    
    html = response.read()
    
    try:
        gameId = re.search('game.php\?id=(\d+)', html).group(1)
    except:
        print game + '\tN/A'
        continue
    
    url = 'URL:http://howlongtobeat.com/game_overview.php?id=' + gameId
    
    request = urllib2.Request(url, None, headers)
    response = urllib2.urlopen(request)
    
    html = response.read()
    
    timeToBeat = re.search('<h5>Main Story</h5>\n<div>(.*)</div>', html).group(1).replace('&#189;', '.5')
    
    print game + '\t' + timeToBeat.replace(' Hours', '').replace('Hour', '')
