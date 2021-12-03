import os
import rich
from rich.console import Console
from rich import print

console=Console()

def header():
    console.print("[bold blue]=============================================================")
    console.print("[bold blue]=                         [bold yellow]TASK LIST                         [bold blue]=")
    console.print("[bold blue]=============================================================")

def cls():
    os.system("cls")

def garis():
     console.print("[bold blue]=============================================================")