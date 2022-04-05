"""
Modules to handle JSON reponses from APIs. Description and scrapbooking
"""
import pprint

pp = pprint.PrettyPrinter(indent=4)


def scrape(schema, response):
    result = {}
    for key, value in schema.items():
        if isinstance(value, dict):
            if isinstance(response, dict):
                result.update(scrape(value, response[key]))
            elif isinstance(response, list):
                result.update(scrape(value, response[int(key)]))
        else:
            result[value] = response[key]
    return result


def describe(thing):
    if isinstance(thing, dict):
        return {key: describe(value) for key, value in thing.items()}
    if isinstance(thing, list):
        try:
            return [describe(thing[0]), "..."]
        except IndexError:
            return []
    if isinstance(thing, tuple):
        return tuple([describe(item) for item in thing])
    return thing


def p(thing):
    pp.pprint(describe(thing))
