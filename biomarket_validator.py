"""
Input validation utilities for the BioMarket system.
"""


class InputValidator:
    """
    Provides methods for validating and sanitizing user input.
    """
    
    @staticmethod
    def get_positive_integer(prompt):
        """
        Get a positive integer from user input.
        
        Args:
            prompt (str): Input prompt message
            
        Returns:
            int: Validated positive integer
            
        Raises:
            ValueError: If input cannot be converted to positive integer
        """
        while True:
            try:
                value = input(prompt).strip()
                
                if not value:
                    print("[ERRORE] Il campo non può essere vuoto. Riprova.")
                    continue
                
                int_value = int(value)
                
                if int_value <= 0:
                    print("[ERRORE] Il valore deve essere un numero positivo. Riprova.")
                    continue
                
                return int_value
                
            except ValueError:
                print("[ERRORE] Inserire un numero intero valido. Riprova.")
            except KeyboardInterrupt:
                raise
            except Exception as e:
                print(f"[ERRORE] Input non valido: {e}. Riprova.")
    
    @staticmethod
    def get_positive_float(prompt):
        """
        Get a positive float from user input.
        
        Args:
            prompt (str): Input prompt message
            
        Returns:
            float: Validated positive float
            
        Raises:
            ValueError: If input cannot be converted to positive float
        """
        while True:
            try:
                value = input(prompt).strip()
                
                if not value:
                    print("[ERRORE] Il campo non può essere vuoto. Riprova.")
                    continue
                
                # Replace comma with dot for European number format
                value = value.replace(',', '.')
                
                float_value = float(value)
                
                if float_value < 0:
                    print("[ERRORE] Il valore deve essere un numero non negativo. Riprova.")
                    continue
                
                return float_value
                
            except ValueError:
                print("[ERRORE] Inserire un numero decimale valido. Riprova.")
            except KeyboardInterrupt:
                raise
            except Exception as e:
                print(f"[ERRORE] Input non valido: {e}. Riprova.")
    
    @staticmethod
    def get_non_empty_string(prompt):
        """
        Get a non-empty string from user input.
        
        Args:
            prompt (str): Input prompt message
            
        Returns:
            str: Validated non-empty string
            
        Raises:
            ValueError: If input is empty
        """
        while True:
            try:
                value = input(prompt).strip()
                
                if not value:
                    print("[ERRORE] Il campo non può essere vuoto. Riprova.")
                    continue
                
                return value
                
            except KeyboardInterrupt:
                raise
            except Exception as e:
                print(f"[ERRORE] Input non valido: {e}. Riprova.")
    
    @staticmethod
    def get_yes_no(prompt):
        """
        Get a yes/no response from user input.
        
        Args:
            prompt (str): Input prompt message
            
        Returns:
            bool: True for yes, False for no
        """
        while True:
            try:
                value = input(f"{prompt} (s/n): ").strip().lower()
                
                if value in ['s', 'si', 'sì', 'y', 'yes']:
                    return True
                elif value in ['n', 'no']:
                    return False
                else:
                    print("[ERRORE] Rispondere con 's' (sì) o 'n' (no). Riprova.")
                    
            except KeyboardInterrupt:
                raise
            except Exception as e:
                print(f"[ERRORE] Input non valido: {e}. Riprova.")
