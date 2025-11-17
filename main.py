"""
BioMarket Management System
Main entry point for the application.
"""

import sys
from src.ui.menu import MenuManager
from src.utils.logger import setup_logger


def main():
    """Main function to run the BioMarket management system."""
    logger = setup_logger()
    
    try:
        logger.info("=== BioMarket Management System Started ===\n")
        menu_manager = MenuManager()
        menu_manager.run()
        
    except KeyboardInterrupt:
        print("\n\n[INFO] Programma interrotto dall'utente")
        logger.info("Program interrupted by user")
        sys.exit(0)
        
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        print(f"\n[ERRORE] Si è verificato un errore inaspettato: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
