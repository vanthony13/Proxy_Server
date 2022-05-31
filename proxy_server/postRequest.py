import requests



url = 'http://127.0.0.1:3002/example.html'

response = requests.post(url, data={"Disciplina": "Arquitetura de Rede", "Professor": "Antonio Varela"})
print(response.status_code)
