from rapidfuzz import process, fuzz

def fuzzy_match_city(query, choices):
    """
    Returns best matching city/state name for a query string.
    """
    match, score, idx = process.extractOne(query, choices, scorer=fuzz.token_sort_ratio)
    return match, score
