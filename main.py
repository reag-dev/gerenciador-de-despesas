from utils.db import Database
from decimal import Decimal
from datetime import date, datetime
from utils.validations import DecimalValidator, DateValidator
from questionary import select, prompt

database = Database('data/app.db')
expense_types = ("Moradia", "Alimentação", "Conta", "Saúde", "Transporte", "Educação", "Lazer", "Assinatura")

def create_expenses_database():
    database.exec_query(""" 
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,      
        date DATE NOT NULL,
        description TEXT,
        category TEXT NOT NULL CHECK (
            category IN (
                'Moradia',
                'Alimentação',
                'Conta',
                'Saúde',
                'Transporte',
                'Educação',
                'Lazer',
                'Assinatura'
            )
        ),
        value REAL NOT NULL,
        created_at DATE NOT NULL DEFAULT CURRENT_DATE
    );
    """)    

def register_expense():
    questions = [
        {
            "type": "text",
            "name": "description",
            "message": "Informe a descrição: ",                              
        }, 
        {
            "type": "select",
            "name": "category",
            "message": "Selecione a categoria da despesa: ",                
            "choices": ["Moradia", "Alimentação", "Conta", "Saúde", "Transporte", "Educação", "Lazer", "Assinatura"]
        }, 
        {
            "type": "text",
            "name": "value",
            "message": "Informe o valor: ",            
            "validate": DecimalValidator  
        }, 
        {
            "type": "text", 
            "name": "date",
            "message": "Informe a data (dd/mm/yyyy): ",
            "default": date.today().strftime("%d/%m/%Y"),
            "validate": DateValidator            
        }
    ]    
    answers = prompt(questions)
    database.exec_query("INSERT INTO expenses (description, category, value, date) VALUES (?, ?, ?, ?)", (answers["description"], answers["category"], answers["value"], datetime.strptime(answers["date"], "%d/%m/%Y").isoformat() ))    
    print("Despesa cadastrada com sucesso!")
    main()
   
def list_expenses():
    results = database.exec_query("SELECT * FROM expenses")
    print(results)

def main():        
    selected_action = select(
        "What do you want to do?",
        choices=[
            "Cadastrar despesa(s)",
            "Listar despesas",
            "Editar despesa",
            "Remover despesa",
            "Relatórios",
            "Exportar CSV",
            "Sair"
        ]
    ).ask()
        
    match selected_action:
            case "Cadastrar despesa(s)":
                register_expense()                
            case "Listar despesas":
                list_expenses()                
            case "Editar despesa":
                return ""
            case "Remover despesa":
                return ""      
            case "Relatórios":
                return ""      
            case "Exportar CSV":
                return ""      
            case "Sair":
                return          

def init():
    create_expenses_database()
    main()

init()