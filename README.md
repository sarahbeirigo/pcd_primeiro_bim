# Projeto "Rifando"

## 1. Visão Geral

**Nome do Produto:** "Rifando"

**Descrição:** O site "Rifando" tem por objetivo ser uma plataforma online para gestão de rifas, oferecendo um sistema integrado para criação, gerenciamento, pagamento e sorteio de números, proporcionando uma experiência simples, intuitiva e segura para administradores e participantes.

**Links Importantes:**
- [Figma](https://www.figma.com/design/Q8N8uP5hx2WJI2540T6yH5/MOckups-Projeto-rifa?node-id=0-1&t=XVW21pingB2RuGH3-1)
- [Diagrama do Banco de Dados](https://portfolio-portfolio-assets.fxflae.easypanel.host/portfolio-assets/modelo-de-dados.pdf)

## 2. Objetivos do Produto

- **Facilitar a criação e administração de rifas** com um sistema intuitivo e acessível.
- **Automatizar pagamentos** via integração com gateways financeiros, garantindo agilidade e segurança nas transações.
- **Garantir transparência nos sorteios**, permitindo a realização automática ou manual, com exibição pública dos resultados.
- **Fornecer um painel administrativo completo**, permitindo o gerenciamento eficiente de rifas, participantes e finanças.
- **Proporcionar uma experiência amigável para usuários**, permitindo fácil participação, acompanhamento de rifas e recebimento de notificações.

## 3. Público-Alvo

- **Empreendedores e pequenos negócios** que utilizam rifas para promoções e engajamento de clintes.
- **ONGs e instituições de caridade** que realizam rifas para arrecadação de fundos.
- **Clubes, associações e comunidades** que organizam rifas entre membros para eventos ou causas expecíficas.
- **Influenciadores e criadores de conteúdo** que utilizam rifas para engajamento e distribuição de prêmios para seguidores.
- **Qualquer pessoa interessada em criar e gerenciar rifas de forma profissional**, sem complicações técnicas.

## 4.  Módulos do Sistema

### 4.1. Módulo de Criação e Configuração de Rifas

Módulo responsável pela geração de rifas, permitindo a personalização completa.

**Funcionalidades:**

- Criar rifas com título, descrição e imagem destacada
- Definir quantidade de números disponíveis
- Estabelecer valor unitário por número ou faixas de preços promocionais
- Configurar data de encerramento e sorteio
- Selecionar entre sorteio manual ou automático
- Gerar link único e compartilhável para cada rifa
- Definir regras e critérios de participação

### 4.2. Módulo de Pagamentos

Gerenciamento dos meios de pagamento e transações financeiras, garantindo segurança e automação.

**Funcionalidades:**

- Integração com gateways de pagamento (Pix, Cartão de Crédito, Boleto)
- Confirmação automática de pagamento via webhook
- Exibição do status de pagamento em tempo real no painel do usuário
- Emissão de comprovante de compra
- Controle de reembolsos e cancelamentos quando aplicável
- Relatórios financeiros detalhados

### 4.3. Módulo do Painel Administrativo

Área central para o gerenciamento da plataforma, oferecendo controle total aos administradores.

**Funcionalidades:**

- Dashboard com estatísticas de rifas ativas e finalizadas
- Listagem e gerenciamento de rifas criadas
- Controle e monitoramento de usuários e suas compras
- Edição de rifas em andamento
- Administração dos sorteios realizados
- Relatórios detalhados e exportação de dados
- Logs de auditoria e histórico de ações

### 4.4. Módulo de Sorteio

Módulo responsável por realizar e administrar os sorteios das rifas de maneira transparente e segura.

**Funcionalidades:**

- Sorteio automático baseado em loterias oficiais ou algoritmo interno
- Opção para sorteio manual pelo administrador
- Notificação automática dos ganhadores via e-mail ou SMS
- Divulgação pública dos resultados com registro de transparência
- Registro histórico de sorteios realizados

### 4.5. Módulo de Usuários

Área destinada aos participantes, permitindo a gestão de suas rifas adquiridas e interações.

**Funcionalidades:**

- Cadastro e login com e-mail ou redes sociais
- Visualização de rifas adquiridas e status de participação
- Histórico de pagamentos e prêmios ganhos
- Opção de indicação de amigos com sistema de bonificação (se aplicável)
- Notificações sobre status de rifas e sorteios
- Suporte ao usuário e área de ajuda

## 5. Requisitos Não Funcionais

- Interface responsiva e intuitiva, adaptável a diferentes dispositivos
- Alto desempenho e escalabilidade para suportar múltiplos acessos simultâneos
- Segurança robusta, incluindo criptografia de dados e proteção contra fraudes
- Conformidade com a LGPD (Lei Geral de Proteção de Dados)
- Logs de auditoria para rastreamento de ações e segurança
- Tempo de carregamento otimizado, inferior a 3 segundos

## 6. Técnologias

- **Frontend/Backend:** Next.js
- **Banco de Dados:** PostgreSQL
- **Autenticação:** Auth.js (antigo NextAuth.js)
- **Pagamentos:** Mercado Pago/Stripe
- **Hospedagem:** Digital Ocean
- **Notificações:** *A definir*

## 7. Métricas de Sucesso

- Número de visitantes no site.
- Taxa de conversão de visitantes em assinantes.
- Número de assinaturas ativas.
- Retenção de clientes e taxa de renovação.
- Novos clientes vindos por indicação dos usuários.
- Feedback positivo dos clientes.

## 8. Considerações Finais

Este documento define a estrutura inicial do projeto e serve como base para desenvolvimento. Revisões e ajustes podem ser necessários à medida que o sistema evolui e recebe feedback dos usuários.

# Integrantes do Grupo

- Caio Caminitti - 2146079
- Pedro Augusto - 2174638
- [Pedro Estevão - 2173562](https://www.pedroestevao.com)
- Sérgio Caminitti - 2171436