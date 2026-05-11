from src.exceptions.exceptions import *

class Validator:

#Checking the price input
    @staticmethod
    def validate_price(price):
        if not isinstance(price,(int,float)): raise ValidationError('Price must be numeric')
        if price < 0: raise NegativePriceError('good pricing requieres a positive value')
        elif price == 0: raise NegativePriceError('Price has to be greater than zero')

#checking the mail input
    @staticmethod
    def validate_email(email):
        if '@' not in email: raise InvalidEmailError('invalid mail; missing @')
        elif len(email) > 30: raise InvalidEmailError('Mail address too long')

#Checking the name input
    @staticmethod
    def validate_name(name):
        if not isinstance(name,str): raise ValidationError('name must be text')
        if not name.strip(): raise ValidationError('name can not be empty')
        elif len(name) > 20: raise ValidationError('name is too long')

#Checking the ID input
    @staticmethod
    def validate_id(id_value):
        if not isinstance(id_value, int): raise ValidationError('ID must be an integer')
        if id_value < 0: raise ValidationError('ID cannot be negative')
        elif id_value == 0: raise ValidationError('ID cannot be zero')

#Checking order status
    @staticmethod
    def validate_order(status):
        valid_status =      [
            'Open',
            'Paid',
            'Cancelled',
                            ]
        if status not in valid_status: raise ValidationError('Order status invalid')

#Checking quantities
    @staticmethod
    def validate_quant(quantity):
        if not isinstance(quantity, int): raise ValidationError('quantity must be an integer')
        if quantity < 0: raise ValidationError('Quantity cannot be negative')
        elif quantity == 0: raise ValidationError('Quantity cannot be zero')
