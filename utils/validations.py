from decimal import Decimal, InvalidOperation
from datetime import date, datetime
from questionary import ValidationError, Validator

class DecimalValidator(Validator):
    def validate(self, document):        
        try:
            value = Decimal(document.text)
        except InvalidOperation:
            raise ValidationError(
                message="Informe um número válido (ex: 10.50)",
                cursor_position=len(document.text)
            )   
                    
        if (value < 0): 
            raise ValidationError(
                message="Informe um número positivo",
                cursor_position=len(document.text)
            )        


class DateValidator(Validator):
    FORMAT = "%d/%m/%Y"    
    def validate(self, document):
        text = document.text.strip()
        if not text: 
            raise ValidationError(
                message="Informe uma data (ex. 01/01/2025)",            
                cursor_position=len(document.text)
            )
        try: 
            validated_date = datetime.strptime(text, self.FORMAT).date()
        except ValueError:
            raise ValidationError(
                message="Data inválida (ex: 24/08/2026)",            
                cursor_position=len(document.text)
            )        

        if validated_date > date.today():
            raise ValidationError(
                message="A data não pode estar no futuro",
                cursor_position=len(document.text)
            )
