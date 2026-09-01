from utils.validations import DecimalValidator, DateValidator
from datetime import date

def description_question():
    return  {
        "type": "text",
        "name": "description",
        "message": "Informe a descrição: ",                              
    }
def category_question():
    return {
        "type": "select",
        "name": "category",
        "message": "Selecione a categoria da despesa: ",                
        "choices": ["Moradia", "Alimentação", "Conta", "Saúde", "Transporte", "Educação", "Lazer", "Assinatura"]
    }
def value_question():
    return {
        "type": "text",
        "name": "value",
        "message": "Informe o valor: ",            
        "validate": DecimalValidator  
    }
def date_question():
    return {
        "type": "text", 
        "name": "date",
        "message": "Informe a data (dd/mm/yyyy): ",
        "default": date.today().strftime("%d/%m/%Y"),
        "validate": DateValidator            
    }