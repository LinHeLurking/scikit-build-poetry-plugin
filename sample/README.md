# Python Template Project

Add these lines into `build.py`.

```python
import subprocess
import sys


def main():
    proc = subprocess.Popen(["poetry", "build-ext"])
    code = proc.wait()
    sys.exit(code)

if __name__ == '__main__':
    main()
```

Add these lines into your `pyproject.toml`.

```toml
[tool.poetry.build]
script = "build.py"
generate-setup-file = false
```

You can add more scikit-build-core related configs in `tool.scikit-build` section in `pyproject.toml`.
After all configs are done, you can build your wheel with CMake:

1. Install `scikit_build_plugin`.
2. Specify install rules in `CMakeLists.txt`.
3. Run `poetry build -f wheel` to build a wheel with C extension.

Then you can use it:

```
Python 3.10.14 (main, Mar 19 2024, 21:46:16) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from python_template.hello_world.greeter import ExtGreeter
>>> greeter = ExtGreeter()
>>> greeter.simple_greet()
'Hello world!'
>>> greeter.complex_greet(["Cloud", "Aerith"], "Have a nice day!")
{'Aerith': 'Hello, Aerith! Have a nice day!', 'Cloud': 'Hello, Cloud! Have a nice day!'}
>>>
```