import urllib.robotparser

rp = urllib.robotparser.RobotFileParser()
rp.set_url("https://www.usa.gov/robots.txt")
rp.read()
print(rp.can_fetch("*", "https://www.usa.gov/"))