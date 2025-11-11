def generate_invitations(template, attendees):
    # Vérifie types
    if not isinstance(template, str):
        print("Error: Template is not a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: Attendees is not a list of dictionaries.")
        return

    # Cas template vide
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    # Cas liste vide
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # Pour chaque invité : substitution + écriture fichier
    for i, attendee in enumerate(attendees, start=1):
        values = {}  # dictionnaire pour stocker les valeurs à injecter
        for key in ['name', 'event_title', 'event_date', 'event_location']:
            value = attendee.get(key, 'N/A')
            if value is None or value == "":
                value = 'N/A'
            values[key] = value

        # Substitution
        invitation_text = template
        for key, value in values.items():
            invitation_text = invitation_text.replace(f"{{{key}}}", value)

        # Écriture dans fichier
        output_filename = f"output_{i}.txt"
        try:
            with open(output_filename, "w", encoding="utf-8") as f:
                f.write(invitation_text)
        except Exception as e:
            print(f"Error writing file {output_filename}: {e}")
