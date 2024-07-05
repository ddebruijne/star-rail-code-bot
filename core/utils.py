import requests
import lxml.html
import sqlite3
import os.path

hsrdb = "codes.db"
zzzdb = "zzzcodes.db"

def get_star_rail_codes():
    result = []

    response = requests.get("https://www.prydwen.gg/star-rail/", stream=True)
    response.raw.decode_content = True
    tree = lxml.html.parse(response.raw)
    codes = tree.xpath('//p[@class="code"]/text()')
    rewards = tree.xpath('//p[@class="rewards"]/text()')

    isNewDb = not os.path.exists(hsrdb)
    con = sqlite3.connect(hsrdb)
    cur = con.cursor()

    if isNewDb:
        cur.execute("CREATE TABLE codes(code, what)")

    for i, code in enumerate(codes):
        code = code.strip()
        rewards[i] = rewards[i].strip()
        print("code: " + code + " / reward: " + rewards[i])

        res = cur.execute("SELECT code from codes WHERE code='" + code + "'")
        if res.fetchone() is None:
            print ("code is new!")
            cur.execute("INSERT INTO codes VALUES ('" + code + "', '" + rewards[i] + "')")
            con.commit()
            resultentry = (code, rewards[i])
            result.append(resultentry)

    con.close()
    return result

def get_zzz_codes():
    result = []

    response = requests.get("https://www.prydwen.gg/zenless/", stream=True)
    response.raw.decode_content = True
    tree = lxml.html.parse(response.raw)
    codes = tree.xpath('//p[@class="code"]/text()')
    rewards = tree.xpath('//p[@class="rewards"]/text()')

    isNewDb = not os.path.exists(zzzdb)
    con = sqlite3.connect(zzzdb)
    cur = con.cursor()

    if isNewDb:
        cur.execute("CREATE TABLE codes(code, what)")

    for i, code in enumerate(codes):
        code = code.strip()
        rewards[i] = rewards[i].strip()
        print("code: " + code + " / reward: " + rewards[i])

        res = cur.execute("SELECT code from codes WHERE code='" + code + "'")
        if res.fetchone() is None:
            print ("code is new!")
            cur.execute("INSERT INTO codes VALUES ('" + code + "', '" + rewards[i] + "')")
            con.commit()
            resultentry = (code, rewards[i])
            result.append(resultentry)

    con.close()
    return result

