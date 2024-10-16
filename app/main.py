def format_linter_error(error: dict) -> dict:
    return {
        "line": error.get("line_number"),
        "column": error.get("column_number"),
        "message": error.get("text"),
        "name": error.get("code"),
        "source": "flake8"
    }
    pass

def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {"errors":
        [{
        "line": error.get("line_number"),
        "column": error.get("column_number"),
        "message": error.get("text"),
        "name": error.get("code"),
        "source": "flake8"} for error in errors],
    "path": file_path,
    "status": "passed"
    if errors == []
    else "failed"
    }
    pass


def format_linter_report(linter_report: dict) -> list:
    return [
        {"errors": [], "path": list(linter_report)[0], "status": "passed"},
        {
            "errors": [
                {
                    "line": linter_report.get("line_number"),
                    "column": linter_report.get("column_number"),
                    "message": linter_report.get("text"),
                    "name": linter_report.get("code"),
                    "source": "flake8"}
                    for errors in linter_report],
            "path": list(linter_report)[1],
            "status": "passed"
            if "errors" == []
            else "failed"},
    ]
    pass
