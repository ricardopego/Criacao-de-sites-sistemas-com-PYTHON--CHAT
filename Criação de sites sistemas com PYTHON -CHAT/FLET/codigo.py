# CHAT DO RICARDÃO 

# Botão iniciar 

# Popup para entrar no chat (CAIXA PARA ESCREVER O MEU NOME )

# Quando entrar no chat: (APARECE PARA TODOS)
    # Mensagem que eu entrei no chat
    # Campo de escrita e botão enviar

# A cada mensagem enviada: (APARECE PARA TODOS)
    # Nome: Texto da mensagem

import flet as ft 


def main(pagina):
    texto = ft.Text('CHAT DO RICARDÃO ')
    chat = ft.Column()
    nome_usuario = ft.TextField(label='Escreva seu nome aqui...')


    def enviar_mensagem_tunel(mensagem):
        # Adicionar a msg no chat
        chat.controls.append(ft.Text(mensagem))
        pagina.update()


    pagina.pubsub.subscribe(enviar_mensagem_tunel)


    def enviar_mensagem(evento):
        pagina.pubsub.send_all(campo_mensagem.value)
        # Limapar campo de msg
        campo_mensagem.value = ''
        pagina.update()


    campo_mensagem = ft.TextField(label='Digite uma mensagem...')
    botao_eviar_mensagem = ft.ElevatedButton('Enviar',on_click=enviar_mensagem)

    def entrar_popup(evento):
        # Adicionar chat
        pagina.add(chat)

        # Fechar popup 
        popup.open=False

        # Remover o botão iniciar chat
        pagina.remove(botao_iniciar)
        pagina.remove(texto)

        # Criar campo de msg do usuário e Criar botão de enviar msg do usuário
        pagina.add(ft.Row(
            [campo_mensagem,botao_eviar_mensagem]
        ))

        # Atualizar página
        pagina.update()


    popup = ft.AlertDialog(
        open=False,
        modal=True,
        title=ft.Text('Bem vindo ao CHAT DO RICARDÃO'),
        content=nome_usuario,
        actions=[ft.ElevatedButton('Entrar',on_click=entrar_popup)])


    def entrar_chat(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()        


    botao_iniciar = ft.ElevatedButton('Iniciar chat',on_click=entrar_chat)

    pagina.add(texto)
    pagina.add(botao_iniciar)


ft.app(target=main, view=ft.WEB_BROWSER) # Para abrir no chorme -> view=ft.WEB_BROWSER
