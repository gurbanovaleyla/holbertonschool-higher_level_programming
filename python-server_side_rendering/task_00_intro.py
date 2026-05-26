def generate_invitations(template, attendees):

    # Validate template type
    if not isinstance(template, str):
        print("Error: template must be a string.")
        return

    # Validate attendees type
    if not isinstance(attendees, list):
        print("Error: attendees must be a list.")
        return

    # Validate each attendee
    for attendee in attendees:
        if not isinstance(attendee, dict):
            print("Error: attendees must contain dictionaries only.")
            return

    # Check empty template
    if template == "":
        print("Template is empty, no output files generated.")
        return

    # Check empty attendees
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Process attendees
    for index, attendee in enumerate(attendees, start=1):

        # Create fresh copy
        personalized = template

        # Replace placeholders
        personalized = personalized.replace(
            "{name}",
            str(attendee.get("name") or "N/A")
        )

        personalized = personalized.replace(
            "{event_title}",
            str(attendee.get("event_title") or "N/A")
        )

        personalized = personalized.replace(
            "{event_date}",
            str(attendee.get("event_date") or "N/A")
        )

        personalized = personalized.replace(
            "{event_location}",
            str(attendee.get("event_location") or "N/A")
        )

        # Create filename
        filename = f"output_{index}.txt"

        # Write file
        with open(filename, "w") as file:
            file.write(personalized)
