# 🍽️ Sabor Express - Consulta de Cardápios (API)

Este é um projeto prático desenvolvido em **Python** utilizando o framework **FastAPI**. O objetivo principal da aplicação é criar uma API local que consome dados de uma API externa (composta por informações de restaurantes e os seus respetivos cardápios) e disponibiliza esses dados de forma filtrada e organizada para o utilizador.

---

## 🚀 Tecnologias e Conceitos Aprendidos

Durante o desenvolvimento deste projeto, explorei e consolidei os seguintes conceitos e tecnologias:

* **Python 3**: Linguagem base utilizada para toda a lógica de programação.
* **FastAPI**: Framework moderno, rápido (alta performance) e robusto para a criação de APIs web em Python.
* **Requests**: Biblioteca Python utilizada para fazer requisições HTTP e consumir dados de APIs externas de forma síncrona.
* **Manipulação de Dados JSON**: Conversão de strings e dados brutos vindos da internet em objetos nativos do Python (Listas e Dicionários) através do método `response.json()`.
* **Orientação a Objetos (POO)**: Aplicação prática de conceitos como Herança, Encapsulamento, Métodos Especiais (`__str__`) e Polimorfismo.
* **Parâmetros de Query (Query Parameters)**: Implementação de filtros dinâmicos nas rotas da API para buscas customizadas.

---

## 🛠️ Como Executar o Projeto

### Pré-requisitos
Antes de começar, você precisar de ter o [Python](https://www.python.org/) instalado na tua máquina.

### Passos para Instalação e Execução

1.**Clona o repositório:**
   ```bash
   git clone [https://github.com/TEU_UTILIZADOR/nome-do-repositorio.git](https://github.com/TEU_UTILIZADOR/nome-do-repositorio.git)
   cd nome-do-repositorio
  ```
2.**Cria e ativa o ambiente virtual (venv):**
  ```bash
  # Criar o ambiente virtual
    python -m venv venv

  # Ativar no Windows (PowerShell)
  .\venv\Scripts\Activate.ps1

  # Ativar no Linux/Mac
  source venv/bin/activate
```

3.**Instala as dependências:**
  ```bash

  pip install fastapi uvicorn requests
```

4.**Iniciar o servidor Uvicon**
```bash
uvicorn main:app --reload
```

## 🧑‍💻 Autor

Desenvolvido por **Ryan Coutinho Barra** — Conecte-se comigo no [LinkedIN](https://www.linkedin.com/in/ryan-coutinho-barra-90b045260/)