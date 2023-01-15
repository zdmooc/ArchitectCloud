from jinja2 import Template

reponse = input("Votre nom : ")

tm = Template("Bonjour {{ nom }}")
texte = tm.render(nom=reponse)

print(texte)
