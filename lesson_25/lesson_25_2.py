from datetime import datetime
from datetime import date
from datetime import timedelta
from time import sleep

mydatetime = datetime.fromtimestamp(1706551390)
print(mydatetime)

# Створення об'єкта datetime за допомогою порядкового номера дня
ordinal_day = 365 # Порядковий номер дня
dt = datetime.fromordinal(ordinal_day)
print(dt)
# Вивід: 0001-12-31 00:00:00 # 31 грудня 1 року
day_number = datetime.today().toordinal()
print(f'Порядковий номер сьогоднішнього дня: {day_number}')
print(datetime.today())
print(date.today())
current_datetime = datetime.now()
print("Поточна дата і час:", current_datetime)


incoming_date = "Aug 24, 1991"
dt_incoming_date = datetime.strptime(incoming_date, '%b %d, %Y')
print(dt_incoming_date)
nix_time_now = dt_incoming_date.strftime("%H:%M:%S and %Y-%m-%d")
print(nix_time_now)
sleep(1)
current_datetime_new = datetime.now()
print("Нова дата", current_datetime_new)
print(current_datetime_new == current_datetime)
print(current_datetime_new - current_datetime <= timedelta(seconds=2))
dt_01 = "19:45:23"
dt_02 = "20:00:22"
dt_03 = "20:00:27"

dt_01_dt = datetime.strptime(dt_01, "%H:%M:%S")
dt_02_dt = datetime.strptime(dt_02, "%H:%M:%S")
dt_03_dt = datetime.strptime(dt_03, "%H:%M:%S")
print(dt_01_dt)
print(dt_02_dt)
if dt_02_dt - dt_01_dt <= timedelta(minutes=15):
    print("yes")
else:
    print("no")

if dt_03_dt - dt_02_dt <= timedelta(seconds=30):
    print("yes")
else:
    print("no")
d = datetime.today()
print(d)
print(d.isocalendar())
print(d.isoformat())
print(d.isoweekday())
print(d.timetuple())
print(d.weekday())
dd = d.replace(year=2023, day=12)
print(dd)

td = timedelta(days=5, hours=3, minutes=30)
print(td)
total_seconds = td.total_seconds()
print(total_seconds)