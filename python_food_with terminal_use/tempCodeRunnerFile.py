for key, value in food.__dict__.items():
    if not key.startswith("__"):
        print(f"{key}: {value}")