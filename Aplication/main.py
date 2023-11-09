import flet as ft


def body(page):
    print('start')
    rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=40,
        leading=ft.FloatingActionButton(icon=ft.icons.CREATE, text="Add"),
        group_alignment=-0.9,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.icons.FAVORITE_BORDER, selected_icon=ft.icons.FAVORITE, label="First"
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Icon(ft.icons.BOOKMARK_BORDER),
                selected_icon_content=ft.Icon(ft.icons.BOOKMARK),
                label="Second",
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.SETTINGS_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.SETTINGS),
                label_content=ft.Text("Settings"),
            ),
        ],
        on_change=lambda e: print("Selected destination:", e.control.selected_index),
    )

    return ft.Row(
        [
            rail,
            ft.VerticalDivider(width=1),
            ft.Column([ft.Text("Body!")], alignment=ft.MainAxisAlignment.START, expand=True),
        ],
        width=400,
        height=800
    )


def main(page: ft.Page):
    page.add(
        body(page)
    )


if __name__ == "__main__":
    ft.app(target=main, view=ft.WEB_BROWSER)
