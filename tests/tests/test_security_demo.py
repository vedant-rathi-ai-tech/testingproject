from sample.simple import (
    render_template,
)


def test_render_template():
    result = render_template(
        "Hello {{ name }}",
        name="RepoGuard",
    )

    assert result == "Hello RepoGuard"
