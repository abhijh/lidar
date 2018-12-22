import myjdapi

class JDownloader(object):
    jd = myjdapi.Myjdapi()
    jd.connect("192.168.1.5","")
    jd.getDevices()
    jd.get_device(name="DeviceName").linkgrabber.add_links([{"autostart" : False, "links" : "https://files1.mp3slash.xyz/stream/8bb06753199bb3619578cec8f8c40b03","packageName" : "one" }])