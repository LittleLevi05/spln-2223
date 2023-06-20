<h1 style="font-size:60px" align="center"><img height=28cm src="https://raw.githubusercontent.com/LittleLevi05/spln-2223/main/TP2/images/logo.png"> HShield</h1>

<h4 align="center">A ferramenta ideal para anonimização de dados pessoais dos seus documentos</h4>

<br>

<img src="https://raw.githubusercontent.com/LittleLevi05/spln-2223/main/TP2/images/banner.png">

<br>

- [🌟 Introdução](#-introdução)
  - [Contexto](#contexto)
  - [Propósito e Objetivos](#propósito-e-objetivos)
- [⚙️ Caracterização do sistema](#️-caracterização-do-sistema)
  - [Arquitetura](#arquitetura)
  - [Anonimização de Nomes](#anonimização-de-nomes)
  - [Anonimização de Endereços](#anonimização-de-endereços)
  - [Anonimização de Documentos](#anonimização-de-documentos)
    - [Utilização spacy](#utilização-spacy)
    - [Algoritmo de anonimização](#algoritmo-de-anonimização)
    - [Estrutura do ficheiro de tipos documentos](#estrutura-do-ficheiro-de-tipos-documentos)
    - [Encontrar os formatos dos vários documentos](#encontrar-os-formatos-dos-vários-documentos)
    - [Verificação da existência de keywords na janela de contexto](#verificação-da-existência-de-keywords-na-janela-de-contexto)
    - [Documentos com função de check](#documentos-com-função-de-check)
- [👋 Modos de Uso](#-modos-de-uso)
- [👥 Equipa](#-equipa)

## 🌟 Introdução

### Contexto

A privacidade de um indivíduo está intimamente ligada aos seus dados. Dados os quais, nos dias de hoje, são gerados numa quantidade nunca antes vista através da Internet. Estas dados, quando não são cuidadosamente tratados, podem afetar a segurança das pessoas. Neste segmento que surge o conceito de anonimização dos dados.

Uma definição conceptual da anonimização de dados pode ser ["para anonimizar quaisquer dados, têm de lhes ser retirados elementos suficientes para que deixe de ser possível identificar (de forma irreversível) o titular dos dados"](https://www.uc.pt/protecao-de-dados/protecao-de-dados-pessoais/anonimizacao-e-pseudonimizacao/) 
. Neste contexto surge o Regulamento Geral de Proteção de Dados (RGPD), como tabmém a A Lei Geral de Proteção de Dados Pessoais (LGPD) que define um [dado anonimizado  aquele que, originariamente, era relativo a uma pessoa, mas que passou por etapas que garantiram a desvinculação dele a essa pessoa](https://www.serpro.gov.br/lgpd/menu/protecao-de-dados/dados-anonimizados-lgpd). Conforme a LGPD, [alguns exemplos de dados pessoais são: nome, CPF, e-mail, idade, profissão, foto, entre outros](https://blog.hosts.green/dados-anonimizados/).

### Propósito e Objetivos

O propósito deste projeto é garantir a anonimização dos dados sensíveis pessoais presentes em documentos. Assim, o seu objetivo é concretizar um *software* que realiza uma série de tratamento de dados por forma a desvincular os dados das pessoas identificadas por eles. Este tratamento de dados resultará numa conversão de um dado documento numa versão sua anonimizada. Dentre as diversas formas de dados pessoais existentes, foram consideradas: o nome das pessoas/organizações, endereços (físicos ou na Web) e números identificadores de documentos (como o CC, carta de condução, entre outros).

Em suma, o objetivo principal do sistema é garantir a segurança dos indíviduos através de processos de anonimização. Uma vez que existem diversas formas de se concretizar esta tarefa, [não havendo um processo único de anonimização, a solução ideal será a que apresente em cada processo a maior impossibilidade da “re-identificação dos titulares dos dados”. Por princípio, a anonimização deverá ser um processo irreversível, análogo à destruição.](https://www.uc.pt/protecao-de-dados/protecao-de-dados-pessoais/anonimizacao-e-pseudonimizacao/)


## ⚙️ Caracterização do sistema

### Arquitetura

 <img src="https://raw.githubusercontent.com/LittleLevi05/spln-2223/main/TP2/images/arq.png" alt="Alex">

### Anonimização de Nomes


Os **nomes** anonimizados nesta etapa da ferramenta consistem em:

* **Nomes de Pessoas**: nomes próprios, apelidos, alcunhas. Por exemplo: *João Pedro*, *Juliana*.
* **Nomes de Organizações**: nomes de entidades estruturadas, geralmente composta por um grupo de pessoas, que trabalha para atingir objetivos específicos. Por exemplo: *Petrobras*, *Banco do Brasil*.

Para a anonimização destes nomes foi decidido que, ao serem identificados, deviam ser substituídos pelas correspondentes iniciais intercaladas com o **ponto final**. Mas **não somente isso**, uma vez que poderia haver a problemática de nomes diferentes corresponderem as mesmas iniciais. Ora, uma coisa é anonimizar um texto, outra é fazer ele **perder o sentido e coesão**. Não pretendemos causar a perda de significado no texto, isto é, deve ser possível continuar a lê-lo sem deixar de compreendê-lo. O seguinte texto é um exemplo disto: 

```
José Pedro esteve na Praça dos Arsenalistas naquela tarde. Quando José Pedro
encontrou João Pinto, já era tarde demais. João Pinto estava morto diante de José Pedro.
A partir deste dia a vida de José Pedro nunca foi a mesma, nem Joana Pedrosa (sua parceira
de trabalho no Banco do Brasil) acreditava mais nele.
```

Reparemos que as três entidades neste texto possuem as mesmas iniciais. Se os seus nomes apenas fossem substituídos pelas respectivas iniciais intercaladas com ponto, então teríamos uma frase do tipo:

```
Quando J.P encontrou J.P, já era tarde demais.
```

A compreensão da frase **foi comprometida** e, por tanto, um cuidado adicional deve ser tomado. Esse cuidado consiste justamente em adicionar um **identificador** numérico as entidades, por forma a, quando for decteado o José Pedro, seja possível distingui-lo do João Pinto. Este identificador, ao ser adicionado na anonimização, torna o texto do seguinte modo:

```
J.P(0) esteve na Praça dos Arsenalistas naquela tarde. Quando J.P(0)
encontrou J.P(1), já era tarde demais. J.P(1) estava morto diante de J.P(0).
A partir deste dia a vida de J.P(0) nunca foi a mesma, nem J.P(2) (sua parceira
de trabalho no B.d.B(0)) acreditava mais nele.
```

Como pode ser visto, sem revelar a identidade de nenhuma entidade, consegue-se agora compreender a natureza do significado das frases.

A metodologia do algoritmo geral para anonimização dos nomes baseou-se então em três etapas:

1.  Detecção das entidades do texto.
2.  Filtragem das entidades que representam **pessoas** e **organizações**;
3.  Calculo do identificador das entidades filtradas;
3. Substituição do nome destas entidades pelo seu nome anonimizado com o identificador.

A etapa 1 e 2 foram concretizadas utilizando a biblioteca Spacy. Após carregar o modelo de processamento de texto no idioma do texto dado pelo utilizador e aplicar os processamentos linguísticos deste modelo no texto, é possível extrair as suas entidades da seguinte maneira:

```Python
nlp = spacy.load('en_core_web_sm')
doc = nlp(self.text)
for ent in doc.ents:
    if ent.label_ == "PERSON" or ent.label_ == "ORG":
        # substitution
```

Por outro lado, a etapa 3 e 4 foram realizadas com técnicas de processamento de texto em Python, utilizando alguns métodos sobre *strings* e o módulo RE para expressões regulares. Dada uma entidade, os seus respectivos nomes foram separados a partir de um ou mais carácter de espaço em branco e, de seguida, o **nome anonimizado**  foi formado com as iniciais de cada nome concatenadas com o carácter **"."**. Inicialmente, foi utilizada a função *split* sobre *strings* com um único delimitador de "espaço" para serem separados os nomes de uma entidade. Porém, esta alternativa não foi seguida, uma vez que alguns textos mal formados poderiam conter mais de um carácter de espaço em branco entre os nomes de uma entidade. Por isso que, como pode ser visto no excerto de código seguinte, foi utilizado o *split* do módulo RE que possibilitar a utilização de uma expressão regular para informar o delimitador do *split*.

```Python
if ent.label_ == "PERSON" or ent.label_ == "ORG":
    ent_names = re.split(r"\s+",ent.text)
    anonymized_name = ".".join(name[0] for name in ent_names)
```

Como foi exemplicado anteriormente, este termo *anonymized_name* ainda não está completo. Falta a adição do identificador da entidade. Para isto foi criado um dicionário chamado *dic_names*. Seu objetivo é relacionar, para cada valor de letras iniciais intercaladas com ponto (*anonymized_name* sem identificador) os nomes das entidades 
que utilizam tais letras iniciais de forma idêntica. Por outras pavras, no caso do exemplo anterior, este dicionário teria:

```
dic_names = {
  "J.P" = ["José Pedro", "João Pinto", "Joana Pedrosa"]
}
```

Deste modo, foi decidido que o identificador de cada entidade
seria justamente a sua posição na lista de nomes do seu nome anonimizado. Daí resulta no José Pedro ser o J.P(0), o João Pinto ser o J.P(1) e a Joana Pedrosa a J.P(2). O algoritmo que efetua o calculo do identificador é o seguinte:

```Python
if anonymized_name in dic_names:
    if ent.text in dic_names[anonymized_name]:
        id = dic_names[anonymized_name].index(ent.text)
    else:
        id = len(dic_names[anonymized_name])
        dic_names[anonymized_name].append(ent.text)
else:
    id = 0
    dic_names[anonymized_name] = [ent.text]
```

 Uma vez em posse do nome anonimizado com o seu identificador, bastava substituir todas as ocorrências do nome sem anonimização pelo termo anonimizado. 
 
 ```
 anonymized_name += '('+str(id)+')'
self.text = re.sub(ent.text,anonymized_name,self.text)   
 ```

### Anonimização de Endereços

Já nesta etapa, o objetivo passou para anonimizar endereços, quer
endereços *web*, quer endereços físicos. Assim, os endereços
anonimizados consistem em:

-   **Endereços de Localização**: endereços físicos de locais no mundo.
    Por exemplo: *Rua Chãozinha, nº23*;

-   **Endereços de *email***: endereços de correio eletrónico. Por
    exemplo: *email@example.com*;

-   **Endereços URL**: estes encontram-se subdivididos em duas partes,
    que serão tratadas de forma diferente:

    -   **Endereços de Redes Sociais**: endereços de aplicações *web*
        muito conhecidas. Por exemplo: *www.facebook.com*;

    -   **Endereços *Web***: todos os endereços URL que não são de uma
        rede social conhecida. Por exemplo: *pt.overleaf.com*.

De forma a anonimizar os endereços, foi seguida a política definida no
trabalho prático. Desta forma, quando um endereço de localização é
encontrado, o mesmo é substituído por *localização\...*, já quando um
endereço de *email* é encontrado, este é substituído por *email\...*,
por outro lado, quando um endereço de rede social é encontrado, este é
substituído pelo nome da rede social em questão seguido de reticências,
por exemplo, *Instagram\...*, por fim, quando um endereço *web* é
encontrado, este é substituído por *www\...*.

Vejamos o seguinte exemplo:

```
Era uma bela manhã de verão, quando o José Pedro decidiu que iria
visitar a Rua da Chãozinha, nº25, 1º andar, em Lisboa. Isto deveu-se ao
anúncio que ele encontrou em www.instagram.com. Inicialmente, o José
Pedro ainda visitou o vídeo presente em www.youtube.com para verificar a
veracidade dos factos apresentados no anúncio. Como parecia tudo muito
bom, dirigiu-se a www.google.com, para aceder ao seu email. Lá, enviou
um email para reservas@gmail.com para reservar o seu lugar.
```

Ao aplicarmos a anonimização definida, obtemos o seguinte resultado:

```
Era uma bela manhã de verão, quando o José Pedro decidiu que iria
visitar a localização... . Isto deveu-se ao anúncio que ele encontrou
em www.... Inicialmente, o José Pedro ainda visitou o vídeo presente em
www... para verificar a veracidade dos factos apresentados no anúncio.
Como parecia tudo muito bom, dirigiu-se a www..., para aceder ao seu
email. Lá, enviou um email para email... para reservar o seu lugar.
```

A metodologia do algoritmo geral para anonimização baseou-se então nas
seguintes etapas:

1.  Deteção dos endereços no texto;

2.  Filtragem dos tipos de endereço;

3.  Substituição dos *tokens* pelo seu valor anonimizado.

À semelhança do módulo anterior, foi utilizada a biblioteca Spacy para
fornecer alguma ajuda na concretização dos objetivos propostos. O
carregamento do modelo de processamento de texto para posteriormente
aplicar os processamentos linguísticos do modelo no texto, sendo
possível efetuar o tratamento pretendido é feito da seguinte maneira:

```
    replace_loc = False
    prev_token_space = False
    for (i, token) in enumerate(doc):
        if token.like_email:
            # trata email
        elif token.like_url:
            # trata urls web e de redes sociais
        elif token.ent_type_ == "LOC" or token.ent_type_ == "GPE":
            # trata endereços de localização
```

Por outro lado, foi ainda necessário a utilização do módulo RE para o
tratamento da diferenciação entre urls genéricos e urls de redes
sociais, bem como para a aglomeração de elementos pertencentes a uma
localização (por exemplo, *Rua da Veiga, nº23, 5230-021* deverá ser
substituído por um único parâmetro *localização\...*).

O tratamento da diferenciação entre urls é realizado da seguinte
maneira:

```
    if token.like_url:
        url_matched = False
        for pattern, replacement in self.social_networks_regex.items():
            if re.search(pattern, token.text, re.IGNORECASE):
                url_matched = True
                # trata endereço de rede social
            if not url_matched:
                # trata endereço geral
```

Assim, de forma a ser possível testar as expressões regulares das
diferentes redes sociais detetadas, foi implementado um dicionário que
associa a cada expressão regular o valor que o token deverá tomar caso
dê *match* com a mesma:

``` 
social_networks_regex = {
r"https?://(?:www\.)?github\.com/([^/?#]+)": "GitHub...",
r"https?://(?:www\.)?gitlab\.com/([^/?#]+)": "GitLab...",
r"""https?://(?:www\.)?goodreads\.com
    /(?:book/show|author/show|user/show)/(\d+)""": 
    "Goodreads...",
...
}
```

As redes consideradas para substituições específicas foram:
-   Facebook;
-   Twitter;
-   Instagram;
-   LinkedIn;
-   YouTube;
-   Telegram;
-   WhatsApp;
-   TikTok;
-   Pinterest;
-   Reddit;
-   Tumblr;
-   Flickr;
-   Quora;
-   Medium;
-   Twitch;
-   Zoom;
-   Google Meet;
-   Jitsi;
-   Trello;
-   Slack;
-   Discord;
-   Stack Exchange;
-   Stack Overflow;
-   Stack Apps;
-   GitHub;
-   GitLab;
-   Goodreads.

Por fim, de forma a efetuarmos o tratamento adequado da localização, é
preciso analisar o contexto envolvente às palavras detetadas como
localização, desta forma, o tratamento é efetuado da seguinte maneira:

```
if replace_loc:
    if (re.match(r"(\d+|em|na|no)", token.text)):
        if (self.check_context(doc, i)):
            continue
        elif (
                token.ent_type_ == "LOC"
                or token.ent_type_ == "GPE"
                or self.match_address(token.text)
            ):
                continue
        else:
            replace_loc = False
...
elif token.ent_type_ == "LOC" or token.ent_type_ == "GPE":
        if not replace_loc:
            replace_loc = True
            anonymized_text += "localização..."
```

O método que permite a verificação de contexto é o seguinte:

```
def check_context(self, doc: spacy.__doc__, i: int) -> bool:
    if i == 0:
        return False
    if self.match_address(doc[i-1].text) or 
        self.match_address(doc[i+1].text):
        return True
    if doc[i + 1].ent_type_ == "LOC" or doc[i + 1].ent_type_ == "GPE":
        return True

def match_address(self, text: str) -> bool:
    for item in self.address_regex:
        if re.search(item, text, re.IGNORECASE):
            return True
    return False
```

Para isto, à semelhança daquilo que foi feito com o caso das redes
sociais, possuímos uma lista com expressões regulares indicadoras de
endereço que o Spacy não é capaz de detetar, visto dependerem do
contexto envolvente:

```
address_regex = [
    r"n(([u|ú]m)?e(ro)?)?º?\.?\s?\d+",
    r"\d{4}-\d{2,3}-?",
    r"[,;:-]"
]
```

### Anonimização de Documentos
Os documentos anonimizados são identificados através de uma expressão regular. De seguida, só é realizada a anonimização se na periferia do formato identificado for encontrada pelo menos uma keyword associada ao documento.

A associação do formato do documento e das keywords permite aumentar o contexto disponível para tomar a decisão se a anonimização está correta. 
Considere-se o caso específico de um número de telemóvel com 9 dígitos e o número de identificação fiscal (NIF). Ambos têm o mesmo formato, 9 dígitos seguidos sem espaços. Se na periferia do formato encontrado se encontrar a keyword "nif" há uma maior confiança que o formato encontrado é de facto um NIF. Se, por outro lado, se encontrar uma keyword "ligar" há uma maior confiança que o formato encontrado é um número de telemóvel. 
No entanto, é necessário um jogo de balanceamento, uma vez que não se pretende pesquisar numa periferia muito grande, onde o contexto se ia tornar muito abrangente, mas também não se pretende ter uma periferia muito pequena.
A figura seguinte permite encontrar um exemplo onde uma periferia muito grande poderia levar a resultados errados. 

```
A Carla está sempre a avisar para eu não me esquecer de adicionar o nif do clube, sempre que ponho
combustível na carrinha do clube. O problema é que já me esqueci, sabes qual é o nif? 
Sim, é 123456789, mas o melhor era ligares para confirmar. O número de telemóvel dela é o 912345678
Obrigado! Vou ver se lhe ligo assim que conseguir. 
```

Neste caso, se a periferia fosse muito abrangente, ao identificar "912345678" ia-se encontrar a keyword "nif" e haveria um falso positivo. 
Por outro lado, se a periferia fosse muito pequena, por exemplo mais ou menos duas palavras, não se identificaria a keyword "ligar" e haveria um falso negativo. 

Este problema poderia ser resolvido se se assumisse que se fizesse duas pesquisas. 
Uma da expressão identificada para o início do texto e da expressão para o fim do texto.
Desta forma a keyword mais próxima era que seria "encontrada" primeiro. 

A razão pela qual foi estabelicido um limite nesta janela de procura era o overhead de procurar no texto todo. 
Na verdade, é comum encontrar-se estas keywords perto da expressão encontrada e quanto mais afastada estiver a keyword menos confiança se tem que realmente a expressão é a que mapeia o tipo de documento que se está a procurar no momento.

#### Utilização spacy
Assim que se obtem o texto é criado o documento spacy do texto. A razão para utilizar o spacy é porque desta forma é possível fazer uma lemalização da janela de contexto, e pesquisar pelo lema de uma keyword nesta janela com lemalização. A vantagem de fazer a lemização é a abrangência de mais palavras mapeadas na mesma keyword.
No exemplo seguinte pode-se encontrar uma palavra, ligou, que não faria match com a palavra ligar. 

```
O Diogo ligou para o número 912345678 da Carla. 
```

Considere-se a janela "ligou para o número 912345678 da Carla.", ao realizar a lemalização desta janela obtém-se
"ligar para o número 912345678 de o Carla ." Desta forma a keyword "ligar" já consegue fazer match.

#### Algoritmo de anonimização
Existem três passos na realização da anonimização. 

1. Parsing do ficheiro que contém os documentos que se pretende identificar;
2. Para cada tipo de documento encontrar formatos que façam match no texto;
3. Para cada match encontrada verificar se existem keywords na janela de contexto. Se um tipo de documento tiver um algoritmo de check apenas subsituir se o check provar que o padrão é válido.

De seguida vai ser explorado cada passo em pormenor.

#### Estrutura do ficheiro de tipos documentos
O ficheiro contém a identificação do país onde os documentos são emitidos. 
De seguida existe uma lista de documentos a serem identificados.
Cada documento contém:
* um identificador do documento;
* o padrão onde deve constar uma expressão regular do formato do documento;
* uma lista de keywords para permitir um maior contexto na identificação do documento;
* um booleano que identifica se o documento tem uma função de check;
* um identificador que substitua o documento encontrado.

#### Encontrar os formatos dos vários documentos
Para cada tipo de documento existente é utilizada a função `re.sub` com a expressão regular do formato do documento,
com um método `change` responsável pela verificação se o match vai ser anonimizado e por último o texto mais atual. 
Ou seja, se já houve anonimizações este texto vai contê-las.

#### Verificação da existência de keywords na janela de contexto
O primeiro obstáculo é a criação da janela de contexto. 
A janela de contexto é composta por tokens e está centrada no primeiro caratér de um match. 
Portanto é necessário saber qual o token que corresponde ao offset desse caratér no texto. 

```
"A Alice e o Bob estão a comunicar por um telefone estragado."
```

Neste exemplo se o match for "Alice" o offset do caratér 'A' vai ser utilizado para calcular qual o token vai ser utilizado 
para centrar a janela de contexto. Para tal percorre-se o documento spacy, token a token, e verifica-se a condição             
`token.idx <= offset < token.idx + len(token.text)`. Se for verdadeira então este token é considerado o token central da janela. 
Neste exemplo a janela seria: `[A_token, Alice_token, e_token]`. De salientar que como o método `re.sub` faz uma travessia do texto
de forma sequencial do primeiro caratér para o último, sem saltos, é possível ir percorrendo o documento spacy na verificação da condição, invés de 
estar sempre a percorrer o documento spacy. Para tal guarda-se o último índice do último token que foi o centro de uma janela. 

No entanto, esta verificação assume um offset do caratér em relação ao texto original, texto usado para criar o documento spacy.
Desta forma sempre que existe uma substituição, e consequente alteração do texto original, é inserido um par `(pos, delta)` numa lista de histórico.
Pode-se considerar que este histórico permite através da última versão de texto e um offset de um caratér nesse texto e um offset de um caratér nesse texto, obter o offset do texto original. Assim, sempre que é inserido este par na lista de histórico é necessário atualizar todas as entradas seguintes com a sua posição nova no novo texto. Ou seja, para as entradas seguintes a sua posição/offset fica pos_antiga + delta_novo.

Ao fazer match de uma expressão de um texto, que não o original, extrai-se o offset do primeiro caratér do match (com recurso ao método `match_object.start(0)`) 
e faz-se uma conversão de qual seria o offset no texto original. No caso de não ter havido nenhuma substituição num caratér com offset inferior 
então o offset obtido pelo o match é equivalente ao do texto orignal. No entanto, se já houve substituição, é necessário fazer uma soma de deltas de substituição prévias e subtrair o delta acumulado.

 
Com a janela já criada, percorre-se token a token da janela e cria-se uma string de lemmas desses tokens separados por espaços.
De seguida, para cada key nas keywords verifica-se se o lemma dessa key existe na string de lemas da janela. Se existir então a match pode eventualmente ser anonimizada.

#### Documentos com função de check
Há documentos que requerem uma função de check. Para tal assume-se que existe uma função com o nome "check_country_tipo_de_padrao" que devolve um booleano.
O exemplo a seguir demonstra um exemplo de um cartão de cidadão (CC) válido e de outro inválido, assim como as contas feitas para verificar se um CC é valido.

```
Cartão de cidadão válido: 00000000 0 ZZ4 
Check: 
- 00000000 0 (35)(35)4
- (0×2) = 0, (0×2) = 0, (0×2) = 0, (0×2) = 0, (0×2) = 0, ((35×2) = 70 – 9) = 61
- (0) + 0 + (0) + 0 + (0) + 0 + (0) + 0 + (0) + 35 + (61) + 4 = 100
- 100 mod 10 == 0, 0 == 0, válido.

Cartão de cidadão inválido: 12345678 2 ZZ4
Check: 
- 123456 2 (35)(35)4
- (1x2) = 2, (3x2) = 6, (5x2) = 10 - 9 = 1, (7x2) = 14 - 9 = 5, (2x2) = 4, ((35x2) = 70 - 9) = 61
- (2) + 2 + (6) + 4 + (1) + 6 + (5) + 8 + (4) + 35 + 61 + 4 = 138
- 138 mod 10 != 0, 8 != 0, inválido.
```







## 👋 Modos de Uso

A utilização do programa HShield pode englobar tanto uma anonimização global do documento de *input*, tanto como uma anonimização especializada para algum termo-alvo. Disponibiliza-se assim opções para serem anonimizados os (1) nomes, (2) documentos e (3) endereços. Estas opções podem ser utilizadas em conjunto, mediante a necessidade do utilizador.

```bash
Data anonymizer tool

positional arguments:
  filename

optional arguments:
  -h, --help            show this help message and exit
  -n, --name            anonymize only names
  -d, --document        anonymize only documents
  -a, --address         anonymize only addresses
  -o OUTPUT, --output OUTPUT
                        output file

Build by Henrique, José and Alex
```

## 👥 Equipa

| ![Henrique Parola](https://raw.githubusercontent.com/LittleLevi05/spln-2223/main/TP2/images/henrique.jpeg) | ![José Pedro](https://raw.githubusercontent.com/LittleLevi05/spln-2223/main/TP2/images/jose.png) | ![Alex](https://raw.githubusercontent.com/LittleLevi05/spln-2223/main/TP2/images/alex.png) |
| :--------------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------: |
|                                              Henrique Parola                                               |                                            José Pedro                                            |                                            Alex                                            |
