from playwright.sync_api import sync_playwright
import logging
from utils.screenshot import take_screenshot

def check_sim24(username, password):
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()

            logging.info("Öffne Login-Seite...")
            page.goto('https://service.sim24.de/mytariff/invoice/showGprsDataUsage')
            
            logging.info("Führe Login durch...")
            page.fill('input[name="UserLoginType[alias]"]', username)
            page.fill('input[name="UserLoginType[password]"]', password)
            
            page.click('a.c-button.submitOnEnter[title="Login"]')
            take_screenshot(page, "after_login", "sim24")
            
            logging.info("Deny Cookies...")
            consent_button = page.query_selector('#consent_wall_optout')
            if consent_button and consent_button.is_visible():
                consent_button.click()
            else:
                logging.info("Consent button not visible, skipping...")
            
            logging.info("Suche nach Button...")
            try:
                button = page.wait_for_selector('#ButtonBuchen-ChangeServiceType-showGprsDataUsage-0V5I3', timeout=10000)
                stats = page.wait_for_selector('.dataUsageBar-info-numbers', timeout=10000)
                
                if stats:
                    used_data = stats.query_selector('.font-weight-bold').inner_text()
                    total_data = stats.query_selector('.l-txt-small').inner_text().replace('von', '').strip()
                    logging.info(f"Verbrauchte Daten: {used_data} von {total_data}")
                    take_screenshot(page, "usage_page", "sim24")
                
                if button:
                    is_disabled = button.get_attribute('disabled') is not None
                    
                    if is_disabled:
                        logging.info("Button gefunden, aber deaktiviert")
                    else:
                        logging.info("Button gefunden und aktiv - Klicke...")
                        button.click()
                        logging.info("Button erfolgreich geklickt")
                    
                        page.click('#ButtonAktivieren-ChangeServiceType-getChangeServiceInfo-1V5I3')
                        take_screenshot(page, "after_booking", "sim24")
                    
                        logging.info("Prozess erfolgreich beendet")
                        return
                else:
                    logging.warning("Button nicht gefunden")
                
            except Exception as e:
                logging.warning(f"Button nicht gefunden oder nicht klickbar: {str(e)}")
            
            logging.info("Schließe Browser")
            browser.close()
            
    except Exception as e:
        logging.error(f"Fehler bei der Ausführung: {str(e)}") 