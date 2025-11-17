"""
Menu and user interface management for the BioMarket system.
"""

import sys
from src.models.warehouse import Warehouse
from src.models.product import Product
from src.models.sales import SalesManager
from src.utils.input_validator import InputValidator


class MenuManager:
    """
    Manages the main menu and user interactions.
    """
    
    def __init__(self):
        """Initialize the MenuManager."""
        self.validator = InputValidator()
        self.sales_manager = SalesManager()
    
    def run(self):
        """Main loop for the menu system."""
        while True:
            try:
                choice = self.display_menu()
                self.handle_choice(choice)
            except Exception as e:
                print(f"\n[ERRORE] {e}\n")
    
    def display_menu(self):
        """
        Display the main menu and get user choice.
        
        Returns:
            str: User's menu choice
        """
        print("\n" + "="*50)
        print("        BIOMARKET - MENU PRINCIPALE")
        print("="*50)
        print("\n1. Aggiungi prodotto")
        print("2. Vendita prodotto")
        print("3. Profitti")
        print("4. Esci")
        print("\n" + "-"*50)
        
        choice = input("\nScelta utente: ").strip()
        return choice
    
    def handle_choice(self, choice):
        """
        Handle user's menu choice.
        
        Args:
            choice (str): User's menu selection
        """
        if choice == "1":
            self.add_product_flow()
        elif choice == "2":
            self.sell_product_flow()
        elif choice == "3":
            self.show_profits()
        elif choice == "4":
            self.exit_program()
        else:
            print("\n[ERRORE] Scelta non valida. Inserire un numero da 1 a 4.\n")
    
    def add_product_flow(self):
        """Handle the product addition workflow."""
        try:
            print("\n" + "="*50)
            print("           AGGIUNGI PRODOTTO")
            print("="*50 + "\n")
            
            warehouse_name = self.select_warehouse()
            warehouse = Warehouse(name=warehouse_name)
            
            print("\n" + "-"*50)
            print("Inserisci i dati del prodotto:")
            print("-"*50)
            
            product_name = self.validator.get_non_empty_string("\nNome prodotto: ")
            quantity = self.validator.get_positive_integer("Quantità: ")
            purchase_price = self.validator.get_positive_float("Prezzo di acquisto (€): ")
            sale_price = self.validator.get_positive_float("Prezzo di vendita (€): ")
            
            product = Product(
                name=product_name,
                quantity=quantity,
                purchase_price=purchase_price,
                sale_price=sale_price
            )
            
            warehouse.add_product(product)
            
        except ValueError as e:
            print(f"\n[ERRORE] {e}\n")
        except Exception as e:
            print(f"\n[ERRORE] Impossibile aggiungere il prodotto: {e}\n")
    
    def sell_product_flow(self):
        """Handle the product sale workflow."""
        try:
            print("\n" + "="*50)
            print("           VENDITA PRODOTTO")
            print("="*50 + "\n")
            
            warehouse_name = self.select_warehouse()
            warehouse = Warehouse(name=warehouse_name)
            
            print("\n" + "-"*50)
            print("Inserisci i dati della vendita:")
            print("-"*50)
            
            product_name = self.validator.get_non_empty_string("\nProdotto da vendere: ")
            
            if not warehouse.product_exists(product_name):
                print(f"\n[ERRORE] Prodotto '{product_name}' non presente nel magazzino\n")
                return
            
            quantity = self.validator.get_positive_integer("Quantità da vendere: ")
            
            # Get product details
            product_data = warehouse.get_product(product_name)
            
            if int(product_data["quantita"]) < quantity:
                print(f"\n[ERRORE] Quantità insufficiente!")
                print(f"         Disponibile: {product_data['quantita']}, Richiesto: {quantity}\n")
                return
            
            # Update warehouse quantity
            warehouse.update_product_quantity(product_name, -quantity)
            
            # Record sale
            profit = self.sales_manager.record_sale(
                product_name=product_name,
                quantity=quantity,
                purchase_price=float(product_data["prezzo di acquisto"]),
                sale_price=float(product_data["prezzo di vendita"])
            )
            
            print(f"\n[OK] Vendita effettuata con successo!")
            print(f"[OK] Profitto dalla vendita: €{profit:.2f}")
            print(f"[OK] Magazzino aggiornato: {warehouse_name}\n")
            
        except ValueError as e:
            print(f"\n[ERRORE] {e}\n")
        except Exception as e:
            print(f"\n[ERRORE] Impossibile completare la vendita: {e}\n")
    
    def show_profits(self):
        """Display total profits."""
        try:
            print("\n" + "="*50)
            print("              PROFITTI")
            print("="*50)
            
            gross_profit, net_profit = self.sales_manager.calculate_profits()
            
            print(f"\nProfitto Lordo:  €{gross_profit:.2f}")
            print(f"Profitto Netto:  €{net_profit:.2f}")
            print("\n" + "="*50 + "\n")
            
        except Exception as e:
            print(f"\n[ERRORE] Impossibile calcolare i profitti: {e}\n")
    
    def select_warehouse(self):
        """
        Allow user to select or create a warehouse.
        
        Returns:
            str: Selected warehouse name
        """
        warehouses = Warehouse.list_warehouses()
        
        if warehouses:
            print("\nMagazzini disponibili:")
            print("-"*50)
            for i, warehouse in enumerate(warehouses, 1):
                print(f"{i}. {warehouse}")
            print("-"*50)
        else:
            print("\nNessun magazzino esistente.")
        
        warehouse_name = self.validator.get_non_empty_string(
            "\nScegli magazzino (o inserisci un nuovo nome): "
        )
        
        return warehouse_name
    
    def exit_program(self):
        """Exit the application."""
        print("\n" + "="*50)
        print("    Grazie per aver usato BioMarket!")
        print("          Programma terminato")
        print("="*50 + "\n")
        sys.exit(0)
