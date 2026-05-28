import textwrap

from ssort import ssort


def _clean(text):
    return textwrap.dedent(text).strip() + "\n"


def test_basic():
    original = _clean(
        """
        class Foo:
            bar: int
            \"""A bar.\"""
            baz: int
            \"""A baz.\"""
        """
    )
    expected = _clean(
        """
        class Foo:
            bar: int
            \"""A bar.\"""
            baz: int
            \"""A baz.\"""
        """
    )
    actual = ssort(original)
    assert actual == expected
