#Weather API com Python e Redis

Projeto desenvolvido para praticar consumo de APIs REST, cache com Redis e manipulação de dados JSON utilizando Python.

##Tecnologias

- Python
- Requests
- Redis
- Visual Crossing Weather API

##Funcionalidades

- Consulta informações climáticas de uma cidade
- Consome dados de uma API externa
- Armazena resultados em cache utilizando Redis
- Evita consultas repetidas à API
- Expiração automática dos dados armazenados

##Exemplo de Retorno

```json
{
  "cidade": "Sao Paulo",
  "temperatura": 21.5,
  "tempMax": 25.0,
  "tempMin": 16.0,
  "umidade": 75,
  "condicao": "Partially cloudy"
}
```
