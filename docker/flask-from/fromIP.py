from flask import Flask, request
from redis import Redis, RedisError
import datetime

redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)

app = Flask(__name__)

def byteToStr(target):
    if isinstance(target, bytes):
        return target.decode('utf-8')
    else:
        return target

@app.route("/")
def fromIP():
    today = datetime.datetime.now()
    todayKOR = today.strftime("%Y 년 %m 월 %d 일")
    today = today.strftime("%Y-%m-%d")

    html = "<h3>Hello!</h3>" \
           "<b>Your IP:</b> {SOURCE}<br>" \
           "Today: {TODAY}<br>" \
           "Visits: {VISITS}<br>"

    if request.headers.getlist("X-Forwarded-For"):
        source = request.headers.getlist("X-Forwarded-For")[0]
    else:
        source = request.remote_addr

    try:
        visits = redis.incr(today)
    except RedisError:
        visits = "Cannot connect to Redis."
        
    return html.format(SOURCE=source, TODAY=todayKOR, VISITS=visits)

@app.route("/stat")
def stat():
    yesterday = (datetime.date.today() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    today = datetime.datetime.now().strftime("%Y-%m-%d")

    html = "<b>Visits</b><br>" \
           "Yesterday: {YESTERDAY}<br>" \
           "Today: {TODAY}<br>"

    try:
        yesterdayVisits = byteToStr(redis.get(yesterday))
        todayVisits = byteToStr(redis.get(today))
    except RedisError:
        yesterdayVisits = "<i>Cannot connect to Redis.</i>"
        todayVisits = yesterdayVisits

    return html.format(YESTERDAY=yesterdayVisits, TODAY=todayVisits)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)