# Validador de documentos para padrões nacionais.
# Projeto
Colocando em prática um pouco do que o pacote Regex pode oferecer para podermos trabalhar com expressões regulares. 

Neste repositória criei alguns códigos que valida vários tipos de documento e até mesmo números de telefones, também desenvolvi uma função que utiliza o módulo Requests, que permite enviar solicitações HTTP, através disso utilizei a API (via cep) para conseguir obter mais informações dos ceps validados.

# Techs
- Python
- Módulo Requets
- Módulo Re

# Funcionamento
Neste primeiro print é o arquivo principal, onde estou importando todos os módulos de validação e um menu principal pro próprio terminal para melhor interação.![main](https://user-images.githubusercontent.com/106001465/180591624-6a74885a-01ac-4dbb-a73c-db494d715d52.PNG)
#
Valida CEP -> no print abaixo é o módulo que verifica um padrão no cep, utilizando a bibli regex e uma segunda função que extrai todas as informações do cep utilizando o módulo Requests.
![cep](https://user-images.githubusercontent.com/106001465/180591690-e8c15601-751f-4568-bd68-1c2b32ec09cd.PNG)
#
Valida CPF -> O módulo que valida o cpf existe três etapas. Neste primeiro print é feito a primeira etapa, que consiste em uma verificação na quantidade de caracteres informados pelo usuário, após isso é feito a ánalise para saber se o primeiro digito do cpf corresponde com os restantes dos caracteres.  ![cpf01](https://user-images.githubusercontent.com/106001465/180591802-56d9222d-422a-4f6a-9968-e6ff3414d56b.PNG)

A partir da verificação do primeiro dígito é realizada uma segunda, só que dessa vez para verificar o segundo digito do cpf. Importante ressaltar que o cálculo é feito a partir do resultado do primeiro dígito. 
![cpf02](https://user-images.githubusercontent.com/106001465/180591913-73b5ef9a-553a-42eb-8a30-3d5165e6c0f6.PNG)

Já nesta etapa final com a ajuda do módulo regex é criando um padrão para exibir ao usuário o cpf formatado em nosso padrão nacional.
![cpf03](https://user-images.githubusercontent.com/106001465/180591971-09175d68-a618-4f99-9456-14c7bc51aa5f.PNG)
#
Valida CNPJ -> Com base nos mesmos métodos do validador de cpf é realizado a validação dos cnpj.
Neste primeiro print é feito a conferência na quantidade de caracteres informados e realizado a verificação do primeiro dígito do cnpj.
![cnpj01](https://user-images.githubusercontent.com/106001465/180592053-7da6fa6b-7c82-4bda-b540-8b4fea6a1cb5.PNG)

Verifica segundo dígito.
![cnpj02](https://user-images.githubusercontent.com/106001465/180592072-a9b9c604-8fc8-4fb6-bc25-d25ccc9afd18.PNG)

E com ajuda do módulo regex é formatado o cnpj em nosso padrão nacional.
![cnpj03](https://user-images.githubusercontent.com/106001465/180592095-dba33c77-2685-4afc-af6e-cc7824174051.PNG)
#
Valida Telefone -> E neste ultimo módulo é feita a validação de um número de telefone com os padrões nacionais. Verifica se é contido DDD e código do pais.
![telefone](https://user-images.githubusercontent.com/106001465/180592146-89fff6aa-954c-49a3-b845-77fd2fb8b2a3.PNG)
