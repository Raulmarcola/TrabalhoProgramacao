# Trabalho de Programação
## Desafio em python para compor a nota de programação de computadores.

* O software usado para versionamento em nuvem foi o beanstalk

## Enunciado do exercício
Crie uma aplicação que contenha uma função para mostrar um menu ao usuário, assim:
1. Cadastrar os cargos da empresa.
2. Cadastrar os funcionários da empresa.
3. Mostrar um relatório contendo o número, o nome e o valor do salário de todos os funcionários.
4. Mostrar o valor pago aos funcionários que pertençam a um cargo informado pelo usuário.
5. Finalizar.

### Opção 1:
Cada vez que essa opção for selecionada deverá ser chamada uma sub-rotina, na qual o usuário
poderá cadastrar todos os cargos. Não se esqueça, nessa empresa existem apenas cinco cargos. Se o usuário
mandar executar esta opção mais de uma vez, mostre a mensagem de erro “Salários dos cargos já cadastrados” e retorne ao menu.

### Opção 2: 
Cada vez que essa opção for selecionada deverá ser chamada uma sub-rotina, na qual o usuário
poderá cadastrar um novo funcionário, ou seja, informará o número do funcionário (este número deve ser
único, você deverá implementar essa validação), nome e código do cargo (lembre-se de que o código informado deverá existir no vetor de cargos). Não se esqueça, nessa empresa existem apenas 15 funcionários. Se
o usuário selecionar essa opção e o vetor de funcionários estiver completamente preenchido, mostrar uma
mensagem de erro e retornar ao menu.

* Crie uma sub-rotina para fazer a validação do número do funcionário — ela não poderá aceitar
número repetido.
* Crie uma sub-rotina para validar o nome do funcionário, obrigando-o a ser composto por pelo
menos duas palavras (nome e sobrenome).
* Crie uma sub-rotina para fazer a validação do código do cargo ocupado pelo funcionário — ela
só poderá aceitar códigos entre 1 e 5 cujos salários já tenham sido cadastrados no vetor de cargos.

### Opção 3: 
Cada vez que essa opção for selecionada deverá ser chamada uma sub-rotina, na qual serão mostrados código, nome e valor do salário de todos os funcionários cadastrados (salários podem ser obtidos no
vetor de cargos).

### Opção 4: 
Cada vez que essa opção for selecionada deverá ser chamada uma sub-rotina, na qual será feito
o somatório do salário de todos os funcionários que pertencerem a determinado cargo. Esse cargo é informado pelo usuário (entre 1 e 5) no módulo principal do seu programa e o somatório calculado deverá ser
mostrado, também, no módulo principal. 
