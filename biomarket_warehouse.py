"""
Warehouse management for the BioMarket system.
"""

import csv
import os
from typing import List, Optional
from src.models.product import Product


class Warehouse:
    """
    Manages warehouse operations including product storage and retrieval.
    
    Attributes:
        name (str): Name/path of the warehouse CSV file
        fieldnames (list): CSV column headers
    """
    
    FIELDNAMES = ["nome", "quantita", "prezzo di acquisto", "prezzo di vendita"]
    
    def __init__(self, name=''):
        """
        Initialize a new Warehouse instance.
        
        Args:
            name (str): Warehouse file name (without .csv extension)
        """
        self.name = name if name.endswith(".csv") else f"{name}.csv"
        self._ensure_file_exists()
    
    def _ensure_file_exists(self):
        """Create warehouse file with headers if it doesn't exist."""
        try:
            if not os.path.exists(self.name):
                with open(self.name, "w", newline='', encoding='utf-8') as f:
                    writer = csv.DictWriter(f, fieldnames=self.FIELDNAMES)
                    writer.writeheader()
        except (IOError, OSError) as e:
            raise IOError(f"Cannot create warehouse file {self.name}: {e}")
    
    @staticmethod
    def warehouse_exists(warehouse_name):
        """
        Check if a warehouse file exists.
        
        Args:
            warehouse_name (str): Name of the warehouse file
            
        Returns:
            bool: True if warehouse exists, False otherwise
        """
        filename = warehouse_name if warehouse_name.endswith(".csv") else f"{warehouse_name}.csv"
        return os.path.exists(filename)
    
    @staticmethod
    def list_warehouses():
        """
        List all available warehouse CSV files in the current directory.
        
        Returns:
            list: List of warehouse filenames
        """
        return [f for f in os.listdir(".") if f.endswith(".csv") and f != "vendite.csv"]
    
    def add_product(self, product):
        """
        Add a product to the warehouse or update existing product quantity.
        
        Args:
            product (Product): Product instance to add
            
        Raises:
            IOError: If file operations fail
            ValueError: If product data is invalid
        """
        try:
            existing_products = self._read_all_products()
            product_updated = False
            
            for row in existing_products:
                if row["nome"] == product.name:
                    # Update existing product
                    row["quantita"] = str(int(row["quantita"]) + product.quantity)
                    
                    # Check if prices changed
                    if (float(row["prezzo di acquisto"]) != product.purchase_price or 
                        float(row["prezzo di vendita"]) != product.sale_price):
                        row["prezzo di acquisto"] = str(product.purchase_price)
                        row["prezzo di vendita"] = str(product.sale_price)
                        print(f"\n[OK] Prezzi di acquisto/vendita aggiornati per '{product.name}'")
                    else:
                        print(f"\n[OK] Quantità aggiornata per '{product.name}'")
                    
                    product_updated = True
                    break
            
            if not product_updated:
                # Add new product
                existing_products.append(product.to_dict())
                print(f"\n[OK] Nuovo prodotto aggiunto: '{product.name}' x {product.quantity}")
            
            self._write_all_products(existing_products)
            print(f"[OK] Magazzino aggiornato: {self.name}\n")
            
        except (IOError, OSError) as e:
            raise IOError(f"Error updating warehouse: {e}")
        except ValueError as e:
            raise ValueError(f"Invalid product data: {e}")
    
    def product_exists(self, product_name):
        """
        Check if a product exists in the warehouse.
        
        Args:
            product_name (str): Name of the product to check
            
        Returns:
            bool: True if product exists, False otherwise
        """
        try:
            products = self._read_all_products()
            return any(row["nome"] == product_name for row in products)
        except (IOError, FileNotFoundError):
            return False
    
    def get_product(self, product_name):
        """
        Retrieve product information from warehouse.
        
        Args:
            product_name (str): Name of the product
            
        Returns:
            dict or None: Product data as dictionary, or None if not found
        """
        try:
            products = self._read_all_products()
            for row in products:
                if row["nome"] == product_name:
                    return row
            return None
        except (IOError, FileNotFoundError):
            return None
    
    def update_product_quantity(self, product_name, quantity_change):
        """
        Update product quantity (for sales).
        
        Args:
            product_name (str): Name of the product
            quantity_change (int): Quantity to subtract (negative value)
            
        Raises:
            ValueError: If insufficient quantity or product not found
            IOError: If file operations fail
        """
        try:
            products = self._read_all_products()
            product_found = False
            
            for row in products:
                if row["nome"] == product_name:
                    current_qty = int(row["quantita"])
                    new_qty = current_qty + quantity_change
                    
                    if new_qty < 0:
                        raise ValueError(f"Quantità insufficiente per '{product_name}'. "
                                       f"Disponibile: {current_qty}, Richiesto: {abs(quantity_change)}")
                    
                    row["quantita"] = str(new_qty)
                    product_found = True
                    break
            
            if not product_found:
                raise ValueError(f"Prodotto '{product_name}' non trovato nel magazzino")
            
            self._write_all_products(products)
            
        except (IOError, OSError) as e:
            raise IOError(f"Error updating product quantity: {e}")
    
    def _read_all_products(self):
        """
        Read all products from the warehouse file.
        
        Returns:
            list: List of product dictionaries
        """
        try:
            with open(self.name, "r", newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                return list(reader)
        except FileNotFoundError:
            return []
    
    def _write_all_products(self, products):
        """
        Write all products to the warehouse file.
        
        Args:
            products (list): List of product dictionaries
        """
        with open(self.name, "w", newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=self.FIELDNAMES)
            writer.writeheader()
            writer.writerows(products)
    
    def list_all_products(self):
        """
        Get list of all products in warehouse.
        
        Returns:
            list: List of Product instances
        """
        try:
            products = self._read_all_products()
            return [Product.from_dict(p) for p in products]
        except (IOError, ValueError) as e:
            print(f"[ERRORE] Impossibile leggere i prodotti: {e}")
            return []
