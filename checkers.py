def people(text):
    if not "landlord" in text or not "tenant" in text:
        return "The landlord or tenant field might be missing"

    return "Included"

def starting_date(text):
    return "Included"


def end_date(text):
    return "Included"

def rent_price(text):
    return "Included"

def pay_day(text):
    return "Included"

def notice_before_rent_increase(text):
    return "Included"   

def security_deposit(text):
    return "Included"

def smoking(text):
    synonyms = ["smoking","cigarette","vape", "marijuana", "weed", "hemp", "cannabis"]
    for synonym in synonyms:
        if synonym in text:
            return "Included"
    return "The smoking policy might be missing."

def pet(text):
    if "pet" in text or "pets" in text:
        return "Included"
    return "The pets policy might be missing."

def utilities(text):
    synonyms = ["utilities","water bills","electricity bills"]
    for synonym in synonyms:
        if synonym in text:
            return "Included"
    return "The utilities policy might be missing."


checkers = [people, end_date, starting_date, adress, rent_price, pay_day, notice_before_rent_increase, security_deposit, smoking, pet, utilities]
