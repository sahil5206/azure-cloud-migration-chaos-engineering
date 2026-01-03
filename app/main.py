from fastapi import FastAPI
from database import get_connection
from models import Order
from prometheus_client import Counter, Histogram, generate_latest
import time

app = FastAPI()

REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total HTTP requests"
)

REQUEST_LATENCY = Histogram(
    "http_request_latency_seconds",
    "Request latency"
)

@app.get("/health")
def health():
    return {"status": "UP"}

@app.post("/orders")
def create_order(order: Order):
    start = time.time()
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO orders (customer_name, amount) VALUES (%s, %s)",
        (order.customer_name, order.amount)
    )
    conn.commit()
    cur.close()
    conn.close()
    REQUEST_COUNT.inc()
    REQUEST_LATENCY.observe(time.time() - start)
    return {"message": "Order created"}

@app.get("/orders")
def get_orders():
    start = time.time()
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM orders")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    REQUEST_COUNT.inc()
    REQUEST_LATENCY.observe(time.time() - start)
    return rows

@app.get("/metrics")
def metrics():
    return generate_latest()
