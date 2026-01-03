from fastapi import FastAPI
from models import Order
from database import get_connection
from prometheus_client import Counter, Histogram, generate_latest
import time
from fastapi import Response
from prometheus_client import CONTENT_TYPE_LATEST


app = FastAPI()

# Prometheus metrics
REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total HTTP requests"
)

REQUEST_LATENCY = Histogram(
    "http_request_latency_seconds",
    "Request latency in seconds"
)

# Initialize SQLite DB
def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT NOT NULL,
            amount REAL NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

init_db()

@app.get("/health")
def health():
    return {"status": "UP"}

@app.post("/orders")
def create_order(order: Order):
    start = time.time()
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO orders (customer_name, amount) VALUES (?, ?)",
        (order.customer_name, order.amount)
    )
    conn.commit()
    conn.close()

    REQUEST_COUNT.inc()
    REQUEST_LATENCY.observe(time.time() - start)

    return {"message": "Order created"}

@app.get("/orders")
def get_orders():
    start = time.time()
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orders")
    rows = cursor.fetchall()
    conn.close()

    REQUEST_COUNT.inc()
    REQUEST_LATENCY.observe(time.time() - start)

    return rows


@app.get("/metrics")
def metrics():
    return Response(
        content=generate_latest(),
        media_type=CONTENT_TYPE_LATEST
    )
