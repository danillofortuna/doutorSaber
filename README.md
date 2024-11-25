# doutorSaber


## API GPT

### Tokens
- A API do GPT funciona com tokens, você gasta tokens para obter respostas. Um token em uma resposta é basicamente uma palavra. Se a resposta da sua pergunta for "o céu é azul", essa resposta terá consumido quatro tokens.
- Ao usar a API, podemos configurar qual o máximo de tokens que cada resposta pode usar. No nosso código nós definimos para 400. Caso queira alterar, busque esse número no código e substitua pelo que preferir.

### API Key
- Primeiro você precisa comprar tokens na plataforma do GPT.
- Acesse o [console da OpenAI](https://platform.openai.com/settings/organization/billing/overview) e faça login com o mesmo email que você usa para logar na sua Alexa.
- Adicione um cartão de crédito e adicione um crédito (5$ são suficientes)
- Acesse suas [chaves de API](https://platform.openai.com/settings/profile?tab=api-keys) e adicione uma chave pessoal clicando em "Create new secret key"
- Dê um nome de sua escolha e deixe selecionada a opção "Permissions -> All".
- Salve a chave de sua API em um local seguro pois vamos utilizá-la mais tarde. Não entregue essa chave para ninguém, ou poderão consumir seus créditos do GPT com ela.

## Skill da Alexa

- Para começar, vamos criar a Skill no console da Amazon.

- Acesse o [console da alexa](https://developer.amazon.com/alexa/console/ask) e clique em "Create Skill"

Escolha as seguintes opções:

### Name, Locale:
1. Name your Skill -> Qualquer nome serve, esse nome não será usado para invocar a skill. Isso será definido depois.
2. Choose a primary locale -> Portuguese (BR)

### Experience, Model, Hosting service:
1. Choose a type of experience -> other
2. Choose a model -> Custom
3. Hosting services -> Alexa-hosted (Python)
   3.1 Hosting region -> US East (N. Virginia)

### Templates
1. Templates -> Start from Scratch

### Create Skill
Após clicar em criar skill, eu recebi várias vezes o erro de que a skill não tem um nome de invocação, parece ser um erro da plataforma, eu tive que tentar 4 vezes desde o início para que desse certo.
Quando a skill for criada, você será redirecionado para a página de configurar a skill:

<img width="1713" alt="Screenshot 2024-10-05 at 16 22 34" src="https://github.com/user-attachments/assets/4e912bdc-c40c-4f99-812a-ddcaf140e694">

### Invocation name
- Nessa skill, vamos usar o nome "Doutor saber" para invocá-la, posteriormente você pode personalizar como quiser, mas vou usar esse nome pois gosto da referência do filme A.I. do Steven Spielberg.
- No menu lateral esquerdo, clique em Invocations -> Skill Invocation Name.
- Na página que será aberta, troque o valor "change me" por "doutor saber" e clique em "Save" (canto superior esquerdo da página aberta).

### Intent
- Clique no menu lateral esquerdo em "Interaction Model" -> "Intents"
- Clique em "+ Add Intent"
- Coloque o nome "PerguntaIntent" e clique em "Create custom intent"
- Será aberto um campo de "Sample Utterances". 
- Escreva -> me diga {Question}
- Em seguida clique no sinal de "+" no fim do campo.
- Abaixo, será automaticamente adicionada uma linha na lista de Intent Slots com o Slot chamado "Question". Em Slot Type, selecione o tipo "AMAZON.SearchQuery".
- Clique em "save" (canto superior esquerdo).

### Code
- No menu superior, clique na aba "Code"
- Abra o arquivo "lambda_function.py"
- Substitua seu conteúdo pelo conteúdo do arquivo "lambda_function.py" disponibilizado nesse repositório.
- Dentro do código substituido, na linha 15, você verá a constante OPENAI_API_KEY com o valor "change_me". 
- Substitua o "change_me" pela sua chave de API do GPT.
- Após isso, clique em SAVE e depois em DEPLOY (ambos no canto superior direito).
- Aguarde o Deploy ser feito.

### Test
- Você já pode testar a skill na sua própria Alexa. Se ela estiver configurada na mesma conta que você usou para acessar o console, a skill estará disponível nela.
- Basta dizer: "Alexa, doutor saber"
- Ela responderá: "Olá! Eu sou o Doutor Saber. O que você deseja saber hoje?"
- Então você poderá fazer um pedido com uma frase que se inicie com "me diga". Por exemplo: "Me diga quem foi sherlock holmes".
- É importante dizer o "me diga" pois ele foi definido como frase padrão na configuração das Intents.

É isso. Se nada deu errado, sua skill está funcionando.
Agora é só ler o código e explorar a plataforma para personalizá-la como quiser.


