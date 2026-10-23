from jinja2.sandbox import SandboxedEnvironment


def add_one(number):
    return number + 1


def render_template(
    template: str,
    **context,
) -> str:
    environment = SandboxedEnvironment()

    return (
        environment
        .from_string(template)
        .render(**context)
    )
