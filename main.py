from questionary import select
import sqlite3


database_name = 'expenses_db.db'
expense_types = ("Moradia", "Alimentação", "Conta", "Saúde", "Transporte", "Educação", "Lazer", "Assinatura")

def register_expense():
    return 

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
            return ""
        case "Listar despesas":
            return ""
        case "Editar despesa":
            return ""
        case "Remover despesa":
            return ""      
        case "Relatórios":
            return ""      
        case "Exportar CSV":
            return ""      
        case "Sair":
            return ""              

main()