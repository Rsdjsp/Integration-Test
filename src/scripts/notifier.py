"""
This module contains the notify function that sends a notification to the user."""
from collections import Counter

def notify(unemployed_candidates):
    """ Notify user"""
    locations = [candidate[1] for candidate in unemployed_candidates]
    location_counts = Counter(locations)
    most_unemployed_location = max(location_counts, key=location_counts.get, default='Unknown')

    unemployed_count = len(unemployed_candidates)
    log_message = f"Notification: {unemployed_count} candidates are unemployed. The location with the most unemployed is {most_unemployed_location}."
    print(log_message)