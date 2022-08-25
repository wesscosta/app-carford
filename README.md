# desafio carfor
### Nork-Town (cidade)
- 1 Pessoa pode ter até 3 veículos
- os veiculos podem ter as cores 'amarelo', 'azul' ou 'cinza'.
- os veiculos podem ser dos modelos: 'escotilha', 'sedan' ou 'conversível'.

### Carford (loja de carros)
- add proprietários (proprietários podem não ter carros → oportunidade de venda)
- add carros (Carros não podem existir sem proprietários)



## :computer: Steps

1. Faça o clone do repositório do github
```bash
  # https
  git clone https://github.com/Transportta/Sistema-Transportta.git sistema-transportta

  # ssh
  git clone git@github.com:Transportta/Sistema-Transportta.git sistema-transportta
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


