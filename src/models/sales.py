"""
Sales management for the BioMarket system.
"""

import csv
import os
from datetime import datetime
from typing import Tuple


class SalesManager:
    """
    Manages sales transactions and profit calculations.
    
    Attributes:
        sales_file (str): Path to the sales CSV file
        fieldnames (list): CSV column headers for sales
    """
    
    SALES_FILE = "vendite.csv"
    FIELDNAMES = ["nome", "quantita venduta", "profitto", "data e ora"]
    
    def __init__(self):
        """Initialize the SalesManager and ensure sales file exists."""
        self.sales_file = self.SALES_FILE
        self._ensure_file_exists()
    
    def _ensure_file_exists(self):
        """Create sales file with headers if it doesn't exist."""
        try:
            if not os.path.exists(self.sales_file):
                with open(self.sales_file, "w", newline='', encoding='utf-8') as f:
                    writer = csv.DictWriter(f, fieldnames=self.FIELDNAMES)
                    writer.writeheader()
        except (IOError, OSError) as e:
            raise IOError(f"Cannot create sales file: {e}")
    
    def record_sale(self, product_name, quantity, purchase_price, sale_price):
        """
        Record a new sale transaction.
        
        Args:
            product_name (str): Name of the sold product
            quantity (int): Quantity sold
            purchase_price (float): Purchase price per unit
            sale_price (float): Sale price per unit
            
        Returns:
            float: Profit from this sale
            
        Raises:
            IOError: If file operations fail
            ValueError: If input data is invalid
        """
        try:
            if quantity <= 0:
                raise ValueError("Quantity must be positive")
            
            profit = (float(sale_price) - float(purchase_price)) * quantity
            timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            
            with open(self.sales_file, "a", newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=self.FIELDNAMES)
                
                # Write header if file is empty
                if f.tell() == 0:
                    writer.writeheader()
                
                writer.writerow({
                    "nome": product_name,
                    "quantita venduta": str(quantity),
                    "profitto": str(profit),
                    "data e ora": timestamp
                })
            
            return profit
            
        except (IOError, OSError) as e:
            raise IOError(f"Error recording sale: {e}")
        except (ValueError, TypeError) as e:
            raise ValueError(f"Invalid sale data: {e}")
    
    def calculate_profits(self):
        """
        Calculate total profits from all sales.
        
        Returns:
            tuple: (gross_profit, net_profit) where both are floats
            
        Note:
            In this system, gross_profit equals net_profit since profit
            is already calculated as (sale_price - purchase_price) * quantity
        """
        try:
            if not os.path.exists(self.sales_file):
                return 0.0, 0.0
            
            total_profit = 0.0
            
            with open(self.sales_file, "r", newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    try:
                        total_profit += float(row["profitto"])
                    except (ValueError, KeyError):
                        continue
            
            # In this system, net profit = gross profit
            # as profit already accounts for purchase costs
            return total_profit, total_profit
            
        except (IOError, OSError) as e:
            print(f"[ERRORE] Impossibile leggere il file vendite: {e}")
            return 0.0, 0.0
    
    def get_all_sales(self):
        """
        Retrieve all sales records.
        
        Returns:
            list: List of sale dictionaries
        """
        try:
            if not os.path.exists(self.sales_file):
                return []
            
            with open(self.sales_file, "r", newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                return list(reader)
                
        except (IOError, OSError) as e:
            print(f"[ERRORE] Impossibile leggere le vendite: {e}")
            return []
