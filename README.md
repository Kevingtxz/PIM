# InovAtiva PIM - Backend

<p align="center">
 <a href="#Sobre">Sobre</a> •
 <a href="#Algoritmo">Formula do bônus - Algoritmo</a> • 
 <a href="#Tecnologias">Tecnologias</a> • 
 <a href="#Manual">Manual</a> • 
 <a href="#Licence">Licence</a> • 
</p>


## Sobre
Espaço para iniciação de mentoria dentro da plataforma da InovAtiva possibilitando pessoas interessadas e qualificadas para realizar atividade de mentoria.
Através deste ambiente mais amigável para novatos, é possívem ingressar em uma trilha de desenvolvimento do mentor, e fazer parte de um sistema de ranking aberto para votos de investidores e mentores experientes da InovAtiva.


## Tecnologias
Python, Django, HTML, CSS, Javascript

## Algoritmo
O algorimo utiliza a média aritmédica de mentores por região e a divide pelo número de mentores em cada região e então multiplica esse valor por 10%, de maneira que o bonus regional em regiões com menos mentores sempre serão muito maiores as capitais. Isso servirá de base para adptação com inteligencia artificia e TensorFlow no futuro

                    Formula do bônus
1. Retirar a média aritmédica de mentores por região
2. Dividir esse valor para cada região individualmente
3. Multiplicar esse valor por 10%
4. Explicação, esse valor será inversamente proporcional ao número de mentores da região, uma vez que esse número dividirá o algoritmo.

## Manual
1. Certifiquesse de instalar devidamente Python (https://www.python.org/downloads/) 

2. -'pip install -r requirements'- para instalar todos os requerimentos da aplicação.

3. Baixe a pasta complet

4. Utilize os comandos'python manage.py makemigrations' e 'python manage.py migrate' para ativar o banco de dados. 

5. Utilize o comando 'python manage.py runserver', após isso o programa estará rodando em 'http://127.0.0.1:8000/' 

6. Vá a página 'http://127.0.0.1:8000/admin' e poderá alterar os dados ou pode fazer isso manualmente com o comando 'python manage.py shell' dentro do shell

7. O frontend está separado então não será possível navegar pelo site devidamente. Porém as páginas views estão prontas.

## Licence
[GPL-3.0](https://www.gnu.org/licenses/gpl-3.0.en.html)
