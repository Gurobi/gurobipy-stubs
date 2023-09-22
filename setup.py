import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gurobipy-stubs",
    url="https://www.gurobi.com",
    description="Type stubs for gurobipy",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="Gurobi Optimization, LLC",
    license="MIT",
    install_requires = [
        'gurobipy==9.5.*',
        ],
    version="1.0.1.post0",
    package_data={"gurobipy-stubs": [
        'gurobipy.pyi',
        '__init__.pyi']},
    packages=["gurobipy-stubs"]
)
