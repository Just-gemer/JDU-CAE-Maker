#JDU CAE MAKER BY Just gemer
import os
print("JDU CAE MAKER BY Just gemer")
mapname = str(input("mapname: "))
webmu = str(input("ultra webm url: "))
webmh = str(input("high webm url: "))
webmm = str(input("mid webm url: "))
webml = str(input("low webm url: "))
ogg = str(input("ogg url: "))


# JDU CAE Maker
cae = open(mapname.lower() + ".json", "w", encoding="utf-8")
cae.write('''{
  "__class": "ContentAuthorizationEntry",
  "duration": 300,
  "changelist": 480634,
  "urls": {
    "jmcs://jd-contents/''' + mapname + '''/''' + mapname + '''_ULTRA.hd.webm": "''' + webmu + '''",
    "jmcs://jd-contents/''' + mapname + '''/''' + mapname + '''_MID.hd.webm": "''' + webmm + '''",
    "jmcs://jd-contents/''' + mapname + '''/''' + mapname + '''_LOW.hd.webm": "''' + webml + '''",
    "jmcs://jd-contents/''' + mapname + '''/''' + mapname + '''_HIGH.hd.webm": "''' + webmh + '''",
    "jmcs://jd-contents/''' + mapname + '''/''' + mapname + '''_ULTRA.webm": "''' + webmu + '''",
    "jmcs://jd-contents/''' + mapname + '''/''' + mapname + '''_MID.webm": "''' + webmm + '''",
    "jmcs://jd-contents/''' + mapname + '''/''' + mapname + '''_LOW.webm": "''' + webml + '''",
    "jmcs://jd-contents/''' + mapname + '''/''' + mapname + '''_HIGH.webm": "''' + webmh + '''",
    "jmcs://jd-contents/''' + mapname + '''/''' + mapname + '''.ogg": "''' + ogg + '''"
  }
}''')
cae.close()
