# gurobipy-stubs

**This package is no longer maintained. gurobipy versions 11.0 and later
will include type hints as part of the installation, so the stubs are no
longer needed.**

This package provides type hints for
[gurobipy](https://pypi.org/project/gurobipy/), the [Python API for
Gurobi](https://www.gurobi.com/documentation/10.0/refman/py_python_api_overview.html).
These stubs help you to write typed Python code, and enhance many IDE's
built-in auto completion features.

### Version Compatibility

- Version `1.0` of this package provides type hints for gurobipy `9.x`.
- Version `2.0` of this package provides type hints for gurobipy `10.x`.
- For later versions of gurobipy, you should not install this package.

### Example

With this type stubs package installed, static type checkers such as
[mypy](https://mypy.readthedocs.io/en/stable/index.html) will be able to
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
