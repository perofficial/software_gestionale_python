"""
Product model for the BioMarket system.
"""


class Product:
    """
    Represents a product in the BioMarket inventory.
    
    Attributes:
        name (str): The product name
        quantity (int): Available quantity in stock
        purchase_price (float): Price paid to acquire the product
        sale_price (float): Price at which the product is sold
    """
    
    def __init__(self, name, quantity, purchase_price, sale_price):
        """
        Initialize a new Product instance.
        
        Args:
            name (str): Product name
            quantity (int): Initial quantity
            purchase_price (float): Purchase price per unit
            sale_price (float): Sale price per unit
            
        Raises:
            ValueError: If any numeric value is negative or quantity is not an integer
        """
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Product name must be a non-empty string")
        
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Quantity must be a non-negative integer")
        
        if not isinstance(purchase_price, (int, float)) or purchase_price < 0:
            raise ValueError("Purchase price must be a non-negative number")
        
        if not isinstance(sale_price, (int, float)) or sale_price < 0:
            raise ValueError("Sale price must be a non-negative number")
        
        self.name = name.strip()
        self.quantity = quantity
        self.purchase_price = float(purchase_price)
        self.sale_price = float(sale_price)
    
    def __repr__(self):
        """Return string representation of the product."""
        return (f"Product(name='{self.name}', quantity={self.quantity}, "
                f"purchase_price={self.purchase_price:.2f}, "
                f"sale_price={self.sale_price:.2f})")
    
    def to_dict(self):
        """
        Convert product to dictionary format for CSV storage.
        
        Returns:
            dict: Product data as dictionary
        """
        return {
            "nome": self.name,
            "quantita": str(self.quantity),
            "prezzo di acquisto": str(self.purchase_price),
            "prezzo di vendita": str(self.sale_price)
        }
    
    @classmethod
    def from_dict(cls, data):
        """
        Create a Product instance from dictionary data.
        
        Args:
            data (dict): Dictionary containing product data
            
        Returns:
            Product: New Product instance
            
        Raises:
            ValueError: If required fields are missing or invalid
        """
        try:
            return cls(
                name=data["nome"],
                quantity=int(data["quantita"]),
                purchase_price=float(data["prezzo di acquisto"]),
                sale_price=float(data["prezzo di vendita"])
            )
        except KeyError as e:
            raise ValueError(f"Missing required field: {e}")
        except (ValueError, TypeError) as e:
            raise ValueError(f"Invalid data format: {e}")
