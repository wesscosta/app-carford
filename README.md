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

1. Acesso: [http://127.0.0.1:80/](http://127.0.0.1:8000) or [http://localhost:80/](http://localhost:8000)
