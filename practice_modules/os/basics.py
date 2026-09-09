import os
from pathlib import Path
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parents[2]
ENV_PATH = PROJECT_ROOT / ".env"

load_dotenv(ENV_PATH)

orders_path = os.getenv("ORDERS_PATH")
app_env = os.getenv("APP_ENV")
timeout = os.getenv("TIMEOUT", "30")

if not orders_path:
    print(f"ORDERS_PATH is missing")


print(f"Orders path: {orders_path}")
print(f"Environment: {app_env}")
print(f"Timeout: {timeout}")

# Ha az összes env változót akarom berakni egybe:
env_variables = os.environ

print(f"orders_path: {env_variables['ORDERS_PATH']}")