from flask import Flask, Response
from prometheus_client import Counter, Histogram, generate_latest
import time

app = Flask(name)

REQUEST_COUNT = Counter(
    'web_requests_total',
    'Total web requests'
)

REQUEST_LATENCY = Histogram(
    'web_request_latency_seconds',
    'Request latency'
)

@app.route('/')
def home():
    start = time.time()

    REQUEST_COUNT.inc()

    response = "Prometheus Monitoring Lab"

    REQUEST_LATENCY.observe(time.time() - start)

    return response

@app.route('/health')
def health():
    return "OK"

@app.route('/metrics')
def metrics():
    return Response(
        generate_latest(),
        mimetype='text/plain'
    )

app.run(host='0.0.0.0', port=5000)
