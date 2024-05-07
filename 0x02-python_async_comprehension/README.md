# 📚 0x02. Python Async Comprehension 🐍
`Python` `Back-end`

## Resources
Read or watch:
- 📜 [PEP 530 – Asynchronous Comprehensions](https://www.python.org/dev/peps/pep-0530/)
- 🆕 [What’s New in Python: Asynchronous Comprehensions / Generators](https://docs.python.org/3/whatsnew/3.6.html#asynchronous-comprehensions)
- 🔄 [Type-hints for generators](https://docs.python.org/3/library/typing.html#typing.Generator)

<br></br>

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone,
without the help of Google:
- ⚙️ How to write an asynchronous generator
- 🔄 How to use async comprehensions
- 📝 How to type-annotate generators

<br></br>

## 🛠️ Requirements
### ⚙️ General
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on `Ubuntu 18.04 LTS` using
`python3` (version 3.7)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `pycodestyle` style (version 2.5.x)
- The length of your files will be tested using wc
- All your modules should have a documentation
(`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your functions should have a documentation
(`python3 -c 'print(__import__("my_module").my_function.__doc__)'`)
- A documentation is not a simple word, it is a real sentence explaining the
purpose of the module, class or method (the length of it will be verified)
- All your functions and coroutines must be type-annotated.

<br></br>

# Tasks
## ⚡️Task 0. Async Generator
- ⏳ Write a coroutine called `async_generator` that takes no arguments.
- 🔢 The coroutine will loop 10 times, each time asynchronously wait 1
second, then yield a random number between 0 and 10. Use the random module.
<br></br>

## 🛠️ Task 1. Async Comprehensions
- 🔄 Import `async_generator` from the previous task and then write a
coroutine called `async_comprehension` that takes no arguments.
- 📊 The coroutine will collect 10 random numbers using an async
comprehension over `async_generator`, then return the 10 random numbers.
<br></br>

## 📏 Task 2. Run time for four parallel comprehensions
- ⏱️ Import `async_comprehension` from the previous file and write a
`measure_runtime` coroutine that will execute `async_comprehension` four times
in parallel using `asyncio.gather`.
- 🔄 `measure_runtime` should measure the total runtime and return it.


