# Observer

## Definição do GoF, no livro "Padrões de Projeto" (2000)

### Intenção: 
Definir uma dependência um-para-muitos entre objetos, de maneira que quando um objeto muda de estado todos os seus 
dependentes são notificados e atualizados automaticamente.

### Tipo de Pattern:
Comportamental

### Também conhecido como:
Dependents, Publish-Subscribe

### Aplicável quando:
- Quando uma abstração tem dois aspectos, um dependente de outro. Encapsulando esses aspectos em objetos separados, 
permite-se variá-los e reutilizá-los independentemente.
- Quando uma mudança em um objeto exige mudanças em outros, e você não sabe quantos objetos necessitam ser mudados.
- Quando um objeto deveria ser capaz de notificar outros objetos sem fazer hipóteses, ou usar informações, sobre quem
 são esses objetos. Em outras palavras, você não quer que esses objetos sejam fortemente acoplados.
 
## Participantes:
- **Subject:** Conhece os seus **Observers**. Um número qualquer de objetos **Observer** pode observar um **Subject**. 
Fornece também uma interface para acrescentar ou remover objetos, permitindo associar e desassociar objetos 
**Observer**.
- **Observer:** Define uma interface de atualização para objetos que deveriam ser notificados sobre mudanças em um 
**Subject**.
- **ConcreteSubject:** Armazena estados de interesse para objetos **ConcreteObserver**. Envia uma notificação para os 
seus **Observers** quando seu estado muda.
- **ConcreteObserver:** Mantém uma referência para um objeto **ConcreteSubject**. Armazena estados que deveriam 
permanecer consistentes com os do **Subject**. Implementa a interface de atualização do **Observer**, para manter seu 
estado consistente com o do **Subject**.
