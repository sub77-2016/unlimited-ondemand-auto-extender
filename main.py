import time
from datetime import datetime
from playwright.sync_api import sync_playwright
import logging
from dotenv import load_dotenv
import os
from checker.sim24 import check_sim24
from checker.oneandone import check_1und1

load_dotenv()

SERVICE = os.getenv("SERVICE")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
CHECK_INTERVAL = int(os.getenv("CHECK_INTERVAL"))

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - [%(prefix)s] %(message)s',
    handlers=[
        logging.FileHandler('automation.log'),
        logging.StreamHandler()
    ]
)

class PrefixFilter(logging.Filter):
    def __init__(self, prefix=""):
        self.prefix = prefix
        super().__init__()

    def filter(self, record):
        record.prefix = self.prefix
        return True

logging.getLogger().addFilter(PrefixFilter(SERVICE))

def main():
    logging.info("Starte Automatisierung...")
    
    while True:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        logging.info(f"Starte neue Überprüfung um {current_time}")
        
        try:
            if SERVICE == "sim24":
                check_sim24(USERNAME, PASSWORD)
            elif SERVICE == "1und1":
                check_1und1(USERNAME, PASSWORD)
            else:
                logging.error(f"Unbekannte Service-ID: {SERVICE}")
        except Exception as e:
            logging.error(f"Fehler im Hauptprozess: {str(e)}")
        
        logging.info(f"Warte {CHECK_INTERVAL} Sekunden bis zur nächsten Überprüfung...")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()
