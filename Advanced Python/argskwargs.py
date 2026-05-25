# Args = Arguments
def total(a: int, *args):
    return a + sum(args)


# print(total(10, 10, 10))
# print(total(10, 10))
# print(total(10))
# print(total(10, 10, 10, 10))


# Kwargs = key words arguments
def log_event(level, message, **kwargs):
    log = f"{level.upper()} | {message}"
    for key, value in kwargs.items():
        log += f" | {key}={value}"
    print(log)


log_event(
    "info", "Польозватель зарегестрировался", user_id=12, ip_address="192.168.0.1"
)
log_event("error", "Ошибка сохранения", table="users", query="SELECT * from USERS;")
