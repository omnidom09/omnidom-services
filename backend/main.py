from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import uuid
import os
import shutil
import json

app = FastAPI()

# allow frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# storage file
DATA_FILE = "orders.json"

# create file if not exists
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump({}, f)

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# EDIT THESE PAYMENT DETAILS LATER
PAYMENT_DETAILS = {
    "upi_id": "8950202342@ibl",
    "bank_name": " INDIAN BANK",
    "account_number": "XXXXXXXX",
    "ifsc": "XXXX0000",
    "phone": "+91 8950202342"
}

# services list
services = [
    {
        "id": "1",
        "name": "Resume Optimization",
        "price": 149,
        "delivery": "24 hours",
        "description": "Handled directly by experienced professional"
    },
    {
        "id": "2",
        "name": "LinkedIn Optimization",
        "price": 199,
        "delivery": "24 hours",
        "description": "Professionally optimized profile"
    },
    {
        "id": "3",
        "name": "Cover Letter Writing",
        "price": 149,
        "delivery": "24 hours",
        "description": "Custom written cover letter"
    }
]

# helper functions
def load_orders():
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_orders(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

@app.get("/")
def home():
    return {"status": "running"}

@app.get("/services")
def get_services():
    return services

@app.get("/payment")
def get_payment():
    return PAYMENT_DETAILS

@app.post("/order")
def create_order(data: dict):

    orders = load_orders()

    order_id = "CF72-" + str(uuid.uuid4())[:6]

    data["order_id"] = order_id
    data["payment_status"] = "pending"
    data["work_status"] = "pending"
    data["delivery"] = ""

    orders[order_id] = data

    save_orders(orders)

    return {"order_id": order_id}

@app.get("/order/{order_id}")
def track(order_id: str):

    orders = load_orders()

    if order_id in orders:
        return orders[order_id]

    return {"error": "not found"}

@app.post("/upload")
def upload(file: UploadFile = File(...)):

    path = f"{UPLOAD_DIR}/{file.filename}"

    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"path": path}

@app.post("/admin/update")
def admin_update(data: dict):

    orders = load_orders()

    order_id = data["order_id"]

    if order_id in orders:

        orders[order_id]["payment_status"] = data["payment_status"]
        orders[order_id]["work_status"] = data["work_status"]
        orders[order_id]["delivery"] = data["delivery"]

        save_orders(orders)

        return {"status": "updated"}

    return {"error": "not found"} 
import json

@app.get("/sections")
def get_sections():
    with open("sections.json") as f:
        return json.load(f)

@app.post("/add-section")
def add_section(section: dict):
    with open("sections.json") as f:
        data = json.load(f)

    data.append(section)

    with open("sections.json", "w") as f:
        json.dump(data, f)

    return {"status": "ok"}
