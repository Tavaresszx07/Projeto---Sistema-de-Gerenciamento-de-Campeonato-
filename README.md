# Sistema de Gerenciamento de Campeonato de Futebol

Projeto backend feito a principio com Django. A ideia é criar um sistema para gerenciar campeonatos de futebol.

Ainda está no começo, mas a intenção é ter cadastro de times, jogadores, partidas e classificação automática.

---

## O que já tem:

## Lincoln Ricardo¬
- Cadastro de times pelo admin
- Listagem e detalhe dos times
-organização básica do sistema

## Cauã¬
- Expansão do campeonato para 16 times com dados reais (estádios, técnicos e cidades) 
- Tabela de Desempenho dos Clubes no Dashboard (calcula jogos, vitórias, empates e derrotas automaticamente)
- Ajuste visual do grid para o novo limite de times
## Pedro Caua¬
- Integração ao banco de dados e criptografia do site
## O que ainda irá se fazer

- Partidas
- Classificação
- Estatísticas
---

## Como rodar

```bash
git clone https://github.com/LincolnRicardo/Projeto---Sistema-de-Gerenciamento-de-Campeonato-.git
cd Projeto---Sistema-de-Gerenciamento-de-Campeonato-/gerenciamento
pip install django
python manage.py migrate
python manage.py runserver
```

Desenvolvido por grupo em cooperação.