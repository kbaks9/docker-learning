from flask import Flask
import redis
import os

app = Flask(__name__)
redis_host = os.getenv('REDIS_HOST', 'redis')
redis_port = int(os.getenv('REDIS_PORT', 6379))
r = redis.Redis(host=redis_host, port=redis_port)

@app.route('/')
def hello_world():
    return '''
    <h1>Homepage of the CoderCo Challenge</h1>
    <p>Click to visit other page: <a href="/count">here</a></p>
    '''

@app.route('/count')
def count():
    count = r.incr('visits')
    return f'<p>Hi, there has been {count} visitors to this page.</p>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)