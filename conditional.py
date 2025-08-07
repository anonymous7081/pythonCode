
hr = 00
min = 23
sec = 45
if hr == 00:
    print(12, min, sec, "AM")
elif hr < 12:
    print(hr,min ,sec, "AM")
elif hr == 12:
    print(hr, min, sec, "PM")
elif hr > 12:
    hr = hr%12
    print(hr, min, sec, "PM")