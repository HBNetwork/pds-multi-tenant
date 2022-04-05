# DevFit

## Installation
```bash
git clone git@github.com:henriquebastos/pds-multi-tenant.git
cd pds-multi-tenant/update_sem_where/
docker-compose up -d
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
pre-commit install
cp contrib/env-sample .env

```

### Test
```bash
pytest
```

### Run
```bash
python manage.py migrate
python manage.py runserver
```


## Fluxo
1. Chega a request
1. TenantMiddleware seta tenant na thread.Local
1. DatabaseRouter escolhe o banco de acordo com o tenant que está no thread.local
1. Django busca esse banco no settings.DATABASES que é o custom DatabaseMapper
1. DatabaseMapper retorna o banco com o usuário do tenant


## Próximos passos
- DatabaseRouter que lê do thread.Local
- Criar usuário do banco quando cria um tenant
- Command para criar novos tenants/schemas
  1. criar schema com `tenants.create`
  2. rodar migrations nesse novo schema para criar tabelas
- criar custom manage.py - [https://books.agiliq.com/projects/django-multi-tenant/en/latest/shared-database-isolated-schema.html#managing-database-migrations](https://books.agiliq.com/projects/django-multi-tenant/en/latest/shared-database-isolated-schema.html#managing-database-migrations)


## Definições
- Cada User é um aluno
- Cada Tenant é uma academia/unidade
- Quando o user loga ele precisa ser redirecionado para o seu schema/tenant


## Objetivos
1. isolar user por schema/tenant
   - Sugestão 1:
     - home page mostra lista de schemas/tenants
     - /<tenant_id>/ redireciona para esse schema
