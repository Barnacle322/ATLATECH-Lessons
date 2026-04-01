from rich import print
from rich.table import Table

table = Table(title="Students")
table.add_column("Name")
table.add_column("Grade")

table.add_row("Arstan", "0")
table.add_row("Zhantai", "100")
table.add_row("Aliya", "100")

print(table)
