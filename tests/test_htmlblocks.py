from curses.ascii import HT
import pytest

from nbdocutils import htmlblocks

def test_bluealertblock():
    from IPython.display import HTML
    expected = """
        <div class="alert alert-block alert-info">
            <b>Testing:</b> To do well, use test-driven development.
        </div>
        """.strip()
    obj = htmlblocks.BlueAlertBlock(
        lead_in="Testing", 
        text="To do well, use test-driven development."
        )
    assert str(obj).strip() == expected
    assert isinstance(obj.html, HTML)