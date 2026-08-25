# 📊 Gerenciador de Despesas

Aplicação de linha de comando (CLI) para registrar e acompanhar despesas pessoais, com persistência em SQLite.

Projeto de estudo para praticar os fundamentos de Python.

## Requisitos

- Python 3.14
- [questionary](https://github.com/tmbo/questionary) — menus e formulários no terminal

```bash
pip install questionary
```

## Como rodar

```bash
python main.py
```

O banco é criado automaticamente em `data/app.db` na primeira execução.

## Funcionalidades

- [x] Cadastrar despesa (data, descrição, categoria, valor)
- [x] Validação de valor (número positivo) e de data (formato e limite)
- [ ] Listar despesas
- [ ] Editar despesa
- [ ] Remover despesa
- [ ] Relatórios
- [ ] Exportar CSV

## Estrutura

```
gerenciador-de-despesas/
├── main.py               # menu principal e fluxos da CLI
├── utils/
│   ├── db.py             # camada de acesso ao SQLite
│   └── validations.py    # validadores de entrada (valor e data)
├── data/
│   └── app.db            # banco local (não versionado)
└── tasks.md              # roteiro de estudo por fases
```

## Categorias

Moradia · Alimentação · Conta · Saúde · Transporte · Educação · Lazer · Assinatura

---

O roteiro completo do estudo, fase a fase, está em [tasks.md](tasks.md).
