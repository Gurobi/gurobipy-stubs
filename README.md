# gurobipy-stubs

This package provides type hints for
[gurobipy](https://pypi.org/project/gurobipy/), the [Python API for
Gurobi](https://www.gurobi.com/documentation/9.1/refman/py_python_api_overview.html).
These stubs help you to write typed Python code, and enhance many IDE's
built-in auto completion features.

### Example

With this type stubs package installed, static type checkers such as
[mypy](https://mypy.readthedocs.io/en/stable/index.html) willl be able to
verify the types given in source code annotations like in this example:

```
import gurobipy as gp

m: gp.Model = gp.Model()
v: gp.Var = m.addVar()
m.optimize()
vval: float = v.X
```

```
% mypy example.py 
Success: no issues found in 1 source file
```
