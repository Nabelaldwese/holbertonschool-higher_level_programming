#!/usr/bin/python3
"""
Task 0: Creating a Simple Templating Program
Generate invitation files from a template and a list of attendees.
"""

import os


def generate_invitations(template, attendees):
    """
    Generate output_X.txt files based on a template and a list of attendee dicts.

    Args:
        template (str): Template content containing placeholders:
                        {name}, {event_title}, {event_date}, {event_location}
        attendees (list): List of dictionaries with keys matching placeholders.

    Behaviors:
        - Empty template -> print message and return (no files created)
        - Empty attendees -> print message and return (no files created)
        - Missing or None values -> replace with "N/A"
        - Invalid input types -> print error and return
    """
    # Validate types
    if not isinstance(template, str):
        print(f"Invalid input type: template must be a string, got {type(template).__name__}.")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        got_type = type(attendees).__name__
        print("Invalid input type: attendees must be a list of dictionaries, "
              f"got {got_type}.")
        return

    # Handle empty inputs
    if template == "":
        print("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    placeholders = ["name", "event_title", "event_date", "event_location"]

    for idx, attendee in enumerate(attendees, start=1):
        content = template

        for key in placeholders:
            value = attendee.get(key, "N/A")
            if value is None:
                value = "N/A"
            content = content.replace("{" + key + "}", str(value))

        filename = f"output_{idx}.txt"

        # Optional existence check (hinted). We still overwrite to ensure output is generated.
        if os.path.exists(filename):
            pass

        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(content)
        except OSError as exc:
            print(f"Error writing file {filename}: {exc}")
