

def transform(db):
    return {
        v.lower(): k
        for k, items in db.items()
        for v in items
    }
