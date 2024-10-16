## Extração de Dados do ViaCEP e Inserção no Banco de Dados

O projeto tem como objetivo extrair dados de endereços a partir da API pública do ViaCEP (https://viacep.com.br/) e inseri-los em um banco de dados SQL Server utilizando a linguagem Python.

 
### Funcionalidade

O script Python faz uma requisição à API do ViaCEP, obtém as informações de endereço de um determinado CEP e insere esses dados em uma tabela de um banco de dados SQL Server.

### Fluxo do Projeto
1. O usuário insere um CEP.
2. O script faz uma requisição HTTP para a API do ViaCEP.
3. Os dados retornados pela API são extraídos e formatados.
4. Os dados extraídos são inseridos em uma tabela de banco de dados SQL Server.

### Tecnologias Utilizadas
- <strong>Linguagem:</strong> Python.
- <strong>Bibliotecas:</strong>
  1. pymssql==2.3.0 – Para conectar e inserir dados no SQL Server.
  2. requests==2.31.0 – Para realizar requisições HTTP à API ViaCEP.
