# página só importando e colocando um texto
    # import flet as ft
    # def main(page):
    #     texto = ft.Text("Hashzap")

    # ft.app(target=main, view=ft.WEB_BROWSER, port=8000)
# depois adiciona o botão de iniciar sem fazer nada
# depois adiciona a funcionalidade de abrir um popup (vazio ainda)
# depois preenche as infos do popup (sem funcionalidade)
# depois adiciona funcionalidade no clique do botão (colocar o campo de chat na página e retirar popup e botao iniciar)
        # import flet as ft

        # def main(page):

        #     campo_mensagem = ft.TextField(label="Digite uma mensagem")

        #     def entrar_chat(e):
        #         page.add(campo_mensagem)
        #         popup.open = False
        #         page.remove(botao_iniciar)
        #         page.update()

        #     nome_usuario = ft.TextField(label="Escreva seu nome no chat")
        #     popup = ft.AlertDialog(
        #         open=False,
        #         modal=True,
        #         title=ft.Text("Bem vindo ao Hashzap"),
        #         content=nome_usuario,
        #         actions=[ft.ElevatedButton("Entrar no chat", on_click=entrar_chat)])

        #     def abrir_popup(e):
        #         page.dialog = popup
        #         popup.open = True
        #         page.update()

        #     botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup)

        #     page.add(botao_iniciar)

        # ft.app(target=main, view=ft.WEB_BROWSER, port=8000)
# adicionar botao de enviar mensagem (logica de ft.Row e ft.Column)

# criar um chat fora do pubsub, no enviar do botao

        # import flet as ft

        # def main(page):

        #     chat = ft.Column()
        #     def enviar_mensagem(e):
        #         chat.controls.append(ft.Text(campo_mensagem.value))
        #         campo_mensagem.value = ""
        #         page.update()

        #     campo_mensagem = ft.TextField(label="Digite uma mensagem")
        #     botao_enviarmensagem = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)

        #     def entrar_chat(e):
        #         page.add(chat)
        #         page.add(ft.Row([campo_mensagem, botao_enviarmensagem]))
        #         popup.open = False
        #         page.remove(botao_iniciar)
        #         page.update()

        #     nome_usuario = ft.TextField(label="Escreva seu nome no chat")
        #     popup = ft.AlertDialog(
        #         open=False,
        #         modal=True,
        #         title=ft.Text("Bem vindo ao Hashzap"),
        #         content=nome_usuario,
        #         actions=[ft.ElevatedButton("Entrar no chat", on_click=entrar_chat)])

        #     def abrir_popup(e):
        #         page.dialog = popup
        #         popup.open = True
        #         page.update()

        #     botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup)

        #     page.add(botao_iniciar)

        # ft.app(target=main, view=ft.WEB_BROWSER, port=8000)

# deixar apenas a mensagem em si no enviar_mensagem (não incluir o usuário)
# editar o enviar_mensagem para virar enviar_mensagem_tunel e criar um evniar msg no botao
# adicionar o pubsubsend all no enviar msg e editar o enviar_mensagem_tunel para renderizar a mensagem
        # import flet as ft

        # def main(page):
            
        #     chat = ft.Column()
        #     def enviar_mensagem_tunel(mensagem):
        #         chat.controls.append(ft.Text(mensagem))
        #         page.update()

        #     page.pubsub.subscribe(enviar_mensagem_tunel)

        #     def enviar_mensagem(e):
        #         page.pubsub.send_all(campo_mensagem.value)
        #         campo_mensagem.value = ""
        #         page.update()

        #     campo_mensagem = ft.TextField(label="Digite uma mensagem")
        #     botao_enviarmensagem = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)

        #     def entrar_chat(e):
        #         page.add(chat)
        #         page.add(ft.Row([campo_mensagem, botao_enviarmensagem]))
        #         popup.open = False
        #         page.remove(botao_iniciar)
        #         page.update()

        #     nome_usuario = ft.TextField(label="Escreva seu nome no chat")
        #     popup = ft.AlertDialog(
        #         open=False,
        #         modal=True,
        #         title=ft.Text("Bem vindo ao Hashzap"),
        #         content=nome_usuario,
        #         actions=[ft.ElevatedButton("Entrar no chat", on_click=entrar_chat)])

        #     def abrir_popup(e):
        #         page.dialog = popup
        #         popup.open = True
        #         page.update()

        #     botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup)

        #     page.add(botao_iniciar)

        # ft.app(target=main, view=ft.WEB_BROWSER, port=8000)

# adicionar outras informações do usuário na mensagem (dicionário)

# se der tempo: adicionar mensagem de "entrou no chat"


import flet as ft

def main(page):
    
    chat = ft.Column()
    def enviar_mensagem_tunel(infos):
        usuario = infos["usuario"]
        if infos["tipo"] == "entrada":
            chat.controls.append(ft.Text(f"{usuario} entrou no chat", size=12, color=ft.colors.AMBER_400, italic=True))
        else:
            mensagem = infos["mensagem"]
            chat.controls.append(ft.Text(f"{usuario}: {mensagem}"))
        page.update()

    page.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(e):
        page.pubsub.send_all({"usuario": nome_usuario.value, "mensagem": campo_mensagem.value, "tipo": "mensagem"})
        campo_mensagem.value = ""
        page.update()

    campo_mensagem = ft.TextField(label="Digite uma mensagem")
    botao_enviarmensagem = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)

    def entrar_chat(e):
        page.add(chat)
        page.add(ft.Row([campo_mensagem, botao_enviarmensagem]))
        popup.open = False
        page.pubsub.send_all({"usuario": nome_usuario.value, "tipo": "entrada"})
        page.remove(botao_iniciar)
        page.update()

    nome_usuario = ft.TextField(label="Escreva seu nome no chat")
    popup = ft.AlertDialog(
        open=False,
        modal=True,
        title=ft.Text("Bem vindo ao Hashzap"),
        content=nome_usuario,
        actions=[ft.ElevatedButton("Entrar no chat", on_click=entrar_chat)])

    def abrir_popup(e):
        page.dialog = popup
        popup.open = True
        page.update()

    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup)

    page.add(botao_iniciar)

ft.app(target=main, view=ft.WEB_BROWSER, port=8000)