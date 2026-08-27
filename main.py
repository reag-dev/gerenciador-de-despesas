from utils.db import Database
import locale
from rich.table import Table
from math import ceil
from rich.console import Console
from datetime import date, datetime
from utils.validations import DecimalValidator, DateValidator
from questionary import select, prompt

locale.setlocale(locale.LC_ALL, '')
database = Database('data/app.db')
date_format = "%d/%m/%Y"
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
            "default": date.today().strftime(date_format),
            "validate": DateValidator            
        }
    ]    
    
    answers = prompt(questions)
    database.exec_query("INSERT INTO expenses (description, category, value, date) VALUES (?, ?, ?, ?)", (answers["description"], answers["category"], answers["value"], datetime.strptime(answers["date"],date_format).isoformat() ))    
    print("Despesa cadastrada com sucesso!")    
   
def render_expense_table(total_value, expenses):
    table = Table(title=f"Lista de despesas - Total gasto: {total_value} ")
    table.add_column("ID", justify="right")
    table.add_column("Categoria")
    table.add_column("Descrição")
    table.add_column("Data")
    table.add_column("Valor")    
    
    for expense in expenses:                
        table.add_row(str(expense[0]), datetime.fromisoformat(expense[1]).strftime(date_format), expense[2], expense[3], locale.currency(expense[4]))
    return table
   
def list_expenses():    
    [items_count, total_value] = database.exec_query("SELECT COUNT(id), SUM(value) AS total_count FROM expenses")[0]
    
    if items_count == 0:
        print ("NENHUM ITEM ENCONTRADO!")
        return
         
    page_count = ceil(items_count / 10)
    current_page = 1
    query = "SELECT id,date,description,category,value FROM expenses ORDER BY date LIMIT 10"    
    expenses = database.exec_query(query)        
    console = Console()
    while True:
        options = []        
        console.clear()
        table = render_expense_table(locale.currency(total_value), expenses)
        console.print(table)            
            
        if current_page > 1:
            options.append("Voltar página")
        if current_page < page_count:
            options.append("Avançar página")
        options.append("Voltar ao menu")
        
        print(f"Página {current_page} de {page_count}")
        selected_action = select(
                "O que deseja fazer?",
                choices=options
            ).ask()    
        
        match selected_action:
            case "Voltar página":
                current_page -= 1
                expenses = database.exec_query(query + f" OFFSET {(current_page - 1) * 10}")
            case "Avançar página":
                current_page += 1
                expenses = database.exec_query(query + f" OFFSET {(current_page - 1) * 10}")
            case "Voltar ao menu":                
                break 
            case _:                
                break 

def main():  
    while True:       
        selected_action = select(
            "O que deseja fazer?",
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
                break
            case "Remover despesa":
                break
            case "Relatórios":
                break
            case "Exportar CSV":
                break
            case "Sair":
                break          
            case _:
                break
                            
def init():
    create_expenses_database()
    main()

init()