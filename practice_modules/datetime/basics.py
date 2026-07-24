from datetime import datetime, date, timedelta

#  mostani dátum/idő
now = datetime.now()
print(now)

#  mai dátum
today = date.today()
print(today)

# saját dátum létrehozás
birthday = date(1995, 5, 20)
birthday_time = datetime(1995, 5, 20, 9, 30)
print(birthday)
print(birthday_time)

# stringből dátum
raw_date = "2026-07-24"
parsed_date = date.fromisoformat(raw_date)

# datetime-nál:
raw_datetime = "2026-07-24T09:30:00"
parsed_datetime = datetime.fromisoformat(raw_datetime)

# dátum formázás stringgé
now = datetime.now()
formatted = now.strftime("%Y-%m-%d")

# Idő különbség
today = date.today()
tomorrow = today + timedelta(days=1)
yesterday = today - timedelta(days=1)

raw_date = "2026-07-20T09:14:32Z"

created_at = datetime.fromisoformat(
    raw_date.replace("Z", "+00:00")
)

print(created_at)

# csak a dátum kiszedése

order_date = created_at.date()
print(order_date)
order_date_mod = str(order_date).replace("-", ".")
print(order_date_mod)

