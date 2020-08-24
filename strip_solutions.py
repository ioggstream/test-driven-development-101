import click
import ast
import astor
from pathlib import Path
import logging

log = logging.getLogger()
logging.basicConfig(level=logging.INFO)


def ignore1():
    """@ignore"""
    pass


def ignore2():
    """@ignore"""
    pass


def mock():
    """This is the mock function.
        and you have to implement it.
    @solution"""
    return True


def test_mock():
    assert mock()


def test_process_function():
    code = ast.parse(Path("strip_solutions.py").read_text())
    code = process_ast(code)
    # The mock function has a comment
    f = [f for f in code.body if getattr(f, "name", None) == "mock"]
    f = f[0]
    assert len(f.body) == 2
    assert astor.to_source(f.body[0]).startswith('"""This is the mock function.')


def _eligible(code, pattern):
    source = astor.to_source(code)
    return source.startswith('"""') and pattern in source


def process_ast(code, skip_pattern=None):
    rs = ast.parse("raise NotImplementedError")
    ignored = [
        f for f in code.body if hasattr(f, "body") and _eligible(f.body[0], "@ignore")
    ]
    code.body = [x for x in code.body if x not in ignored]
    for f in code.body:
        if f.__class__ != ast.FunctionDef:
            continue

        if skip_pattern and f.name.startswith(skip_pattern):
            continue

        if not _eligible(f.body[0], "@solution"):
            continue

        # This is a solution: I preserve the docstring and
        # replace the body.
        log.info(astor.to_source(f))
        f.body = [f.body[0], rs]
        log.info(astor.to_source(f))
    return code


def process_file(fpath, skip_pattern=None, destdir=None, replace=False):
    log.info("Process %r %r", fpath, skip_pattern)
    code = ast.parse(Path(fpath).read_text())

    new_code = process_ast(code, skip_pattern)
    if destdir:
        dpath = Path(destdir) / Path(fpath).name
    elif replace:
        dpath = Path(fpath)
    else:
        dpath = Path(fpath + "ex.py")

    if dpath.exists() and not replace:
        raise SystemError("File already exists: ", dpath)
    dpath.write_text(astor.to_source(new_code))


@click.command()
@click.argument("files", nargs=-1)
@click.option("--skip-pattern", default="", help="Skip functions starting with")
@click.option("--destdir", default=False, help="destination directory")
@click.option("--replace", default=False, help="replace the current file")
def main(files, skip_pattern="", destdir=None, replace=False):
    """Replace function code with 
       raise NotImplementedError("Write me")
       for python exercises.
    """
    if destdir:
        Path(destdir).mkdir(exist_ok=True, parents=True)
    for fpath in files:
        process_file(fpath, skip_pattern, destdir, replace)


if __name__ == "__main__":
    main()
