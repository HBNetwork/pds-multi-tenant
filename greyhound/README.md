# Controle Financeiro

Mútiplos clientes (tenants) com suas operações bancárias separadas.
Multi-tenant funcionando com subdiretório ao invés de subdomínio.


## Installation
```bash
git clone git@github.com:henriquebastos/pds-multi-tenant.git
cd pds-multi-tenant/greyhound/
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Test
```bash
pytest
```

### Run
```bash
python manage.py runserver
```

# TO DO

- [X] Extrair tenant_name do ínicio da URL
- [X] Criar exceção para /admin/
- [X] Tratar URLs sem barra
- [X] Testes
- [X] Criar model de tenants
- [X] Criar models da aplicação
- [ ] Criar test para o TenantMiddleware
- [ ] Criar um app isolado com as funcionalidades multi-tenant
- [ ] Tratar na criação de tenants as exceções (exempt? boolean no tenant model?)
- [ ] Resolver url resolve sem tenant. Criar um template tag?
- [ ] Como tratar a url /? Criar namespace t/?
- [ ] Definar como os usuários se relacionarão com os tenants


# Dúvidas

- Por que funcionou com getattr com o manager errado? (AttributeError: '_thread._local' objects has no attribute 'tenant_id'

- A aplicação deve ficar responsável pelo "rewrite" da url?
- MiddlewareMixin deprecated, como lidar com process_request?
- Ordem dos middlewares influência? Onde colocar?
- Middleware acumulam as operações sobre o request/response
- Que cargas d'água seria thredlocal? Por que foi usado no artigo referência?

# Referências

https://www.viget.com/articles/multi-tenancy-in-django/

