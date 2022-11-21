from modelo import *

def run():
    p1 = Pessoa(nome = "Akemi", email = "akemi.shibukawa@gmail.com", senha = "antilopes1galopantes")
    p2 = Pessoa(nome = "João", email = "joao.abreu@gmail.com", senha = "luzes1para2o3mundo")

    db.session.add(p1)
    db.session.add(p2)
    db.session.commit()

    print(".....................................")
    print(p1)
    print(p2)
    print(".....................................")

    e1 = Emoji(pessoa = p1, dcria = date(2022, 10, 3), nemo = "coelho", repre = "O emoji representa um coelho femea", classi = "Animais", femo= 'sla')
    e2 = Emoji(pessoa = p2, dcria = date(2022, 10, 2), nemo = "pinheiro", repre = "O emoji representa o pinheiro que fica na minha casa", classi = "Planta", femo= 'sla2')

    db.session.add(e1)
    db.session.add(e2)
    db.session.commit()

    print(".....................................")
    print(e1)
    print(e2)
    print(".....................................")

    s1 = Sugestao(catalogacao = "Planta", ideia = "Samambaia")
    s2 = Sugestao(catalogacao = "Expressões", ideia = "Sorridente")

    db.session.add(s1)
    db.session.add(s2)
    db.session.commit()

    print(".....................................")
    print(s1)
    print(s2)
    print(".....................................")