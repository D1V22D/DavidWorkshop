import flet as ft 
import time
def main (page:ft.Page):
    page.add(
    ft.Row(controls=[
        ft.Text("A"),
        ft.Text("B"),
        ft.Text("C")
    ])
)
def sur(pg:ft.pg):
    pg.add
    t = ft.Text()
    pg.add(t) # it's a shortcut for pg.controls.append(t) and then pg.update()

    for i in range(10):
        t.value = f"Step {i}"
        pg.update()
        time.sleep(1)
    
ft.app(target=main)
ft.app(target=sur)