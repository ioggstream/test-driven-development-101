#!/usr/bin/env python
"""
This file provides:

- a script to replace mermaidjs blocks to rendered svg urls (NB relies on a mermaid server);
- a cell_magic that can be loaded into jupyter to render interactively a mermaidjs block.


Examples:

1- running ./mermaid_magic.py on a file, replaces the code below

```mermaid

graph LR
    build --> test --> update --> distribute

```

  with

"![](https://mermaid.ink/svg/eyJjb2RlIjogImdyYXBoIExSXG4gIGJ1aWxkIC0tPiB0ZXN0IC0tPiB1cGRhdGUgLS0-IGRpc3RyaWJ1dGVcblxuIn0=)"


2- importing mermaid magic in jupyter


TBD

"""
from IPython import get_ipython
from IPython.core.magic import register_cell_magic

from base64 import urlsafe_b64encode
import json
import re


def encode_json(_dict):
    return urlsafe_b64encode(json.dumps(_dict).encode()).decode()


def mermaidize(s):
    mermaid_url = "https://mermaid.ink/svg"

    strip_header = re.sub("^```mermaid", "", s.strip()).strip().strip("`")
    mermaid = encode_json({"code": strip_header})
    return f"""![]({mermaid_url}/{mermaid})"""


if get_ipython():

    @register_cell_magic
    def mermaid(line, cell):
        "my cell magic"
        return mermaidize(cell)

    # In an interactive session, we need to delete these to avoid
    # name conflicts for automagic to work on line magics.
    del mermaid


def test_mermaidize():
    s = "```mermaid\n\ngraph LR\n  build --> test --> update --> distribute\n\n```"
    assert (
        mermaidize(s)
        == "![](https://mermaid.ink/svg/eyJjb2RlIjogImdyYXBoIExSXG4gIGJ1aWxkIC0tPiB0ZXN0IC0tPiB1cGRhdGUgLS0-IGRpc3RyaWJ1dGVcblxuIn0=)"
    )


def test_replacize():
    txt = """
    ---
    # This is a slide
    
    ----
    ## This is another one
    
    ```mermaid
    
    graph LR
      build --> test --> update --> distribute

    ```
    
    ----
    ## This is another one
    
    ```mermaid
    
    graph LR
      build --> test --> update --> distribute

    ```
    
    """

    ret = re.sub(
        "```mermaid(\n|[^`].)*?```", lambda m: mermaidize(m.group(0)), txt, re.MULTILINE
    )
    print(ret)
    assert (
        "## This is another one\n    \n    ![](https://mermaid.ink/svg/eyJjb2RlIjogImdyYXBoIExSXG4gICAgICBidWlsZCAtLT4gdGVzdCAtLT4gdXBkYXRlIC0tPiBkaXN0cmlidXRlXG5cbiAgICAifQ==)"
        in ret
    )


if __name__ == "__main__":
    import click

    @click.command()
    @click.argument("fpath", type=click.File("r"))
    def main(fpath):
        body = fpath.read()
        ret = re.sub(
            "```mermaid(\n|[^`].)*?```",
            lambda m: mermaidize(m.group(0)),
            body,
            re.MULTILINE,
        )
        print(ret)

    main()
