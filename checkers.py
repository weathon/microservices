def people(text):
    if not "landlord" in text or not "tenant" in text:
        return "The landlord or tenant field might be missing"

    return "Included"

def starting_date(text):
    synonyms = ["starting date","move in date", "starts on:"]
    for synonym in synonyms:
        if synonym in text:
            return "Included"
    return "The starting date might be missing."

def address(text):
    return "Included"

def end_date(text):
    synonyms = ["continues on a month-to-month basis", "continues on another periodic basis", "a fixed term ending on"]
    for synonym in synonyms:
        if synonym in text:
            return "Included"
    return "The ending date might be missing."


def rent_price(text):
    return "Did not check for rent price!"

def pay_day(text):
    return "Did not check for pay_day!"

def notice_before_rent_increase(text):
    synonyms = ["rent increase"]
    for synonym in synonyms:
        if synonym in text:
            return "Included"
    return "The rent increase policy might be missing."

def security_deposit(text):
    if "security deposit" in text:
        return "Included"
    return "The security deposit policy might be missing."

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


checkers = [people, end_date, starting_date, address, rent_price, pay_day, notice_before_rent_increase, security_deposit, smoking, pet, utilities]
