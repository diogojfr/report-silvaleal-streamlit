# Easy Pallet – Silva Leal Dashboard (Streamlit)

Dashboard operacional no estilo do Looker/Easy Pallet, construído com **Streamlit + Plotly**.

## Estrutura do Projeto

```
report-silvaleal-streamlit/
│
├── app.py                      ← Ponto de entrada principal (run this)
│
├── requirements.txt
│
├── components/
│   ├── data_loader.py          ← Funções de leitura de CSV (cached)
│   └── ui_components.py        ← Componentes reutilizáveis (cards, gráficos, filtros)
│
├── pages/
│   ├── painel_geral.py         ← Painel Geral (KPIs + Donut + Bar + Line)
│   ├── painel_montagem.py      ← Painel Montagem (Bar + Line + Tabela)
│   ├── painel_conferencia.py   ← Painel Conferência (Bar + Line + Tabela por Operador)
│   ├── painel_erros.py         ← Painel Erros (Donut + Bar Stacked + Tabela)
│   └── painel_operacoes.py     ← Painel Operações (duração, perfil, horas trabalhadas)
│
└── data/                       ← Coloque seus CSVs aqui
    ├── tab_orders.csv
    ├── tab_loads.csv
    ├── conf_registros.csv
    ├── tab_errors.csv
    └── ...
```

## Como Rodar

```bash
pip install -r requirements.txt
cp .env.example .env          # defina APP_PASSWORD
streamlit run app.py
```

## CSVs utilizados

| Arquivo                      | Carregado por                    |
|------------------------------|----------------------------------|
| `tab_orders.csv`             | `load_pallets()`                 |
| `tab_loads.csv`              | `load_cargas()`                  |
| `conf_registros.csv`         | `load_conferencia()`             |
| `tab_errors.csv`             | `load_erros()`                   |
| `tab_erros_dia.csv`          | `load_erros_dia()`               |
| `caixa_hora.csv`             | `load_caixa_hora()`              |
| `tempo_medio_mont.csv`       | `load_tempo_montagem()`          |
| `media_conf_dia.csv`         | `load_tempo_conferencia_dia()`   |
| `montagem_transporte.csv`    | `load_montagem_transporte()`     |
| `tab_duracao_operacao.csv`   | `load_duracao_operacao()`        |
| `tab_op_perfil.csv`          | `load_op_perfil()`               |
| `tab_horas_trabalhadas.csv`  | `load_horas_trabalhadas()`       |

Datas no formato `YYYY-MM-DD`.

## Adicionando um Novo Painel

1. Crie `pages/painel_novo.py`
2. Adicione um `st.Page(...)` na lista `pages` em `app.py`
3. Opcionalmente adicione um loader em `data_loader.py`
