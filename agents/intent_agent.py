import re


class IntentAgent:

    def extract_intent(self, user_message):
        text = user_message.lower()

        intent = {
            "destination": None,
            "budget": None,
            "duration_days": None,
            "category": "travel"
        }

        # -------------------------
        # Destination Detection
        # -------------------------
        destinations = [
            "goa",
            "manali",
            "jaipur"
        ]

        for destination in destinations:
            if destination in text:
                intent["destination"] = destination.title()
                break

        # -------------------------
        # Budget Detection
        # -------------------------
        budget_patterns = [
            r"(?:under|below|within|budget|around|upto|up to)\s*[₹rs.]?\s*(\d+(?:,\d+)?)\s*(k|thousand|lakh)?",
            r"[₹rs.]\s*(\d+(?:,\d+)?)\s*(k|thousand|lakh)?"
        ]

        for pattern in budget_patterns:
            match = re.search(pattern, text)

            if match:
                amount = int(match.group(1).replace(",", ""))
                multiplier = match.group(2)

                if multiplier:
                    multiplier = multiplier.lower()

                    if multiplier in ["k", "thousand"]:
                        amount *= 1000
                    elif multiplier == "lakh":
                        amount *= 100000

                intent["budget"] = amount
                break

        # -------------------------
        # Duration Detection
        # -------------------------
        duration_patterns = [
            r"(\d+)\s*(?:day|days|din)",
            r"(\d+)\s*(?:night|nights)"
        ]

        for pattern in duration_patterns:
            match = re.search(pattern, text)

            if match:
                intent["duration_days"] = int(match.group(1))
                break

        return intent


if __name__ == "__main__":

    agent = IntentAgent()

    message = input("\nEnter customer request: ")

    result = agent.extract_intent(message)

    print("\nDetected Customer Intent:")
    print(result)