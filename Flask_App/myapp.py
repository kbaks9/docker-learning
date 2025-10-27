from flask import Flask
import redis
import os

app = Flask(__name__)

#Connect to Redis Database
redis_host = os.environ.get("REDIS_HOST", "localhost") # use redis later for docker
redis_port = int(os.environ.get("REDIS_PORT", 6379))
r = redis.Redis(host=redis_host, port=redis_port, db=0)

@app.route("/")
def home():
    return '''
    <h3>Welcome to CoderCo Containers Challenge.</h3>
    <p>Click to visit: <a href="/count">count</a></p>
    '''

@app.route("/count")
# Increment visitor count
def count():
    visits = r.incr("visits")
    return f'''
    <h3> Visitor count: {visits}</h3>
    <p>To go back <a href="/">home</a></p>
    '''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)