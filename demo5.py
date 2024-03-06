import random

def display_introduction():
    intro1 = '''In 2100 AD, in the face of changes in the world's environment, population growth, and resource shortages, governments around the world jointly funded the construction of five giant Noah's Arks. These Arks - carrying tens of thousands of colonists from all walks of life - venture into a wormhole discovered decades ago in search of humanity's future. After they entered the wormhole one after another, no more signals were received on the earth.
No one knew that after going through many hardships, the two Arks narrowly escaped the wormhole, landed on a habitable planet that was very similar to the Earth, and established a prosperous colony.
'''
    print(intro1)
    intro2 = '''After struggling to gain a foothold in a strange land and finally developing mature intergalactic navigation technology, these humans embarked on a new exploration plan.'''
    print(intro2)
    print("You are now the leader of this great civilization. Will you lead mankind to unprecedented glory, or to destruction?")

def enter_civilization_details():
    civilization_name = input("Enter the name of your civilization: ")
    leader_name = input("Enter your leader's name: ")
    return civilization_name, leader_name

def choose_origin():
    print("Choose your political system and ideology:")
    print("1. Democracy/Pacifism")
    print("2. Democracy/Idealism")
    print("3. Democracy/Xenophilia")
    print("4. Empire/Militarism")
    print("5. Empire/Exclusivism")
    print("6. Empire/Theocracy")
    print("7. Oligarchy/Authoritarianism")
    print("8. Oligarchy/Materialism")
    print("9. Hive Society/Hive Mind")
    choice = input("Enter the number of your choice: ")
    return int(choice)

def initialize_resources(origin):
    if origin == 1:  
        return 10, 5, 5, 10
    elif origin == 2:  
        return 5, 10, 10, 5

def generate_resources(origin, colonizer, research_ship, construction_ship, fleet, event_choice=None):
    if origin == 1:  
        if event_choice == 1:
            colonizer += 2
            research_ship += 1
            construction_ship += 1
            fleet += 2
        elif event_choice == 2:
            fleet += 5
            research_ship += 3
    elif origin == 2:  
        if event_choice == 1:
            colonizer += 1
            research_ship += 2
            construction_ship += 2
            fleet += 1
        elif event_choice == 2:
            colonizer += 3
            research_ship += 2
            construction_ship += 1
    return colonizer, research_ship, construction_ship, fleet

def display_resources(colonizer, research_ship, construction_ship, fleet):
    print("Resources:")
    print(f"Colonizer: {colonizer}")
    print(f"Research Ship: {research_ship}")
    print(f"Construction Ship: {construction_ship}")
    print(f"Fleet: {fleet}\n")

def add_extra_resource(colonizer, research_ship, construction_ship, fleet):
    print("Choose one resource to add:")
    print("1. Colonizer")
    print("2. Research Ship")
    print("3. Construction Ship")
    print("4. Fleet")
    choice = int(input("Enter the number of your choice: "))
    if choice == 1:
        colonizer += 1
    elif choice == 2:
        research_ship += 1
    elif choice == 3:
        construction_ship += 1
    elif choice == 4:
        fleet += 1
    return colonizer, research_ship, construction_ship, fleet

def handle_event(colonizer, research_ship, construction_ship, fleet, origin, completed_events, round_count=1):
    events = [
        {
            "name": "Resource",
            "description": "rrrrrrrrrrrrr.",
            "trigger_conditions": {"Colonizer": 15, "Fleet": 15},
            "origin_requirement": None,
            "options": [
                {
                    "text": "Option1:pppppppppppp.",
                    "resource_changes": {"Colonizer": -5, "Research_Ship": 2},
                    "probability": 0.8,
                    "subsequent_event": "Event 2 option1"
                },
                {
                    "text": "Trade excess resources for advanced technology.",
                    "resource_changes": {"Fleet": 5, "Research_Ship": 3},
                    "probability": 0.6,
                    "subsequent_event": "Event 2 option2"
                }
            ],
            "dependencies": []  # No dependencies for the first event
        },
        {
            "name": "Event 2 option1",
            "description": "222222222",
            "trigger_conditions": {"Colonizer": 15, "Construction_Ship": 15},
            "origin_requirement": None,
            "options": [
                {
                    "text": "Option1: building more colonies.",
                    "resource_changes": {"Colonizer": -3, "Construction_Ship": -2, "Research_Ship": 1},
                    "probability": 0.7,
                    "subsequent_event": "Event3.1 Option1"
                },
                {
                    "text": "Option2: no",
                    "resource_changes": {"Construction_Ship": 3, "Research_Ship": 2},
                    "probability": 0.5,
                    "subsequent_event": "Event3.1 Option2"
                }
            ],
            "dependencies": ["Resource"]
        },
        {
            "name": "Event 2 option2",
            "description": "tech",
            "trigger_conditions": {"Research_Ship": 30, "Fleet": 30},
            "origin_requirement": None,
            "options": [
                {
                    "text": "Option1: yes",
                    "resource_changes": {"Fleet": 5, "Research_Ship": -2},
                    "probability": 0.6,
                    "subsequent_event": "Event3.2 option1"
                },
                {
                    "text": "Option2: ok",
                    "resource_changes": {"Construction_Ship": 3, "Research_Ship": 4},
                    "probability": 0.8,
                    "subsequent_event": "Event3.2 option2"
                }
            ],
            "dependencies": ["Resource"]
        },
        # More events
    ]

    available_events = [event for event in events if event["name"] not in completed_events]
    triggered_events = []

    for event in available_events:
        # Check the event dependencies 
        if all(dependency in completed_events for dependency in event.get("dependencies", [])):
            # Check the trigger condition
            trigger_conditions_met = trigger_condition_met(colonizer, research_ship, construction_ship, fleet, event["trigger_conditions"])
            if trigger_conditions_met:
                # Calculate the probability of triggering with round count
                probability = min(0.4 + (round_count - 1) * 0.1, 1.0)

                # Simulate event trigger with the probability
                if random.random() < probability:
                    print("\nEvent:", event["name"])
                    print("Description:", event["description"])

                    display_event_options(event["options"])

                    # Get player choice
                    player_choice = int(input("Enter your choice: "))

                    # Modify resources based on player's choice
                    resource_changes = event["options"][player_choice - 1]["resource_changes"]
                    colonizer, research_ship, construction_ship, fleet = generate_resources(
                        origin, colonizer, research_ship, construction_ship, fleet, player_choice
                    )

                    # Add the event to completed events and triggered events
                    completed_events.append(event["name"])
                    triggered_events.append(event["name"])

                    # Check the subsequent event
                    subsequent_event_name = event["options"][player_choice - 1].get("subsequent_event")
                    if subsequent_event_name:
                        completed_events.append(subsequent_event_name)

    return colonizer, research_ship, construction_ship, fleet, completed_events, triggered_events

def trigger_condition_met(colonizer, research_ship, construction_ship, fleet, trigger_conditions):
    for resource, amount in trigger_conditions.items():
        resource_value = locals().get(resource.lower())
        if resource_value is None or resource_value < amount:
            return False
    return True

def display_event_options(options):
    print("Options:")
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option['text']}")

def determine_victory(colonizer, research_ship, construction_ship, fleet):
    # Check victory conditions
    if colonizer >= 30 and research_ship >= 20 and construction_ship >= 20 and fleet >= 30:
        print("Congratulations! You have achieved victory!")
        exit()

def main():
    display_introduction()

    civilization_name, leader_name = enter_civilization_details()
    print(f"Welcome, Leader {leader_name}, to the civilization of {civilization_name}.")

    origin = choose_origin()

    colonizer, research_ship, construction_ship, fleet = initialize_resources(origin)
    completed_events = []
    round_count = 1

    for round in range(1, 21):
        print(f"\n----- Round {round} -----")

        colonizer, research_ship, construction_ship, fleet, completed_events, triggered_events = handle_event(
            colonizer, research_ship, construction_ship, fleet, origin, completed_events, round_count
        )

        if triggered_events:
            print("\nTriggered events:")
            for event_name in triggered_events:
                print(f"- {event_name}")

        colonizer, research_ship, construction_ship, fleet = generate_resources(
            origin, colonizer, research_ship, construction_ship, fleet
        )
        colonizer, research_ship, construction_ship, fleet = add_extra_resource(
            colonizer, research_ship, construction_ship, fleet
        )
        display_resources(colonizer, research_ship, construction_ship, fleet)

        determine_victory(colonizer, research_ship, construction_ship, fleet)

        round_count += 1

    print("Game Over. You have completed 20 rounds.")

main()