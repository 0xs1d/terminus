import os
import sys
import time
from pyfiglet import Figlet
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

def animate_once(text: str, delay: float = 0.01, color: str = "magenta"):
    fig = Figlet(font="slant")
    art = fig.renderText(text).splitlines()
    if os.name == 'nt':
        os.system('')  # Enable ANSI

    console = Console()
    width = max(len(line) for line in art)

    for step in range(width + 1):
        # Clear screen
        sys.stdout.write("\x1b[2J\x1b[H")
        for line in art:
            console.print(line[:step], style=f"bold {color}")
        time.sleep(delay)

def show_footer():
    console = Console()
    footer = Text()
    footer.append("\n✨ Welcome to Terminus CLI! ✨\n\n", style="bold green")
    footer.append("Tips for getting started:\n", style="dim")
    footer.append("• Ask questions, edit files, or run commands.\n")
    footer.append("• Be specific for the best results.\n")
    footer.append("• Use '--help' to explore options.\n")
    panel = Panel(footer, border_style="purple", padding=(1, 2))
    console.print(panel)

def main():
    animate_once("Terminus", delay=0.009, color="magenta")
    show_footer()

if __name__ == "__main__":
    main()
