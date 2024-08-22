import flet as ft
from click import style

btns = [
    {'letter': 'k', 'filling': "#089db2", "width":45},
    {'letter': 'w', 'filling': "#089db2", "width":45},
    {'letter': 'e', 'filling': "#089db2", "width":45},
    {'letter': 'ɛ', 'filling': "#089db2", "width":45},
    {'letter': 'ẽ', 'filling': "#089db2", "width":45},
    {'letter': 'ɾ', 'filling': "#089db2", "width":45},
    {'letter': 'r', 'filling': "#089db2", "width":45},
    {'letter': 't', 'filling': "#089db2", "width":45},
    {'letter': 'I', 'filling': "#089db2", "width":45},
    {'letter': 'i', 'filling': "#089db2", "width":45},
    {'letter': 'ĩ', 'filling': "#089db2", "width":45},
    {'letter': 'j', 'filling': "#089db2", "width":45},
    {'letter': 'u', 'filling': "#089db2", "width":45},
    {'letter': 'ũ', 'filling': "#089db2", "width":45},
    {'letter': 'ʊ', 'filling': "#089db2", "width":45},
    {'letter': 'w', 'filling': "#089db2", "width":45},
    {'letter': 'ɔ', 'filling': "#089db2", "width":45},
    {'letter': 'o', 'filling': "#089db2", "width":45},
    {'letter': 'õ', 'filling': "#089db2", "width":45},
    {'letter': 'p', 'filling': "#089db2", "width":45},
    {'letter': 'a', 'filling': "#089db2", "width":45},
    {'letter': 'ã', 'filling': "#089db2", "width":45},
    {'letter': 'ɘ', 'filling': "#089db2", "width":45},
    {'letter': 'ɘ', 'filling': "#089db2", "width":45},
    {'letter': 's', 'filling': "#089db2", "width":45},
    {'letter': 'd', 'filling': "#089db2", "width":45},
    {'letter': 'f', 'filling': "#089db2", "width":45},
    {'letter': 'g', 'filling': "#089db2", "width":45},
    {'letter': 'h', 'filling': "#089db2", "width":45},
    {'letter': 'ɦ', 'filling': "#089db2", "width":45},
    {'letter': 'x', 'filling': "#089db2", "width":45},
    {'letter': 'ɣ', 'filling': "#089db2", "width":45},
    {'letter': 'ʒ', 'filling': "#089db2", "width":45},
    {'letter': 'l', 'filling': "#089db2", "width":45},
    {'letter': 'ʎ', 'filling': "#089db2", "width":45},
    {'letter': 'z', 'filling': "#089db2", "width":45},
    {'letter': 'ʃ', 'filling': "#089db2", "width":45},
    {'letter': 'v', 'filling': "#089db2", "width":45},
    {'letter': 'b', 'filling': "#089db2", "width":45},
    {'letter': '[', 'filling': "#089db1", "width":60},
    {'letter': 'n', 'filling': "#089db2", "width":45},
    {'letter': 'ɲ', 'filling': "#089db2", "width":45},
    {'letter': 'ʧ', 'filling': "#089db2", "width":45},
    {'letter': 'ʤ', 'filling': "#089db2", "width":45},
    {'letter': ']', 'filling': "#089db0", "width":60},
]
# output do sistema
transcript = []
def main(page: ft.Page):
    page.window_title_bar_hidden=True
    page.alignment = ft.MainAxisAlignment.CENTER
    page.spacing=0
    page.padding=20
    page.window_height=650
    page.window_max_height=650
    page.window_min_height = 650
    page.window_width = 430
    page.window_min_width=450
    page.window_max_width = 450
    #page.window_resizable=False
    page.fonts = {"ipa": "assets/fonts/DoulosSIL-Regular.ttf"}

    # =========================== Funções =================================#

    def add_output(e):
        transcript.append({'entrada': input.value})
        output_column.controls = [
            ft.ListTile(
                title=ft.Text(value=item['entrada'],
                              bgcolor="#089db2",
                              color="#ffffff",
                              size=20),
                trailing=ft.IconButton(
                    icon=ft.icons.DELETE_FOREVER_ROUNDED,
                    icon_color="#089db2",
                    icon_size=30,
                    tooltip="excluir",
                    on_click=lambda e: page.remove(output_column.controls)
                )) for item in transcript]
        page.update()
        input.value = ''
        input.update()

    def letter_key(e):
        value_atual = input.value if input.value != '' else ''
        value = e.control.content.value
        input.value = value_atual+ value
        input.update()
# =========================== AppBar =================================#
    page.appbar = ft.AppBar(
        leading=ft.IconButton(ft.icons.KEYBOARD),
        leading_width=40,
        title=ft.Text(value="Keyboard IPA", tooltip="Home"),
        center_title=False,
        bgcolor="#089db2",
        color=ft.colors.WHITE,
        actions=[
            ft.IconButton(ft.icons.EXIT_TO_APP, tooltip="Sair", on_click=lambda _: page.window_close()),
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="Documentation", icon=ft.icons.DOCUMENT_SCANNER),
                    ft.PopupMenuItem(text="Version", icon=ft.icons.EDIT_DOCUMENT,),
                ]
            ),
        ],
    )
# =========================== Input do usuário ================================= #
    input = ft.TextField(value='', 
                         label="Input", 
                         expand=True, 
                         keyboard_type="ipa",
                         border_color="#089db2",
                         border_width = 2,
                         border_radius= ft.border_radius.all(20),
                         suffix_icon= ft.IconButton(ft.icons.SEND, tooltip="Enviar"),
                         )

# =========================== Output para o usuário ================================= #
    output_column = ft.Column(
        expand=True,
        scroll=True
    )
    # =========================== Teclado virtual ================================= #
    keyboard = ft.Row(
                wrap = True,
                spacing=3,
                alignment = ft.MainAxisAlignment.CENTER,
                #molde dos botões
                controls =[
                    ft.Container(
                        content=ft.Text(
                            value=btn['letter'],
                            color= ft.colors.BLUE_100,
                            size=25,
                            font_family="ipa"),
                        alignment = ft.alignment.center,
                        height=40,
                        width = btn['width'],
                        bgcolor = btn['filling'],
                        border_radius = ft.border_radius.all(10),
                        tooltip= f"botão {btn['letter']}",
                        on_click=letter_key) for btn in btns]
                    )
# =========================== Layout do programa =================================#
    layout = ft.Column(
        expand = True,
        spacing = 20,
        controls = [
            output_column,
            # input do usuário
            ft.Row(controls = [input, ft.IconButton(
                ft.icons.SEND, tooltip="Enviar",
                icon_color="white",
                bgcolor="#089db2",
                on_click= add_output)]),
            keyboard,
            ]
        )
    page.add(layout)

if __name__=="__main__":
    ft.app(target=main, assets_dir="assets")