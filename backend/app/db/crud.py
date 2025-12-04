fake_db = {}

def save_link(code, original_url):
    fake_db[code] = original_url

def get_link(code):
    return fake_db.get(code)