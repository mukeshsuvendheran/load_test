from config import MAX_TEMP, MAX_RPM

def check_limits(data):
    if data["temperature"] > MAX_TEMP:
        print("⚠ WARNING: Temperature exceeded!")

    if data["rpm"] > MAX_RPM:
        print("⚠ WARNING: RPM exceeded!")