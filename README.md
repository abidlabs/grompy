<p align="center">
    <a href="https://github.com/abidlabs/grompy/blob/main/LICENSE"><img alt="License" src="https://img.shields.io/github/license/abidlabs/grompy.svg?color=blue"></a>
    <a href="https://pypi.org/project/grompy/"><img alt="PyPI" src="https://img.shields.io/pypi/v/grompy"></a>
    <img alt="Python version" src="https://img.shields.io/badge/python-3.10+-important">
    <a href="https://github.com/abidlabs/grompy/actions/workflows/format.yml"><img alt="Format" src="https://github.com/abidlabs/grompy/actions/workflows/format.yml/badge.svg"></a>
    <a href="https://github.com/abidlabs/grompy/actions/workflows/test.yml"><img alt="Test" src="https://github.com/abidlabs/grompy/actions/workflows/test.yml/badge.svg"></a>
</p>


<h1 align="center"> 🐻 Grompy</h1>


## 🐻 Grompy

Grompy is a Python-to-JavaScript transpiler designed specifically for use in the [Gradio](https://gradio.app) library. Instead of aiming for full coverage of Python features, Grompy prioritizes **clear error reporting** for unsupported code, making it easier for developers to modify their functions accordingly.

### 🚀 Features
- Converts simple Python functions into JavaScript equivalents.
- Provides **detailed warnings** when something can't be transpiled.
- Designed to integrate seamlessly with Gradio.

### 📦 Installation
Install Grompy via pip:
```bash
pip install grompy
```

### 🔧 Usage
```python
from grompy import transpile

def my_function(x):
    return x + 1

js_code = transpile(my_function)
print(js_code)  # Outputs equivalent JavaScript code
```
If Grompy encounters unsupported syntax, it will **complain loudly** so you know what to fix.

### ❗ Why "Grompy"?
Like a grumpy bear 🐻, Grompy isn’t here to cover everything—just to **clearly tell you what’s wrong** when something can't be transpiled.

### 📜 License
Grompy is open-source under the [MIT License](https://github.com/abidlabs/grompy/blob/main/LICENSE).

---
Contributions are welcome! Feel free to open an issue or PR if you have suggestions.