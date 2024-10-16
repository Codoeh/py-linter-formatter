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
        [{format_linter_error(error)} for error in errors],
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
                    {format_single_linter_file(linter_report["errors"])}
                    for errors in linter_report],
                "path": list(linter_report)[1],
                "status": "passed"
                if "errors" == []
                else "failed"},
        ]
    pass
