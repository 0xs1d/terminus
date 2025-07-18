import sys
import argparse
from livekit.agents.cli import run_app
from livekit.agents import WorkerOptions
from cli import banner, agent
from tools import lucy


def parse_args():
    parser = argparse.ArgumentParser(
        description="Terminus: A Command Line AI Assistant",
        add_help=False  # We'll add custom -h
    )

    parser.add_argument("-h", "--help", action="store_true",
                        help="Show this help message and exit")
    parser.add_argument("-x", "--action", action="store_true",
                        help="Action mode start")
    return parser.parse_args()


def main():

    args = parse_args()

    if args.help:

        banner.main()

        print("""
            Terminus - Command Line AI Assistant

            Usage:
            python main.py              Start in voice mode     (default)
            python main.py + ctr-b      Switch to chat mode     (text-based)
            python main.py -x           Switch to action mode   (voice-based)
            python main.py -h           Show this help message

            """)

        sys.exit(0)

    if args.action:
        sys.argv = [arg for arg in sys.argv if arg not in ("-x", "--action")]
        sys.argv.insert(1, "console")
        banner.main()
        lucy.main()

        sys.exit(0)

    # 1. Show the animated banner & footer
    banner.main()

    # 2. Inject "console" subcommand into sys.argv so run_app will auto-select it
    # If your entrypoint accepts additional CLI args, include them here.
    sys.argv.insert(1, "console")

    # 3. Start the LiveKit voice agent interactively
    opts = WorkerOptions(entrypoint_fnc=agent.entrypoint)
    run_app(opts)


if __name__ == "__main__":
    main()
