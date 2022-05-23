# Silly dbt-duckdb playground

This is a port of Rubén Berenguel's [dbt-sqlite-playground](https://github.com/rberenguel/dbt-sqlite-playground) to DuckDB.


---


## What is available here

All commands are defined in a [taskfile](https://taskfile.dev) to make life easier.

- Technically, a [Poetry](http://python-poetry.org) project, containing helper tools (including `dbt` via `dbt-duckdb`);
- A small (and somewhat dirty) Python script (`populate.py`) to place some not-very-fancy data in a DuckDB file. It will always delete it on load;
- A `dbt` project with sources (based on this pre-populated data) and models. Includes some tests, too.

## Playing with this

Assuming you have `poetry` installed, you should only need to run 
`poetry install --no-root` to install all dependencies. Then, if you want you can also install [taskfile](https://taskfile.dev) to run the commands easily. The Python version is so high because of issues with Python and Mac M1, this one works well with my setup and all libraries I need work well with it.

The two most interesting commands are:
- `task check-total`: this runs the whole pipe of populating the database and getting a single number out of the final model. They should be the same (total amount of money in paid invoices);
- `task dbt-docs`: this runs the whole pipe as well, but ends up opening the docs (with lineage) for the models. It's neat to see;
- `task dbt-test`: you should only run this after having run `task dbt-run`, particularly if you are tweaking the models.
