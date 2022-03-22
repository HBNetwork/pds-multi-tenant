# Estratégias de Aplicações Multi-Tenant estudadas no Passaporte Dev Sênior.

**Team Pycore**

## Estratégia de aplicação Multi-Tenant Single App with Multi Databa Instances

## How to Use this

### Crie as configurações no etc hosts para os mapeamentos de subdominios

Em `/etc/hosts` adicione:

```
127.0.0.1 poc.local
127.0.0.1 thor.poc.local
127.0.0.1 potter.poc.local
```

Cada subdominio é um `tenant` da aplicação. 
Portanto as estratégias de autenticação e login são separadas.

### Crie as migrações para cada `tenant`

```
python manage.py migrate --database=thor
python manage.py migrate --database=potter
```

### Use o `manage_tenants.py` para executar comandos especificos para cada tenant

`python tenant_context_manage.py thor createsuperuser --database=thor`

## To Do's

- [ ] Escrever testes;
- [ ] Usar resources na request para determinar o tenant ao invés de um subdominio;
- [ ] Adicionar steps de CI/CD com Githubflow;
- [ ] Tentar usar outra ferramenta ou linguagem para aplicar a estratégia;
- [X] Preencher o documento do PDS com informações das atividades;
- [X] Adicionar python decouple;
- [X] Alterar os nomes para nosso contexto de contabilidade(ou não, os bancos já estão com nomes próprios para nossos clientes :));
