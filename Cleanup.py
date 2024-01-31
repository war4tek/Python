import os
import shutil
from datetime import datetime

# Specify desktop path
desktop_path = os.path.expanduser("~/Desktop")

# Create a folder name with the current date
current_date = datetime.now().strftime("%Y-%m-%d")
cleanup_folder = os.path.join(desktop_path, f"Cleanup_{current_date}")

# Create the Cleanup folder if it doesn't exist
if not os.path.exists(cleanup_folder):
    os.makedirs(cleanup_folder)

# Get a list of all items (files and folders) on the desktop
items_on_desktop = [item for item in os.listdir(desktop_path) if item != f"Cleanup_{current_date}" and os.path.exists(os.path.join(desktop_path, item))]

# Move each item to the Cleanup folder
for item_name in items_on_desktop:
    source_path = os.path.join(desktop_path, item_name)
    destination_path = os.path.join(cleanup_folder, item_name)

    try:
        shutil.move(source_path, destination_path)
    except (shutil.Error, PermissionError) as e:
        print(f"Failed to move {item_name}: {e}")

print(f"Desktop cleanup completed. Items moved to {cleanup_folder}")
