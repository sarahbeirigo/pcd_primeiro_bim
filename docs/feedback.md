# Avaliação Entregas

## E1

Excelente pessoal ! Gostei muito da documentação e fizeram até bem a mais nesse quesito do que eu havia pedido. O Figma fiquei em dúvida como seriam os menus ali para as ações, visão do administrador (quem cria as rifas) e a visão do cliente (quem compra) mas consegui visualizar como estao pensando. O modelo de DER está legal! Apenas 2 sugestões. A table "Draw" representa o sorteio certo? Os números que foram sorteador. Se for isso talvez faça sentido ter somente o relacionamento 1-1 com Ticket.  Poderia ser até um campo datetime indicando se aquele Ticket foi o sorteado mas podemos ter outras informaçòes ali então fica ate legal ter outra tabela, poderiamos guardar quem foi o "sorteador" ou o método, etc.  Em todo o caso nao precisaria do user_id nem do raffle_id, somente do ticket_id. Mas posso ter me enganado no entendimento (ex: faz sentido sortear números que nao foram comprados? acredito que não).  Outra coisa em relação as tecnologias, essas serão fixas para todos os grupos em termos de framework, todos vamos usar Django e um banco relacional.  No segundo semestre teremos uma entrega extra em que vcs podem usar qualquer tecnologia, mas como parte do curso, vamos ficar com Django nessas primeiras entregas ok? Com certeza vcs nao precisaram fazer o projeto inteiro, na oprecisa ter integracao com meio de pagamento, nem login social. A ideia é fazer o CRUD de uma ou 2 tabelas mas isso para as próximas entregas. Mas ótimo projeto Parabéns!!!0

## E3

Olá pessoal! Segue avaliação
- Models: Ótimo, legal que usaram o uuid, falei pouco dessa questão, nao sei se investigaram as vantages e desvantagens de usar, vale a pena. Como colocaram created_at e updated_at em todos os models, era possível criar um model "pai" e herdar todos os outros models dele. Mas tudo certo! (3)
- Admin: legal, acho que poderiam ter registrado todos os models no admin (1)
- Autenticação:  tudo certo! (2)
- 2 Views com Models: tudo certo por aqui tbm, esta tudo bem organizado tbm, parabéns!
- **Como vcs ja fizeram o CRUD completo, na próxima entrega pode ser só a apresentação que esta tudo certo! **(4)
