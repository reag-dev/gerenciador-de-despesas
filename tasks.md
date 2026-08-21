# 📊 Gerenciador de Despesas em Python

Projeto de estudo para praticar Python através do desenvolvimento de um gerenciador de despesas com persistência de dados, relatórios e exportação/importação CSV.

## 🎯 Objetivo

Desenvolver uma aplicação de linha de comando (CLI) capaz de:

- Cadastrar despesas
- Listar despesas
- Editar despesas
- Remover despesas
- Filtrar despesas
- Gerar relatórios
- Persistir dados
- Exportar dados para CSV
- Importar dados de CSV

> A primeira versão deve utilizar somente a biblioteca padrão do Python.

---

## 🟢 Fase 1 — Estrutura inicial

- [ ] Criar o diretório do projeto
- [ ] Criar `main.py`
- [ ] Criar o menu principal
- [ ] Criar opção para cadastrar despesa
- [ ] Criar opção para listar despesas
- [ ] Criar opção para editar despesa
- [ ] Criar opção para remover despesa
- [ ] Criar opção para relatórios
- [ ] Criar opção para exportar CSV
- [ ] Criar opção para sair
- [ ] Criar uma estrutura inicial para representar uma despesa

**Campos da despesa**

- [ ] `id`
- [ ] `data`
- [ ] `descricao`
- [ ] `categoria`
- [ ] `valor`

**Conceitos**

`Variáveis` · `Tipos de dados` · `Listas` · `Dicionários` · `Funções` · `if/elif/else` · `while` · `for`

---

## 🟢 Fase 2 — Cadastro de despesas

- [ ] Criar `adicionar_despesa()`
- [ ] Solicitar descrição
- [ ] Solicitar valor
- [ ] Solicitar categoria
- [ ] Solicitar data
- [ ] Gerar ID único
- [ ] Adicionar a despesa à lista
- [ ] Validar o valor informado
- [ ] Impedir valores negativos
- [ ] Validar a data
- [ ] Exibir mensagem de sucesso

**Desafio**

- [ ] Impedir o cadastro quando algum campo obrigatório estiver vazio
- [ ] Garantir que o programa não encerre quando o usuário digitar um valor inválido

---

## 🟢 Fase 3 — Listagem de despesas

- [ ] Criar `listar_despesas()`
- [ ] Exibir todas as despesas
- [ ] Exibir ID
- [ ] Exibir data
- [ ] Exibir descrição
- [ ] Exibir categoria
- [ ] Exibir valor
- [ ] Exibir o total gasto
- [ ] Exibir mensagem quando não existirem despesas

**Ordenação**

- [ ] Ordenar por data
- [ ] Ordenar por valor
- [ ] Ordenar por categoria

**Conceitos**

`sorted()` · `lambda` · Formatação de strings · Formatação numérica

---

## 🟡 Fase 4 — CRUD completo

**Editar**

- [ ] Criar `editar_despesa()`
- [ ] Solicitar o ID da despesa
- [ ] Verificar se o ID existe
- [ ] Permitir alterar descrição
- [ ] Permitir alterar valor
- [ ] Permitir alterar categoria
- [ ] Permitir alterar data
- [ ] Validar os novos dados

**Remover**

- [ ] Criar `remover_despesa()`
- [ ] Solicitar o ID
- [ ] Verificar se o ID existe
- [ ] Solicitar confirmação
- [ ] Remover a despesa
- [ ] Exibir mensagem de sucesso

**Tratamento de erros**

- [ ] Tratar ID inexistente
- [ ] Tratar ID inválido
- [ ] Tratar valores inválidos

---

## 🟡 Fase 5 — Categorias

**Criar categorias padrão**

- [ ] Alimentação
- [ ] Transporte
- [ ] Moradia
- [ ] Saúde
- [ ] Lazer
- [ ] Educação
- [ ] Outros

**Funcionalidades**

- [ ] Filtrar despesas por categoria
- [ ] Calcular total de uma categoria
- [ ] Identificar categoria com maior gasto
- [ ] Identificar categoria com menor gasto
- [ ] Permitir criação de categorias personalizadas

**Desafio**

- [ ] Impedir categorias duplicadas
- [ ] Permitir renomear categorias

---

## 🟡 Fase 6 — Persistência com JSON

> As despesas devem continuar disponíveis depois que o programa for encerrado.

- [ ] Criar diretório `data/`
- [ ] Criar `data/despesas.json`
- [ ] Criar `salvar_despesas()`
- [ ] Criar `carregar_despesas()`
- [ ] Carregar dados ao iniciar o programa
- [ ] Salvar após adicionar uma despesa
- [ ] Salvar após editar uma despesa
- [ ] Salvar após remover uma despesa
- [ ] Tratar arquivo inexistente
- [ ] Tratar JSON inválido

**Conceitos**

`json` · `open()` · Context manager (`with`) · `pathlib` · Serialização · Desserialização · Exceções

---

## 🟡 Fase 7 — Relatórios

Criar uma seção específica para relatórios.

**Relatório geral**

- [ ] Total gasto
- [ ] Quantidade de despesas
- [ ] Média por despesa
- [ ] Maior despesa
- [ ] Menor despesa

**Relatório por categoria**

- [ ] Total gasto por categoria
- [ ] Quantidade de despesas por categoria
- [ ] Percentual de cada categoria sobre o total
- [ ] Categoria com maior gasto

**Relatório por período**

- [ ] Solicitar data inicial
- [ ] Solicitar data final
- [ ] Filtrar despesas pelo período
- [ ] Calcular total do período
- [ ] Calcular média do período
- [ ] Mostrar quantidade de despesas

**Relatório mensal**

Criar uma saída semelhante a:

```
RELATÓRIO — AGOSTO/2026

Total gasto: R$ 3.250,00
Quantidade: 24
Média: R$ 135,42

Por categoria:

Alimentação    R$ 850,00
Moradia        R$ 1.200,00
Transporte     R$ 450,00
Lazer          R$ 350,00
Outros         R$ 400,00
```

---

## 🟠 Fase 8 — Exportação CSV

Criar um módulo responsável pelos arquivos CSV.

- [ ] Criar `csv_manager.py`
- [ ] Criar `exportar_csv()`
- [ ] Criar diretório `exports/`
- [ ] Exportar todas as despesas
- [ ] Criar cabeçalho CSV
- [ ] Garantir uma despesa por linha
- [ ] Formatar corretamente datas
- [ ] Formatar corretamente valores
- [ ] Permitir definir o nome do arquivo
- [ ] Informar o caminho do arquivo gerado

**Estrutura esperada**

```csv
id,data,descricao,categoria,valor
1,2026-08-01,Supermercado,Alimentação,250.50
2,2026-08-02,Uber,Transporte,35.90
3,2026-08-03,Aluguel,Moradia,1500.00
```

**Exportações adicionais**

- [ ] `despesas.csv` — todas as despesas
- [ ] `relatorio_mensal.csv` — resumo mensal
- [ ] `relatorio_categorias.csv` — resumo por categoria
- [ ] CSV filtrado por período

---

## 🟠 Fase 9 — Importação CSV

- [ ] Criar `importar_csv()`
- [ ] Solicitar o arquivo CSV
- [ ] Ler o arquivo
- [ ] Interpretar o cabeçalho
- [ ] Converter cada linha em uma despesa
- [ ] Validar os dados
- [ ] Validar valores
- [ ] Validar datas
- [ ] Verificar IDs duplicados
- [ ] Tratar linhas inválidas
- [ ] Informar quais linhas apresentaram erro

**Estratégia de importação**

- [ ] Permitir adicionar os dados aos existentes
- [ ] Permitir substituir os dados existentes
- [ ] Solicitar confirmação antes de substituir

---

## 🟠 Fase 10 — Tratamento de erros

Revisar todo o sistema para garantir que entradas inválidas não quebrem a aplicação.

- [ ] `ValueError`
- [ ] `FileNotFoundError`
- [ ] `PermissionError`
- [ ] `JSONDecodeError`
- [ ] CSV inválido
- [ ] Data inválida
- [ ] Valor inválido
- [ ] ID inexistente
- [ ] Campo obrigatório vazio

**Boas práticas**

- [ ] Evitar `except Exception` sem necessidade
- [ ] Criar mensagens de erro claras
- [ ] Validar dados antes de processá-los
- [ ] Não esconder erros silenciosamente

---

## 🔵 Fase 11 — Refatoração

Depois de finalizar as funcionalidades, reorganizar o projeto.

**Estrutura sugerida**

```
gerenciador_despesas/
│
├── main.py
├── despesas.py
├── relatorios.py
├── csv_manager.py
├── storage.py
├── validators.py
│
├── data/
│   └── despesas.json
│
├── exports/
│   └── despesas.csv
│
└── tests/
    ├── test_despesas.py
    ├── test_relatorios.py
    └── test_csv.py
```

**Tasks**

- [ ] Separar interface da lógica de negócio
- [ ] Separar persistência
- [ ] Separar CSV
- [ ] Separar relatórios
- [ ] Separar validações
- [ ] Reduzir funções muito grandes
- [ ] Remover código duplicado
- [ ] Melhorar nomes de variáveis
- [ ] Melhorar nomes de funções
- [ ] Adicionar docstrings onde fizer sentido

---

## 🔵 Fase 12 — Testes

> Escolher `unittest` ou `pytest`.

- [ ] Criar testes para adicionar despesas
- [ ] Criar testes para editar despesas
- [ ] Criar testes para remover despesas
- [ ] Criar testes para filtros
- [ ] Criar testes para cálculos
- [ ] Criar testes para validação
- [ ] Criar testes para exportação CSV
- [ ] Criar testes para importação CSV
- [ ] Criar testes para JSON
- [ ] Criar testes para casos de erro

**Casos de teste importantes**

- [ ] Valor negativo
- [ ] Valor não numérico
- [ ] Data inválida
- [ ] ID inexistente
- [ ] Arquivo inexistente
- [ ] CSV inválido
- [ ] JSON inválido
- [ ] Lista de despesas vazia

---

## 🚀 Desafios extras

Depois de concluir o projeto principal:

**Receitas**

- [ ] Adicionar suporte a receitas
- [ ] Diferenciar receita e despesa
- [ ] Calcular total de receitas
- [ ] Calcular total de despesas
- [ ] Calcular saldo

> Saldo = Receitas − Despesas

**Orçamento**

- [ ] Criar orçamento mensal
- [ ] Definir limite por categoria
- [ ] Comparar gasto com orçamento
- [ ] Alertar quando o limite for ultrapassado

**Despesas recorrentes**

- [ ] Criar despesas recorrentes
- [ ] Definir periodicidade
- [ ] Gerar automaticamente despesas futuras

---

## 🔴 Desafios avançados

- [ ] Migrar JSON para SQLite
- [ ] Criar camada de acesso ao banco
- [ ] Utilizar dataclasses
- [ ] Utilizar Enum
- [ ] Criar CLI com `argparse`
- [ ] Criar gráficos dos gastos
- [ ] Criar API REST
- [ ] Criar interface web
- [ ] Criar autenticação de usuários
- [ ] Criar documentação da API

---

## 🧠 Regras do estudo

Para aproveitar melhor o projeto como estudo de Python:

- [ ] Tentar resolver cada task antes de pesquisar a implementação
- [ ] Consultar a documentação oficial quando necessário
- [ ] Evitar copiar soluções completas
- [ ] Refatorar código antigo depois de aprender novos conceitos
- [ ] Criar testes para funcionalidades importantes
- [ ] Fazer commits pequenos e descritivos
- [ ] Manter o projeto executável durante todas as fases

---

## 🏁 Ordem recomendada

1. Estrutura inicial
2. Cadastro
3. Listagem
4. CRUD
5. Categorias
6. JSON
7. Relatórios
8. Exportação CSV
9. Importação CSV
10. Tratamento de erros
11. Refatoração
12. Testes
13. SQLite
14. API / Interface

---

## ✅ Critério de conclusão

O projeto principal estará concluído quando for possível:

- [ ] Cadastrar uma despesa
- [ ] Listar despesas
- [ ] Editar uma despesa
- [ ] Remover uma despesa
- [ ] Filtrar despesas
- [ ] Persistir os dados em JSON
- [ ] Gerar relatórios
- [ ] Exportar os dados para CSV
- [ ] Importar dados de CSV
- [ ] Tratar entradas e arquivos inválidos
- [ ] Executar testes automatizados
- [ ] Ter o código organizado em módulos

> **Objetivo final:** ter um projeto pequeno o suficiente para ser desenvolvido sozinho, mas completo o suficiente para praticar os principais fundamentos de Python e introduzir conceitos de organização de software.