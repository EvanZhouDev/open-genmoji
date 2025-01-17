import json
from huggingface_hub import hf_hub_download
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt, IntPrompt

console = Console()

with open("./lora/info.json", "r") as f:
    models = json.load(f)

table = Table(title="Available Models", show_header=True, header_style="bold magenta")
table.add_column("Index", style="dim", width=6)
table.add_column("Name", style="bold cyan")
table.add_column("Model", style="green")
table.add_column("Description", style="yellow")

for i, model in enumerate(models):
    table.add_row(
        str(i),
        model['name'],
        model['model'].split('/')[1],
        model['description']
    )

console.print(table)

choice = IntPrompt.ask("\nSelect a model (enter number)", choices=[str(i) for i in range(len(models))])

if 0 <= choice < len(models):
    selected = models[choice]
    filename = f"{selected['name']}.safetensors"

    console.print(f"\n[bold green]Downloading {selected['name']}...[/bold green]")
    downloaded_path = hf_hub_download(
        repo_id=selected["huggingface"], filename=filename, local_dir="./lora"
    )
    console.print(f"[bold blue]Downloaded weights to: {downloaded_path}[/bold blue]")
else:
    console.print("[bold red]Invalid selection[/bold red]")