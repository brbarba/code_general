from rich import print

print("Hello, [bold blue]Towards Data Science[/bold blue]!", ":thumbs_up:", "[u]By[/u]", "[i]Christopher Tao[/i]")


from simple_colors import *
print('Normal:', blue('Welcome Finxter!'))
print('BOLD: ', green('Welcome Finxter!', 'bold'))
print('BOLD and Underlined: ', red('Welcome Finxter!', ['bold', 'underlined']))
print(green('Activo', 'bold'))
