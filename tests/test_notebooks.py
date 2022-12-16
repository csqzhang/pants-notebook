from testbook import testbook
from testbook.client import TestbookNotebookClient
from notebooks import PATH_NOTEBOOKS

## https://testbook.readthedocs.io/en/latest/examples/index.html


@testbook(PATH_NOTEBOOKS / "sample.ipynb", execute=True)
def test_notebook(tb: TestbookNotebookClient):
    assert tb.cell_output_text(1) == 'hello world!'