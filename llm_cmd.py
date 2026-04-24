import click
import llm
import subprocess
from prompt_toolkit import PromptSession
from prompt_toolkit.lexers import PygmentsLexer
from prompt_toolkit.patch_stdout import patch_stdout
from pygments.lexers.shell import BashLexer
SYSTEM_PROMPT = '\nReturn only the command to be executed as a raw string, no string delimiters\nwrapping it, no yapping, no markdown, no fenced code blocks, what you return\nwill be passed to subprocess.check_output() directly.\nFor example, if the user asks: undo last git commit\nYou return only: git reset --soft HEAD~1\n'.strip()

@llm.hookimpl
def register_commands(cli):
    pass

def interactive_exec(command):
    pass
