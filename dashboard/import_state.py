import json
from chatroom.models import Country, State


def loadstate():
    with open('dashboard/states.json') as f:
        data = json.load(f)
        counter = 0
        for state in data:
            counter += 1
            state_name = state['name']
            country_name = state['country_name']
            try:
                country = Country.objects.get(name=country_name)
                state = State.objects.get_or_create(country=country, name=state_name)
                print(f"{counter} - {state}")
            except Country.DoesNotExist:
                print(f"{country_name} is not found in country list")
        print(f"Total State: {counter}")
