import os
import glob
from datetime import datetime, timedelta
import time

def take_screenshot(page, name, service):
    """
    Creates a screenshot and saves it with a timestamp.
    Deletes old screenshots with the same name, if they are older than 1 minute.
    """
    os.makedirs('screenshots', exist_ok=True)
    
    old_screenshots = glob.glob(f'screenshots/{service}_{name}_*.png')
    current_time = datetime.now()
    
    for old_screenshot in old_screenshots:
        try:
            timestamp_str = old_screenshot.split('_')[-1].replace('.png', '')
            file_time = datetime.strptime(timestamp_str, "%Y%m%d_%H%M%S")
            
            if current_time - file_time > timedelta(minutes=1):
                os.remove(old_screenshot)
        except Exception as e:
            print(f"Fehler beim Verarbeiten von {old_screenshot}: {e}")
    
    timestamp = current_time.strftime("%Y%m%d_%H%M%S")
    filename = f'screenshots/{service}_{name}_{timestamp}.png'
    page.screenshot(path=filename) 