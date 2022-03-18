# DevFit

- Cada User é um aluno
- Cada Tenant é uma academia/unidade
- Quando o user loga ele precisa ser redirecionado para o seu schema/tenant

- Objetivo 1: isolar user por schema/tenant

- Sugestão 1: 
  - home page mostra lista de schemas/tenants
  - /<tenant_id>/
  - redireciona para esse schema
