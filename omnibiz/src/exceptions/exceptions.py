
#Base exception for whole system
class OmniBizError(Exception):
    '''OmniBizz-BaseError'''
    pass

#Invalid input
class ValidationError(OmniBizError):
    '''Invalid data input'''
    pass

#Price can't be negative
class NegativePriceError(ValidationError):
    '''Price has to be greater than zero'''
    pass

#Invalid mail address
class InvalidEmailError(ValidationError):
    '''emaild address is not valid'''
    pass

#Customer not found
class CustomerNotFoundError(OmniBizError):
    '''Customer not found'''
    pass

#Order does not exist
class OrderNotFoundError(OmniBizError):
    '''No existing order'''
    pass
