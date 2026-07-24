import csv
from pathlib import Path

import nbformat
from nbclient import NotebookClient


NOTEBOOK_PATH = (
    Path(__file__).parents[1]
    / "notebooks"
    / "pluralize_a_list_of_dutch_words.ipynb"
)


def test_pluralization_notebook_runs(tmp_path):
    notebook = nbformat.read(NOTEBOOK_PATH, as_version=4)
    output_path = tmp_path / "test_output.csv"

    for cell in notebook.cells:
        if cell.get("id") == "output-settings":
            cell["source"] = f"output_csv_file_name = {str(output_path)!r}"
            break
    else:
        raise AssertionError("The notebook has no output-settings cell")

    executed_notebook = NotebookClient(
        notebook,
        timeout=600,
        kernel_name="python3",
        resources={"metadata": {"path": str(NOTEBOOK_PATH.parent)}},
    ).execute()

    cells_by_id = {
        cell.get("id"): cell
        for cell in executed_notebook.cells
        if cell.get("cell_type") == "code"
    }

    for cell_id in ("pluralize-results", "singularize-results", "combine-results"):
        assert any(
            output.get("output_type") == "display_data"
            for output in cells_by_id[cell_id].get("outputs", [])
        ), f"{cell_id} did not display a result"

    assert output_path.is_file()

    with output_path.open(newline="", encoding="utf-8") as output_file:
        rows = list(csv.DictReader(output_file))

    assert len(rows) == 21
    assert {"plural", "plural_source", "singular", "singular_source"} <= rows[0].keys()

    huizen = next(row for row in rows if row["word"] == "huizen")
    assert huizen["plural"] == "huizen"
    assert huizen["singular"] == "huis"
