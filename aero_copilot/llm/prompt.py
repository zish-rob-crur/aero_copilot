from pathlib import Path

import jinja2

jinja2_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(Path(__file__).parent.parent / "data" / "prompts")
)


def get_prompt(
    name: str,
    variables: dict = None,
):
    if variables is None:
        variables = {}
    template = jinja2_env.get_template("{}.md".format(name))

    return template.render(**variables)

