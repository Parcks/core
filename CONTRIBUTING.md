# Contributing to Parcks
First off, thanks for taking the time to contribute!

The following is a set of guidelines for contributing to Parcks and its repositories, which are hosted in [the Parcks organisation on GitHub](https://github.com/Parcks). Feel free to propose changes to this document in a pull request.

## Style Guide for the core
The conventions are based on [PEP8](https://www.python.org/dev/peps/pep-0008/).
### Naming conventions
|      **What?**     | **Convention**                                                                                                                                      | **Example**    |
|:------------------:|-----------------------------------------------------------------------------------------------------------------------------------------------------|----------------|
| Module name        | Modules should have short, all-lowercase names. Underscores can be used in the module name for improving readability.                               | module_name    |
| Class name         | Class names should normally use the CapWords convention.                                                                                            | NameOfTheClass |
| Exceptions name    | Because exceptions should be classes, the class naming convention applies here. However, you should use the suffix "Error" on your exception names. | ExampleError   |
| Function names     | Function names should be lowercase, with words separated by underscores as necessary to improve readability.                                        | function_name  |
| Instance Variables | Use the function naming rules: lowercase with words separated by underscores as necessary to improve readability.                                   | variable_name  |
| Constants          | Constants are usually defined on a module level and written in all capital letters with underscores separating words.                               | CONSTANT_NAME  |

## The boy scout rule
"Always leave code cleaner than you find it" (see [full explanation](http://programmer.97things.oreilly.com/wiki/index.php/The_Boy_Scout_Rule)). Even if you didn't add new functionality, feel free to reorganise the code so it's cleaner.

## Submitting changes
Please send a Pull Request (PR) with a clear list of what you have done or changed. Always write a clear log message for your commits. An example of a good commit message can be found [here](https://github.com/Parcks/core/commit/6fb529273409edb0aa4194126a37ee89e76ce277).

### What should it look like?
- First line capitalized indicating briefly what you've changed
- A more detailed explanation of your changes
- A list containing all the changed, added, renamed, deleted files

### Response time
You can expect a response from a maintainer within 7 days. If you haven’t heard anything by then, feel free to ping the thread. You can find the name of the maintainer(s) in the [README](https://github.com/Parcks/core/blob/master/README.md) file. 

## Testing
We don't accept failing pull requests. New functionality should be tested if possible. Please keep in mind that testing is done on a **Debian** system.

## Opening issues
Things to keep in mind:
* Ensure the issue was not already reported by searching on GitHub under [Issues](https://github.com/Parcks/core/issues).
* Indicate what kind of issue you are opening: a bug? a feature request (FR)? ...
* Start the name of your issue with: `[<parcks_version> KIND_OF_ISSUE]` for example: `[2.0 BUG]` or `[2.0 FR]`
