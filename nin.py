from jinja2 import Template
template = Template("Hello, {{ name }}")

print(template.render(name = "Daniel"))
print(template.render(name = "Montoya"))

print(f"Hola {name}")