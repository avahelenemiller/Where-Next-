# WHERE NEXT? - Travel Destination Recommender

destinations = [
    {
        "name": "Bali",
        "budget": "mid",
        "climate": "warm",
        "holiday_type": "relaxing",
        "activities": ["swimming", "surfing", "walking"]
    },
    {
        "name": "Tokyo",
        "budget": "mid",
        "climate": "temperate",
        "holiday_type": "city",
        "activities": ["shopping", "food", "culture"]
    },
    {
        "name": "Queenstown",
        "budget": "mid",
        "climate": "cool",
        "holiday_type": "adventure",
        "activities": ["hiking", "skiing", "nature"]
    },
    {
        "name": "Fiji",
        "budget": "luxury",
        "climate": "warm",
        "holiday_type": "relaxing",
        "activities": ["swimming", "snorkelling", "beach"]
    },
        {
        "name": "New York",
        "budget": "luxury",
        "climate": "cool",
        "holiday_type": "city",
        "activities": ["shopping", "food", "sightseeing"]
    },
    {
        "name": "Paris",
        "budget": "luxury",
        "climate": "temperate",
        "holiday_type": "city",
        "activities": ["food", "shopping", "culture"]
    },
    {
        "name": "Bangkok",
        "budget": "budget",
        "climate": "warm",
        "holiday_type": "city",
        "activities": ["food", "shopping", "culture"]
    },
    {
        "name": "Gold Coast",
        "budget": "mid",
        "climate": "warm",
        "holiday_type": "relaxing",
        "activities": ["swimming", "surfing", "beach"]
    }
]
if __name__ == "__main__":
        # Ask the user about their ideal holiday

        print("✈️ WHERE NEXT?")
        print("Let's find your perfect travel destination!")

        budget = input("Choose a budget (budget, mid, luxury): ").strip().lower()

        climate = input("Choose a climate (warm, temperate, cool): ").strip().lower()

        holiday_type = input(
            "Choose a holiday style (relaxing, city, adventure): "
        ).strip().lower()

        activities_input = input(
            "Enter your favourite activities separated by commas: "
        ).lower()

        activities = [activity.strip() for activity in activities_input.split(",")]
        # Compare the user's preferences with each destination

        best_destination = None
        best_score = -1

        for destination in destinations:
            score = 0

            if budget == destination["budget"]:
                score += 1

            if climate == destination["climate"]:
                score += 1

            if holiday_type == destination["holiday_type"]:
                score += 1

            for activity in activities:
                if activity in destination["activities"]:
                    score += 1

            if score > best_score:
                best_score = score
                best_destination = destination


        # Show the best matching destination

        print("\n Your recommended destination is:")
        print(best_destination["name"])
        print("Match score:", best_score)

            
