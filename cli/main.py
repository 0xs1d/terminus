import sys
import argparse
import banner, agent
from livekit.agents.cli import run_app
from livekit.agents import WorkerOptions


def parse_args():
    parser = argparse.ArgumentParser(
        description="Terminus: A Command Line AI Assistant",
        add_help=False  # We'll add custom -h
    )
    parser.add_argument("-c", "--chat", action="store_true", help="Start in chat mode (text-based)")
    parser.add_argument("-h", "--help", action="store_true", help="Show this help message and exit")
    return parser.parse_args()


def main():

    args = parse_args()

    if args.help:

        banner.main()

        print("""
            Terminus - Command Line AI Assistant

            Usage:
            python main.py              Start in voice mode (default)
            python main.py + ctr-b      Switch to chat mode (text-based)
            python main.py -h           Show this help message

            """)

        sys.exit(0)


    if args.chat:
        sys.argv.insert(1, console)


    #1. Show the animated banner & footer
    banner.main()
    
    # 2. Inject "console" subcommand into sys.argv so run_app will auto-select it
    # If your entrypoint accepts additional CLI args, include them here.
    sys.argv.insert(1, "console")

    # 3. Start the LiveKit voice agent interactively
    opts = WorkerOptions(entrypoint_fnc=agent.entrypoint)
    run_app(opts)


if __name__ == "__main__":
    main()
