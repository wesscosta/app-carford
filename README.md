# Carford
Este é um projeto fullstack com o backend em flask(python), frontend em desenvolvimento em react
Banco de dados com Postgres e PGadmin4 além do uso de tecnologias como docker, docker-compose, nginx, gunicorn...
 O desafio consiste na seguinte logica.
 
### Nork-Town (cidade)
- Uma Pessoa pode ter até 3 veículos
- Os veículos podem ter as cores 'amarelo', 'azul' ou 'cinza'.
- Os veículos podem ser dos modelos: 'escotilha', 'sedan' ou 'conversível'.

### Carford (loja de carros)
- add proprietários (proprietários podem não ter carros → oportunidade de venda)
- add carros (Carros não podem existir sem proprietários)



## :computer: Steps

1. Faça o clone do repositório do github
```bash
  # https
  git clone https://github.com/wesscosta/carford-flask-postgres-api.git

  # ssh
  git clone git@github.com:wesscosta/carford-flask-postgres-api.git
```
2. Subir os containers
```bash
  # run in background
  docker-compose up -d
```
3. Para visualizar o nome dos containers rodando
```bash
  docker ps
```
4. Entra no container web
```bash
  docker exec -it CONTAINER_NAME bash
```
4. Entra no container web
```bash
  docker exec -it CONTAINER_NAME bash
```
5. Acesso: [http://localhost:80/](http://localhost:80)

6. Acesso ao PGAdmin: [http://localhost:15432/](http://localhost:15432)
```text
  - email: postgres@postgres.com
  - senha: postgres
```


