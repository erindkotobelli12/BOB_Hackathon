# 📚 Documentation Report: click

**Generated:** 2026-05-01 17:22:43 UTC
**Root Directory:** `C:\Users\I.C.T\OneDrive\Documents\git\click`

## 📊 Coverage Summary

| Language | Files | Functions | Coverage % |
|----------|-------|-----------|------------|
| python | 63 | 1087 | 33.4% |
| **Total** | **63** | **1087** | **33.4%** |

## ⚠️ Undocumented Items

Found **100** undocumented functions/methods:

### `C:\Users\I.C.T\OneDrive\Documents\git\click\examples\aliases\aliases.py`

- **Config.__init__** (method) - Line 10
- **Config.add_alias** (method) - Line 14
- **Config.read_config** (method) - Line 17
- **Config.write_config** (method) - Line 25
- **AliasedGroup.get_command** (method) - Line 42
- **AliasedGroup.resolve_command** (method) - Line 70

### `C:\Users\I.C.T\OneDrive\Documents\git\click\examples\completion\completion.py`

- **cli** (function) - Line 8
- **ls** (function) - Line 14
- **get_env_vars** (function) - Line 18
- **show_env** (function) - Line 26
- **group** (function) - Line 32
- **list_users** (function) - Line 36
- **select_user** (function) - Line 52

### `C:\Users\I.C.T\OneDrive\Documents\git\click\examples\complex\complex\cli.py`

- **Environment.__init__** (method) - Line 11
- **ComplexCLI.list_commands** (method) - Line 32
- **ComplexCLI.get_command** (method) - Line 40

### `C:\Users\I.C.T\OneDrive\Documents\git\click\examples\imagepipe\imagepipe.py`

- **copy_filename** (function) - Line 69
- **convert_rotation** (function) - Line 165
- **convert_flip** (function) - Line 178

### `C:\Users\I.C.T\OneDrive\Documents\git\click\examples\repo\repo.py`

- **Repo.__init__** (method) - Line 9
- **Repo.set_config** (method) - Line 14
- **Repo.__repr__** (method) - Line 19

### `C:\Users\I.C.T\OneDrive\Documents\git\click\examples\validation\validation.py`

- **validate_count** (function) - Line 6
- **URL.convert** (method) - Line 15

### `C:\Users\I.C.T\OneDrive\Documents\git\click\src\click\__init__.py`

- **__getattr__** (function) - Line 77

### `C:\Users\I.C.T\OneDrive\Documents\git\click\src\click\_compat.py`

- **_make_text_stream** (function) - Line 19
- **_NonClosingTextIOWrapper.__init__** (method) - Line 57
- **_NonClosingTextIOWrapper.__del__** (method) - Line 71
- **_NonClosingTextIOWrapper.isatty** (method) - Line 77
- **_FixupStream.__init__** (method) - Line 92
- **_FixupStream.__getattr__** (method) - Line 102
- **_FixupStream.read1** (method) - Line 105
- **_FixupStream.readable** (method) - Line 113
- **_FixupStream.writable** (method) - Line 125
- **_FixupStream.seekable** (method) - Line 140
- **_is_binary_reader** (function) - Line 151
- **_is_binary_writer** (function) - Line 160
- **_find_binary_reader** (function) - Line 173
- **_find_binary_writer** (function) - Line 191
- **_force_correct_text_stream** (function) - Line 238
- **_force_correct_text_reader** (function) - Line 284
- **_force_correct_text_writer** (function) - Line 300
- **get_binary_stdin** (function) - Line 316
- **get_binary_stdout** (function) - Line 323
- **get_binary_stderr** (function) - Line 330
- **get_text_stdin** (function) - Line 337
- **get_text_stdout** (function) - Line 344
- **get_text_stderr** (function) - Line 351
- **open_stream** (function) - Line 371
- **_AtomicFile.__init__** (method) - Line 453
- **_AtomicFile.name** (method) - Line 460
- **_AtomicFile.close** (method) - Line 463
- **_AtomicFile.__getattr__** (method) - Line 470
- **_AtomicFile.__enter__** (method) - Line 473
- **_AtomicFile.__exit__** (method) - Line 476
- **_AtomicFile.__repr__** (method) - Line 484
- **strip_ansi** (function) - Line 488
- **_is_jupyter_kernel_output** (function) - Line 492
- **should_strip_ansi** (function) - Line 499
- **term_len** (function) - Line 572
- **isatty** (function) - Line 576
- **_make_cached_stream_func** (function) - Line 583

### `C:\Users\I.C.T\OneDrive\Documents\git\click\src\click\_termui_impl.py`

- **ProgressBar.__init__** (method) - Line 44
- **ProgressBar.__enter__** (method) - Line 115
- **ProgressBar.__exit__** (method) - Line 120
- **ProgressBar.__iter__** (method) - Line 128
- **ProgressBar.__next__** (method) - Line 134
- **ProgressBar.render_finish** (method) - Line 142
- **ProgressBar.pct** (method) - Line 149
- **ProgressBar.time_per_iteration** (method) - Line 155
- **ProgressBar.eta** (method) - Line 161
- **ProgressBar.format_eta** (method) - Line 166
- **ProgressBar.format_pos** (method) - Line 181
- **ProgressBar.format_pct** (method) - Line 187
- **ProgressBar.format_bar** (method) - Line 190
- **ProgressBar.format_progress_line** (method) - Line 209
- **ProgressBar.render_progress** (method) - Line 236
- **ProgressBar.make_step** (method) - Line 282
- **ProgressBar.finish** (method) - Line 330
- **MaybeStripAnsi.__init__** (method) - Line 370
- **MaybeStripAnsi.write** (method) - Line 374
- **Editor.__init__** (method) - Line 603
- **Editor.get_editor** (method) - Line 615
- **Editor.edit** (method) - Line 663
- **Editor.edit** (method) - Line 668
- **Editor.edit** (method) - Line 670
- **open_url** (function) - Line 718
- **_translate_ch_to_exc** (function) - Line 788

### `C:\Users\I.C.T\OneDrive\Documents\git\click\src\click\_textwrap.py`

- **TextWrapper._handle_long_word** (method) - Line 9
- **TextWrapper.extra_indent** (method) - Line 28
- **TextWrapper.indent_only** (method) - Line 40

### `C:\Users\I.C.T\OneDrive\Documents\git\click\src\click\_utils.py`

- **Sentinel.__repr__** (method) - Line 18

### `C:\Users\I.C.T\OneDrive\Documents\git\click\src\click\_winconsole.py`

- **_WindowsConsoleRawIOBase.__init__** (method) - Line 119
- **_WindowsConsoleRawIOBase.isatty** (method) - Line 122
- **_WindowsConsoleReader.readable** (method) - Line 128
- **_get_text_stdin** (function) - Line 226
- **_get_text_stdout** (function) - Line 236
- **_get_text_stderr** (function) - Line 246
- **_is_console** (function) - Line 263
- **_get_windows_console_stream** (function) - Line 276

## 📄 File Documentation

### `C:\Users\I.C.T\OneDrive\Documents\git\click\docs\conf.py`

**Language:** python

_No functions or classes found._

---

### `C:\Users\I.C.T\OneDrive\Documents\git\click\examples\aliases\aliases.py`

**Language:** python

#### Functions

##### `read_config(ctx, param, value)`

**Line:** 76 | **Returns:** `None`

**Parameters:**
- `ctx`
- `param`
- `value`

**Documentation:**

> Callback that is used whenever --config is passed.  We use this to
> always load the correct config.  This means that the config is loaded
> even if the group itself never executes so our aliases stay always
> available.

##### `cli()`

**Line:** 97 | **Returns:** `None`

**Documentation:**

> An example application that supports aliases.

##### `push()`

**Line:** 102 | **Returns:** `None`

**Documentation:**

> Pushes changes.

##### `pull()`

**Line:** 108 | **Returns:** `None`

**Documentation:**

> Pulls changes.

##### `clone()`

**Line:** 114 | **Returns:** `None`

**Documentation:**

> Clones a repository.

##### `commit()`

**Line:** 120 | **Returns:** `None`

**Documentation:**

> Commits pending changes.

##### `status(config)`

**Line:** 127 | **Returns:** `None`

**Parameters:**
- `config`

**Documentation:**

> Shows the status.

##### `alias(config, alias_, cmd, config_file)`

**Line:** 139 | **Returns:** `None`

**Parameters:**
- `config`
- `alias_`
- `cmd`
- `config_file`

**Documentation:**

> Adds an alias to the specified configuration file.

#### Classes

##### Class: `Config`

**Line:** 7

**Documentation:**

> The config in this example only holds aliases.

**Methods:**

- **`__init__(self)`** (Line 10)
  - Returns: `None`
  - _No documentation_

- **`add_alias(self, alias, cmd)`** (Line 14)
  - Returns: `None`
  - _No documentation_

- **`read_config(self, filename)`** (Line 17)
  - Returns: `None`
  - _No documentation_

- **`write_config(self, filename)`** (Line 25)
  - Returns: `None`
  - _No documentation_

##### Class: `AliasedGroup`

**Line:** 37

**Documentation:**

> This subclass of a group supports looking up aliases in a config
> file and with a bit of magic.

**Methods:**

- **`get_command(self, ctx, cmd_name)`** (Line 42)
  - Returns: `None`
  - _No documentation_

- **`resolve_command(self, ctx, args)`** (Line 70)
  - Returns: `None`
  - _No documentation_

---

### `C:\Users\I.C.T\OneDrive\Documents\git\click\examples\colors\colors.py`

**Language:** python

#### Functions

##### `cli()`

**Line:** 25 | **Returns:** `None`

**Documentation:**

> This script prints some colors. It will also automatically remove
> all ANSI styles if data is piped into a file.
> 
> Give it a try!

---

### `C:\Users\I.C.T\OneDrive\Documents\git\click\examples\completion\completion.py`

**Language:** python

#### Functions

##### `cli()`

**Line:** 8 | **Returns:** `None`

**Documentation:** _No documentation_

##### `ls(dir)`

**Line:** 14 | **Returns:** `None`

**Parameters:**
- `dir`

**Documentation:** _No documentation_

##### `get_env_vars(ctx, param, incomplete)`

**Line:** 18 | **Returns:** `None`

**Parameters:**
- `ctx`
- `param`
- `incomplete`

**Documentation:** _No documentation_

##### `show_env(envvar)`

**Line:** 26 | **Returns:** `None`

**Parameters:**
- `envvar`

**Documentation:** _No documentation_

##### `group()`

**Line:** 32 | **Returns:** `None`

**Documentation:** _No documentation_

##### `list_users(ctx, param, incomplete)`

**Line:** 36 | **Returns:** `None`

**Parameters:**
- `ctx`
- `param`
- `incomplete`

**Documentation:** _No documentation_

##### `select_user(user)`

**Line:** 52 | **Returns:** `None`

**Parameters:**
- `user`

**Documentation:** _No documentation_

---

### `C:\Users\I.C.T\OneDrive\Documents\git\click\examples\complex\complex\__init__.py`

**Language:** python

_No functions or classes found._

---

### `C:\Users\I.C.T\OneDrive\Documents\git\click\examples\complex\complex\cli.py`

**Language:** python

#### Functions

##### `cli(ctx, verbose, home)`

**Line:** 56 | **Returns:** `None`

**Parameters:**
- `ctx`
- `verbose`
- `home`

**Documentation:**

> A complex command line interface.

#### Classes

##### Class: `Environment`

**Line:** 10

**Documentation:** _No documentation_

**Methods:**

- **`__init__(self)`** (Line 11)
  - Returns: `None`
  - _No documentation_

- **`log(self, msg, *args)`** (Line 15)
  - Returns: `None`
  - Logs a message to stderr.

- **`vlog(self, msg, *args)`** (Line 21)
  - Returns: `None`
  - Logs a message to stderr only if verbose is enabled.

##### Class: `ComplexCLI`

**Line:** 31

**Documentation:** _No documentation_

**Methods:**

- **`list_commands(self, ctx)`** (Line 32)
  - Returns: `None`
  - _No documentation_

- **`get_command(self, ctx, name)`** (Line 40)
  - Returns: `None`
  - _No documentation_

---

### `C:\Users\I.C.T\OneDrive\Documents\git\click\examples\complex\complex\commands\__init__.py`

**Language:** python

_No functions or classes found._

---

### `C:\Users\I.C.T\OneDrive\Documents\git\click\examples\complex\complex\commands\cmd_init.py`

**Language:** python

#### Functions

##### `cli(ctx, path)`

**Line:** 9 | **Returns:** `None`

**Parameters:**
- `ctx`
- `path`

**Documentation:**

> Initializes a repository.

---

### `C:\Users\I.C.T\OneDrive\Documents\git\click\examples\complex\complex\commands\cmd_status.py`

**Language:** python

#### Functions

##### `cli(ctx)`

**Line:** 8 | **Returns:** `None`

**Parameters:**
- `ctx`

**Documentation:**

> Shows file changes in the current working directory.

---

### `C:\Users\I.C.T\OneDrive\Documents\git\click\examples\imagepipe\imagepipe.py`

**Language:** python

#### Functions

##### `cli()`

**Line:** 11 | **Returns:** `None`

**Documentation:**

> This script processes a bunch of images through pillow in a unix
> pipe.  One commands feeds into the next.
> 
> Example:
> 
> 
>     imagepipe open -i example01.jpg resize -w 128 display
>     imagepipe open -i example02.jpg blur save

##### `process_commands(processors)`

**Line:** 24 | **Returns:** `None`

**Parameters:**
- `processors`

**Documentation:**

> This result callback is invoked with an iterable of all the chained
> subcommands.  As in this example each subcommand returns a function
> we can chain them together to feed one into the other, similar to how
> a pipe on unix works.

##### `processor(f)`

**Line:** 42 | **Returns:** `None`

**Parameters:**
- `f`

**Documentation:**

> Helper decorator to rewrite a function so that it returns another
> function from it.

##### `generator(f)`

**Line:** 56 | **Returns:** `None`

**Parameters:**
- `f`

**Documentation:**

> Similar to the :func:`processor` but passes through old values
> unchanged and does not pass through the values as parameter.

##### `copy_filename(new, old)`

**Line:** 69 | **Returns:** `None`

**Parameters:**
- `new`
- `old`

**Documentation:** _No documentation_

##### `open_cmd(images)`

**Line:** 84 | **Returns:** `None`

**Parameters:**
- `images`

**Documentation:**

> Loads one or multiple images for processing.  The input parameter
> can be specified multiple times to load more than one image.

##### `save_cmd(images, filename)`

**Line:** 110 | **Returns:** `None`

**Parameters:**
- `images`
- `filename`

**Documentation:**

> Saves all processed images to a series of files.

##### `display_cmd(images)`

**Line:** 123 | **Returns:** `None`

**Parameters:**
- `images`

**Documentation:**

> Opens all images in an image viewer.

##### `resize_cmd(images, width, height)`

**Line:** 135 | **Returns:** `None`

**Parameters:**
- `images`
- `width`
- `height`

**Documentation:**

> Resizes an image by fitting it into the box without changing
> the aspect ratio.

##### `crop_cmd(images, border)`

**Line:** 151 | **Returns:** `None`

**Parameters:**
- `images`
- `border`

**Documentation:**

> Crops an image from all edges.

##### `convert_rotation(ctx, param, value)`

**Line:** 165 | **Returns:** `None`

**Parameters:**
- `ctx`
- `param`
- `value`

**Documentation:** _No documentation_

##### `convert_flip(ctx, param, value)`

**Line:** 178 | **Returns:** `None`

**Parameters:**
- `ctx`
- `param`
- `value`

**Documentation:** _No documentation_

##### `transpose_cmd(images, rotate, flip)`

**Line:** 195 | **Returns:** `None`

**Parameters:**
- `images`
- `rotate`
- `flip`

**Documentation:**

> Transposes an image by either rotating or flipping it.

##### `blur_cmd(images, radius)`

**Line:** 212 | **Returns:** `None`

**Parameters:**
- `images`
- `radius`

**Documentation:**

> Applies gaussian blur.

##### `smoothen_cmd(images, iterations)`

**Line:** 229 | **Returns:** `None`

**Parameters:**
- `images`
- `iterations`

**Documentation:**

> Applies a smoothening filter.

##### `emboss_cmd(images)`

**Line:** 243 | **Returns:** `None`

**Parameters:**
- `images`

**Documentation:**

> Embosses an image.

##### `sharpen_cmd(images, factor)`

**Line:** 255 | **Returns:** `None`

**Parameters:**
- `images`
- `factor`

**Documentation:**

> Sharpens an image.

##### `paste_cmd(images, left, right)`

**Line:** 267 | **Returns:** `None`

**Parameters:**
- `images`
- `left`
- `right`

**Documentation:**

> Pastes the second image on the first image and leaves the rest
> unchanged.

---

### `C:\Users\I.C.T\OneDrive\Documents\git\click\examples\inout\inout.py`

**Language:** python

#### Functions

##### `cli(input, output)`

**Line:** 7 | **Returns:** `None`

**Parameters:**
- `input`
- `output`

**Documentation:**

> This script works similar to the Unix `cat` command but it writes
> into a specific file (which could be the standard output as denoted by
> the ``-`` sign).
> 
> 
> Copy stdin to stdout:
>     inout - -
> 
> 
> Copy foo.txt and bar.txt to stdout:
>     inout foo.txt bar.txt -
> 
> 
> Write stdin into the file foo.txt
>     inout - foo.txt

---

### `C:\Users\I.C.T\OneDrive\Documents\git\click\examples\naval\naval.py`

**Language:** python

#### Functions

##### `cli()`

**Line:** 6 | **Returns:** `None`

**Documentation:**

> Naval Fate.
> 
> This is the docopt example adopted to Click but with some actual
> commands implemented and not just the empty parsing which really
> is not all that interesting.

##### `ship()`

**Line:** 16 | **Returns:** `None`

**Documentation:**

> Manages ships.

##### `ship_new(name)`

**Line:** 22 | **Returns:** `None`

**Parameters:**
- `name`

**Documentation:**

> Creates a new ship.

##### `ship_move(ship, x, y, speed)`

**Line:** 32 | **Returns:** `None`

**Parameters:**
- `ship`
- `x`
- `y`
- `speed`

**Documentation:**

> Moves SHIP to the new location X,Y.

##### `ship_shoot(ship, x, y)`

**Line:** 41 | **Returns:** `None`

**Parameters:**
- `ship`
- `x`
- `y`

**Documentation:**

> Makes SHIP fire to X,Y.

##### `mine()`

**Line:** 47 | **Returns:** `None`

**Documentation:**

> Manages mines.

##### `mine_set(x, y, ty)`

**Line:** 62 | **Returns:** `None`

**Parameters:**
- `x`
- `y`
- `ty`

**Documentation:**

> Sets a mine at a specific coordinate.

##### `mine_remove(x, y)`

**Line:** 70 | **Returns:** `None`

**Parameters:**
- `x`
- `y`

**Documentation:**

> Removes a mine at a specific coordinate.

---

### `C:\Users\I.C.T\OneDrive\Documents\git\click\examples\repo\repo.py`

**Language:** python

#### Functions

##### `cli(ctx, repo_home, config, verbose)`

**Line:** 44 | **Returns:** `None`

**Parameters:**
- `ctx`
- `repo_home`
- `config`
- `verbose`

**Documentation:**

> Repo is a command line tool that showcases how to build complex
> command line interfaces with Click.
> 
> This tool is supposed to look like a distributed version control
> system to show how something like this can be structured.

##### `clone(repo, src, dest, shallow, rev)`

**Line:** 72 | **Returns:** `None`

**Parameters:**
- `repo`
- `src`
- `dest`
- `shallow`
- `rev`

**Documentation:**

> Clones a repository.
> 
> This will clone the repository at SRC into the folder DEST.  If DEST
> is not provided this will automatically use the last path component
> of SRC and create that folder.

##### `delete(repo)`

**Line:** 91 | **Returns:** `None`

**Parameters:**
- `repo`

**Documentation:**

> Deletes a repository.
> 
> This will throw away the current repository.

##### `setuser(repo, username, email, password)`

**Line:** 105 | **Returns:** `None`

**Parameters:**
- `repo`
- `username`
- `email`
- `password`

**Documentation:**

> Sets the user credentials.
> 
> This will override the current user config.

##### `commit(repo, files, message)`

**Line:** 126 | **Returns:** `None`

**Parameters:**
- `repo`
- `files`
- `message`

**Documentation:**

> Commits outstanding changes.
> 
> Commit changes to the given files into the repository.  You will need to
> "repo push" to push up your changes to other repositories.
> 
> If a list of files is omitted, all changes reported by "repo status"
> will be committed.

##### `copy(repo, src, dst, force)`

**Line:** 161 | **Returns:** `None`

**Parameters:**
- `repo`
- `src`
- `dst`
- `force`

**Documentation:**

> Copies one or multiple files to a new location.  This copies all
> files from SRC to DST.

#### Classes

##### Class: `Repo`

**Line:** 8

**Documentation:** _No documentation_

**Methods:**

- **`__init__(self, home)`** (Line 9)
  - Returns: `None`
  - _No documentation_

- **`set_config(self, key, value)`** (Line 14)
  - Returns: `None`
  - _No documentation_

- **`__repr__(self)`** (Line 19)
  - Returns: `None`
  - _No documentation_

---

### `C:\Users\I.C.T\OneDrive\Documents\git\click\examples\termui\termui.py`

**Language:** python

#### Functions

##### `cli()`

**Line:** 9 | **Returns:** `None`

**Documentation:**

> This script showcases different terminal UI helpers in Click.

##### `colordemo()`

**Line:** 15 | **Returns:** `None`

**Documentation:**

> Demonstrates ANSI color support.

##### `pager()`

**Line:** 23 | **Returns:** `None`

**Documentation:**

> Demonstrates using the pager.

##### `progress(count)`

**Line:** 38 | **Returns:** `None`

**Parameters:**
- `count`

**Documentation:**

> Demonstrates the progress bar.

##### `open(url)`

**Line:** 105 | **Returns:** `None`

**Parameters:**
- `url`

**Documentation:**

> Opens a file or URL In the default application.

##### `locate(url)`

**Line:** 112 | **Returns:** `None`

**Parameters:**
- `url`

**Documentation:**

> Opens a file or URL In the default application.

##### `edit()`

**Line:** 118 | **Returns:** `None`

**Documentation:**

> Opens an editor with some text in it.

##### `clear()`

**Line:** 133 | **Returns:** `None`

**Documentation:**

> Clears the entire screen.

##### `pause()`

**Line:** 139 | **Returns:** `None`

**Documentation:**

> Waits for the user to press a button.

##### `menu()`

**Line:** 145 | **Returns:** `None`

**Documentation:**

> Shows a simple menu.

---

### `C:\Users\I.C.T\OneDrive\Documents\git\click\examples\validation\validation.py`

**Language:** python

#### Functions

##### `validate_count(ctx, param, value)`

**Line:** 6 | **Returns:** `None`

**Parameters:**
- `ctx`
- `param`
- `value`

**Documentation:** _No documentation_

##### `cli(count, foo, url)`

**Line:** 34 | **Returns:** `None`

**Parameters:**
- `count`
- `foo`
- `url`

**Documentation:**

> Validation.
> 
> This example validates parameters in different ways.  It does it
> through callbacks, through a custom type as well as by validating
> manually in the function.

#### Classes

##### Class: `URL`

**Line:** 12

**Documentation:** _No documentation_

**Methods:**

- **`convert(self, value, param, ctx)`** (Line 15)
  - Returns: `urlparse.ParseResult`
  - _No documentation_

---

### `C:\Users\I.C.T\OneDrive\Documents\git\click\src\click\__init__.py`

**Language:** python

#### Functions

##### `__getattr__(name)`

**Line:** 77 | **Returns:** `object`

**Parameters:**
- `name` (str)

**Documentation:** _No documentation_

---

### `C:\Users\I.C.T\OneDrive\Documents\git\click\src\click\_compat.py`

**Language:** python

#### Functions

##### `_make_text_stream(stream, encoding, errors, force_readable, force_writable)`

**Line:** 19 | **Returns:** `t.TextIO`

**Parameters:**
- `stream` (t.BinaryIO)
- `encoding` (str | None)
- `errors` (str | None)
- `force_readable` (bool)
- `force_writable` (bool)

**Documentation:** _No documentation_

##### `is_ascii_encoding(encoding)`

**Line:** 40 | **Returns:** `bool`

**Parameters:**
- `encoding` (str)

**Documentation:**

> Checks if a given encoding is ascii.

##### `get_best_encoding(stream)`

**Line:** 48 | **Returns:** `str`

**Parameters:**
- `stream` (t.IO[t.Any])

**Documentation:**

> Returns the default stream encoding if not found.

##### `_is_binary_reader(stream, default)`

**Line:** 151 | **Returns:** `bool`

**Parameters:**
- `stream` (t.IO[t.Any])
- `default` (bool)

**Documentation:** _No documentation_

##### `_is_binary_writer(stream, default)`

**Line:** 160 | **Returns:** `bool`

**Parameters:**
- `stream` (t.IO[t.Any])
- `default` (bool)

**Documentation:** _No documentation_

##### `_find_binary_reader(stream)`

**Line:** 173 | **Returns:** `t.BinaryIO | None`

**Parameters:**
- `stream` (t.IO[t.Any])

**Documentation:** _No documentation_

##### `_find_binary_writer(stream)`

**Line:** 191 | **Returns:** `t.BinaryIO | None`

**Parameters:**
- `stream` (t.IO[t.Any])

**Documentation:** _No documentation_

##### `_stream_is_misconfigured(stream)`

**Line:** 209 | **Returns:** `bool`

**Parameters:**
- `stream` (t.TextIO)

**Documentation:**

> A stream is misconfigured if its encoding is ASCII.

##### `_is_compat_stream_attr(stream, attr, value)`

**Line:** 218 | **Returns:** `bool`

**Parameters:**
- `stream` (t.TextIO)
- `attr` (str)
- `value` (str | None)

**Documentation:**

> A stream attribute is compatible if it is equal to the
> desired value or the desired value is unset and the attribute
> has a value.

##### `_is_compatible_text_stream(stream, encoding, errors)`

**Line:** 227 | **Returns:** `bool`

**Parameters:**
- `stream` (t.TextIO)
- `encoding` (str | None)
- `errors` (str | None)

**Documentation:**

> Check if a stream's encoding and errors attributes are
> compatible with the desired values.

##### `_force_correct_text_stream(text_stream, encoding, errors, is_binary, find_binary, force_readable, force_writable)`

**Line:** 238 | **Returns:** `t.TextIO`

**Parameters:**
- `text_stream` (t.IO[t.Any])
- `encoding` (str | None)
- `errors` (str | None)
- `is_binary` (t.Callable[[t.IO[t.Any], bool], bool])
- `find_binary` (t.Callable[[t.IO[t.Any]], t.BinaryIO | None])
- `force_readable` (bool)
- `force_writable` (bool)

**Documentation:** _No documentation_

##### `_force_correct_text_reader(text_reader, encoding, errors, force_readable)`

**Line:** 284 | **Returns:** `t.TextIO`

**Parameters:**
- `text_reader` (t.IO[t.Any])
- `encoding` (str | None)
- `errors` (str | None)
- `force_readable` (bool)

**Documentation:** _No documentation_

##### `_force_correct_text_writer(text_writer, encoding, errors, force_writable)`

**Line:** 300 | **Returns:** `t.TextIO`

**Parameters:**
- `text_writer` (t.IO[t.Any])
- `encoding` (str | None)
- `errors` (str | None)
- `force_writable` (bool)

**Documentation:** _No documentation_

##### `get_binary_stdin()`

**Line:** 316 | **Returns:** `t.BinaryIO`

**Documentation:** _No documentation_

##### `get_binary_stdout()`

**Line:** 323 | **Returns:** `t.BinaryIO`

**Documentation:** _No documentation_

##### `get_binary_stderr()`

**Line:** 330 | **Returns:** `t.BinaryIO`

**Documentation:** _No documentation_

##### `get_text_stdin(encoding, errors)`

**Line:** 337 | **Returns:** `t.TextIO`

**Parameters:**
- `encoding` (str | None)
- `errors` (str | None)

**Documentation:** _No documentation_

##### `get_text_stdout(encoding, errors)`

**Line:** 344 | **Returns:** `t.TextIO`

**Parameters:**
- `encoding` (str | None)
- `errors` (str | None)

**Documentation:** _No documentation_

##### `get_text_stderr(encoding, errors)`

**Line:** 351 | **Returns:** `t.TextIO`

**Parameters:**
- `encoding` (str | None)
- `errors` (str | None)

**Documentation:** _No documentation_

##### `_wrap_io_open(file, mode, encoding, errors)`

**Line:** 358 | **Returns:** `t.IO[t.Any]`

**Parameters:**
- `file` (str | os.PathLike[str] | int)
- `mode` (str)
- `encoding` (str | None)
- `errors` (str | None)

**Documentation:**

> Handles not passing ``encoding`` and ``errors`` in binary mode.

##### `open_stream(filename, mode, encoding, errors, atomic)`

**Line:** 371 | **Returns:** `tuple[t.IO[t.Any], bool]`

**Parameters:**
- `filename` (str | os.PathLike[str])
- `mode` (str)
- `encoding` (str | None)
- `errors` (str | None)
- `atomic` (bool)

**Documentation:** _No documentation_

##### `strip_ansi(value)`

**Line:** 488 | **Returns:** `str`

**Parameters:**
- `value` (str)

**Documentation:** _No documentation_

##### `_is_jupyter_kernel_output(stream)`

**Line:** 492 | **Returns:** `bool`

**Parameters:**
- `stream` (t.IO[t.Any])

**Documentation:** _No documentation_

##### `should_strip_ansi(stream, color)`

**Line:** 499 | **Returns:** `bool`

**Parameters:**
- `stream` (t.IO[t.Any] | None)
- `color` (bool | None)

**Documentation:** _No documentation_

##### `term_len(x)`

**Line:** 572 | **Returns:** `int`

**Parameters:**
- `x` (str)

**Documentation:** _No documentation_

##### `isatty(stream)`

**Line:** 576 | **Returns:** `bool`

**Parameters:**
- `stream` (t.IO[t.Any])

**Documentation:** _No documentation_

##### `_make_cached_stream_func(src_func, wrapper_func)`

**Line:** 583 | **Returns:** `t.Callable[[], t.TextIO | None]`

**Parameters:**
- `src_func` (t.Callable[[], t.TextIO | None])
- `wrapper_func` (t.Callable[[], t.TextIO])

**Documentation:** _No documentation_

#### Classes

##### Class: `_NonClosingTextIOWrapper`

**Line:** 56

**Documentation:** _No documentation_

**Methods:**

- **`__init__(self, stream, encoding, errors, force_readable, force_writable, **extra)`** (Line 57)
  - Returns: `None`
  - _No documentation_

- **`__del__(self)`** (Line 71)
  - Returns: `None`
  - _No documentation_

- **`isatty(self)`** (Line 77)
  - Returns: `bool`
  - _No documentation_

##### Class: `_FixupStream`

**Line:** 82

**Documentation:**

> The new io interface needs more from streams than streams
> traditionally implement.  As such, this fix-up code is necessary in
> some circumstances.
> 
> The forcing of readable and writable flags are there because some tools
> put badly patched objects on sys (one such offender are certain version
> of jupyter notebook).

**Methods:**

- **`__init__(self, stream, force_readable, force_writable)`** (Line 92)
  - Returns: `None`
  - _No documentation_

- **`__getattr__(self, name)`** (Line 102)
  - Returns: `t.Any`
  - _No documentation_

- **`read1(self, size)`** (Line 105)
  - Returns: `bytes`
  - _No documentation_

- **`readable(self)`** (Line 113)
  - Returns: `bool`
  - _No documentation_

- **`writable(self)`** (Line 125)
  - Returns: `bool`
  - _No documentation_

- **`seekable(self)`** (Line 140)
  - Returns: `bool`
  - _No documentation_

##### Class: `_AtomicFile`

**Line:** 452

**Documentation:** _No documentation_

**Methods:**

- **`__init__(self, f, tmp_filename, real_filename)`** (Line 453)
  - Returns: `None`
  - _No documentation_

- **`name(self)`** (Line 460)
  - Returns: `str`
  - _No documentation_

- **`close(self, delete)`** (Line 463)
  - Returns: `None`
  - _No documentation_

- **`__getattr__(self, name)`** (Line 470)
  - Returns: `t.Any`
  - _No documentation_

- **`__enter__(self)`** (Line 473)
  - Returns: `_AtomicFile`
  - _No documentation_

- **`__exit__(self, exc_type, exc_value, tb)`** (Line 476)
  - Returns: `None`
  - _No documentation_

- **`__repr__(self)`** (Line 484)
  - Returns: `str`
  - _No documentation_

---

### `C:\Users\I.C.T\OneDrive\Documents\git\click\src\click\_termui_impl.py`

**Language:** python

#### Functions

##### `_pager_contextmanager(color)`

**Line:** 380 | **Returns:** `t.ContextManager[tuple[t.BinaryIO | t.TextIO, str, bool]]`

**Parameters:**
- `color` (bool | None)

**Documentation:**

> Decide what method to use for paging through text.

##### `get_pager_file(color)`

**Line:** 412 | **Returns:** `t.Generator[t.TextIO, None, None]`

**Parameters:**
- `color` (bool | None)

**Documentation:**

> Context manager.
> Yields a writable file-like object which can be used as an output pager.
> .. versionadded:: 8.2
> :param color: controls if the pager supports ANSI colors or not.  The
>               default is autodetection.

##### `_pipepager(cmd_parts, color)`

**Line:** 437 | **Returns:** `t.Iterator[tuple[t.BinaryIO | t.TextIO, str, bool]]`

**Parameters:**
- `cmd_parts` (list[str])
- `color` (bool | None)

**Documentation:**

> Page through text by feeding it to another program.
> 
> Invokes the pager via :class:`subprocess.Popen` with an ``argv`` list
> produced by :func:`shlex.split`. The command is resolved to an absolute
> path with :func:`shutil.which` as recommended by the
> :mod:`subprocess` docs for Windows compatibility.
> 
> Invoking a pager through this might support colors: if piping to
> ``less`` and the user hasn't decided on colors, ``LESS=-R`` is set
> automatically.

##### `_tempfilepager(cmd_parts, color)`

**Line:** 541 | **Returns:** `t.Iterator[tuple[t.BinaryIO | t.TextIO, str, bool]]`

**Parameters:**
- `cmd_parts` (list[str])
- `color` (bool | None)

**Documentation:**

> Page through text by invoking a program on a temporary file.
> 
> Used as the primary pager strategy on Windows (where piping to
> ``more`` adds spurious ``\r\n``), and as a fallback on other
> platforms. The command is resolved to an absolute path with
> :func:`shutil.which`.

##### `_nullpager(stream, color)`

**Line:** 592 | **Returns:** `t.Iterator[tuple[t.TextIO, str, bool]]`

**Parameters:**
- `stream` (t.TextIO)
- `color` (bool | None)

**Documentation:**

> Simply print unformatted text.  This is the ultimate fallback.

##### `open_url(url, wait, locate)`

**Line:** 718 | **Returns:** `int`

**Parameters:**
- `url` (str)
- `wait` (bool)
- `locate` (bool)

**Documentation:** _No documentation_

##### `_translate_ch_to_exc(ch)`

**Line:** 788 | **Returns:** `None`

**Parameters:**
- `ch` (str)

**Documentation:** _No documentation_

#### Classes

##### Class: `ProgressBar`

**Line:** 43

**Documentation:** _No documentation_

**Methods:**

- **`__init__(self, iterable, length, fill_char, empty_char, bar_template, info_sep, hidden, show_eta, show_percent, show_pos, item_show_func, label, file, color, update_min_steps, width)`** (Line 44)
  - Returns: `None`
  - _No documentation_

- **`__enter__(self)`** (Line 115)
  - Returns: `ProgressBar[V]`
  - _No documentation_

- **`__exit__(self, exc_type, exc_value, tb)`** (Line 120)
  - Returns: `None`
  - _No documentation_

- **`__iter__(self)`** (Line 128)
  - Returns: `cabc.Iterator[V]`
  - _No documentation_

- **`__next__(self)`** (Line 134)
  - Returns: `V`
  - _No documentation_

- **`render_finish(self)`** (Line 142)
  - Returns: `None`
  - _No documentation_

- **`pct(self)`** (Line 149)
  - Returns: `float`
  - _No documentation_

- **`time_per_iteration(self)`** (Line 155)
  - Returns: `float`
  - _No documentation_

- **`eta(self)`** (Line 161)
  - Returns: `float`
  - _No documentation_

- **`format_eta(self)`** (Line 166)
  - Returns: `str`
  - _No documentation_

- **`format_pos(self)`** (Line 181)
  - Returns: `str`
  - _No documentation_

- **`format_pct(self)`** (Line 187)
  - Returns: `str`
  - _No documentation_

- **`format_bar(self)`** (Line 190)
  - Returns: `str`
  - _No documentation_

- **`format_progress_line(self)`** (Line 209)
  - Returns: `str`
  - _No documentation_

- **`render_progress(self)`** (Line 236)
  - Returns: `None`
  - _No documentation_

- **`make_step(self, n_steps)`** (Line 282)
  - Returns: `None`
  - _No documentation_

- **`update(self, n_steps, current_item)`** (Line 304)
  - Returns: `None`
  - Update the progress bar by advancing a specified number of

- **`finish(self)`** (Line 330)
  - Returns: `None`
  - _No documentation_

- **`generator(self)`** (Line 335)
  - Returns: `cabc.Iterator[V]`
  - Return a generator which yields the items added to the bar

##### Class: `MaybeStripAnsi`

**Line:** 369

**Documentation:** _No documentation_

**Methods:**

- **`__init__(self, stream, **kwargs)`** (Line 370)
  - Returns: `None`
  - _No documentation_

- **`write(self, text)`** (Line 374)
  - Returns: `int`
  - _No documentation_

##### Class: `Editor`

**Line:** 602

**Documentation:** _No documentation_

**Methods:**

- **`__init__(self, editor, env, require_save, extension)`** (Line 603)
  - Returns: `None`
  - _No documentation_

- **`get_editor(self)`** (Line 615)
  - Returns: `str`
  - _No documentation_

- **`edit_files(self, filenames)`** (Line 632)
  - Returns: `None`
  - Open files in the user's editor.

- **`edit(self, text)`** (Line 663)
  - Returns: `bytes | None`
  - _No documentation_

- **`edit(self, text)`** (Line 668)
  - Returns: `str | None`
  - _No documentation_

- **`edit(self, text)`** (Line 670)
  - Returns: `str | bytes | None`
  - _No documentation_

---

### `C:\Users\I.C.T\OneDrive\Documents\git\click\src\click\_textwrap.py`

**Language:** python

#### Classes

##### Class: `TextWrapper`

**Line:** 8

**Documentation:** _No documentation_

**Methods:**

- **`_handle_long_word(self, reversed_chunks, cur_line, cur_len, width)`** (Line 9)
  - Returns: `None`
  - _No documentation_

- **`extra_indent(self, indent)`** (Line 28)
  - Returns: `cabc.Iterator[None]`
  - _No documentation_

- **`indent_only(self, text)`** (Line 40)
  - Returns: `str`
  - _No documentation_

---

### `C:\Users\I.C.T\OneDrive\Documents\git\click\src\click\_utils.py`

**Language:** python

#### Classes

##### Class: `Sentinel`

**Line:** 7

**Documentation:**

> Enum used to define sentinel values.
> 
> .. seealso::
> 
>     `PEP 661 - Sentinel Values <https://peps.python.org/pep-0661/>`_.

**Methods:**

- **`__repr__(self)`** (Line 18)
  - Returns: `str`
  - _No documentation_

---

### `C:\Users\I.C.T\OneDrive\Documents\git\click\src\click\_winconsole.py`

**Language:** python

#### Functions

##### `_get_text_stdin(buffer_stream)`

**Line:** 226 | **Returns:** `t.TextIO`

**Parameters:**
- `buffer_stream` (t.BinaryIO)

**Documentation:** _No documentation_

##### `_get_text_stdout(buffer_stream)`

**Line:** 236 | **Returns:** `t.TextIO`

**Parameters:**
- `buffer_stream` (t.BinaryIO)

**Documentation:** _No documentation_

##### `_get_text_stderr(buffer_stream)`

**Line:** 246 | **Returns:** `t.TextIO`

**Parameters:**
- `buffer_stream` (t.BinaryIO)

**Documentation:** _No documentation_

##### `_is_console(f)`

**Line:** 263 | **Returns:** `bool`

**Parameters:**
- `f` (t.TextIO)

**Documentation:** _No documentation_

##### `_get_windows_console_stream(f, encoding, errors)`

**Line:** 276 | **Returns:** `t.TextIO | None`

**Parameters:**
- `f` (t.TextIO)
- `encoding` (str | None)
- `errors` (str | None)

**Documentation:** _No documentation_

#### Classes

##### Class: `Py_buffer`

**Line:** 87

**Documentation:** _No documentation_

##### Class: `_WindowsConsoleRawIOBase`

**Line:** 118

**Documentation:** _No documentation_

**Methods:**

- **`__init__(self, handle)`** (Line 119)
  - Returns: `None`
  - _No documentation_

- **`isatty(self)`** (Line 122)
  - Returns: `t.Literal[True]`
  - _No documentation_

##### Class: `_WindowsConsoleReader`

**Line:** 127

**Documentation:** _No documentation_

**Methods:**

- **`readable(self)`** (Line 128)
  - Returns: `t.Literal[True]`
  - _No documentation_

- **`readinto(self, b)`** (Line 131)
  - Returns: `int`
  - _No documentation_

##### Class: `_WindowsConsoleWriter`

**Line:** 162

**Documentation:** _No documentation_

**Methods:**

- **`writable(self)`** (Line 163)
  - Returns: `t.Literal[True]`
  - _No documentation_

- **`_get_error_message(errno)`** (Line 167)
  - Returns: `str`
  - _No documentation_

- **`write(self, b)`** (Line 174)
  - Returns: `int`
  - _No documentation_

##### Class: `ConsoleStream`

**Line:** 194

**Documentation:** _No documentation_

**Methods:**

- **`__init__(self, text_stream, byte_stream)`** (Line 195)
  - Returns: `None`
  - _No documentation_

- **`name(self)`** (Line 200)
  - Returns: `str`
  - _No documentation_

- **`write(self, x)`** (Line 203)
  - Returns: `int`
  - _No documentation_

- **`writelines(self, lines)`** (Line 212)
  - Returns: `None`
  - _No documentation_

- **`__getattr__(self, name)`** (Line 216)
  - Returns: `t.Any`
  - _No documentation_

- **`isatty(self)`** (Line 219)
  - Returns: `bool`
  - _No documentation_

- **`__repr__(self)`** (Line 222)
  - Returns: `str`
  - _No documentation_

---

### `C:\Users\I.C.T\OneDrive\Documents\git\click\src\click\core.py`

**Language:** python

#### Functions

##### `_complete_visible_commands(ctx, incomplete)`

**Line:** 57 | **Returns:** `cabc.Iterator[tuple[str, Command]]`

**Parameters:**
- `ctx` (Context)
- `incomplete` (str)

**Documentation:**

> List all the subcommands of a group that start with the
> incomplete value and aren't hidden.
> 
> :param ctx: Invocation context for the group.
> :param incomplete: Value being completed. May be empty.

##### `_check_nested_chain(base_command, cmd_name, cmd, register)`

**Line:** 76 | **Returns:** `None`

**Parameters:**
- `base_command` (Group)
- `cmd_name` (str)
- `cmd` (Command)
- `register` (bool)

**Documentation:** _No documentation_

##### `batch(iterable, batch_size)`

**Line:** 96 | **Returns:** `list[tuple[V, ...]]`

**Parameters:**
- `iterable` (cabc.Iterable[V])
- `batch_size` (int)

**Documentation:** _No documentation_

##### `augment_usage_errors(ctx, param)`

**Line:** 101 | **Returns:** `cabc.Iterator[None]`

**Parameters:**
- `ctx` (Context)
- `param` (Parameter | None)

**Documentation:**

> Context manager that attaches extra information to exceptions.

##### `iter_params_for_processing(invocation_order, declaration_order)`

**Line:** 119 | **Returns:** `list[Parameter]`

**Parameters:**
- `invocation_order` (cabc.Sequence[Parameter])
- `declaration_order` (cabc.Sequence[Parameter])

**Documentation:**

> Returns all declared parameters in the order they should be processed.
> 
> The declared parameters are re-shuffled depending on the order in which
> they were invoked, as well as the eagerness of each parameters.
> 
> The invocation order takes precedence over the declaration order. I.e. the
> order in which the user provided them to the CLI is respected.
> 
> This behavior and its effect on callback evaluation is detailed at:
> https://click.palletsprojects.com/en/stable/advanced/#callback-evaluation-order

##### `_check_iter(value)`

**Line:** 2046 | **Returns:** `cabc.Iterator[t.Any]`

**Parameters:**
- `value` (t.Any)

**Documentation:**

> Check if the value is iterable but not a string. Raises a type
> error, or return an iterator over the value.

##### `__getattr__(name)`

**Line:** 3474 | **Returns:** `object`

**Parameters:**
- `name` (str)

**Documentation:** _No documentation_

#### Classes

##### Class: `ParameterSource`

**Line:** 146

**Documentation:**

> This is an :class:`~enum.IntEnum` that indicates the source of a
> parameter's value.
> 
> Use :meth:`click.Context.get_parameter_source` to get the
> source for a parameter by name.
> 
> Members are ordered from most explicit to least explicit source.
> This allows comparison to check if a value was explicitly provided:
> 
> .. code-block:: python
> 
>     source = ctx.get_parameter_source("port")
>     if source < click.ParameterSource.DEFAULT_MAP:
>         ...  # value was explicitly set
> 
> .. versionchanged:: 8.3.3
>     Use :class:`~enum.IntEnum` and reorder members from most to
>     least explicit. Supports comparison operators.
> 
> .. versionchanged:: 8.0
>     Use :class:`~enum.Enum` and drop the ``validate`` method.
> 
> .. versionchanged:: 8.0
>     Added the ``PROMPT`` value.

##### Class: `Context`

**Line:** 185

**Documentation:**

> The context is a special internal object that holds state relevant
> for the script execution at every single level.  It's normally invisible
> to commands unless they opt-in to getting access to it.
> 
> The context is useful as it can pass internal objects around and can
> control special execution features such as reading data from
> environment variables.
> 
> A context can be used as context manager in which case it will call
> :meth:`close` on teardown.
> 
> :param command: the command class for this context.
> :param parent: the parent context.
> :param info_name: the info name for this invocation.  Generally this
>                   is the most descriptive name for the script or
>                   command.  For the toplevel script it is usually
>                   the name of the script, for commands below that it's
>                   the name of the script.
> :param obj: an arbitrary object of user data.
> :param auto_envvar_prefix: the prefix to use for automatic environment
>                            variables.  If this is `None` then reading
>                            from environment variables is disabled.  This
>                            does not affect manually set environment
>                            variables which are always read.
> :param default_map: a dictionary (like object) with default values
>                     for parameters.
> :param terminal_width: the width of the terminal.  The default is
>                        inherit from parent context.  If no context
>                        defines the terminal width then auto
>                        detection will be applied.
> :param max_content_width: the maximum width for content rendered by
>                           Click (this currently only affects help
>                           pages).  This defaults to 80 characters if
>                           not overridden.  In other words: even if the
>                           terminal is larger than that, Click will not
>                           format things wider than 80 characters by
>                           default.  In addition to that, formatters might
>                           add some safety mapping on the right.
> :param resilient_parsing: if this flag is enabled then Click will
>                           parse without any interactivity or callback
>                           invocation.  Default values will also be
>                           ignored.  This is useful for implementing
>                           things such as completion support.
> :param allow_extra_args: if this is set to `True` then extra arguments
>                          at the end will not raise an error and will be
>                          kept on the context.  The default is to inherit
>                          from the command.
> :param allow_interspersed_args: if this is set to `False` then options
>                                 and arguments cannot be mixed.  The
>                                 default is to inherit from the command.
> :param ignore_unknown_options: instructs click to ignore options it does
>                                not know and keeps them for later
>                                processing.
> :param help_option_names: optionally a list of strings that define how
>                           the default help parameter is named.  The
>                           default is ``['--help']``.
> :param token_normalize_func: an optional function that is used to
>                              normalize tokens (options, choices,
>                              etc.).  This for instance can be used to
>                              implement case insensitive behavior.
> :param color: controls if the terminal supports ANSI colors or not.  The
>               default is autodetection.  This is only needed if ANSI
>               codes are used in texts that Click prints which is by
>               default not the case.  This for instance would affect
>               help output.
> :param show_default: Show the default value for commands. If this
>     value is not set, it defaults to the value from the parent
>     context. ``Command.show_default`` overrides this default for the
>     specific command.
> 
> .. versionchanged:: 8.2
>     The ``protected_args`` attribute is deprecated and will be removed in
>     Click 9.0. ``args`` will contain remaining unparsed tokens.
> 
> .. versionchanged:: 8.1
>     The ``show_default`` parameter is overridden by
>     ``Command.show_default``, instead of the other way around.
> 
> .. versionchanged:: 8.0
>     The ``show_default`` parameter defaults to the value from the
>     parent context.
> 
> .. versionchanged:: 7.1
>    Added the ``show_default`` parameter.
> 
> .. versionchanged:: 4.0
>     Added the ``color``, ``ignore_unknown_options``, and
>     ``max_content_width`` parameters.
> 
> .. versionchanged:: 3.0
>     Added the ``allow_extra_args`` and ``allow_interspersed_args``
>     parameters.
> 
> .. versionchanged:: 2.0
>     Added the ``resilient_parsing``, ``help_option_names``, and
>     ``token_normalize_func`` parameters.

**Methods:**

- **`__init__(self, command, parent, info_name, obj, auto_envvar_prefix, default_map, terminal_width, max_content_width, resilient_parsing, allow_extra_args, allow_interspersed_args, ignore_unknown_options, help_option_names, token_normalize_func, color, show_default)`** (Line 289)
  - Returns: `None`
  - _No documentation_

- **`protected_args(self)`** (Line 460)
  - Returns: `list[str]`
  - _No documentation_

- **`to_info_dict(self)`** (Line 471)
  - Returns: `dict[str, t.Any]`
  - Gather information that could be useful for a tool generating

- **`__enter__(self)`** (Line 492)
  - Returns: `Context`
  - _No documentation_

- **`__exit__(self, exc_type, exc_value, tb)`** (Line 497)
  - Returns: `bool | None`
  - _No documentation_

- **`scope(self, cleanup)`** (Line 512)
  - Returns: `cabc.Iterator[Context]`
  - This helper method can be used with the context object to promote

- **`meta(self)`** (Line 550)
  - Returns: `dict[str, t.Any]`
  - This is a dictionary which is shared with all the contexts

- **`make_formatter(self)`** (Line 577)
  - Returns: `HelpFormatter`
  - Creates the :class:`~click.HelpFormatter` for the help and

- **`with_resource(self, context_manager)`** (Line 591)
  - Returns: `V`
  - Register a resource as if it were used in a ``with``

- **`call_on_close(self, f)`** (Line 620)
  - Returns: `t.Callable[..., t.Any]`
  - Register a function to be called when the context tears down.

- **`close(self)`** (Line 632)
  - Returns: `None`
  - Invoke all close callbacks registered with

- **`_close_with_exception_info(self, exc_type, exc_value, tb)`** (Line 639)
  - Returns: `bool | None`
  - Unwind the exit stack by calling its :meth:`__exit__` providing the exception

- **`command_path(self)`** (Line 658)
  - Returns: `str`
  - The computed command path.  This is used for the ``usage``

- **`find_root(self)`** (Line 676)
  - Returns: `Context`
  - Finds the outermost context.

- **`find_object(self, object_type)`** (Line 683)
  - Returns: `V | None`
  - Finds the closest object of a given type.

- **`ensure_object(self, object_type)`** (Line 695)
  - Returns: `V`
  - Like :meth:`find_object` but sets the innermost object to a

- **`_default_map_has(self, name)`** (Line 704)
  - Returns: `bool`
  - Check if :attr:`default_map` contains a real value for ``name``.

- **`lookup_default(self, name, call)`** (Line 719)
  - Returns: `t.Any | None`
  - _No documentation_

- **`lookup_default(self, name, call)`** (Line 724)
  - Returns: `t.Any | t.Callable[[], t.Any] | None`
  - _No documentation_

- **`lookup_default(self, name, call)`** (Line 728)
  - Returns: `t.Any | None`
  - Get the default for a parameter from :attr:`default_map`.

- **`fail(self, message)`** (Line 750)
  - Returns: `t.NoReturn`
  - Aborts the execution of the program with a specific error

- **`abort(self)`** (Line 758)
  - Returns: `t.NoReturn`
  - Aborts the script.

- **`exit(self, code)`** (Line 762)
  - Returns: `t.NoReturn`
  - Exits the application with a given exit code.

- **`get_usage(self)`** (Line 772)
  - Returns: `str`
  - Helper method to get formatted usage string for the current

- **`get_help(self)`** (Line 778)
  - Returns: `str`
  - Helper method to get formatted help page for the current

- **`_make_sub_context(self, command)`** (Line 784)
  - Returns: `Context`
  - Create a new context of the same type as this context, but

- **`invoke(*args, **kwargs)`** (Line 793)
  - Returns: `V`
  - _No documentation_

- **`invoke(*args, **kwargs)`** (Line 798)
  - Returns: `t.Any`
  - _No documentation_

- **`invoke(*args, **kwargs)`** (Line 800)
  - Returns: `t.Any | V`
  - Invokes a command callback in exactly the way it expects.  There

- **`forward(*args, **kwargs)`** (Line 856)
  - Returns: `t.Any`
  - Similar to :meth:`invoke` but fills in default keyword

- **`set_parameter_source(self, name, source)`** (Line 875)
  - Returns: `None`
  - Set the source of a parameter. This indicates the location

- **`get_parameter_source(self, name)`** (Line 884)
  - Returns: `ParameterSource | None`
  - Get the source of a parameter. This indicates the location

##### Class: `Command`

**Line:** 903

**Documentation:**

> Commands are the basic building block of command line interfaces in
> Click.  A basic command handles command line parsing and might dispatch
> more parsing to commands nested below it.
> 
> :param name: the name of the command to use unless a group overrides it.
> :param context_settings: an optional dictionary with defaults that are
>                          passed to the context object.
> :param callback: the callback to invoke.  This is optional.
> :param params: the parameters to register with this command.  This can
>                be either :class:`Option` or :class:`Argument` objects.
> :param help: the help string to use for this command.
> :param epilog: like the help string but it's printed at the end of the
>                help page after everything else.
> :param short_help: the short help to use for this command.  This is
>                    shown on the command listing of the parent command.
> :param add_help_option: by default each command registers a ``--help``
>                         option.  This can be disabled by this parameter.
> :param no_args_is_help: this controls what happens if no arguments are
>                         provided.  This option is disabled by default.
>                         If enabled this will add ``--help`` as argument
>                         if no arguments are passed
> :param hidden: hide this command from help outputs.
> :param deprecated: If ``True`` or non-empty string, issues a message
>                     indicating that the command is deprecated and highlights
>                     its deprecation in --help. The message can be customized
>                     by using a string as the value.
> 
> .. versionchanged:: 8.2
>     This is the base class for all commands, not ``BaseCommand``.
>     ``deprecated`` can be set to a string as well to customize the
>     deprecation message.
> 
> .. versionchanged:: 8.1
>     ``help``, ``epilog``, and ``short_help`` are stored unprocessed,
>     all formatting is done when outputting help text, not at init,
>     and is done even if not using the ``@command`` decorator.
> 
> .. versionchanged:: 8.0
>     Added a ``repr`` showing the command name.
> 
> .. versionchanged:: 7.1
>     Added the ``no_args_is_help`` parameter.
> 
> .. versionchanged:: 2.0
>     Added the ``context_settings`` parameter.

**Methods:**

- **`__init__(self, name, context_settings, callback, params, help, epilog, short_help, options_metavar, add_help_option, no_args_is_help, hidden, deprecated)`** (Line 965)
  - Returns: `None`
  - _No documentation_

- **`to_info_dict(self, ctx)`** (Line 1009)
  - Returns: `dict[str, t.Any]`
  - _No documentation_

- **`__repr__(self)`** (Line 1020)
  - Returns: `str`
  - _No documentation_

- **`get_usage(self, ctx)`** (Line 1023)
  - Returns: `str`
  - Formats the usage line into a string and returns it.

- **`get_params(self, ctx)`** (Line 1032)
  - Returns: `list[Parameter]`
  - _No documentation_

- **`format_usage(self, ctx, formatter)`** (Line 1057)
  - Returns: `None`
  - Writes the usage line into the formatter.

- **`collect_usage_pieces(self, ctx)`** (Line 1065)
  - Returns: `list[str]`
  - Returns all the pieces that go into the usage line and returns

- **`get_help_option_names(self, ctx)`** (Line 1076)
  - Returns: `list[str]`
  - Returns the names for the help option.

- **`get_help_option(self, ctx)`** (Line 1084)
  - Returns: `Option | None`
  - Returns the help option object.

- **`make_parser(self, ctx)`** (Line 1111)
  - Returns: `_OptionParser`
  - Creates the underlying option parser for this command.

- **`get_help(self, ctx)`** (Line 1118)
  - Returns: `str`
  - Formats the help into a string and returns it.

- **`get_short_help_str(self, limit)`** (Line 1127)
  - Returns: `str`
  - Gets short help for the command or makes it by shortening the

- **`format_help(self, ctx, formatter)`** (Line 1150)
  - Returns: `None`
  - Writes the help into the formatter if it exists.

- **`format_help_text(self, ctx, formatter)`** (Line 1167)
  - Returns: `None`
  - Writes the help text to the formatter if it exists.

- **`format_options(self, ctx, formatter)`** (Line 1191)
  - Returns: `None`
  - Writes all the options into the formatter if they exist.

- **`format_epilog(self, ctx, formatter)`** (Line 1203)
  - Returns: `None`
  - Writes the epilog into the formatter if it exists.

- **`make_context(self, info_name, args, parent, **extra)`** (Line 1212)
  - Returns: `Context`
  - This function when given an info name and arguments will kick

- **`parse_args(self, ctx, args)`** (Line 1249)
  - Returns: `list[str]`
  - _No documentation_

- **`invoke(self, ctx)`** (Line 1285)
  - Returns: `t.Any`
  - Given a context, this invokes the attached callback (if it exists)

- **`shell_complete(self, ctx, incomplete)`** (Line 1301)
  - Returns: `list[CompletionItem]`
  - Return a list of completions for the incomplete value. Looks

- **`main(self, args, prog_name, complete_var, standalone_mode, **extra)`** (Line 1349)
  - Returns: `t.NoReturn`
  - _No documentation_

- **`main(self, args, prog_name, complete_var, standalone_mode, **extra)`** (Line 1359)
  - Returns: `t.Any`
  - _No documentation_

- **`main(self, args, prog_name, complete_var, standalone_mode, windows_expand_args, **extra)`** (Line 1368)
  - Returns: `t.Any`
  - This is the way to invoke a script with all the bells and

- **`_main_shell_completion(self, ctx_args, prog_name, complete_var)`** (Line 1481)
  - Returns: `None`
  - Check if the shell is asking for tab completion, process

- **`__call__(self, *args, **kwargs)`** (Line 1513)
  - Returns: `t.Any`
  - Alias for :meth:`main`.

##### Class: `_FakeSubclassCheck`

**Line:** 1518

**Documentation:** _No documentation_

**Methods:**

- **`__subclasscheck__(cls, subclass)`** (Line 1519)
  - Returns: `bool`
  - _No documentation_

- **`__instancecheck__(cls, instance)`** (Line 1522)
  - Returns: `bool`
  - _No documentation_

##### Class: `_BaseCommand`

**Line:** 1526

**Documentation:**

> .. deprecated:: 8.2
>     Will be removed in Click 9.0. Use ``Command`` instead.

##### Class: `Group`

**Line:** 1533

**Documentation:**

> A group is a command that nests other commands (or more groups).
> 
> :param name: The name of the group command.
> :param commands: Map names to :class:`Command` objects. Can be a list, which
>     will use :attr:`Command.name` as the keys.
> :param invoke_without_command: Invoke the group's callback even if a
>     subcommand is not given.
> :param no_args_is_help: If no arguments are given, show the group's help and
>     exit. Defaults to the opposite of ``invoke_without_command``.
> :param subcommand_metavar: How to represent the subcommand argument in help.
>     The default will represent whether ``chain`` is set or not.
> :param chain: Allow passing more than one subcommand argument. After parsing
>     a command's arguments, if any arguments remain another command will be
>     matched, and so on.
> :param result_callback: A function to call after the group's and
>     subcommand's callbacks. The value returned by the subcommand is passed.
>     If ``chain`` is enabled, the value will be a list of values returned by
>     all the commands. If ``invoke_without_command`` is enabled, the value
>     will be the value returned by the group's callback, or an empty list if
>     ``chain`` is enabled.
> :param kwargs: Other arguments passed to :class:`Command`.
> 
> .. versionchanged:: 8.0
>     The ``commands`` argument can be a list of command objects.
> 
> .. versionchanged:: 8.2
>     Merged with and replaces the ``MultiCommand`` base class.

**Methods:**

- **`__init__(self, name, commands, invoke_without_command, no_args_is_help, subcommand_metavar, chain, result_callback, **kwargs)`** (Line 1586)
  - Returns: `None`
  - _No documentation_

- **`to_info_dict(self, ctx)`** (Line 1634)
  - Returns: `dict[str, t.Any]`
  - _No documentation_

- **`add_command(self, cmd, name)`** (Line 1652)
  - Returns: `None`
  - Registers another :class:`Command` with this group.  If the name

- **`command(self, __func)`** (Line 1663)
  - Returns: `Command`
  - _No documentation_

- **`command(self, *args, **kwargs)`** (Line 1666)
  - Returns: `t.Callable[[t.Callable[..., t.Any]], Command]`
  - _No documentation_

- **`command(self, *args, **kwargs)`** (Line 1670)
  - Returns: `t.Callable[[t.Callable[..., t.Any]], Command] | Command`
  - A shortcut decorator for declaring and attaching a command to

- **`group(self, __func)`** (Line 1712)
  - Returns: `Group`
  - _No documentation_

- **`group(self, *args, **kwargs)`** (Line 1715)
  - Returns: `t.Callable[[t.Callable[..., t.Any]], Group]`
  - _No documentation_

- **`group(self, *args, **kwargs)`** (Line 1719)
  - Returns: `t.Callable[[t.Callable[..., t.Any]], Group] | Group`
  - A shortcut decorator for declaring and attaching a group to

- **`result_callback(self, replace)`** (Line 1763)
  - Returns: `t.Callable[[F], F]`
  - Adds a result callback to the command.  By default if a

- **`get_command(self, ctx, cmd_name)`** (Line 1808)
  - Returns: `Command | None`
  - Given a context and a command name, this returns a :class:`Command`

- **`list_commands(self, ctx)`** (Line 1814)
  - Returns: `list[str]`
  - Returns a list of subcommand names in the order they should appear.

- **`collect_usage_pieces(self, ctx)`** (Line 1818)
  - Returns: `list[str]`
  - _No documentation_

- **`format_options(self, ctx, formatter)`** (Line 1823)
  - Returns: `None`
  - _No documentation_

- **`format_commands(self, ctx, formatter)`** (Line 1827)
  - Returns: `None`
  - Extra format methods for multi methods that adds all the commands

- **`parse_args(self, ctx, args)`** (Line 1855)
  - Returns: `list[str]`
  - _No documentation_

- **`invoke(self, ctx)`** (Line 1869)
  - Returns: `t.Any`
  - _No documentation_

- **`resolve_command(self, ctx, args)`** (Line 1937)
  - Returns: `tuple[str | None, Command | None, list[str]]`
  - _No documentation_

- **`shell_complete(self, ctx, incomplete)`** (Line 1963)
  - Returns: `list[CompletionItem]`
  - Return a list of completions for the incomplete value. Looks

##### Class: `_MultiCommand`

**Line:** 1983

**Documentation:**

> .. deprecated:: 8.2
>     Will be removed in Click 9.0. Use ``Group`` instead.

##### Class: `CommandCollection`

**Line:** 1990

**Documentation:**

> A :class:`Group` that looks up subcommands on other groups. If a command
> is not found on this group, each registered source is checked in order.
> Parameters on a source are not added to this group, and a source's callback
> is not invoked when invoking its commands. In other words, this "flattens"
> commands in many groups into this one group.
> 
> :param name: The name of the group command.
> :param sources: A list of :class:`Group` objects to look up commands from.
> :param kwargs: Other arguments passed to :class:`Group`.
> 
> .. versionchanged:: 8.2
>     This is a subclass of ``Group``. Commands are looked up first on this
>     group, then each of its sources.

**Methods:**

- **`__init__(self, name, sources, **kwargs)`** (Line 2006)
  - Returns: `None`
  - _No documentation_

- **`add_source(self, group)`** (Line 2016)
  - Returns: `None`
  - Add a group as a source of commands.

- **`get_command(self, ctx, cmd_name)`** (Line 2020)
  - Returns: `Command | None`
  - _No documentation_

- **`list_commands(self, ctx)`** (Line 2037)
  - Returns: `list[str]`
  - _No documentation_

##### Class: `Parameter`

**Line:** 2056

**Documentation:**

> A parameter to a command comes in two versions: they are either
> :class:`Option`\s or :class:`Argument`\s.  Other subclasses are currently
> not supported by design as some of the internals for parsing are
> intentionally not finalized.
> 
> Some settings are supported by both options and arguments.
> 
> :param param_decls: the parameter declarations for this option or
>                     argument.  This is a list of flags or argument
>                     names.
> :param type: the type that should be used.  Either a :class:`ParamType`
>              or a Python type.  The latter is converted into the former
>              automatically if supported.
> :param required: controls if this is optional or not.
> :param default: the default value if omitted.  This can also be a callable,
>                 in which case it's invoked when the default is needed
>                 without any arguments.
> :param callback: A function to further process or validate the value
>     after type conversion. It is called as ``f(ctx, param, value)``
>     and must return the value. It is called for all sources,
>     including prompts.
> :param nargs: the number of arguments to match.  If not ``1`` the return
>               value is a tuple instead of single value.  The default for
>               nargs is ``1`` (except if the type is a tuple, then it's
>               the arity of the tuple). If ``nargs=-1``, all remaining
>               parameters are collected.
> :param metavar: how the value is represented in the help page.
> :param expose_value: if this is `True` then the value is passed onwards
>                      to the command callback and stored on the context,
>                      otherwise it's skipped.
> :param is_eager: eager values are processed before non eager ones.  This
>                  should not be set for arguments or it will inverse the
>                  order of processing.
> :param envvar: environment variable(s) that are used to provide a default value for
>     this parameter. This can be a string or a sequence of strings. If a sequence is
>     given, only the first non-empty environment variable is used for the parameter.
> :param shell_complete: A function that returns custom shell
>     completions. Used instead of the param's type completion if
>     given. Takes ``ctx, param, incomplete`` and must return a list
>     of :class:`~click.shell_completion.CompletionItem` or a list of
>     strings.
> :param deprecated: If ``True`` or non-empty string, issues a message
>                     indicating that the argument is deprecated and highlights
>                     its deprecation in --help. The message can be customized
>                     by using a string as the value. A deprecated parameter
>                     cannot be required, a ValueError will be raised otherwise.
> 
> .. versionchanged:: 8.2.0
>     Introduction of ``deprecated``.
> 
> .. versionchanged:: 8.2
>     Adding duplicate parameter names to a :class:`~click.core.Command` will
>     result in a ``UserWarning`` being shown.
> 
> .. versionchanged:: 8.2
>     Adding duplicate parameter names to a :class:`~click.core.Command` will
>     result in a ``UserWarning`` being shown.
> 
> .. versionchanged:: 8.0
>     ``process_value`` validates required parameters and bounded
>     ``nargs``, and invokes the parameter callback before returning
>     the value. This allows the callback to validate prompts.
>     ``full_process_value`` is removed.
> 
> .. versionchanged:: 8.0
>     ``autocompletion`` is renamed to ``shell_complete`` and has new
>     semantics described above. The old name is deprecated and will
>     be removed in 8.1, until then it will be wrapped to match the
>     new requirements.
> 
> .. versionchanged:: 8.0
>     For ``multiple=True, nargs>1``, the default must be a list of
>     tuples.
> 
> .. versionchanged:: 8.0
>     Setting a default is no longer required for ``nargs>1``, it will
>     default to ``None``. ``multiple=True`` or ``nargs=-1`` will
>     default to ``()``.
> 
> .. versionchanged:: 7.1
>     Empty environment variables are ignored rather than taking the
>     empty string value. This makes it possible for scripts to clear
>     variables if they can't unset them.
> 
> .. versionchanged:: 2.0
>     Changed signature for parameter callback to also be passed the
>     parameter. The old callback format will still work, but it will
>     raise a warning to give you a chance to migrate the code easier.

**Methods:**

- **`__init__(self, param_decls, type, required, default, callback, nargs, multiple, metavar, expose_value, is_eager, envvar, shell_complete, deprecated)`** (Line 2149)
  - Returns: `None`
  - _No documentation_

- **`to_info_dict(self)`** (Line 2220)
  - Returns: `dict[str, t.Any]`
  - Gather information that could be useful for a tool generating

- **`__repr__(self)`** (Line 2248)
  - Returns: `str`
  - _No documentation_

- **`_parse_decls(self, decls, expose_value)`** (Line 2252)
  - Returns: `tuple[str, list[str], list[str]]`
  - _No documentation_

- **`human_readable_name(self)`** (Line 2257)
  - Returns: `str`
  - Returns the human readable name of this parameter.  This is the

- **`make_metavar(self, ctx)`** (Line 2263)
  - Returns: `str`
  - _No documentation_

- **`get_default(self, ctx, call)`** (Line 2278)
  - Returns: `t.Any | None`
  - _No documentation_

- **`get_default(self, ctx, call)`** (Line 2283)
  - Returns: `t.Any | t.Callable[[], t.Any] | None`
  - _No documentation_

- **`get_default(self, ctx, call)`** (Line 2287)
  - Returns: `t.Any | t.Callable[[], t.Any] | None`
  - Get the default for the parameter. Tries

- **`add_to_parser(self, parser, ctx)`** (Line 2321)
  - Returns: `None`
  - _No documentation_

- **`consume_value(self, ctx, opts)`** (Line 2323)
  - Returns: `tuple[t.Any, ParameterSource]`
  - Returns the parameter value produced by the parser.

- **`type_cast_value(self, ctx, value)`** (Line 2371)
  - Returns: `t.Any`
  - Convert and validate a value against the parameter's

- **`value_is_missing(self, value)`** (Line 2427)
  - Returns: `bool`
  - A value is considered missing if:

- **`process_value(self, ctx, value)`** (Line 2445)
  - Returns: `t.Any`
  - Process the value of this parameter:

- **`resolve_envvar_value(self, ctx)`** (Line 2511)
  - Returns: `str | None`
  - Returns the value found in the environment variable(s) attached to this

- **`value_from_envvar(self, ctx)`** (Line 2556)
  - Returns: `str | cabc.Sequence[str] | None`
  - Process the raw environment variable string for this parameter.

- **`handle_parse_result(self, ctx, opts, args)`** (Line 2572)
  - Returns: `tuple[t.Any, list[str]]`
  - Process the value produced by the parser from user input.

- **`get_help_record(self, ctx)`** (Line 2633)
  - Returns: `tuple[str, str] | None`
  - _No documentation_

- **`get_usage_pieces(self, ctx)`** (Line 2636)
  - Returns: `list[str]`
  - _No documentation_

- **`get_error_hint(self, ctx)`** (Line 2639)
  - Returns: `str`
  - Get a stringified version of the param for use in error messages to

- **`shell_complete(self, ctx, incomplete)`** (Line 2649)
  - Returns: `list[CompletionItem]`
  - Return a list of completions for the incomplete value. If a

##### Class: `Option`

**Line:** 2673

**Documentation:**

> Options are usually optional values on the command line and
> have some extra features that arguments don't have.
> 
> All other parameters are passed onwards to the parameter constructor.
> 
> :param show_default: Show the default value for this option in its
>     help text. Values are not shown by default, unless
>     :attr:`Context.show_default` is ``True``. If this value is a
>     string, it shows that string in parentheses instead of the
>     actual value. This is particularly useful for dynamic options.
>     For single option boolean flags, the default remains hidden if
>     its value is ``False``.
> :param show_envvar: Controls if an environment variable should be
>     shown on the help page and error messages.
>     Normally, environment variables are not shown.
> :param prompt: If set to ``True`` or a non empty string then the
>     user will be prompted for input. If set to ``True`` the prompt
>     will be the option name capitalized. A deprecated option cannot be
>     prompted.
> :param confirmation_prompt: Prompt a second time to confirm the
>     value if it was prompted for. Can be set to a string instead of
>     ``True`` to customize the message.
> :param prompt_required: If set to ``False``, the user will be
>     prompted for input only when the option was specified as a flag
>     without a value.
> :param hide_input: If this is ``True`` then the input on the prompt
>     will be hidden from the user. This is useful for password input.
> :param is_flag: forces this option to act as a flag.  The default is
>                 auto detection.
> :param flag_value: which value should be used for this flag if it's
>                    enabled.  This is set to a boolean automatically if
>                    the option string contains a slash to mark two options.
> :param multiple: if this is set to `True` then the argument is accepted
>                  multiple times and recorded.  This is similar to ``nargs``
>                  in how it works but supports arbitrary number of
>                  arguments.
> :param count: this flag makes an option increment an integer.
> :param allow_from_autoenv: if this is enabled then the value of this
>                            parameter will be pulled from an environment
>                            variable in case a prefix is defined on the
>                            context.
> :param help: the help string.
> :param hidden: hide this option from help outputs.
> :param attrs: Other command arguments described in :class:`Parameter`.
> 
> .. versionchanged:: 8.4
>     Non-basic ``flag_value`` types (not ``str``, ``int``, ``float``, or
>     ``bool``) are passed through unchanged instead of being stringified.
>     Previously, ``type=click.UNPROCESSED`` was required to preserve them.
> 
> .. versionchanged:: 8.2
>     ``envvar`` used with ``flag_value`` will always use the ``flag_value``,
>     previously it would use the value of the environment variable.
> 
> .. versionchanged:: 8.1
>     Help text indentation is cleaned here instead of only in the
>     ``@option`` decorator.
> 
> .. versionchanged:: 8.1
>     The ``show_default`` parameter overrides
>     ``Context.show_default``.
> 
> .. versionchanged:: 8.1
>     The default of a single option boolean flag is not shown if the
>     default value is ``False``.
> 
> .. versionchanged:: 8.0.1
>     ``type`` is detected from ``flag_value`` if given, for basic Python
>     types (``str``, ``int``, ``float``, ``bool``).

**Methods:**

- **`__init__(self, param_decls, show_default, prompt, confirmation_prompt, prompt_required, hide_input, is_flag, flag_value, multiple, count, allow_from_autoenv, type, help, hidden, show_choices, show_envvar, deprecated, **attrs)`** (Line 2747)
  - Returns: `None`
  - _No documentation_

- **`to_info_dict(self)`** (Line 2918)
  - Returns: `dict[str, t.Any]`
  - .. versionchanged:: 8.3.0

- **`get_default(self, ctx, call)`** (Line 2937)
  - Returns: `t.Any | t.Callable[[], t.Any] | None`
  - Return the default value for this option.

- **`get_error_hint(self, ctx)`** (Line 2970)
  - Returns: `str`
  - _No documentation_

- **`_parse_decls(self, decls, expose_value)`** (Line 2976)
  - Returns: `tuple[str, list[str], list[str]]`
  - _No documentation_

- **`add_to_parser(self, parser, ctx)`** (Line 3031)
  - Returns: `None`
  - _No documentation_

- **`get_help_record(self, ctx)`** (Line 3070)
  - Returns: `tuple[str, str] | None`
  - _No documentation_

- **`get_help_extra(self, ctx)`** (Line 3115)
  - Returns: `types.OptionHelpExtra`
  - _No documentation_

- **`prompt_for_value(self, ctx)`** (Line 3199)
  - Returns: `t.Any`
  - This is an alternative flow that can be activated in the full

- **`resolve_envvar_value(self, ctx)`** (Line 3249)
  - Returns: `str | None`
  - :class:`Option` resolves its environment variable the same way as

- **`value_from_envvar(self, ctx)`** (Line 3273)
  - Returns: `t.Any`
  - For :class:`Option`, this method processes the raw environment variable

- **`consume_value(self, ctx, opts)`** (Line 3315)
  - Returns: `tuple[t.Any, ParameterSource]`
  - For :class:`Option`, the value can be collected from an interactive prompt

- **`process_value(self, ctx, value)`** (Line 3376)
  - Returns: `t.Any`
  - _No documentation_

##### Class: `Argument`

**Line:** 3394

**Documentation:**

> Arguments are positional parameters to a command.  They generally
> provide fewer features than options but can have infinite ``nargs``
> and are required by default.
> 
> All parameters are passed onwards to the constructor of :class:`Parameter`.

**Methods:**

- **`__init__(self, param_decls, required, **attrs)`** (Line 3404)
  - Returns: `None`
  - _No documentation_

- **`human_readable_name(self)`** (Line 3426)
  - Returns: `str`
  - _No documentation_

- **`make_metavar(self, ctx)`** (Line 3431)
  - Returns: `str`
  - _No documentation_

- **`_parse_decls(self, decls, expose_value)`** (Line 3445)
  - Returns: `tuple[str, list[str], list[str]]`
  - _No documentation_

- **`get_usage_pieces(self, ctx)`** (Line 3462)
  - Returns: `list[str]`
  - _No documentation_

- **`get_error_hint(self, ctx)`** (Line 3465)
  - Returns: `str`
  - _No documentation_

- **`add_to_parser(self, parser, ctx)`** (Line 3470)
  - Returns: `None`
  - _No documentation_

---

### `C:\Users\I.C.T\OneDrive\Documents\git\click\src\click\decorators.py`

**Language:** python

#### Functions

##### `pass_context(f)`

**Line:** 28 | **Returns:** `t.Callable[P, R]`

**Parameters:**
- `f` (t.Callable[te.Concatenate[Context, P], R])

**Documentation:**

> Marks a callback as wanting to receive the current context
> object as first argument.

##### `pass_obj(f)`

**Line:** 39 | **Returns:** `t.Callable[P, R]`

**Parameters:**
- `f` (t.Callable[te.Concatenate[T, P], R])

**Documentation:**

> Similar to :func:`pass_context`, but only pass the object on the
> context onwards (:attr:`Context.obj`).  This is useful if that object
> represents the state of a nested system.

##### `make_pass_decorator(object_type, ensure)`

**Line:** 51 | **Returns:** `t.Callable[[t.Callable[te.Concatenate[T, P], R]], t.Callable[P, R]]`

**Parameters:**
- `object_type` (type[T])
- `ensure` (bool)

**Documentation:**

> Given an object type this creates a decorator that will work
> similar to :func:`pass_obj` but instead of passing the object of the
> current context, it will find the innermost context of type
> :func:`object_type`.
> 
> This generates a decorator that works roughly like this::
> 
>     from functools import update_wrapper
> 
>     def decorator(f):
>         @pass_context
>         def new_func(ctx, *args, **kwargs):
>             obj = ctx.find_object(object_type)
>             return ctx.invoke(f, obj, *args, **kwargs)
>         return update_wrapper(new_func, f)
>     return decorator
> 
> :param object_type: the type of the object to pass.
> :param ensure: if set to `True`, a new object will be created and
>                remembered on the context if it's not there yet.

##### `pass_meta_key(key)`

**Line:** 100 | **Returns:** `t.Callable[[t.Callable[te.Concatenate[T, P], R]], t.Callable[P, R]]`

**Parameters:**
- `key` (str)

**Documentation:**

> Create a decorator that passes a key from
> :attr:`click.Context.meta` as the first argument to the decorated
> function.
> 
> :param key: Key in ``Context.meta`` to pass.
> :param doc_description: Description of the object being passed,
>     inserted into the decorator's docstring. Defaults to "the 'key'
>     key from Context.meta".
> 
> .. versionadded:: 8.0

##### `command(name)`

**Line:** 138 | **Returns:** `Command`

**Parameters:**
- `name` (_AnyCallable)

**Documentation:** _No documentation_

##### `command(name, cls, **attrs)`

**Line:** 144 | **Returns:** `t.Callable[[_AnyCallable], CmdType]`

**Parameters:**
- `name` (str | None)
- `cls` (type[CmdType])
- `**attrs` (t.Any)

**Documentation:** _No documentation_

##### `command(name, **attrs)`

**Line:** 153 | **Returns:** `t.Callable[[_AnyCallable], CmdType]`

**Parameters:**
- `name` (None)
- `**attrs` (t.Any)

**Documentation:** _No documentation_

##### `command(name, cls, **attrs)`

**Line:** 163 | **Returns:** `t.Callable[[_AnyCallable], Command]`

**Parameters:**
- `name` (str | None)
- `cls` (None)
- `**attrs` (t.Any)

**Documentation:** _No documentation_

##### `command(name, cls, **attrs)`

**Line:** 168 | **Returns:** `Command | t.Callable[[_AnyCallable], Command | CmdType]`

**Parameters:**
- `name` (str | _AnyCallable | None)
- `cls` (type[CmdType] | None)
- `**attrs` (t.Any)

**Documentation:**

> Creates a new :class:`Command` and uses the decorated function as
> callback.  This will also automatically attach all decorated
> :func:`option`\s and :func:`argument`\s as parameters to the command.
> 
> The name of the command defaults to the name of the function, converted to
> lowercase, with underscores ``_`` replaced by dashes ``-``, and the suffixes
> ``_command``, ``_cmd``, ``_group``, and ``_grp`` are removed. For example,
> ``init_data_command`` becomes ``init-data``.
> 
> All keyword arguments are forwarded to the underlying command class.
> For the ``params`` argument, any decorated params are appended to
> the end of the list.
> 
> Once decorated the function turns into a :class:`Command` instance
> that can be invoked as a command line utility or be attached to a
> command :class:`Group`.
> 
> :param name: The name of the command. Defaults to modifying the function's
>     name as described above.
> :param cls: The command class to create. Defaults to :class:`Command`.
> 
> .. versionchanged:: 8.2
>     The suffixes ``_command``, ``_cmd``, ``_group``, and ``_grp`` are
>     removed when generating the name.
> 
> .. versionchanged:: 8.1
>     This decorator can be applied without parentheses.
> 
> .. versionchanged:: 8.1
>     The ``params`` argument can be used. Decorated params are
>     appended to the end of the list.

##### `group(name)`

**Line:** 263 | **Returns:** `Group`

**Parameters:**
- `name` (_AnyCallable)

**Documentation:** _No documentation_

##### `group(name, cls, **attrs)`

**Line:** 269 | **Returns:** `t.Callable[[_AnyCallable], GrpType]`

**Parameters:**
- `name` (str | None)
- `cls` (type[GrpType])
- `**attrs` (t.Any)

**Documentation:** _No documentation_

##### `group(name, **attrs)`

**Line:** 278 | **Returns:** `t.Callable[[_AnyCallable], GrpType]`

**Parameters:**
- `name` (None)
- `**attrs` (t.Any)

**Documentation:** _No documentation_

##### `group(name, cls, **attrs)`

**Line:** 288 | **Returns:** `t.Callable[[_AnyCallable], Group]`

**Parameters:**
- `name` (str | None)
- `cls` (None)
- `**attrs` (t.Any)

**Documentation:** _No documentation_

##### `group(name, cls, **attrs)`

**Line:** 293 | **Returns:** `Group | t.Callable[[_AnyCallable], Group | GrpType]`

**Parameters:**
- `name` (str | _AnyCallable | None)
- `cls` (type[GrpType] | None)
- `**attrs` (t.Any)

**Documentation:**

> Creates a new :class:`Group` with a function as callback.  This
> works otherwise the same as :func:`command` just that the `cls`
> parameter is set to :class:`Group`.
> 
> .. versionchanged:: 8.1
>     This decorator can be applied without parentheses.

##### `_param_memo(f, param)`

**Line:** 314 | **Returns:** `None`

**Parameters:**
- `f` (t.Callable[..., t.Any])
- `param` (Parameter)

**Documentation:** _No documentation_

##### `argument(*param_decls, **attrs)`

**Line:** 324 | **Returns:** `t.Callable[[FC], FC]`

**Parameters:**
- `*param_decls` (str)
- `**attrs` (t.Any)

**Documentation:**

> Attaches an argument to the command.  All positional arguments are
> passed as parameter declarations to :class:`Argument`; all keyword
> arguments are forwarded unchanged (except ``cls``).
> This is equivalent to creating an :class:`Argument` instance manually
> and attaching it to the :attr:`Command.params` list.
> 
> For the default argument class, refer to :class:`Argument` and
> :class:`Parameter` for descriptions of parameters.
> 
> :param cls: the argument class to instantiate.  This defaults to
>             :class:`Argument`.
> :param param_decls: Passed as positional arguments to the constructor of
>     ``cls``.
> :param attrs: Passed as keyword arguments to the constructor of ``cls``.

##### `option(*param_decls, **attrs)`

**Line:** 352 | **Returns:** `t.Callable[[FC], FC]`

**Parameters:**
- `*param_decls` (str)
- `**attrs` (t.Any)

**Documentation:**

> Attaches an option to the command.  All positional arguments are
> passed as parameter declarations to :class:`Option`; all keyword
> arguments are forwarded unchanged (except ``cls``).
> This is equivalent to creating an :class:`Option` instance manually
> and attaching it to the :attr:`Command.params` list.
> 
> For the default option class, refer to :class:`Option` and
> :class:`Parameter` for descriptions of parameters.
> 
> :param cls: the option class to instantiate.  This defaults to
>             :class:`Option`.
> :param param_decls: Passed as positional arguments to the constructor of
>     ``cls``.
> :param attrs: Passed as keyword arguments to the constructor of ``cls``.

##### `confirmation_option(*param_decls, **kwargs)`

**Line:** 380 | **Returns:** `t.Callable[[FC], FC]`

**Parameters:**
- `*param_decls` (str)
- `**kwargs` (t.Any)

**Documentation:**

> Add a ``--yes`` option which shows a prompt before continuing if
> not passed. If the prompt is declined, the program will exit.
> 
> :param param_decls: One or more option names. Defaults to the single
>     value ``"--yes"``.
> :param kwargs: Extra arguments are passed to :func:`option`.

##### `password_option(*param_decls, **kwargs)`

**Line:** 404 | **Returns:** `t.Callable[[FC], FC]`

**Parameters:**
- `*param_decls` (str)
- `**kwargs` (t.Any)

**Documentation:**

> Add a ``--password`` option which prompts for a password, hiding
> input and asking to enter the value again for confirmation.
> 
> :param param_decls: One or more option names. Defaults to the single
>     value ``"--password"``.
> :param kwargs: Extra arguments are passed to :func:`option`.

##### `version_option(version, *param_decls, **kwargs)`

**Line:** 421 | **Returns:** `t.Callable[[FC], FC]`

**Parameters:**
- `version` (str | None)
- `*param_decls` (str)
- `**kwargs` (t.Any)

**Documentation:**

> Add a ``--version`` option which immediately prints the version
> number and exits the program.
> 
> If ``version`` is not provided, Click will try to detect it using
> :func:`importlib.metadata.version` to get the version for the
> ``package_name``.
> 
> If ``package_name`` is not provided, Click will try to detect it by
> inspecting the stack frames. This will be used to detect the
> version, so it must match the name of the installed package.
> 
> :param version: The version number to show. If not provided, Click
>     will try to detect it.
> :param param_decls: One or more option names. Defaults to the single
>     value ``"--version"``.
> :param package_name: The package name to detect the version from. If
>     not provided, Click will try to detect it.
> :param prog_name: The name of the CLI to show in the message. If not
>     provided, it will be detected from the command.
> :param message: The message to show. The values ``%(prog)s``,
>     ``%(package)s``, and ``%(version)s`` are available. Defaults to
>     ``"%(prog)s, version %(version)s"``.
> :param kwargs: Extra arguments are passed to :func:`option`.
> :raise RuntimeError: ``version`` could not be detected.
> 
> .. versionchanged:: 8.0
>     Add the ``package_name`` parameter, and the ``%(package)s``
>     value for messages.
> 
> .. versionchanged:: 8.0
>     Use :mod:`importlib.metadata` instead of ``pkg_resources``. The
>     version is detected based on the package name, not the entry
>     point name. The Python package name must match the installed
>     package name, or be passed with ``package_name=``.

##### `help_option(*param_decls, **kwargs)`

**Line:** 527 | **Returns:** `t.Callable[[FC], FC]`

**Parameters:**
- `*param_decls` (str)
- `**kwargs` (t.Any)

**Documentation:**

> Pre-configured ``--help`` option which immediately prints the help page
> and exits the program.
> 
> :param param_decls: One or more option names. Defaults to the single
>     value ``"--help"``.
> :param kwargs: Extra arguments are passed to :func:`option`.

---

### `C:\Users\I.C.T\OneDrive\Documents\git\click\src\click\exceptions.py`

**Language:** python

#### Functions

##### `_join_param_hints(param_hint)`

**Line:** 19 | **Returns:** `str | None`

**Parameters:**
- `param_hint` (cabc.Sequence[str] | str | None)

**Documentation:** _No documentation_

##### `_format_possibilities(possibilities)`

**Line:** 26 | **Returns:** `str`

**Parameters:**
- `possibilities` (list[str])

**Documentation:** _No documentation_

#### Classes

##### Class: `ClickException`

**Line:** 35

**Documentation:**

> An exception that Click can handle and show to the user.

**Methods:**

- **`__init__(self, message)`** (Line 41)
  - Returns: `None`
  - _No documentation_

- **`format_message(self)`** (Line 48)
  - Returns: `str`
  - _No documentation_

- **`__str__(self)`** (Line 51)
  - Returns: `str`
  - _No documentation_

- **`show(self, file)`** (Line 54)
  - Returns: `None`
  - _No documentation_

##### Class: `UsageError`

**Line:** 65

**Documentation:**

> An internal exception that signals a usage error.  This typically
> aborts any further handling.
> 
> :param message: the error message to display.
> :param ctx: optionally the context that caused this error.  Click will
>             fill in the context automatically in some situations.

**Methods:**

- **`__init__(self, message, ctx)`** (Line 76)
  - Returns: `None`
  - _No documentation_

- **`show(self, file)`** (Line 81)
  - Returns: `None`
  - _No documentation_

##### Class: `BadParameter`

**Line:** 108

**Documentation:**

> An exception that formats out a standardized error message for a
> bad parameter.  This is useful when thrown from a callback or type as
> Click will attach contextual information to it (for instance, which
> parameter it is).
> 
> .. versionadded:: 2.0
> 
> :param param: the parameter object that caused this error.  This can
>               be left out, and Click will attach this info itself
>               if possible.
> :param param_hint: a string that shows up as parameter name.  This
>                    can be used as alternative to `param` in cases
>                    where custom validation should happen.  If it is
>                    a string it's used as such, if it's a list then
>                    each item is quoted and separated.

**Methods:**

- **`__init__(self, message, ctx, param, param_hint)`** (Line 126)
  - Returns: `None`
  - _No documentation_

- **`format_message(self)`** (Line 137)
  - Returns: `str`
  - _No documentation_

##### Class: `MissingParameter`

**Line:** 150

**Documentation:**

> Raised if click required an option or argument but it was not
> provided when invoking the script.
> 
> .. versionadded:: 4.0
> 
> :param param_type: a string that indicates the type of the parameter.
>                    The default is to inherit the parameter type from
>                    the given `param`.  Valid values are ``'parameter'``,
>                    ``'option'`` or ``'argument'``.

**Methods:**

- **`__init__(self, message, ctx, param, param_hint, param_type)`** (Line 162)
  - Returns: `None`
  - _No documentation_

- **`format_message(self)`** (Line 173)
  - Returns: `str`
  - _No documentation_

- **`__str__(self)`** (Line 213)
  - Returns: `str`
  - _No documentation_

##### Class: `NoSuchOption`

**Line:** 221

**Documentation:**

> Raised if Click attempted to handle an option that does not exist.
> 
> .. versionadded:: 4.0

**Methods:**

- **`__init__(self, option_name, message, possibilities, ctx)`** (Line 227)
  - Returns: `None`
  - _No documentation_

- **`format_message(self)`** (Line 245)
  - Returns: `str`
  - _No documentation_

##### Class: `NoSuchCommand`

**Line:** 251

**Documentation:**

> Raised if Click attempted to handle a command that does not exist.

**Methods:**

- **`__init__(self, command_name, message, possibilities, ctx)`** (Line 254)
  - Returns: `None`
  - _No documentation_

- **`format_message(self)`** (Line 272)
  - Returns: `str`
  - _No documentation_

##### Class: `BadOptionUsage`

**Line:** 278

**Documentation:**

> Raised if an option is generally supplied but the use of the option
> was incorrect.  This is for instance raised if the number of arguments
> for an option is not correct.
> 
> .. versionadded:: 4.0
> 
> :param option_name: the name of the option being used incorrectly.

**Methods:**

- **`__init__(self, option_name, message, ctx)`** (Line 288)
  - Returns: `None`
  - _No documentation_

##### Class: `BadArgumentUsage`

**Line:** 295

**Documentation:**

> Raised if an argument is generally supplied but the use of the argument
> was incorrect.  This is for instance raised if the number of values
> for an argument is not correct.
> 
> .. versionadded:: 6.0

##### Class: `NoArgsIsHelpError`

**Line:** 304

**Documentation:** _No documentation_

**Methods:**

- **`__init__(self, ctx)`** (Line 305)
  - Returns: `None`
  - _No documentation_

- **`show(self, file)`** (Line 309)
  - Returns: `None`
  - _No documentation_

##### Class: `FileError`

**Line:** 313

**Documentation:**

> Raised if a file cannot be opened.

**Methods:**

- **`__init__(self, filename, hint)`** (Line 316)
  - Returns: `None`
  - _No documentation_

- **`format_message(self)`** (Line 324)
  - Returns: `str`
  - _No documentation_

##### Class: `Abort`

**Line:** 330

**Documentation:**

> An internal signalling exception that signals Click to abort.

##### Class: `Exit`

**Line:** 334

**Documentation:**

> An exception that indicates that the application should exit with some
> status code.
> 
> :param code: the status code to exit with.

**Methods:**

- **`__init__(self, code)`** (Line 343)
  - Returns: `None`
  - _No documentation_

---

### `C:\Users\I.C.T\OneDrive\Documents\git\click\src\click\formatting.py`

**Language:** python

#### Functions

##### `measure_table(rows)`

**Line:** 14 | **Returns:** `tuple[int, ...]`

**Parameters:**
- `rows` (cabc.Iterable[tuple[str, str]])

**Documentation:** _No documentation_

##### `iter_rows(rows, col_count)`

**Line:** 24 | **Returns:** `cabc.Iterator[tuple[str, ...]]`

**Parameters:**
- `rows` (cabc.Iterable[tuple[str, str]])
- `col_count` (int)

**Documentation:** _No documentation_

##### `wrap_text(text, width, initial_indent, subsequent_indent, preserve_paragraphs)`

**Line:** 31 | **Returns:** `str`

**Parameters:**
- `text` (str)
- `width` (int)
- `initial_indent` (str)
- `subsequent_indent` (str)
- `preserve_paragraphs` (bool)

**Documentation:**

> A helper function that intelligently wraps text.  By default, it
> assumes that it operates on a single paragraph of text but if the
> `preserve_paragraphs` parameter is provided it will intelligently
> handle paragraphs (defined by two empty lines).
> 
> If paragraphs are handled, a paragraph can be prefixed with an empty
> line containing the ``\b`` character (``\x08``) to indicate that
> no rewrapping should happen in that block.
> 
> :param text: the text that should be rewrapped.
> :param width: the maximum width for the text.
> :param initial_indent: the initial indent that should be placed on the
>                        first line as a string.
> :param subsequent_indent: the indent string that should be placed on
>                           each consecutive line.
> :param preserve_paragraphs: if this flag is set then the wrapping will
>                             intelligently handle paragraphs.

##### `join_options(options)`

**Line:** 283 | **Returns:** `tuple[str, bool]`

**Parameters:**
- `options` (cabc.Sequence[str])

**Documentation:**

> Given a list of option strings this joins them in the most appropriate
> way and returns them in the form ``(formatted_string,
> any_prefix_is_slash)`` where the second item in the tuple is a flag that
> indicates if any of the option prefixes was a slash.

#### Classes

##### Class: `HelpFormatter`

**Line:** 104

**Documentation:**

> This class helps with formatting text-based help pages.  It's
> usually just needed for very special internal cases, but it's also
> exposed so that developers can write their own fancy outputs.
> 
> At present, it always writes into memory.
> 
> :param indent_increment: the additional increment for each level.
> :param width: the width for the text.  This defaults to the terminal
>               width clamped to a maximum of 78.

**Methods:**

- **`__init__(self, indent_increment, width, max_width)`** (Line 116)
  - Returns: `None`
  - _No documentation_

- **`write(self, string)`** (Line 135)
  - Returns: `None`
  - Writes a unicode string into the internal buffer.

- **`indent(self)`** (Line 139)
  - Returns: `None`
  - Increases the indentation.

- **`dedent(self)`** (Line 143)
  - Returns: `None`
  - Decreases the indentation.

- **`write_usage(self, prog, args, prefix)`** (Line 147)
  - Returns: `None`
  - Writes a usage line into the buffer.

- **`write_heading(self, heading)`** (Line 185)
  - Returns: `None`
  - Writes a heading into the buffer.

- **`write_paragraph(self)`** (Line 189)
  - Returns: `None`
  - Writes a paragraph into the buffer.

- **`write_text(self, text)`** (Line 194)
  - Returns: `None`
  - Writes re-indented text into the buffer.  This rewraps and

- **`write_dl(self, rows, col_max, col_spacing)`** (Line 210)
  - Returns: `None`
  - Writes a definition list into the buffer.  This is how options

- **`section(self, name)`** (Line 255)
  - Returns: `cabc.Iterator[None]`
  - Helpful context manager that writes a paragraph, a heading,

- **`indentation(self)`** (Line 270)
  - Returns: `cabc.Iterator[None]`
  - A context manager that increases the indentation.

- **`getvalue(self)`** (Line 278)
  - Returns: `str`
  - Returns the buffer contents.

---

### `C:\Users\I.C.T\OneDrive\Documents\git\click\src\click\globals.py`

**Language:** python

#### Functions

##### `get_current_context(silent)`

**Line:** 13 | **Returns:** `Context`

**Parameters:**
- `silent` (t.Literal[False])

**Documentation:** _No documentation_

##### `get_current_context(silent)`

**Line:** 17 | **Returns:** `Context | None`

**Parameters:**
- `silent` (bool)

**Documentation:** _No documentation_

##### `get_current_context(silent)`

**Line:** 20 | **Returns:** `Context | None`

**Parameters:**
- `silent` (bool)

**Documentation:**

> Returns the current click context.  This can be used as a way to
> access the current context object from anywhere.  This is a more implicit
> alternative to the :func:`pass_context` decorator.  This function is
> primarily useful for helpers such as :func:`echo` which might be
> interested in changing its behavior based on the current context.
> 
> To push the current context, :meth:`Context.scope` can be used.
> 
> .. versionadded:: 5.0
> 
> :param silent: if set to `True` the return value is `None` if no context
>                is available.  The default behavior is to raise a
>                :exc:`RuntimeError`.

##### `push_context(ctx)`

**Line:** 44 | **Returns:** `None`

**Parameters:**
- `ctx` (Context)

**Documentation:**

> Pushes a new context to the current stack.

##### `pop_context()`

**Line:** 49 | **Returns:** `None`

**Documentation:**

> Removes the top level from the stack.

##### `resolve_color_default(color)`

**Line:** 54 | **Returns:** `bool | None`

**Parameters:**
- `color` (bool | None)

**Documentation:**

> Internal helper to get the default value of the color flag.  If a
> value is passed it's returned unchanged, otherwise it's looked up from
> the current context.

---

### `C:\Users\I.C.T\OneDrive\Documents\git\click\src\click\parser.py`

**Language:** python

#### Functions

##### `_unpack_args(args, nargs_spec)`

**Line:** 51 | **Returns:** `tuple[cabc.Sequence[str | cabc.Sequence[str | None] | None], list[str]]`

**Parameters:**
- `args` (cabc.Sequence[str])
- `nargs_spec` (cabc.Sequence[int])

**Documentation:**

> Given an iterable of arguments and an iterable of nargs specifications,
> it returns a tuple with all the unpacked arguments at the first index
> and all remaining arguments as the second.
> 
> The nargs specification is the number of arguments that should be consumed
> or `-1` to indicate that this position should eat up all the remainders.
> 
> Missing items are filled with ``UNSET``.

##### `_split_opt(opt)`

**Line:** 111 | **Returns:** `tuple[str, str]`

**Parameters:**
- `opt` (str)

**Documentation:** _No documentation_

##### `_normalize_opt(opt, ctx)`

**Line:** 120 | **Returns:** `str`

**Parameters:**
- `opt` (str)
- `ctx` (Context | None)

**Documentation:** _No documentation_

##### `__getattr__(name)`

**Line:** 499 | **Returns:** `object`

**Parameters:**
- `name` (str)

**Documentation:** _No documentation_

#### Classes

##### Class: `_Option`

**Line:** 127

**Documentation:** _No documentation_

**Methods:**

- **`__init__(self, obj, opts, dest, action, nargs, const)`** (Line 128)
  - Returns: `None`
  - _No documentation_

- **`takes_value(self)`** (Line 162)
  - Returns: `bool`
  - _No documentation_

- **`process(self, value, state)`** (Line 165)
  - Returns: `None`
  - _No documentation_

##### Class: `_Argument`

**Line:** 181

**Documentation:** _No documentation_

**Methods:**

- **`__init__(self, obj, dest, nargs)`** (Line 182)
  - Returns: `None`
  - _No documentation_

- **`process(self, value, state)`** (Line 187)
  - Returns: `None`
  - _No documentation_

##### Class: `_ParsingState`

**Line:** 212

**Documentation:** _No documentation_

**Methods:**

- **`__init__(self, rargs)`** (Line 213)
  - Returns: `None`
  - _No documentation_

##### Class: `_OptionParser`

**Line:** 220

**Documentation:**

> The option parser is an internal class that is ultimately used to
> parse options and arguments.  It's modelled after optparse and brings
> a similar but vastly simplified API.  It should generally not be used
> directly as the high level Click classes wrap it for you.
> 
> It's not nearly as extensible as optparse or argparse as it does not
> implement features that are implemented on a higher level (such as
> types or defaults).
> 
> :param ctx: optionally the :class:`~click.Context` where this parser
>             should go with.
> 
> .. deprecated:: 8.2
>     Will be removed in Click 9.0.

**Methods:**

- **`__init__(self, ctx)`** (Line 237)
  - Returns: `None`
  - _No documentation_

- **`add_option(self, obj, opts, dest, action, nargs, const)`** (Line 261)
  - Returns: `None`
  - Adds a new option named `dest` to the parser.  The destination

- **`add_argument(self, obj, dest, nargs)`** (Line 286)
  - Returns: `None`
  - Adds a positional argument named `dest` to the parser.

- **`parse_args(self, args)`** (Line 294)
  - Returns: `tuple[dict[str, t.Any], list[str], list[CoreParameter]]`
  - Parses positional arguments and returns ``(values, args, order)``

- **`_process_args_for_args(self, state)`** (Line 312)
  - Returns: `None`
  - _No documentation_

- **`_process_args_for_options(self, state)`** (Line 323)
  - Returns: `None`
  - _No documentation_

- **`_match_long_opt(self, opt, explicit_value, state)`** (Line 359)
  - Returns: `None`
  - _No documentation_

- **`_match_short_opt(self, arg, state)`** (Line 386)
  - Returns: `None`
  - _No documentation_

- **`_get_value_from_state(self, option_name, option, state)`** (Line 426)
  - Returns: `str | cabc.Sequence[str] | T_FLAG_NEEDS_VALUE`
  - _No documentation_

- **`_process_opts(self, arg, state)`** (Line 466)
  - Returns: `None`
  - _No documentation_

---

### `C:\Users\I.C.T\OneDrive\Documents\git\click\src\click\shell_completion.py`

**Language:** python

#### Functions

##### `shell_complete(cli, ctx_args, prog_name, complete_var, instruction)`

**Line:** 19 | **Returns:** `int`

**Parameters:**
- `cli` (Command)
- `ctx_args` (cabc.MutableMapping[str, t.Any])
- `prog_name` (str)
- `complete_var` (str)
- `instruction` (str)

**Documentation:**

> Perform shell completion for the given CLI program.
> 
> :param cli: Command being called.
> :param ctx_args: Extra arguments to pass to
>     ``cli.make_context``.
> :param prog_name: Name of the executable in the shell.
> :param complete_var: Name of the environment variable that holds
>     the completion instruction.
> :param instruction: Value of ``complete_var`` with the completion
>     instruction and shell, in the form ``instruction_shell``.
> :return: Status code to exit with.

##### `add_completion_class(cls, name)`

**Line:** 449 | **Returns:** `ShellCompleteType`

**Parameters:**
- `cls` (ShellCompleteType)
- `name` (str | None)

**Documentation:**

> Register a :class:`ShellComplete` subclass under the given name.
> The name will be provided by the completion instruction environment
> variable during completion.
> 
> :param cls: The completion class that will handle completion for the
>     shell.
> :param name: Name to register the class under. Defaults to the
>     class's ``name`` attribute.

##### `get_completion_class(shell)`

**Line:** 469 | **Returns:** `type[ShellComplete] | None`

**Parameters:**
- `shell` (str)

**Documentation:**

> Look up a registered :class:`ShellComplete` subclass by the name
> provided by the completion instruction environment variable. If the
> name isn't registered, returns ``None``.
> 
> :param shell: Name the class is registered under.

##### `split_arg_string(string)`

**Line:** 479 | **Returns:** `list[str]`

**Parameters:**
- `string` (str)

**Documentation:**

> Split an argument string as with :func:`shlex.split`, but don't
> fail if the string is incomplete. Ignores a missing closing quote or
> incomplete escape sequence and uses the partial token as-is.
> 
> .. code-block:: python
> 
>     split_arg_string("example 'my file")
>     ["example", "my file"]
> 
>     split_arg_string("example my\")
>     ["example", "my"]
> 
> :param string: String to split.
> 
> .. versionchanged:: 8.2
>     Moved to ``shell_completion`` from ``parser``.

##### `_is_incomplete_argument(ctx, param)`

**Line:** 516 | **Returns:** `bool`

**Parameters:**
- `ctx` (Context)
- `param` (Parameter)

**Documentation:**

> Determine if the given parameter is an argument that can still
> accept values.
> 
> :param ctx: Invocation context for the command represented by the
>     parsed complete args.
> :param param: Argument object being checked.

##### `_start_of_option(ctx, value)`

**Line:** 539 | **Returns:** `bool`

**Parameters:**
- `ctx` (Context)
- `value` (str)

**Documentation:**

> Check if the value looks like the start of an option.

##### `_is_incomplete_option(ctx, args, param)`

**Line:** 548 | **Returns:** `bool`

**Parameters:**
- `ctx` (Context)
- `args` (list[str])
- `param` (Parameter)

**Documentation:**

> Determine if the given parameter is an option that needs a value.
> 
> :param args: List of complete args before the incomplete value.
> :param param: Option object being checked.

##### `_resolve_context(cli, ctx_args, prog_name, args)`

**Line:** 573 | **Returns:** `Context`

**Parameters:**
- `cli` (Command)
- `ctx_args` (cabc.MutableMapping[str, t.Any])
- `prog_name` (str)
- `args` (list[str])

**Documentation:**

> Produce the context hierarchy starting with the command and
> traversing the complete arguments. This only follows the commands,
> it doesn't trigger input prompts or callbacks.
> 
> :param cli: Command being called.
> :param prog_name: Name of the executable in the shell.
> :param args: List of complete args before the incomplete value.

##### `_resolve_incomplete(ctx, args, incomplete)`

**Line:** 634 | **Returns:** `tuple[Command | Parameter, str]`

**Parameters:**
- `ctx` (Context)
- `args` (list[str])
- `incomplete` (str)

**Documentation:**

> Find the Click object that will handle the completion of the
> incomplete value. Return the object and the incomplete value.
> 
> :param ctx: Invocation context for the command represented by
>     the parsed complete args.
> :param args: List of complete args before the incomplete value.
> :param incomplete: Value being completed. May be empty.

#### Classes

##### Class: `CompletionItem`

**Line:** 57

**Documentation:**

> Represents a completion value and metadata about the value. The
> default metadata is ``type`` to indicate special shell handling,
> and ``help`` if a shell supports showing a help string next to the
> value.
> 
> Arbitrary parameters can be passed when creating the object, and
> accessed using ``item.attr``. If an attribute wasn't passed,
> accessing it returns ``None``.
> 
> :param value: The completion suggestion.
> :param type: Tells the shell script to provide special completion
>     support for the type. Click uses ``"dir"`` and ``"file"``.
> :param help: String shown next to the value if supported.
> :param kwargs: Arbitrary metadata. The built-in implementations
>     don't use this, but custom type completions paired with custom
>     shell support could use it.

**Methods:**

- **`__init__(self, value, type, help, **kwargs)`** (Line 78)
  - Returns: `None`
  - _No documentation_

- **`__getattr__(self, name)`** (Line 90)
  - Returns: `t.Any`
  - _No documentation_

##### Class: `ShellComplete`

**Line:** 204

**Documentation:**

> Base class for providing shell completion support. A subclass for
> a given shell will override attributes and methods to implement the
> completion instructions (``source`` and ``complete``).
> 
> :param cli: Command being called.
> :param prog_name: Name of the executable in the shell.
> :param complete_var: Name of the environment variable that holds
>     the completion instruction.
> 
> .. versionadded:: 8.0

**Methods:**

- **`__init__(self, cli, ctx_args, prog_name, complete_var)`** (Line 228)
  - Returns: `None`
  - _No documentation_

- **`func_name(self)`** (Line 241)
  - Returns: `str`
  - The name of the shell function defined by the completion

- **`source_vars(self)`** (Line 248)
  - Returns: `dict[str, t.Any]`
  - Vars for formatting :attr:`source_template`.

- **`source(self)`** (Line 260)
  - Returns: `str`
  - Produce the shell script that defines the completion

- **`get_completion_args(self)`** (Line 268)
  - Returns: `tuple[list[str], str]`
  - Use the env vars defined by the shell script to return a

- **`get_completions(self, args, incomplete)`** (Line 275)
  - Returns: `list[CompletionItem]`
  - Determine the context and last complete command or parameter

- **`format_completion(self, item)`** (Line 287)
  - Returns: `str`
  - Format a completion item into the form recognized by the

- **`complete(self)`** (Line 295)
  - Returns: `str`
  - Produce the completion data to send back to the shell.

##### Class: `BashComplete`

**Line:** 308

**Documentation:**

> Shell completion for Bash.

**Methods:**

- **`_check_version()`** (Line 315)
  - Returns: `None`
  - _No documentation_

- **`source(self)`** (Line 347)
  - Returns: `str`
  - _No documentation_

- **`get_completion_args(self)`** (Line 351)
  - Returns: `tuple[list[str], str]`
  - _No documentation_

- **`format_completion(self, item)`** (Line 363)
  - Returns: `str`
  - _No documentation_

##### Class: `ZshComplete`

**Line:** 367

**Documentation:**

> Shell completion for Zsh.

**Methods:**

- **`get_completion_args(self)`** (Line 373)
  - Returns: `tuple[list[str], str]`
  - _No documentation_

- **`format_completion(self, item)`** (Line 385)
  - Returns: `str`
  - _No documentation_

##### Class: `FishComplete`

**Line:** 403

**Documentation:**

> Shell completion for Fish.

**Methods:**

- **`get_completion_args(self)`** (Line 409)
  - Returns: `tuple[list[str], str]`
  - _No documentation_

- **`format_completion(self, item)`** (Line 423)
  - Returns: `str`
  - Format completion item for Fish shell.

---

### `C:\Users\I.C.T\OneDrive\Documents\git\click\src\click\termui.py`

**Language:** python

#### Functions

##### `hidden_prompt_func(prompt)`

**Line:** 56 | **Returns:** `str`

**Parameters:**
- `prompt` (str)

**Documentation:** _No documentation_

##### `_readline_prompt(func, text, err)`

**Line:** 62 | **Returns:** `str`

**Parameters:**
- `func` (t.Callable[[str], str])
- `text` (str)
- `err` (bool)

**Documentation:**

> Call a prompt function, passing the full prompt on non-Windows so
> readline can handle line editing and cursor positioning correctly.
> 
> On Windows the prompt is written separately via :func:`echo` for
> colorama support, with only the last character passed to *func*.

##### `_build_prompt(text, suffix, show_default, default, show_choices, type)`

**Line:** 82 | **Returns:** `str`

**Parameters:**
- `text` (str)
- `suffix` (str)
- `show_default` (bool | str)
- `default` (t.Any | None)
- `show_choices` (bool)
- `type` (ParamType[t.Any] | None)

**Documentation:** _No documentation_

##### `_format_default(default)`

**Line:** 100 | **Returns:** `t.Any`

**Parameters:**
- `default` (t.Any)

**Documentation:** _No documentation_

##### `prompt(text, default, hide_input, confirmation_prompt, type, value_proc, prompt_suffix, show_default, err, show_choices)`

**Line:** 107 | **Returns:** `t.Any`

**Parameters:**
- `text` (str)
- `default` (t.Any | None)
- `hide_input` (bool)
- `confirmation_prompt` (bool | str)
- `type` (ParamType[t.Any] | t.Any | None)
- `value_proc` (t.Callable[[str], t.Any] | None)
- `prompt_suffix` (str)
- `show_default` (bool | str)
- `err` (bool)
- `show_choices` (bool)

**Documentation:**

> Prompts a user for input.  This is a convenience function that can
> be used to prompt a user for input later.
> 
> If the user aborts the input by sending an interrupt signal, this
> function will catch it and raise a :exc:`Abort` exception.
> 
> :param text: the text to show for the prompt.
> :param default: the default value to use if no input happens.  If this
>                 is not given it will prompt until it's aborted.
> :param hide_input: if this is set to true then the input value will
>                    be hidden.
> :param confirmation_prompt: Prompt a second time to confirm the
>     value. Can be set to a string instead of ``True`` to customize
>     the message.
> :param type: the type to use to check the value against.
> :param value_proc: if this parameter is provided it's a function that
>                    is invoked instead of the type conversion to
>                    convert a value.
> :param prompt_suffix: a suffix that should be added to the prompt.
> :param show_default: shows or hides the default value in the prompt.
>                      If this value is a string, it shows that string
>                      in parentheses instead of the actual value.
> :param err: if set to true the file defaults to ``stderr`` instead of
>             ``stdout``, the same as with echo.
> :param show_choices: Show or hide choices if the passed type is a Choice.
>                      For example if type is a Choice of either day or week,
>                      show_choices is true and text is "Group by" then the
>                      prompt will be "Group by (day, week): ".
> 
> .. versionchanged:: 8.3.3
>     ``show_default`` can be a string to show a custom value instead
>     of the actual default, matching the help text behavior.
> 
> .. versionchanged:: 8.3.1
>     A space is no longer appended to the prompt.
> 
> .. versionadded:: 8.0
>     ``confirmation_prompt`` can be a custom string.
> 
> .. versionadded:: 7.0
>     Added the ``show_choices`` parameter.
> 
> .. versionadded:: 6.0
>     Added unicode support for cmd.exe on Windows.
> 
> .. versionadded:: 4.0
>     Added the `err` parameter.

##### `confirm(text, default, abort, prompt_suffix, show_default, err)`

**Line:** 222 | **Returns:** `bool`

**Parameters:**
- `text` (str)
- `default` (bool | None)
- `abort` (bool)
- `prompt_suffix` (str)
- `show_default` (bool)
- `err` (bool)

**Documentation:**

> Prompts for confirmation (yes/no question).
> 
> If the user aborts the input by sending a interrupt signal this
> function will catch it and raise a :exc:`Abort` exception.
> 
> :param text: the question to ask.
> :param default: The default value to use when no input is given. If
>     ``None``, repeat until input is given.
> :param abort: if this is set to `True` a negative answer aborts the
>               exception by raising :exc:`Abort`.
> :param prompt_suffix: a suffix that should be added to the prompt.
> :param show_default: shows or hides the default value in the prompt.
> :param err: if set to true the file defaults to ``stderr`` instead of
>             ``stdout``, the same as with echo.
> 
> .. versionchanged:: 8.3.1
>     A space is no longer appended to the prompt.
> 
> .. versionchanged:: 8.0
>     Repeat until input is given if ``default`` is ``None``.
> 
> .. versionadded:: 4.0
>     Added the ``err`` parameter.

##### `get_pager_file(color)`

**Line:** 281 | **Returns:** `t.ContextManager[t.TextIO]`

**Parameters:**
- `color` (bool | None)

**Documentation:**

> Context manager.
> 
> Yields a writable file-like object which can be used as an output pager.
> 
> .. versionadded:: 8.2
> 
> :param color: controls if the pager supports ANSI colors or not.  The
>               default is autodetection.

##### `echo_via_pager(text_or_generator, color)`

**Line:** 300 | **Returns:** `None`

**Parameters:**
- `text_or_generator` (cabc.Iterable[str] | t.Callable[[], cabc.Iterable[str]] | str)
- `color` (bool | None)

**Documentation:**

> This function takes a text and shows it via an environment specific
> pager on stdout.
> 
> .. versionchanged:: 3.0
>    Added the `color` flag.
> 
> :param text_or_generator: the text to page, or alternatively, a
>                           generator emitting the text to page.
> :param color: controls if the pager supports ANSI colors or not.  The
>               default is autodetection.

##### `progressbar()`

**Line:** 332 | **Returns:** `ProgressBar[int]`

**Documentation:** _No documentation_

##### `progressbar(iterable, length, label, hidden, show_eta, show_percent, show_pos, item_show_func, fill_char, empty_char, bar_template, info_sep, width, file, color, update_min_steps)`

**Line:** 352 | **Returns:** `ProgressBar[V]`

**Parameters:**
- `iterable` (cabc.Iterable[V] | None)
- `length` (int | None)
- `label` (str | None)
- `hidden` (bool)
- `show_eta` (bool)
- `show_percent` (bool | None)
- `show_pos` (bool)
- `item_show_func` (t.Callable[[V | None], str | None] | None)
- `fill_char` (str)
- `empty_char` (str)
- `bar_template` (str)
- `info_sep` (str)
- `width` (int)
- `file` (t.TextIO | None)
- `color` (bool | None)
- `update_min_steps` (int)

**Documentation:** _No documentation_

##### `progressbar(iterable, length, label, hidden, show_eta, show_percent, show_pos, item_show_func, fill_char, empty_char, bar_template, info_sep, width, file, color, update_min_steps)`

**Line:** 372 | **Returns:** `ProgressBar[V]`

**Parameters:**
- `iterable` (cabc.Iterable[V] | None)
- `length` (int | None)
- `label` (str | None)
- `hidden` (bool)
- `show_eta` (bool)
- `show_percent` (bool | None)
- `show_pos` (bool)
- `item_show_func` (t.Callable[[V | None], str | None] | None)
- `fill_char` (str)
- `empty_char` (str)
- `bar_template` (str)
- `info_sep` (str)
- `width` (int)
- `file` (t.TextIO | None)
- `color` (bool | None)
- `update_min_steps` (int)

**Documentation:**

> This function creates an iterable context manager that can be used
> to iterate over something while showing a progress bar.  It will
> either iterate over the `iterable` or `length` items (that are counted
> up).  While iteration happens, this function will print a rendered
> progress bar to the given `file` (defaults to stdout) and will attempt
> to calculate remaining time and more.  By default, this progress bar
> will not be rendered if the file is not a terminal.
> 
> The context manager creates the progress bar.  When the context
> manager is entered the progress bar is already created.  With every
> iteration over the progress bar, the iterable passed to the bar is
> advanced and the bar is updated.  When the context manager exits,
> a newline is printed and the progress bar is finalized on screen.
> 
> Note: The progress bar is currently designed for use cases where the
> total progress can be expected to take at least several seconds.
> Because of this, the ProgressBar class object won't display
> progress that is considered too fast, and progress where the time
> between steps is less than a second.
> 
> No printing must happen or the progress bar will be unintentionally
> destroyed.
> 
> Example usage::
> 
>     with progressbar(items) as bar:
>         for item in bar:
>             do_something_with(item)
> 
> Alternatively, if no iterable is specified, one can manually update the
> progress bar through the `update()` method instead of directly
> iterating over the progress bar.  The update method accepts the number
> of steps to increment the bar with::
> 
>     with progressbar(length=chunks.total_bytes) as bar:
>         for chunk in chunks:
>             process_chunk(chunk)
>             bar.update(chunks.bytes)
> 
> The ``update()`` method also takes an optional value specifying the
> ``current_item`` at the new position. This is useful when used
> together with ``item_show_func`` to customize the output for each
> manual step::
> 
>     with click.progressbar(
>         length=total_size,
>         label='Unzipping archive',
>         item_show_func=lambda a: a.filename
>     ) as bar:
>         for archive in zip_file:
>             archive.extract()
>             bar.update(archive.size, archive)
> 
> :param iterable: an iterable to iterate over.  If not provided the length
>                  is required.
> :param length: the number of items to iterate over.  By default the
>                progressbar will attempt to ask the iterator about its
>                length, which might or might not work.  If an iterable is
>                also provided this parameter can be used to override the
>                length.  If an iterable is not provided the progress bar
>                will iterate over a range of that length.
> :param label: the label to show next to the progress bar.
> :param hidden: hide the progressbar. Defaults to ``False``. When no tty is
>     detected, it will only print the progressbar label. Setting this to
>     ``False`` also disables that.
> :param show_eta: enables or disables the estimated time display.  This is
>                  automatically disabled if the length cannot be
>                  determined.
> :param show_percent: enables or disables the percentage display.  The
>                      default is `True` if the iterable has a length or
>                      `False` if not.
> :param show_pos: enables or disables the absolute position display.  The
>                  default is `False`.
> :param item_show_func: A function called with the current item which
>     can return a string to show next to the progress bar. If the
>     function returns ``None`` nothing is shown. The current item can
>     be ``None``, such as when entering and exiting the bar.
> :param fill_char: the character to use to show the filled part of the
>                   progress bar.
> :param empty_char: the character to use to show the non-filled part of
>                    the progress bar.
> :param bar_template: the format string to use as template for the bar.
>                      The parameters in it are ``label`` for the label,
>                      ``bar`` for the progress bar and ``info`` for the
>                      info section.
> :param info_sep: the separator between multiple info items (eta etc.)
> :param width: the width of the progress bar in characters, 0 means full
>               terminal width
> :param file: The file to write to. If this is not a terminal then
>     only the label is printed.
> :param color: controls if the terminal supports ANSI colors or not.  The
>               default is autodetection.  This is only needed if ANSI
>               codes are included anywhere in the progress bar output
>               which is not the case by default.
> :param update_min_steps: Render only when this many updates have
>     completed. This allows tuning for very fast iterators.
> 
> .. versionadded:: 8.2
>     The ``hidden`` argument.
> 
> .. versionchanged:: 8.0
>     Output is shown even if execution time is less than 0.5 seconds.
> 
> .. versionchanged:: 8.0
>     ``item_show_func`` shows the current item, not the previous one.
> 
> .. versionchanged:: 8.0
>     Labels are echoed if the output is not a TTY. Reverts a change
>     in 7.0 that removed all output.
> 
> .. versionadded:: 8.0
>    The ``update_min_steps`` parameter.
> 
> .. versionadded:: 4.0
>     The ``color`` parameter and ``update`` method.
> 
> .. versionadded:: 2.0

##### `clear()`

**Line:** 531 | **Returns:** `None`

**Documentation:**

> Clears the terminal screen.  This will have the effect of clearing
> the whole visible space of the terminal and moving the cursor to the
> top left.  This does not do anything if not connected to a terminal.
> 
> .. versionadded:: 2.0

##### `_interpret_color(color, offset)`

**Line:** 545 | **Returns:** `str`

**Parameters:**
- `color` (int | tuple[int, int, int] | str)
- `offset` (int)

**Documentation:** _No documentation_

##### `style(text, fg, bg, bold, dim, underline, overline, italic, blink, reverse, strikethrough, reset)`

**Line:** 556 | **Returns:** `str`

**Parameters:**
- `text` (t.Any)
- `fg` (int | tuple[int, int, int] | str | None)
- `bg` (int | tuple[int, int, int] | str | None)
- `bold` (bool | None)
- `dim` (bool | None)
- `underline` (bool | None)
- `overline` (bool | None)
- `italic` (bool | None)
- `blink` (bool | None)
- `reverse` (bool | None)
- `strikethrough` (bool | None)
- `reset` (bool)

**Documentation:**

> Styles a text with ANSI styles and returns the new string.  By
> default the styling is self contained which means that at the end
> of the string a reset code is issued.  This can be prevented by
> passing ``reset=False``.
> 
> Examples::
> 
>     click.echo(click.style('Hello World!', fg='green'))
>     click.echo(click.style('ATTENTION!', blink=True))
>     click.echo(click.style('Some things', reverse=True, fg='cyan'))
>     click.echo(click.style('More colors', fg=(255, 12, 128), bg=117))
> 
> Supported color names:
> 
> * ``black`` (might be a gray)
> * ``red``
> * ``green``
> * ``yellow`` (might be an orange)
> * ``blue``
> * ``magenta``
> * ``cyan``
> * ``white`` (might be light gray)
> * ``bright_black``
> * ``bright_red``
> * ``bright_green``
> * ``bright_yellow``
> * ``bright_blue``
> * ``bright_magenta``
> * ``bright_cyan``
> * ``bright_white``
> * ``reset`` (reset the color code only)
> 
> If the terminal supports it, color may also be specified as:
> 
> -   An integer in the interval [0, 255]. The terminal must support
>     8-bit/256-color mode.
> -   An RGB tuple of three integers in [0, 255]. The terminal must
>     support 24-bit/true-color mode.
> 
> See https://en.wikipedia.org/wiki/ANSI_color and
> https://gist.github.com/XVilka/8346728 for more information.
> 
> :param text: the string to style with ansi codes.
> :param fg: if provided this will become the foreground color.
> :param bg: if provided this will become the background color.
> :param bold: if provided this will enable or disable bold mode.
> :param dim: if provided this will enable or disable dim mode.  This is
>             badly supported.
> :param underline: if provided this will enable or disable underline.
> :param overline: if provided this will enable or disable overline.
> :param italic: if provided this will enable or disable italic.
> :param blink: if provided this will enable or disable blinking.
> :param reverse: if provided this will enable or disable inverse
>                 rendering (foreground becomes background and the
>                 other way round).
> :param strikethrough: if provided this will enable or disable
>     striking through text.
> :param reset: by default a reset-all code is added at the end of the
>               string which means that styles do not carry over.  This
>               can be disabled to compose styles.
> 
> .. versionchanged:: 8.0
>     A non-string ``message`` is converted to a string.
> 
> .. versionchanged:: 8.0
>    Added support for 256 and RGB color codes.
> 
> .. versionchanged:: 8.0
>     Added the ``strikethrough``, ``italic``, and ``overline``
>     parameters.
> 
> .. versionchanged:: 7.0
>     Added support for bright colors.
> 
> .. versionadded:: 2.0

##### `unstyle(text)`

**Line:** 685 | **Returns:** `str`

**Parameters:**
- `text` (str)

**Documentation:**

> Removes ANSI styling information from a string.  Usually it's not
> necessary to use this function as Click's echo function will
> automatically remove styling if necessary.
> 
> .. versionadded:: 2.0
> 
> :param text: the text to remove style information from.

##### `secho(message, file, nl, err, color, **styles)`

**Line:** 697 | **Returns:** `None`

**Parameters:**
- `message` (t.Any | None)
- `file` (t.IO[t.AnyStr] | None)
- `nl` (bool)
- `err` (bool)
- `color` (bool | None)
- `**styles` (t.Any)

**Documentation:**

> This function combines :func:`echo` and :func:`style` into one
> call.  As such the following two calls are the same::
> 
>     click.secho('Hello World!', fg='green')
>     click.echo(click.style('Hello World!', fg='green'))
> 
> All keyword arguments are forwarded to the underlying functions
> depending on which one they go with.
> 
> Non-string types will be converted to :class:`str`. However,
> :class:`bytes` are passed directly to :meth:`echo` without applying
> style. If you want to style bytes that represent text, call
> :meth:`bytes.decode` first.
> 
> .. versionchanged:: 8.0
>     A non-string ``message`` is converted to a string. Bytes are
>     passed through without style applied.
> 
> .. versionadded:: 2.0

##### `edit(text, editor, env, require_save, extension)`

**Line:** 732 | **Returns:** `bytes | None`

**Parameters:**
- `text` (bytes | bytearray)
- `editor` (str | None)
- `env` (cabc.Mapping[str, str] | None)
- `require_save` (bool)
- `extension` (str)

**Documentation:** _No documentation_

##### `edit(text, editor, env, require_save, extension)`

**Line:** 742 | **Returns:** `str | None`

**Parameters:**
- `text` (str)
- `editor` (str | None)
- `env` (cabc.Mapping[str, str] | None)
- `require_save` (bool)
- `extension` (str)

**Documentation:** _No documentation_

##### `edit(text, editor, env, require_save, extension, filename)`

**Line:** 752 | **Returns:** `None`

**Parameters:**
- `text` (None)
- `editor` (str | None)
- `env` (cabc.Mapping[str, str] | None)
- `require_save` (bool)
- `extension` (str)
- `filename` (str | cabc.Iterable[str] | None)

**Documentation:** _No documentation_

##### `edit(text, editor, env, require_save, extension, filename)`

**Line:** 762 | **Returns:** `str | bytes | bytearray | None`

**Parameters:**
- `text` (str | bytes | bytearray | None)
- `editor` (str | None)
- `env` (cabc.Mapping[str, str] | None)
- `require_save` (bool)
- `extension` (str)
- `filename` (str | cabc.Iterable[str] | None)

**Documentation:**

> Edits the given text in the defined editor.  If an editor is given
> (should be the full path to the executable but the regular operating
> system search path is used for finding the executable) it overrides
> the detected editor.  Optionally, some environment variables can be
> used.  If the editor is closed without changes, `None` is returned.  In
> case a file is edited directly the return value is always `None` and
> `require_save` and `extension` are ignored.
> 
> If the editor cannot be opened a :exc:`UsageError` is raised.
> 
> Note for Windows: to simplify cross-platform usage, the newlines are
> automatically converted from POSIX to Windows and vice versa.  As such,
> the message here will have ``\n`` as newline markers.
> 
> :param text: the text to edit.
> :param editor: optionally the editor to use.  Defaults to automatic
>                detection.
> :param env: environment variables to forward to the editor.
> :param require_save: if this is true, then not saving in the editor
>                      will make the return value become `None`.
> :param extension: the extension to tell the editor about.  This defaults
>                   to `.txt` but changing this might change syntax
>                   highlighting.
> :param filename: if provided it will edit this file instead of the
>                  provided text contents.  It will not use a temporary
>                  file as an indirection in that case. If the editor supports
>                  editing multiple files at once, a sequence of files may be
>                  passed as well. Invoke `click.file` once per file instead
>                  if multiple files cannot be managed at once or editing the
>                  files serially is desired.
> 
> .. versionchanged:: 8.2.0
>     ``filename`` now accepts any ``Iterable[str]`` in addition to a ``str``
>     if the ``editor`` supports editing multiple files at once.

##### `launch(url, wait, locate)`

**Line:** 820 | **Returns:** `int`

**Parameters:**
- `url` (str)
- `wait` (bool)
- `locate` (bool)

**Documentation:**

> This function launches the given URL (or filename) in the default
> viewer application for this file type.  If this is an executable, it
> might launch the executable in a new session.  The return value is
> the exit code of the launched application.  Usually, ``0`` indicates
> success.
> 
> Examples::
> 
>     click.launch('https://click.palletsprojects.com/')
>     click.launch('/my/downloaded/file', locate=True)
> 
> .. versionadded:: 2.0
> 
> :param url: URL or filename of the thing to launch.
> :param wait: Wait for the program to exit before returning. This
>     only works if the launched program blocks. In particular,
>     ``xdg-open`` on Linux does not block.
> :param locate: if this is set to `True` then instead of launching the
>                application associated with the URL it will attempt to
>                launch a file manager with the file located.  This
>                might have weird effects if the URL does not point to
>                the filesystem.

##### `getchar(echo)`

**Line:** 854 | **Returns:** `str`

**Parameters:**
- `echo` (bool)

**Documentation:**

> Fetches a single character from the terminal and returns it.  This
> will always return a unicode character and under certain rare
> circumstances this might return more than one character.  The
> situations which more than one character is returned is when for
> whatever reason multiple characters end up in the terminal buffer or
> standard input was not actually a terminal.
> 
> Note that this will always read from the terminal, even if something
> is piped into the standard input.
> 
> Note for Windows: in rare cases when typing non-ASCII characters, this
> function might wait for a second character and then return both at once.
> This is because certain Unicode characters look like special-key markers.
> 
> .. versionadded:: 2.0
> 
> :param echo: if set to `True`, the character read will also show up on
>              the terminal.  The default is to not show it.

##### `raw_terminal()`

**Line:** 884 | **Returns:** `AbstractContextManager[int]`

**Documentation:** _No documentation_

##### `pause(info, err)`

**Line:** 890 | **Returns:** `None`

**Parameters:**
- `info` (str | None)
- `err` (bool)

**Documentation:**

> This command stops execution and waits for the user to press any
> key to continue.  This is similar to the Windows batch "pause"
> command.  If the program is not run through a terminal, this command
> will instead do nothing.
> 
> .. versionadded:: 2.0
> 
> .. versionadded:: 4.0
>    Added the `err` parameter.
> 
> :param info: The message to print before pausing. Defaults to
>     ``"Press any key to continue..."``.
> :param err: if set to message goes to ``stderr`` instead of
>             ``stdout``, the same as with echo.

---

### `C:\Users\I.C.T\OneDrive\Documents\git\click\src\click\testing.py`

**Language:** python

#### Functions

##### `_pause_echo(stream)`

**Line:** 61 | **Returns:** `cabc.Iterator[None]`

**Parameters:**
- `stream` (EchoingStdin | None)

**Documentation:** _No documentation_

##### `make_input_stream(input, charset)`

**Line:** 163 | **Returns:** `t.BinaryIO`

**Parameters:**
- `input` (str | bytes | t.IO[t.Any] | None)
- `charset` (str)

**Documentation:** _No documentation_

#### Classes

##### Class: `EchoingStdin`

**Line:** 26

**Documentation:** _No documentation_

**Methods:**

- **`__init__(self, input, output)`** (Line 27)
  - Returns: `None`
  - _No documentation_

- **`__getattr__(self, x)`** (Line 32)
  - Returns: `t.Any`
  - _No documentation_

- **`_echo(self, rv)`** (Line 35)
  - Returns: `bytes`
  - _No documentation_

- **`read(self, n)`** (Line 41)
  - Returns: `bytes`
  - _No documentation_

- **`read1(self, n)`** (Line 44)
  - Returns: `bytes`
  - _No documentation_

- **`readline(self, n)`** (Line 47)
  - Returns: `bytes`
  - _No documentation_

- **`readlines(self)`** (Line 50)
  - Returns: `list[bytes]`
  - _No documentation_

- **`__iter__(self)`** (Line 53)
  - Returns: `cabc.Iterator[bytes]`
  - _No documentation_

- **`__repr__(self)`** (Line 56)
  - Returns: `str`
  - _No documentation_

##### Class: `BytesIOCopy`

**Line:** 70

**Documentation:**

> Patch ``io.BytesIO`` to let the written stream be copied to another.
> 
> .. versionadded:: 8.2

**Methods:**

- **`__init__(self, copy_to)`** (Line 76)
  - Returns: `None`
  - _No documentation_

- **`flush(self)`** (Line 80)
  - Returns: `None`
  - _No documentation_

- **`write(self, b)`** (Line 84)
  - Returns: `int`
  - _No documentation_

##### Class: `StreamMixer`

**Line:** 89

**Documentation:**

> Mixes `<stdout>` and `<stderr>` streams.
> 
> The result is available in the ``output`` attribute.
> 
> .. versionadded:: 8.2

**Methods:**

- **`__init__(self)`** (Line 97)
  - Returns: `None`
  - _No documentation_

##### Class: `_NamedTextIOWrapper`

**Line:** 103

**Documentation:**

> A :class:`~io.TextIOWrapper` with custom ``name`` and ``mode``
> that does not close its underlying buffer.
> 
> An optional ``original_fd`` preserves the file descriptor of the
> stream being replaced, so that C-level consumers that call
> :meth:`fileno` (``faulthandler``, ``subprocess``, ...) still work.
> Inspired by pytest's ``capsys``/``capfd`` split: see :doc:`/testing`
> for details.
> 
> .. versionchanged:: 8.3.3
>     Added ``original_fd`` parameter and :meth:`fileno` override.

**Methods:**

- **`__init__(self, buffer, name, mode, **kwargs)`** (Line 117)
  - Returns: `None`
  - _No documentation_

- **`close(self)`** (Line 131)
  - Returns: `None`
  - The buffer this object contains belongs to some other object,

- **`fileno(self)`** (Line 139)
  - Returns: `int`
  - Return the file descriptor of the original stream, if one was

- **`name(self)`** (Line 155)
  - Returns: `str`
  - _No documentation_

- **`mode(self)`** (Line 159)
  - Returns: `str`
  - _No documentation_

##### Class: `Result`

**Line:** 183

**Documentation:**

> Holds the captured result of an invoked CLI script.
> 
> :param runner: The runner that created the result
> :param stdout_bytes: The standard output as bytes.
> :param stderr_bytes: The standard error as bytes.
> :param output_bytes: A mix of ``stdout_bytes`` and ``stderr_bytes``, as the
>     user would see  it in its terminal.
> :param return_value: The value returned from the invoked command.
> :param exit_code: The exit code as integer.
> :param exception: The exception that happened if one did.
> :param exc_info: Exception information (exception type, exception instance,
>     traceback type).
> 
> .. versionchanged:: 8.2
>     ``stderr_bytes`` no longer optional, ``output_bytes`` introduced and
>     ``mix_stderr`` has been removed.
> 
> .. versionadded:: 8.0
>     Added ``return_value``.

**Methods:**

- **`__init__(self, runner, stdout_bytes, stderr_bytes, output_bytes, return_value, exit_code, exception, exc_info)`** (Line 205)
  - Returns: `None`
  - _No documentation_

- **`output(self)`** (Line 227)
  - Returns: `str`
  - The terminal output as unicode string, as the user would see it.

- **`stdout(self)`** (Line 239)
  - Returns: `str`
  - The standard output as unicode string.

- **`stderr(self)`** (Line 246)
  - Returns: `str`
  - The standard error as unicode string.

- **`__repr__(self)`** (Line 256)
  - Returns: `str`
  - _No documentation_

##### Class: `CliRunner`

**Line:** 261

**Documentation:**

> The CLI runner provides functionality to invoke a Click command line
> script for unittesting purposes in a isolated environment.  This only
> works in single-threaded systems without any concurrency as it changes the
> global interpreter state.
> 
> :param charset: the character set for the input and output data.
> :param env: a dictionary with environment variables for overriding.
> :param echo_stdin: if this is set to `True`, then reading from `<stdin>` writes
>                    to `<stdout>`.  This is useful for showing examples in
>                    some circumstances.  Note that regular prompts
>                    will automatically echo the input.
> :param catch_exceptions: Whether to catch any exceptions other than
>                          ``SystemExit`` when running :meth:`~CliRunner.invoke`.
> 
> .. versionchanged:: 8.2
>     Added the ``catch_exceptions`` parameter.
> 
> .. versionchanged:: 8.2
>     ``mix_stderr`` parameter has been removed.

**Methods:**

- **`__init__(self, charset, env, echo_stdin, catch_exceptions)`** (Line 283)
  - Returns: `None`
  - _No documentation_

- **`get_default_prog_name(self, cli)`** (Line 295)
  - Returns: `str`
  - Given a command object it will return the default program name

- **`make_env(self, overrides)`** (Line 302)
  - Returns: `cabc.Mapping[str, str | None]`
  - Returns the environment overrides for invoking a script.

- **`isolation(self, input, env, color)`** (Line 312)
  - Returns: `cabc.Iterator[tuple[io.BytesIO, io.BytesIO, io.BytesIO]]`
  - A context manager that sets up the isolation for invoking of a

- **`invoke(self, cli, args, input, env, catch_exceptions, color, **extra)`** (Line 525)
  - Returns: `Result`
  - Invokes a command in an isolated environment.  The arguments are

- **`isolated_filesystem(self, temp_dir)`** (Line 639)
  - Returns: `cabc.Iterator[str]`
  - A context manager that creates a temporary directory and

---

### `C:\Users\I.C.T\OneDrive\Documents\git\click\src\click\types.py`

**Language:** python

#### Functions

##### `_is_file_like(value)`

**Line:** 910 | **Returns:** `te.TypeGuard[t.IO[t.Any]]`

**Parameters:**
- `value` (t.Any)

**Documentation:** _No documentation_

##### `_guess_type(ty, default)`

**Line:** 1160 | **Returns:** `type[t.Any] | tuple[type[t.Any], ...] | ParamType[t.Any] | None`

**Parameters:**
- `ty` (type[t.Any] | ParamType[t.Any] | None)
- `default` (t.Any | None)

**Documentation:**

> Infer a type from *ty* or *default*.
> 
> Returns *ty* unchanged when it is not ``None``.  Otherwise inspects
> *default* to produce a ``type``, a ``tuple`` of types (for tuple
> defaults), or ``None``.

##### `convert_type(ty, default)`

**Line:** 1196 | **Returns:** `StringParamType`

**Parameters:**
- `ty` (None)
- `default` (None)

**Documentation:** _No documentation_

##### `convert_type(ty, default)`

**Line:** 1200 | **Returns:** `ParamType[t.Any]`

**Parameters:**
- `ty` (type[t.Any] | ParamType[t.Any])
- `default` (t.Any | None)

**Documentation:** _No documentation_

##### `convert_type(ty, default)`

**Line:** 1206 | **Returns:** `ParamType[t.Any]`

**Parameters:**
- `ty` (t.Any | None)
- `default` (t.Any | None)

**Documentation:** _No documentation_

##### `convert_type(ty, default)`

**Line:** 1211 | **Returns:** `ParamType[t.Any]`

**Parameters:**
- `ty` (t.Any | None)
- `default` (t.Any | None)

**Documentation:**

> Find the most appropriate :class:`ParamType` for the given Python
> type. If the type isn't provided, it can be inferred from a default
> value.

#### Classes

##### Class: `ParamTypeInfoDict`

**Line:** 32

**Documentation:** _No documentation_

##### Class: `ParamType`

**Line:** 37

**Documentation:**

> Represents the type of a parameter. Validates and converts values
> from the command line or Python into the correct type.
> 
> To implement a custom type, subclass and implement at least the
> following:
> 
> -   The :attr:`name` class attribute must be set.
> -   Calling an instance of the type with ``None`` must return
>     ``None``. This is already implemented by default.
> -   :meth:`convert` must convert string values to the correct type.
> -   :meth:`convert` must accept values that are already the correct
>     type.
> -   It must be able to convert a value if the ``ctx`` and ``param``
>     arguments are ``None``. This can occur when converting prompt
>     input.

**Methods:**

- **`to_info_dict(self)`** (Line 69)
  - Returns: `ParamTypeInfoDict`
  - Gather information that could be useful for a tool generating

- **`__call__(self, value, param, ctx)`** (Line 90)
  - Returns: `ParamTypeValue | None`
  - _No documentation_

- **`get_metavar(self, param, ctx)`** (Line 100)
  - Returns: `str | None`
  - Returns the metavar default for this param if it provides one.

- **`get_missing_message(self, param, ctx)`** (Line 103)
  - Returns: `str | None`
  - Optionally might return extra information about a missing

- **`convert(self, value, param, ctx)`** (Line 110)
  - Returns: `ParamTypeValue`
  - Convert the value to the correct type. This is not called if

- **`split_envvar_value(self, rv)`** (Line 136)
  - Returns: `cabc.Sequence[str]`
  - Given a value from an environment variable this splits it up

- **`fail(self, message, param, ctx)`** (Line 146)
  - Returns: `t.NoReturn`
  - Helper method to fail with an invalid value message.

- **`shell_complete(self, ctx, param, incomplete)`** (Line 155)
  - Returns: `list[CompletionItem]`
  - Return a list of

##### Class: `CompositeParamType`

**Line:** 173

**Documentation:** _No documentation_

**Methods:**

- **`arity(self)`** (Line 178)
  - Returns: `int`
  - _No documentation_

##### Class: `FuncParamTypeInfoDict`

**Line:** 181

**Documentation:** _No documentation_

##### Class: `FuncParamType`

**Line:** 185

**Documentation:** _No documentation_

**Methods:**

- **`__init__(self, func)`** (Line 186)
  - Returns: `None`
  - _No documentation_

- **`to_info_dict(self)`** (Line 190)
  - Returns: `FuncParamTypeInfoDict`
  - _No documentation_

- **`convert(self, value, param, ctx)`** (Line 193)
  - Returns: `ParamTypeValue`
  - _No documentation_

##### Class: `UnprocessedParamType`

**Line:** 207

**Documentation:** _No documentation_

**Methods:**

- **`convert(self, value, param, ctx)`** (Line 210)
  - Returns: `t.Any`
  - _No documentation_

- **`__repr__(self)`** (Line 215)
  - Returns: `str`
  - _No documentation_

##### Class: `StringParamType`

**Line:** 219

**Documentation:** _No documentation_

**Methods:**

- **`convert(self, value, param, ctx)`** (Line 222)
  - Returns: `str`
  - _No documentation_

- **`__repr__(self)`** (Line 241)
  - Returns: `str`
  - _No documentation_

##### Class: `ChoiceInfoDict`

**Line:** 245

**Documentation:** _No documentation_

##### Class: `Choice`

**Line:** 250

**Documentation:**

> The choice type allows a value to be checked against a fixed set
> of supported values.
> 
> You may pass any iterable value which will be converted to a tuple
> and thus will only be iterated once.
> 
> The resulting value will always be one of the originally passed choices.
> See :meth:`normalize_choice` for more info on the mapping of strings
> to choices. See :ref:`choice-opts` for an example.
> 
> :param case_sensitive: Set to false to make choices case
>     insensitive. Defaults to true.
> 
> .. versionchanged:: 8.2.0
>     Non-``str`` ``choices`` are now supported. It can additionally be any
>     iterable. Before you were not recommended to pass anything but a list or
>     tuple.
> 
> .. versionadded:: 8.2.0
>     Choice normalization can be overridden via :meth:`normalize_choice`.

**Methods:**

- **`__init__(self, choices, case_sensitive)`** (Line 275)
  - Returns: `None`
  - _No documentation_

- **`to_info_dict(self)`** (Line 281)
  - Returns: `ChoiceInfoDict`
  - _No documentation_

- **`_normalized_mapping(self, ctx)`** (Line 288)
  - Returns: `cabc.Mapping[ParamTypeValue, str]`
  - Returns mapping where keys are the original choices and the values are

- **`normalize_choice(self, choice, ctx)`** (Line 306)
  - Returns: `str`
  - Normalize a choice value, used to map a passed string to a choice.

- **`get_metavar(self, param, ctx)`** (Line 326)
  - Returns: `str | None`
  - _No documentation_

- **`get_missing_message(self, param, ctx)`** (Line 344)
  - Returns: `str`
  - Message shown when no choice is passed.

- **`convert(self, value, param, ctx)`** (Line 354)
  - Returns: `ParamTypeValue`
  - For a given value from the parser, normalize it and find its

- **`get_invalid_choice_message(self, value, ctx)`** (Line 378)
  - Returns: `str`
  - Get the error message when the given choice is invalid.

- **`__repr__(self)`** (Line 392)
  - Returns: `str`
  - _No documentation_

- **`shell_complete(self, ctx, param, incomplete)`** (Line 395)
  - Returns: `list[CompletionItem]`
  - Complete choices that start with the incomplete value.

##### Class: `DateTimeInfoDict`

**Line:** 419

**Documentation:** _No documentation_

##### Class: `DateTime`

**Line:** 423

**Documentation:**

> The DateTime type converts date strings into `datetime` objects.
> 
> The format strings which are checked are configurable, but default to some
> common (non-timezone aware) ISO 8601 formats.
> 
> When specifying *DateTime* formats, you should only pass a list or a tuple.
> Other iterables, like generators, may lead to surprising results.
> 
> The format strings are processed using ``datetime.strptime``, and this
> consequently defines the format strings which are allowed.
> 
> Parsing is tried using each format, in order, and the first format which
> parses successfully is used.
> 
> :param formats: A list or tuple of date format strings, in the order in
>                 which they should be tried. Defaults to
>                 ``'%Y-%m-%d'``, ``'%Y-%m-%dT%H:%M:%S'``,
>                 ``'%Y-%m-%d %H:%M:%S'``.

**Methods:**

- **`__init__(self, formats)`** (Line 446)
  - Returns: `None`
  - _No documentation_

- **`to_info_dict(self)`** (Line 453)
  - Returns: `DateTimeInfoDict`
  - _No documentation_

- **`get_metavar(self, param, ctx)`** (Line 456)
  - Returns: `str | None`
  - _No documentation_

- **`_try_to_convert_date(self, value, format)`** (Line 459)
  - Returns: `datetime | None`
  - _No documentation_

- **`convert(self, value, param, ctx)`** (Line 465)
  - Returns: `datetime`
  - _No documentation_

- **`__repr__(self)`** (Line 488)
  - Returns: `str`
  - _No documentation_

##### Class: `_NumberParamTypeBase`

**Line:** 492

**Documentation:** _No documentation_

**Methods:**

- **`convert(self, value, param, ctx)`** (Line 495)
  - Returns: `ParamTypeValue`
  - _No documentation_

##### Class: `NumberRangeInfoDict`

**Line:** 510

**Documentation:** _No documentation_

##### Class: `_NumberRangeBase`

**Line:** 518

**Documentation:** _No documentation_

**Methods:**

- **`__init__(self, min, max, min_open, max_open, clamp)`** (Line 519)
  - Returns: `None`
  - _No documentation_

- **`to_info_dict(self)`** (Line 533)
  - Returns: `NumberRangeInfoDict`
  - _No documentation_

- **`convert(self, value, param, ctx)`** (Line 543)
  - Returns: `ParamTypeValue`
  - _No documentation_

- **`_clamp(self, bound, dir, open)`** (Line 577)
  - Returns: `ParamTypeValue`
  - Find the valid value to clamp to bound in the given

- **`_describe_range(self)`** (Line 589)
  - Returns: `str`
  - Describe the range for use in help text.

- **`__repr__(self)`** (Line 603)
  - Returns: `str`
  - _No documentation_

##### Class: `IntParamType`

**Line:** 608

**Documentation:** _No documentation_

**Methods:**

- **`__repr__(self)`** (Line 612)
  - Returns: `str`
  - _No documentation_

##### Class: `IntRange`

**Line:** 616

**Documentation:**

> Restrict an :data:`click.INT` value to a range of accepted
> values. See :ref:`ranges`.
> 
> If ``min`` or ``max`` are not passed, any value is accepted in that
> direction. If ``min_open`` or ``max_open`` are enabled, the
> corresponding boundary is not included in the range.
> 
> If ``clamp`` is enabled, a value outside the range is clamped to the
> boundary instead of failing.
> 
> .. versionchanged:: 8.0
>     Added the ``min_open`` and ``max_open`` parameters.

**Methods:**

- **`_clamp(self, bound, dir, open)`** (Line 633)
  - Returns: `int`
  - _No documentation_

##### Class: `FloatParamType`

**Line:** 640

**Documentation:** _No documentation_

**Methods:**

- **`__repr__(self)`** (Line 644)
  - Returns: `str`
  - _No documentation_

##### Class: `FloatRange`

**Line:** 648

**Documentation:**

> Restrict a :data:`click.FLOAT` value to a range of accepted
> values. See :ref:`ranges`.
> 
> If ``min`` or ``max`` are not passed, any value is accepted in that
> direction. If ``min_open`` or ``max_open`` are enabled, the
> corresponding boundary is not included in the range.
> 
> If ``clamp`` is enabled, a value outside the range is clamped to the
> boundary instead of failing. This is not supported if either
> boundary is marked ``open``.
> 
> .. versionchanged:: 8.0
>     Added the ``min_open`` and ``max_open`` parameters.

**Methods:**

- **`__init__(self, min, max, min_open, max_open, clamp)`** (Line 666)
  - Returns: `None`
  - _No documentation_

- **`_clamp(self, bound, dir, open)`** (Line 681)
  - Returns: `float`
  - _No documentation_

##### Class: `BoolParamType`

**Line:** 691

**Documentation:** _No documentation_

**Methods:**

- **`str_to_bool(value)`** (Line 728)
  - Returns: `bool | None`
  - Convert a string to a boolean value.

- **`convert(self, value, param, ctx)`** (Line 742)
  - Returns: `bool`
  - _No documentation_

- **`__repr__(self)`** (Line 756)
  - Returns: `str`
  - _No documentation_

##### Class: `UUIDParameterType`

**Line:** 760

**Documentation:** _No documentation_

**Methods:**

- **`convert(self, value, param, ctx)`** (Line 763)
  - Returns: `uuid.UUID`
  - _No documentation_

- **`__repr__(self)`** (Line 778)
  - Returns: `str`
  - _No documentation_

##### Class: `FileInfoDict`

**Line:** 782

**Documentation:** _No documentation_

##### Class: `File`

**Line:** 787

**Documentation:**

> Declares a parameter to be a file for reading or writing.  The file
> is automatically closed once the context tears down (after the command
> finished working).
> 
> Files can be opened for reading or writing.  The special value ``-``
> indicates stdin or stdout depending on the mode.
> 
> By default, the file is opened for reading text data, but it can also be
> opened in binary mode or for writing.  The encoding parameter can be used
> to force a specific encoding.
> 
> The `lazy` flag controls if the file should be opened immediately or upon
> first IO. The default is to be non-lazy for standard input and output
> streams as well as files opened for reading, `lazy` otherwise. When opening a
> file lazily for reading, it is still opened temporarily for validation, but
> will not be held open until first IO. lazy is mainly useful when opening
> for writing to avoid creating the file until it is needed.
> 
> Files can also be opened atomically in which case all writes go into a
> separate file in the same folder and upon completion the file will
> be moved over to the original location.  This is useful if a file
> regularly read by other users is modified.
> 
> See :ref:`file-args` for more information.
> 
> .. versionchanged:: 2.0
>     Added the ``atomic`` parameter.

**Methods:**

- **`__init__(self, mode, encoding, errors, lazy, atomic)`** (Line 820)
  - Returns: `None`
  - _No documentation_

- **`to_info_dict(self)`** (Line 834)
  - Returns: `FileInfoDict`
  - _No documentation_

- **`resolve_lazy_flag(self, value)`** (Line 841)
  - Returns: `bool`
  - _No documentation_

- **`convert(self, value, param, ctx)`** (Line 850)
  - Returns: `t.IO[t.Any]`
  - _No documentation_

- **`shell_complete(self, ctx, param, incomplete)`** (Line 893)
  - Returns: `list[CompletionItem]`
  - Return a special completion marker that tells the completion

##### Class: `PathInfoDict`

**Line:** 914

**Documentation:** _No documentation_

##### Class: `Path`

**Line:** 923

**Documentation:**

> The ``Path`` type is similar to the :class:`File` type, but
> returns the filename instead of an open file. Various checks can be
> enabled to validate the type of file and permissions.
> 
> :param exists: The file or directory needs to exist for the value to
>     be valid. If this is not set to ``True``, and the file does not
>     exist, then all further checks are silently skipped.
> :param file_okay: Allow a file as a value.
> :param dir_okay: Allow a directory as a value.
> :param readable: if true, a readable check is performed.
> :param writable: if true, a writable check is performed.
> :param executable: if true, an executable check is performed.
> :param resolve_path: Make the value absolute and resolve any
>     symlinks. A ``~`` is not expanded, as this is supposed to be
>     done by the shell only.
> :param allow_dash: Allow a single dash as a value, which indicates
>     a standard stream (but does not open it). Use
>     :func:`~click.open_file` to handle opening this value.
> :param path_type: Convert the incoming path value to this type. If
>     ``None``, keep Python's default, which is ``str``. Useful to
>     convert to :class:`pathlib.Path`.
> 
> .. versionchanged:: 8.1
>     Added the ``executable`` parameter.
> 
> .. versionchanged:: 8.0
>     Allow passing ``path_type=pathlib.Path``.
> 
> .. versionchanged:: 6.0
>     Added the ``allow_dash`` parameter.

**Methods:**

- **`__init__(self, exists, file_okay, dir_okay, writable, readable, resolve_path, allow_dash, path_type, executable)`** (Line 958)
  - Returns: `None`
  - _No documentation_

- **`to_info_dict(self)`** (Line 987)
  - Returns: `PathInfoDict`
  - _No documentation_

- **`coerce_path_result(self, value)`** (Line 998)
  - Returns: `str | bytes | os.PathLike[str]`
  - _No documentation_

- **`convert(self, value, param, ctx)`** (Line 1011)
  - Returns: `str | bytes | os.PathLike[str]`
  - _No documentation_

- **`shell_complete(self, ctx, param, incomplete)`** (Line 1084)
  - Returns: `list[CompletionItem]`
  - Return a special completion marker that tells the completion

##### Class: `TupleInfoDict`

**Line:** 1103

**Documentation:** _No documentation_

##### Class: `Tuple`

**Line:** 1107

**Documentation:**

> The default behavior of Click is to apply a type on a value directly.
> This works well in most cases, except for when `nargs` is set to a fixed
> count and different types should be used for different items.  In this
> case the :class:`Tuple` type can be used.  This type can only be used
> if `nargs` is set to a fixed number.
> 
> For more information see :ref:`tuple-type`.
> 
> This can be selected by using a Python tuple literal as a type.
> 
> :param types: a list of types that should be used for the tuple items.

**Methods:**

- **`__init__(self, types)`** (Line 1121)
  - Returns: `None`
  - _No documentation_

- **`to_info_dict(self)`** (Line 1124)
  - Returns: `TupleInfoDict`
  - _No documentation_

- **`name(self)`** (Line 1131)
  - Returns: `str`
  - _No documentation_

- **`arity(self)`** (Line 1135)
  - Returns: `int`
  - _No documentation_

- **`convert(self, value, param, ctx)`** (Line 1138)
  - Returns: `tuple[t.Any, ...]`
  - _No documentation_

##### Class: `OptionHelpExtra`

**Line:** 1288

**Documentation:** _No documentation_

---

### `C:\Users\I.C.T\OneDrive\Documents\git\click\src\click\utils.py`

**Language:** python

#### Functions

##### `_posixify(name)`

**Line:** 32 | **Returns:** `str`

**Parameters:**
- `name` (str)

**Documentation:** _No documentation_

##### `safecall(func)`

**Line:** 36 | **Returns:** `t.Callable[P, R | None]`

**Parameters:**
- `func` (t.Callable[P, R])

**Documentation:**

> Wraps a function so that it swallows exceptions.

##### `make_str(value)`

**Line:** 49 | **Returns:** `str`

**Parameters:**
- `value` (t.Any)

**Documentation:**

> Converts a value into a valid string.

##### `make_default_short_help(help, max_length)`

**Line:** 59 | **Returns:** `str`

**Parameters:**
- `help` (str)
- `max_length` (int)

**Documentation:**

> Returns a condensed version of help string.
> 
> :meta private:

##### `echo(message, file, nl, err, color)`

**Line:** 225 | **Returns:** `None`

**Parameters:**
- `message` (t.Any | None)
- `file` (t.IO[t.Any] | None)
- `nl` (bool)
- `err` (bool)
- `color` (bool | None)

**Documentation:**

> Print a message and newline to stdout or a file. This should be
> used instead of :func:`print` because it provides better support
> for different data, files, and environments.
> 
> Compared to :func:`print`, this does the following:
> 
> -   Ensures that the output encoding is not misconfigured on Linux.
> -   Supports Unicode in the Windows console.
> -   Supports writing to binary outputs, and supports writing bytes
>     to text outputs.
> -   Supports colors and styles on Windows.
> -   Removes ANSI color and style codes if the output does not look
>     like an interactive terminal.
> -   Always flushes the output.
> 
> :param message: The string or bytes to output. Other objects are
>     converted to strings.
> :param file: The file to write to. Defaults to ``stdout``.
> :param err: Write to ``stderr`` instead of ``stdout``.
> :param nl: Print a newline after the message. Enabled by default.
> :param color: Force showing or hiding colors and other styles. By
>     default Click will remove color if the output does not look like
>     an interactive terminal.
> 
> .. versionchanged:: 6.0
>     Support Unicode output on the Windows console. Click does not
>     modify ``sys.stdout``, so ``sys.stdout.write()`` and ``print()``
>     will still not support Unicode.
> 
> .. versionchanged:: 4.0
>     Added the ``color`` parameter.
> 
> .. versionadded:: 3.0
>     Added the ``err`` parameter.
> 
> .. versionchanged:: 2.0
>     Support colors on Windows if colorama is installed.

##### `get_binary_stream(name)`

**Line:** 328 | **Returns:** `t.BinaryIO`

**Parameters:**
- `name` (t.Literal['stdin', 'stdout', 'stderr'])

**Documentation:**

> Returns a system stream for byte processing.
> 
> :param name: the name of the stream to open.  Valid names are ``'stdin'``,
>              ``'stdout'`` and ``'stderr'``

##### `get_text_stream(name, encoding, errors)`

**Line:** 340 | **Returns:** `t.TextIO`

**Parameters:**
- `name` (t.Literal['stdin', 'stdout', 'stderr'])
- `encoding` (str | None)
- `errors` (str | None)

**Documentation:**

> Returns a system stream for text processing.  This usually returns
> a wrapped stream around a binary stream returned from
> :func:`get_binary_stream` but it also can take shortcuts for already
> correctly configured streams.
> 
> :param name: the name of the stream to open.  Valid names are ``'stdin'``,
>              ``'stdout'`` and ``'stderr'``
> :param encoding: overrides the detected default encoding.
> :param errors: overrides the default error mode.

##### `open_file(filename, mode, encoding, errors, lazy, atomic)`

**Line:** 361 | **Returns:** `t.IO[t.Any]`

**Parameters:**
- `filename` (str | os.PathLike[str])
- `mode` (str)
- `encoding` (str | None)
- `errors` (str | None)
- `lazy` (bool)
- `atomic` (bool)

**Documentation:**

> Open a file, with extra behavior to handle ``'-'`` to indicate
> a standard stream, lazy open on write, and atomic write. Similar to
> the behavior of the :class:`~click.File` param type.
> 
> If ``'-'`` is given to open ``stdout`` or ``stdin``, the stream is
> wrapped so that using it in a context manager will not close it.
> This makes it possible to use the function without accidentally
> closing a standard stream:
> 
> .. code-block:: python
> 
>     with open_file(filename) as f:
>         ...
> 
> :param filename: The name or Path of the file to open, or ``'-'`` for
>     ``stdin``/``stdout``.
> :param mode: The mode in which to open the file.
> :param encoding: The encoding to decode or encode a file opened in
>     text mode.
> :param errors: The error handling mode.
> :param lazy: Wait to open the file until it is accessed. For read
>     mode, the file is temporarily opened to raise access errors
>     early, then closed until it is read again.
> :param atomic: Write to a temporary file and replace the given file
>     on close.
> 
> .. versionadded:: 3.0

##### `format_filename(filename, shorten)`

**Line:** 410 | **Returns:** `str`

**Parameters:**
- `filename` (str | bytes | os.PathLike[str] | os.PathLike[bytes])
- `shorten` (bool)

**Documentation:**

> Format a filename as a string for display. Ensures the filename can be
> displayed by replacing any invalid bytes or surrogate escapes in the name
> with the replacement character ``�``.
> 
> Invalid bytes or surrogate escapes will raise an error when written to a
> stream with ``errors="strict"``. This will typically happen with ``stdout``
> when the locale is something like ``en_GB.UTF-8``.
> 
> Many scenarios *are* safe to write surrogates though, due to PEP 538 and
> PEP 540, including:
> 
> -   Writing to ``stderr``, which uses ``errors="backslashreplace"``.
> -   The system has ``LANG=C.UTF-8``, ``C``, or ``POSIX``. Python opens
>     stdout and stderr with ``errors="surrogateescape"``.
> -   None of ``LANG/LC_*`` are set. Python assumes ``LANG=C.UTF-8``.
> -   Python is started in UTF-8 mode  with  ``PYTHONUTF8=1`` or ``-X utf8``.
>     Python opens stdout and stderr with ``errors="surrogateescape"``.
> 
> :param filename: formats a filename for UI display.  This will also convert
>                  the filename into unicode without failing.
> :param shorten: this optionally shortens the filename to strip of the
>                 path that leads up to it.

##### `get_app_dir(app_name, roaming, force_posix)`

**Line:** 452 | **Returns:** `str`

**Parameters:**
- `app_name` (str)
- `roaming` (bool)
- `force_posix` (bool)

**Documentation:**

> Returns the config folder for the application.  The default behavior
> is to return whatever is most appropriate for the operating system.
> 
> To give you an idea, for an app called ``"Foo Bar"``, something like
> the following folders could be returned:
> 
> Mac OS X:
>   ``~/Library/Application Support/Foo Bar``
> Mac OS X (POSIX):
>   ``~/.foo-bar``
> Unix:
>   ``~/.config/foo-bar``
> Unix (POSIX):
>   ``~/.foo-bar``
> Windows (roaming):
>   ``C:\Users\<user>\AppData\Roaming\Foo Bar``
> Windows (not roaming):
>   ``C:\Users\<user>\AppData\Local\Foo Bar``
> 
> .. versionadded:: 2.0
> 
> :param app_name: the application name.  This should be properly capitalized
>                  and can contain whitespace.
> :param roaming: controls if the folder should be roaming or not on Windows.
>                 Has no effect otherwise.
> :param force_posix: if this is set to `True` then on any POSIX system the
>                     folder will be stored in the home folder with a leading
>                     dot instead of the XDG config home or darwin's
>                     application support folder.

##### `_detect_program_name(path, _main)`

**Line:** 526 | **Returns:** `str`

**Parameters:**
- `path` (str | None)
- `_main` (ModuleType | None)

**Documentation:**

> Determine the command used to run the program, for use in help
> text. If a file or entry point was executed, the file name is
> returned. If ``python -m`` was used to execute a module or package,
> ``python -m name`` is returned.
> 
> This doesn't try to be too precise, the goal is to give a concise
> name for help text. Files are only shown as their name without the
> path. ``python`` is only shown for modules, and the full path to
> ``sys.executable`` is not shown.
> 
> :param path: The Python file being executed. Python puts this in
>     ``sys.argv[0]``, which is used by default.
> :param _main: The ``__main__`` module. This should only be passed
>     during internal testing.
> 
> .. versionadded:: 8.0
>     Based on command args detection in the Werkzeug reloader.
> 
> :meta private:

##### `_expand_args(args)`

**Line:** 581 | **Returns:** `list[str]`

**Parameters:**
- `args` (cabc.Iterable[str])

**Documentation:**

> Simulate Unix shell expansion with Python functions.
> 
> See :func:`glob.glob`, :func:`os.path.expanduser`, and
> :func:`os.path.expandvars`.
> 
> This is intended for use on Windows, where the shell does not do any
> expansion. It may not exactly match what a Unix shell would do.
> 
> :param args: List of command line arguments to expand.
> :param user: Expand user home directory.
> :param env: Expand environment variables.
> :param glob_recursive: ``**`` matches directories recursively.
> 
> .. versionchanged:: 8.1
>     Invalid glob patterns are treated as empty expansions rather
>     than raising an error.
> 
> .. versionadded:: 8.0
> 
> :meta private:

#### Classes

##### Class: `LazyFile`

**Line:** 112

**Documentation:**

> A lazy file works like a regular file but it does not fully open
> the file but it does perform some basic checks early to see if the
> filename parameter does make sense.  This is useful for safely opening
> files for writing.

**Methods:**

- **`__init__(self, filename, mode, encoding, errors, atomic)`** (Line 119)
  - Returns: `None`
  - _No documentation_

- **`__getattr__(self, name)`** (Line 146)
  - Returns: `t.Any`
  - _No documentation_

- **`__repr__(self)`** (Line 149)
  - Returns: `str`
  - _No documentation_

- **`open(self)`** (Line 154)
  - Returns: `t.IO[t.Any]`
  - Opens the file if it's not yet open.  This call might fail with

- **`close(self)`** (Line 172)
  - Returns: `None`
  - Closes the underlying file, no matter what.

- **`close_intelligently(self)`** (Line 177)
  - Returns: `None`
  - This function only closes the file if it was opened by the lazy

- **`__enter__(self)`** (Line 184)
  - Returns: `LazyFile`
  - _No documentation_

- **`__exit__(self, exc_type, exc_value, tb)`** (Line 187)
  - Returns: `None`
  - _No documentation_

- **`__iter__(self)`** (Line 195)
  - Returns: `cabc.Iterator[t.AnyStr]`
  - _No documentation_

##### Class: `KeepOpenFile`

**Line:** 200

**Documentation:** _No documentation_

**Methods:**

- **`__init__(self, file)`** (Line 201)
  - Returns: `None`
  - _No documentation_

- **`__getattr__(self, name)`** (Line 204)
  - Returns: `t.Any`
  - _No documentation_

- **`__enter__(self)`** (Line 207)
  - Returns: `KeepOpenFile`
  - _No documentation_

- **`__exit__(self, exc_type, exc_value, tb)`** (Line 210)
  - Returns: `None`
  - _No documentation_

- **`__repr__(self)`** (Line 218)
  - Returns: `str`
  - _No documentation_

- **`__iter__(self)`** (Line 221)
  - Returns: `cabc.Iterator[t.AnyStr]`
  - _No documentation_

##### Class: `PacifyFlushWrapper`

**Line:** 501

**Documentation:**

> This wrapper is used to catch and suppress BrokenPipeErrors resulting
> from ``.flush()`` being called on broken pipe during the shutdown/final-GC
> of the Python interpreter. Notably ``.flush()`` is always called on
> ``sys.stdout`` and ``sys.stderr``. So as to have minimal impact on any
> other cleanup code, and the case where the underlying file is not a broken
> pipe, all calls and attributes are proxied.

**Methods:**

- **`__init__(self, wrapped)`** (Line 510)
  - Returns: `None`
  - _No documentation_

- **`flush(self)`** (Line 513)
  - Returns: `None`
  - _No documentation_

- **`__getattr__(self, attr)`** (Line 522)
  - Returns: `t.Any`
  - _No documentation_

---

### `C:\Users\I.C.T\OneDrive\Documents\git\click\tests\conftest.py`

**Language:** python

#### Functions

##### `runner(request)`

**Line:** 7 | **Returns:** `None`

**Parameters:**
- `request`

**Documentation:** _No documentation_

---

### `C:\Users\I.C.T\OneDrive\Documents\git\click\tests\test_arguments.py`

**Language:** python

#### Functions

##### `test_nargs_star(runner)`

**Line:** 10 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_nargs_tup(runner)`

**Line:** 23 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_nargs_tup_composite(runner, opts)`

**Line:** 46 | **Returns:** `None`

**Parameters:**
- `runner`
- `opts`

**Documentation:** _No documentation_

##### `test_nargs_mismatch_with_tuple_type()`

**Line:** 58 | **Returns:** `None`

**Documentation:** _No documentation_

##### `test_nargs_err(runner)`

**Line:** 67 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_bytes_args(runner, monkeypatch)`

**Line:** 82 | **Returns:** `None`

**Parameters:**
- `runner`
- `monkeypatch`

**Documentation:** _No documentation_

##### `test_file_args(runner)`

**Line:** 105 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_path_allow_dash(runner)`

**Line:** 128 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_file_atomics(runner)`

**Line:** 139 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_stdout_default(runner)`

**Line:** 159 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_nargs_envvar(runner, nargs, value, expect)`

**Line:** 184 | **Returns:** `None`

**Parameters:**
- `runner`
- `nargs`
- `value`
- `expect`

**Documentation:** _No documentation_

##### `test_nargs_envvar_only_if_values_empty(runner)`

**Line:** 204 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_empty_nargs(runner)`

**Line:** 217 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_missing_arg(runner)`

**Line:** 237 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_required_argument(value, expect_missing, processed_value)`

**Line:** 272 | **Returns:** `None`

**Parameters:**
- `value`
- `expect_missing`
- `processed_value`

**Documentation:**

> Test how a required argument is processing the provided values.

##### `test_implicit_non_required(runner)`

**Line:** 287 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_deprecated_usage(runner)`

**Line:** 298 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_deprecated_warning(runner, deprecated)`

**Line:** 310 | **Returns:** `None`

**Parameters:**
- `runner`
- `deprecated`

**Documentation:** _No documentation_

##### `test_deprecated_required(runner)`

**Line:** 331 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_eat_options(runner)`

**Line:** 336 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_nargs_star_ordering(runner)`

**Line:** 352 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_nargs_specified_plus_star_ordering(runner)`

**Line:** 365 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_good_defaults_for_nargs(runner, argument_params, args, expected)`

**Line:** 401 | **Returns:** `None`

**Parameters:**
- `runner`
- `argument_params`
- `args`
- `expected`

**Documentation:**

> Comprehensive check of default-value processing for arguments with
> ``nargs``.
> 
> .. hint::
>     An option-specific equivalent is available in
>     ``test_options.py::test_good_defaults_for_multiple``.
> 
>     A smoke test covering a single basic case is in
>     ``test_defaults.py::test_nargs_plus_multiple``.

##### `test_bad_defaults_for_nargs(runner, default, message)`

**Line:** 488 | **Returns:** `None`

**Parameters:**
- `runner`
- `default`
- `message`

**Documentation:**

> Some defaults are not valid when nargs is set.

##### `test_multiple_param_decls_not_allowed(runner)`

**Line:** 500 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_multiple_not_allowed()`

**Line:** 509 | **Returns:** `None`

**Documentation:** _No documentation_

##### `test_subcommand_help(runner)`

**Line:** 514 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_nested_subcommand_help(runner)`

**Line:** 533 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_when_argument_decorator_is_used_multiple_times_cls_is_preserved()`

**Line:** 555 | **Returns:** `None`

**Documentation:** _No documentation_

##### `test_duplicate_names_warning(runner, args_one, args_two)`

**Line:** 584 | **Returns:** `None`

**Parameters:**
- `runner`
- `args_one`
- `args_two`

**Documentation:** _No documentation_

##### `test_argument_custom_class_can_override_type_cast_value_and_never_sees_unset(runner, argument_kwargs, pass_argv)`

**Line:** 608 | **Returns:** `None`

**Parameters:**
- `runner`
- `argument_kwargs`
- `pass_argv`

**Documentation:**

> Test that overriding type_cast_value is supported
> 
> In particular, the argument is never passed an UNSET sentinel value.

#### Classes

##### Class: `CustomArgument`

**Line:** 556

**Documentation:** _No documentation_

##### Class: `CustomArgument`

**Line:** 617

**Documentation:** _No documentation_

**Methods:**

- **`type_cast_value(self, ctx, value)`** (Line 618)
  - Returns: `None`
  - _No documentation_

---

### `C:\Users\I.C.T\OneDrive\Documents\git\click\tests\test_basic.py`

**Language:** python

#### Functions

##### `test_basic_functionality(runner)`

**Line:** 13 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_repr()`

**Line:** 32 | **Returns:** `None`

**Documentation:** _No documentation_

##### `test_return_values()`

**Line:** 50 | **Returns:** `None`

**Documentation:** _No documentation_

##### `test_basic_group(runner)`

**Line:** 60 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_group_commands_dict(runner)`

**Line:** 86 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:**

> A Group can be built with a dict of commands.

##### `test_group_from_list(runner)`

**Line:** 98 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:**

> A Group can be built with a list of commands.

##### `test_string_option(runner, args, expect)`

**Line:** 120 | **Returns:** `None`

**Parameters:**
- `runner`
- `args`
- `expect`

**Documentation:** _No documentation_

##### `test_int_option(runner, args, expect)`

**Line:** 143 | **Returns:** `None`

**Parameters:**
- `runner`
- `args`
- `expect`

**Documentation:** _No documentation_

##### `test_uuid_option(runner, args, expect)`

**Line:** 169 | **Returns:** `None`

**Parameters:**
- `runner`
- `args`
- `expect`

**Documentation:** _No documentation_

##### `test_float_option(runner, args, expect)`

**Line:** 194 | **Returns:** `None`

**Parameters:**
- `runner`
- `args`
- `expect`

**Documentation:** _No documentation_

##### `test_boolean_switch(runner, args, default, expect)`

**Line:** 226 | **Returns:** `None`

**Parameters:**
- `runner`
- `args`
- `default`
- `expect`

**Documentation:** _No documentation_

##### `test_boolean_flag(runner, default, args, expect)`

**Line:** 249 | **Returns:** `None`

**Parameters:**
- `runner`
- `default`
- `args`
- `expect`

**Documentation:** _No documentation_

##### `test_boolean_conversion(runner, value, expect)`

**Line:** 266 | **Returns:** `None`

**Parameters:**
- `runner`
- `value`
- `expect`

**Documentation:** _No documentation_

##### `test_flag_value_dual_options(runner, default, args, expected)`

**Line:** 314 | **Returns:** `None`

**Parameters:**
- `runner`
- `default`
- `args`
- `expected`

**Documentation:**

> Check how default is processed when options compete for the same variable name.
> 
> Covers the regression reported in
> https://github.com/pallets/click/issues/3024#issuecomment-3146199461
> 
> .. hint::
>     Similar to ``test_options.py::test_default_dual_option_callback``.
> 
>     ``test_defaults.py::test_shared_param_prefers_first_default``
>     is a smoke-test complement that exercises both default placements.

##### `test_file_option(runner)`

**Line:** 337 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_file_lazy_mode(runner)`

**Line:** 358 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_path_option(runner)`

**Line:** 398 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_choice_option(runner)`

**Line:** 444 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_choice_argument(runner)`

**Line:** 465 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_choice_argument_enum(runner)`

**Line:** 486 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_choice_argument_custom_type(runner)`

**Line:** 513 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_choice_argument_none(runner)`

**Line:** 544 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_datetime_option_default(runner)`

**Line:** 572 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_datetime_option_custom(runner)`

**Line:** 599 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_required_option(runner)`

**Line:** 610 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_evaluation_order(runner)`

**Line:** 621 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_hidden_option(runner)`

**Line:** 664 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_hidden_command(runner)`

**Line:** 675 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_hidden_group(runner)`

**Line:** 689 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_summary_line(runner)`

**Line:** 708 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_help_invalid_default(runner)`

**Line:** 727 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

#### Classes

##### Class: `MyEnum`

**Line:** 487

**Documentation:** _No documentation_

##### Class: `MyClass`

**Line:** 514

**Documentation:** _No documentation_

**Methods:**

- **`__init__(self, value)`** (Line 515)
  - Returns: `None`
  - _No documentation_

- **`__str__(self)`** (Line 518)
  - Returns: `str`
  - _No documentation_

---

### `C:\Users\I.C.T\OneDrive\Documents\git\click\tests\test_chain.py`

**Language:** python

#### Functions

##### `debug()`

**Line:** 8 | **Returns:** `None`

**Documentation:** _No documentation_

##### `test_basic_chaining(runner)`

**Line:** 15 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_chaining_help(runner, args, expect)`

**Line:** 47 | **Returns:** `None`

**Parameters:**
- `runner`
- `args`
- `expect`

**Documentation:** _No documentation_

##### `test_chaining_with_options(runner)`

**Line:** 68 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_no_command_result_callback(runner, chain, expect)`

**Line:** 89 | **Returns:** `None`

**Parameters:**
- `runner`
- `chain`
- `expect`

**Documentation:**

> When a group has ``invoke_without_command=True``, the result
> callback is always invoked. A regular group invokes it with
> its return value, a chained group with ``[]``.

##### `test_chaining_with_arguments(runner)`

**Line:** 107 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_pipeline(runner, args, input, expect)`

**Line:** 135 | **Returns:** `None`

**Parameters:**
- `runner`
- `args`
- `input`
- `expect`

**Documentation:** _No documentation_

##### `test_args_and_chain(runner)`

**Line:** 170 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_group_arg_behavior(runner)`

**Line:** 192 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_group_chaining(runner)`

**Line:** 222 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

---

### `C:\Users\I.C.T\OneDrive\Documents\git\click\tests\test_command_decorators.py`

**Language:** python

#### Functions

##### `test_command_no_parens(runner)`

**Line:** 6 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_custom_command_no_parens(runner)`

**Line:** 16 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_group_no_parens(runner)`

**Line:** 36 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_params_argument(runner)`

**Line:** 62 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_generate_name(name)`

**Line:** 86 | **Returns:** `None`

**Parameters:**
- `name` (str)

**Documentation:** _No documentation_

#### Classes

##### Class: `CustomCommand`

**Line:** 17

**Documentation:** _No documentation_

##### Class: `CustomGroup`

**Line:** 20

**Documentation:** _No documentation_

---

### `C:\Users\I.C.T\OneDrive\Documents\git\click\tests\test_commands.py`

**Language:** python

#### Functions

##### `test_other_command_invoke(runner)`

**Line:** 8 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_other_command_forward(runner)`

**Line:** 24 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_forwarded_params_consistency(runner)`

**Line:** 44 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_auto_shorthelp(runner)`

**Line:** 66 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_command_no_args_is_help(runner)`

**Line:** 98 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_default_maps(runner)`

**Line:** 104 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_group_with_args(runner, args, exit_code, expect)`

**Line:** 129 | **Returns:** `None`

**Parameters:**
- `runner`
- `args`
- `exit_code`
- `expect`

**Documentation:** _No documentation_

##### `test_custom_parser(runner)`

**Line:** 144 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_object_propagation(runner)`

**Line:** 210 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_other_command_invoke_with_defaults(runner, opt_params, expected)`

**Line:** 262 | **Returns:** `None`

**Parameters:**
- `runner`
- `opt_params`
- `expected`

**Documentation:** _No documentation_

##### `test_invoked_subcommand(runner)`

**Line:** 279 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_aliased_command_canonical_name(runner)`

**Line:** 302 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_group_add_command_name(runner)`

**Line:** 322 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_iter_params_for_processing(invocation_order, declaration_order, expected_order)`

**Line:** 374 | **Returns:** `None`

**Parameters:**
- `invocation_order`
- `declaration_order`
- `expected_order`

**Documentation:** _No documentation_

##### `test_help_param_priority(runner)`

**Line:** 395 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:**

> Cover the edge-case in which the eagerness of help option was not
> respected, because it was internally generated multiple times.
> 
> See: https://github.com/pallets/click/pull/2811

##### `test_unprocessed_options(runner)`

**Line:** 464 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_deprecated_in_help_messages(runner, doc, deprecated)`

**Line:** 482 | **Returns:** `None`

**Parameters:**
- `runner`
- `doc`
- `deprecated`

**Documentation:** _No documentation_

##### `test_deprecated_in_invocation(runner, deprecated)`

**Line:** 495 | **Returns:** `None`

**Parameters:**
- `runner`
- `deprecated`

**Documentation:** _No documentation_

##### `test_command_parse_args_collects_option_prefixes()`

**Line:** 507 | **Returns:** `None`

**Documentation:** _No documentation_

##### `test_group_parse_args_collects_base_option_prefixes()`

**Line:** 520 | **Returns:** `None`

**Documentation:** _No documentation_

##### `test_group_invoke_collects_used_option_prefixes(runner)`

**Line:** 542 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_abort_exceptions_with_disabled_standalone_mode(runner, exc)`

**Line:** 567 | **Returns:** `None`

**Parameters:**
- `runner`
- `exc`

**Documentation:** _No documentation_

##### `test_unknown_command(runner)`

**Line:** 578 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_suggest_possible_commands(runner, value, expect)`

**Line:** 591 | **Returns:** `None`

**Parameters:**
- `runner`
- `value`
- `expect`

**Documentation:** _No documentation_

#### Classes

##### Class: `OptParseCommand`

**Line:** 151

**Documentation:** _No documentation_

**Methods:**

- **`__init__(self, name, parser, callback)`** (Line 152)
  - Returns: `None`
  - _No documentation_

- **`parse_args(self, ctx, args)`** (Line 157)
  - Returns: `None`
  - _No documentation_

- **`get_usage(self, ctx)`** (Line 165)
  - Returns: `None`
  - _No documentation_

- **`get_help(self, ctx)`** (Line 168)
  - Returns: `None`
  - _No documentation_

- **`invoke(self, ctx)`** (Line 171)
  - Returns: `None`
  - _No documentation_

##### Class: `AliasedGroup`

**Line:** 303

**Documentation:** _No documentation_

**Methods:**

- **`get_command(self, ctx, cmd_name)`** (Line 304)
  - Returns: `None`
  - _No documentation_

- **`resolve_command(self, ctx, args)`** (Line 307)
  - Returns: `None`
  - _No documentation_

---

### `C:\Users\I.C.T\OneDrive\Documents\git\click\tests\test_compat.py`

**Language:** python

#### Functions

##### `test_is_jupyter_kernel_output()`

**Line:** 10 | **Returns:** `None`

**Documentation:** _No documentation_

##### `test_should_strip_ansi(monkeypatch, stream, color, expected_override, isatty, is_jupyter, expected)`

**Line:** 39 | **Returns:** `None`

**Parameters:**
- `monkeypatch`
- `stream`
- `color` (bool | None)
- `expected_override` (bool | None)
- `isatty` (bool)
- `is_jupyter` (bool)
- `expected` (bool)

**Documentation:** _No documentation_

#### Classes

##### Class: `JupyterKernelFakeStream`

**Line:** 11

**Documentation:** _No documentation_

---

### `C:\Users\I.C.T\OneDrive\Documents\git\click\tests\test_context.py`

**Language:** python

#### Functions

##### `test_ensure_context_objects(runner)`

**Line:** 17 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_get_context_objects(runner)`

**Line:** 39 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_get_context_objects_no_ensuring(runner)`

**Line:** 62 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_get_context_objects_missing(runner)`

**Line:** 85 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_multi_enter(runner)`

**Line:** 110 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_global_context_object(runner)`

**Line:** 130 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_context_meta(runner)`

**Line:** 143 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_make_pass_meta_decorator(runner)`

**Line:** 162 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_make_pass_meta_decorator_doc()`

**Line:** 177 | **Returns:** `None`

**Documentation:** _No documentation_

##### `test_hiding_of_unset_sentinel_in_callbacks()`

**Line:** 184 | **Returns:** `None`

**Documentation:**

> Fix: https://github.com/pallets/click/issues/3136

##### `test_context_pushing()`

**Line:** 294 | **Returns:** `None`

**Documentation:** _No documentation_

##### `test_pass_obj(runner)`

**Line:** 320 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_close_before_pop(runner)`

**Line:** 336 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_close_before_exit(runner)`

**Line:** 357 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_multiple_eager_callbacks(runner, cli_args, expect)`

**Line:** 395 | **Returns:** `None`

**Parameters:**
- `runner`
- `cli_args`
- `expect`

**Documentation:**

> Checks all callbacks are called on exit, even the nasty ones hidden within
> callbacks.
> 
> Also checks the order in which they're called.

##### `test_no_state_leaks(runner)`

**Line:** 436 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:**

> Demonstrate state leaks with a specific case of the generic test above.
> 
> Use a logger as a real-world example of a common fixture which, due to its global
> nature, can leak state if not clean-up properly in a callback.

##### `test_with_resource()`

**Line:** 522 | **Returns:** `None`

**Documentation:** _No documentation_

##### `test_with_resource_exception()`

**Line:** 538 | **Returns:** `None`

**Documentation:** _No documentation_

##### `test_with_resource_nested_exception()`

**Line:** 592 | **Returns:** `None`

**Documentation:** _No documentation_

##### `test_make_pass_decorator_args(runner)`

**Line:** 663 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:**

> Test to check that make_pass_decorator doesn't consume arguments based on
> invocation order.

##### `test_propagate_show_default_setting(runner)`

**Line:** 700 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:**

> A context's ``show_default`` setting defaults to the value from
> the parent context.

##### `test_exit_not_standalone()`

**Line:** 714 | **Returns:** `None`

**Documentation:** _No documentation_

##### `test_parameter_source(runner, option_args, invoke_args, expect)`

**Line:** 766 | **Returns:** `None`

**Parameters:**
- `runner`
- `option_args`
- `invoke_args`
- `expect`

**Documentation:** _No documentation_

##### `test_propagate_opt_prefixes()`

**Line:** 777 | **Returns:** `None`

**Documentation:** _No documentation_

#### Classes

##### Class: `Foo`

**Line:** 18

**Documentation:** _No documentation_

**Methods:**

- **`__init__(self)`** (Line 19)
  - Returns: `None`
  - _No documentation_

##### Class: `Foo`

**Line:** 40

**Documentation:** _No documentation_

**Methods:**

- **`__init__(self)`** (Line 41)
  - Returns: `None`
  - _No documentation_

##### Class: `Foo`

**Line:** 63

**Documentation:** _No documentation_

**Methods:**

- **`__init__(self)`** (Line 64)
  - Returns: `None`
  - _No documentation_

##### Class: `Foo`

**Line:** 86

**Documentation:** _No documentation_

##### Class: `ParameterInternalCheck`

**Line:** 199

**Documentation:**

> An option that checks internal state during processing.

**Methods:**

- **`process_value(self, ctx, value)`** (Line 202)
  - Returns: `None`
  - Check that UNSET values are hidden as None in ctx.params within the

##### Class: `NonExitingOption`

**Line:** 404

**Documentation:** _No documentation_

**Methods:**

- **`reset_state(self)`** (Line 405)
  - Returns: `None`
  - _No documentation_

- **`set_state(self, ctx, param, value)`** (Line 408)
  - Returns: `str`
  - _No documentation_

- **`__init__(self, *args, **kwargs)`** (Line 412)
  - Returns: `None`
  - _No documentation_

##### Class: `ExitingOption`

**Line:** 417

**Documentation:** _No documentation_

**Methods:**

- **`set_state(self, ctx, param, value)`** (Line 418)
  - Returns: `str`
  - _No documentation_

##### Class: `DebugLoggerOption`

**Line:** 445

**Documentation:**

> A custom option to set the name of the debug logger.

**Methods:**

- **`reset_loggers(self)`** (Line 451)
  - Returns: `None`
  - Forces logger managed by the option to be reset to the default level.

- **`set_level(self, ctx, param, value)`** (Line 462)
  - Returns: `None`
  - Set the logger to DEBUG level.

- **`__init__(self, *args, **kwargs)`** (Line 481)
  - Returns: `None`
  - _No documentation_

##### Class: `TestContext`

**Line:** 539

**Documentation:** _No documentation_

**Methods:**

- **`__init__(self, base_val)`** (Line 544)
  - Returns: `None`
  - _No documentation_

- **`__enter__(self)`** (Line 548)
  - Returns: `list[int]`
  - _No documentation_

- **`__exit__(self, exc_type, exc_value, traceback)`** (Line 552)
  - Returns: `bool | None`
  - _No documentation_

##### Class: `TestException`

**Line:** 565

**Documentation:** _No documentation_

##### Class: `TestContext`

**Line:** 593

**Documentation:** _No documentation_

**Methods:**

- **`__init__(self, base_val)`** (Line 598)
  - Returns: `None`
  - _No documentation_

- **`__enter__(self)`** (Line 602)
  - Returns: `list[int]`
  - _No documentation_

- **`__exit__(self, exc_type, exc_value, traceback)`** (Line 606)
  - Returns: `bool | None`
  - _No documentation_

##### Class: `TestException`

**Line:** 619

**Documentation:** _No documentation_

##### Class: `Foo`

**Line:** 669

**Documentation:** _No documentation_

---

### `C:\Users\I.C.T\OneDrive\Documents\git\click\tests\test_custom_classes.py`

**Language:** python

#### Functions

##### `test_command_context_class()`

**Line:** 4 | **Returns:** `None`

**Documentation:**

> A command with a custom ``context_class`` should produce a
> context using that type.

##### `test_context_invoke_type(runner)`

**Line:** 20 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:**

> A command invoked from a custom context should have a new
> context with the same type.

##### `test_context_formatter_class()`

**Line:** 47 | **Returns:** `None`

**Documentation:**

> A context with a custom ``formatter_class`` should format help
> using that type.

##### `test_group_command_class(runner)`

**Line:** 66 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:**

> A group with a custom ``command_class`` should create subcommands
> of that type by default.

##### `test_group_group_class(runner)`

**Line:** 84 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:**

> A group with a custom ``group_class`` should create subgroups
> of that type by default.

##### `test_group_group_class_self(runner)`

**Line:** 102 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:**

> A group with ``group_class = type`` should create subgroups of
> the same type as itself.

#### Classes

##### Class: `CustomContext`

**Line:** 9

**Documentation:** _No documentation_

##### Class: `CustomCommand`

**Line:** 12

**Documentation:** _No documentation_

##### Class: `CustomContext`

**Line:** 25

**Documentation:** _No documentation_

##### Class: `CustomCommand`

**Line:** 28

**Documentation:** _No documentation_

##### Class: `CustomFormatter`

**Line:** 52

**Documentation:** _No documentation_

**Methods:**

- **`write_heading(self, heading)`** (Line 53)
  - Returns: `None`
  - _No documentation_

##### Class: `CustomContext`

**Line:** 57

**Documentation:** _No documentation_

##### Class: `CustomCommand`

**Line:** 71

**Documentation:** _No documentation_

##### Class: `CustomGroup`

**Line:** 74

**Documentation:** _No documentation_

##### Class: `CustomSubGroup`

**Line:** 89

**Documentation:** _No documentation_

##### Class: `CustomGroup`

**Line:** 92

**Documentation:** _No documentation_

##### Class: `CustomGroup`

**Line:** 107

**Documentation:** _No documentation_

---

### `C:\Users\I.C.T\OneDrive\Documents\git\click\tests\test_defaults.py`

**Language:** python

#### Functions

##### `test_basic_defaults(runner, default, type, expected_output, expected_type)`

**Line:** 19 | **Returns:** `None`

**Parameters:**
- `runner`
- `default`
- `type`
- `expected_output`
- `expected_type`

**Documentation:**

> Smoke test: a single option's default is type-coerced.
> 
> This covers basic single-option default type coercion.

##### `test_multiple_defaults(runner)`

**Line:** 36 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:**

> Smoke test: each element in a multiple-option default is type-coerced.
> 
> .. hint::
>     ``test_options.py::test_good_defaults_for_multiple``
>     covers the structural default processing (``list`` to
>     ``tuple``, various ``nargs``) exhaustively.
> 
>     This test fills the gap of explicit
>     ``type=click.FLOAT`` coercion on the elements.

##### `test_nargs_plus_multiple(runner)`

**Line:** 60 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:**

> Smoke test: option with ``nargs=2`` + ``multiple=True`` and a
> tuple-of-tuples default.
> 
> .. hint::
>     ``test_options.py::test_good_defaults_for_multiple``
>     expands this with many more edge cases with various
>     ``nargs``/``multiple``/``default`` combinations.
> 
>     An argument-specific equivalent is in
>     ``test_arguments.py::test_good_defaults_for_nargs``.

##### `test_multiple_flag_default(runner)`

**Line:** 86 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:**

> Default for flags when multiple=True should be empty tuple.

##### `test_flag_default_map(runner)`

**Line:** 107 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:**

> test flag with default map

##### `test_shared_param_prefers_first_default(runner)`

**Line:** 132 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:**

> The first ``default=True`` wins when multiple ``flag_value`` options share
> a parameter name, regardless of which positional option carries it.
> 
> .. hint::
>     ``test_basic.py::test_flag_value_dual_options`` and
>     ``test_options.py::test_default_dual_option_callback`` are wider
>     parametrized sibling tests covering many more default-value types (``None``,
>     ``UNSET``, strings, numbers) but always place the default on the first
>     option. This test complements them by exercising both placements.

##### `test_lookup_default_returns_hides_sentinel(default_map, key, expected)`

**Line:** 184 | **Returns:** `None`

**Parameters:**
- `default_map`
- `key`
- `expected`

**Documentation:**

> ``lookup_default()`` should return ``None`` for missing keys, not :attr:`UNSET`.
> 
> Regression test for https://github.com/pallets/click/issues/3145.

##### `test_lookup_default_callable_in_default_map(runner)`

**Line:** 196 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:**

> A callable in ``default_map`` is invoked with ``call=True``
> (the default) and returned as-is with ``call=False``.
> 
> Click uses both paths internally:
> - ``get_default()`` passes ``call=False``,
> - ``resolve_ctx()`` passes ``call=True``.

##### `test_default_map_source(runner, args, default_map, expected_value, expected_source)`

**Line:** 247 | **Returns:** `None`

**Parameters:**
- `runner`
- `args`
- `default_map`
- `expected_value`
- `expected_source`

**Documentation:**

> ``get_parameter_source()`` reports the correct origin for a parameter
> value across the resolution chain: CLI > default_map > parameter default.

##### `test_lookup_default_override_respected(runner)`

**Line:** 268 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:**

> A subclass override of ``lookup_default()`` should be called by Click
> internals, not bypassed by a private method.
> 
> Reproduce exactly https://github.com/pallets/click/issues/3145 in which a
> subclass that falls back to prefix-based lookup when the parent returns
> ``None``.
> 
> Previous attempts in https://github.com/pallets/click/pr/3199 were entirely
> bypassing the user's overridden method.

##### `test_default_map_with_callable_flag_value(runner, default_map, args, expected)`

**Line:** 339 | **Returns:** `None`

**Parameters:**
- `runner`
- `default_map`
- `args`
- `expected`

**Documentation:**

> ``default_map`` entries should override the auto-aligned callable ``flag_value``,
> and callable entries in ``default_map`` should still be invoked.
> 
> Verifies the fix for https://github.com/pallets/click/issues/3121 does not
> break ``default_map`` precedence.

##### `test_default_map_nargs(runner, default_map, option_kwargs, cli_args, expected)`

**Line:** 380 | **Returns:** `None`

**Parameters:**
- `runner`
- `default_map`
- `option_kwargs`
- `cli_args`
- `expected`

**Documentation:**

> A string in ``default_map`` for an option with ``nargs > 1`` should be
> split the same way an environment variable string is split.
> 
> Regression test for https://github.com/pallets/click/issues/2745.

##### `test_unset_in_default_map(runner)`

**Line:** 397 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:**

> An ``UNSET`` value in ``default_map`` should be treated as if
> the key is absent, and so fallback to the parameter's own default.
> 
> Refs: https://github.com/pallets/click/pull/3224#issuecomment-3968643305

#### Classes

##### Class: `CustomContext`

**Line:** 280

**Documentation:** _No documentation_

**Methods:**

- **`lookup_default(self, name, call)`** (Line 281)
  - Returns: `None`
  - _No documentation_

##### Class: `_Marker`

**Line:** 316

**Documentation:**

> Dummy callable used as a flag_value in default tests.

---

### `C:\Users\I.C.T\OneDrive\Documents\git\click\tests\test_formatting.py`

**Language:** python

#### Functions

##### `test_basic_functionality(runner)`

**Line:** 6 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_wrapping_long_options_strings(runner)`

**Line:** 54 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_wrapping_long_command_name(runner)`

**Line:** 89 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_formatting_empty_help_lines(runner)`

**Line:** 124 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_formatting_usage_error(runner)`

**Line:** 147 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_formatting_usage_error_metavar_missing_arg(runner)`

**Line:** 163 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:**

> :author: @r-m-n
> Including attribution to #612

##### `test_formatting_usage_error_metavar_bad_arg(runner)`

**Line:** 184 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_formatting_usage_error_nested(runner)`

**Line:** 200 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_formatting_usage_error_no_help(runner)`

**Line:** 220 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_formatting_usage_custom_help(runner)`

**Line:** 235 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_formatting_usage_error_help_hint(runner, help_names, extra_options, expected_hint)`

**Line:** 284 | **Returns:** `None`

**Parameters:**
- `runner`
- `help_names`
- `extra_options`
- `expected_hint`

**Documentation:**

> The error hint should only show non-shadowed help option names,
> picking the longest for readability.
> 
> https://github.com/pallets/click/issues/2790

##### `test_formatting_custom_type_metavar(runner)`

**Line:** 316 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_truncating_docstring(runner)`

**Line:** 337 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_truncating_docstring_no_help(runner)`

**Line:** 366 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_removing_multiline_marker(runner)`

**Line:** 386 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_global_show_default(runner)`

**Line:** 405 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_formatting_with_options_metavar_empty(runner)`

**Line:** 422 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_help_formatter_write_text()`

**Line:** 428 | **Returns:** `None`

**Documentation:** _No documentation_

#### Classes

##### Class: `MyType`

**Line:** 317

**Documentation:** _No documentation_

**Methods:**

- **`get_metavar(self, param, ctx)`** (Line 318)
  - Returns: `None`
  - _No documentation_

---

### `C:\Users\I.C.T\OneDrive\Documents\git\click\tests\test_imports.py`

**Language:** python

#### Functions

##### `test_light_imports()`

**Line:** 69 | **Returns:** `None`

**Documentation:** _No documentation_

---

### `C:\Users\I.C.T\OneDrive\Documents\git\click\tests\test_info_dict.py`

**Language:** python

#### Functions

##### `test_parameter(obj, expect)`

**Line:** 211 | **Returns:** `None`

**Parameters:**
- `obj`
- `expect`

**Documentation:** _No documentation_

##### `test_command(obj, expect)`

**Line:** 252 | **Returns:** `None`

**Parameters:**
- `obj`
- `expect`

**Documentation:** _No documentation_

##### `test_context()`

**Line:** 258 | **Returns:** `None`

**Documentation:** _No documentation_

##### `test_paramtype_no_name()`

**Line:** 271 | **Returns:** `None`

**Documentation:** _No documentation_

#### Classes

##### Class: `TestType`

**Line:** 272

**Documentation:** _No documentation_

---

### `C:\Users\I.C.T\OneDrive\Documents\git\click\tests\test_normalization.py`

**Language:** python

#### Functions

##### `test_option_normalization(runner)`

**Line:** 6 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_choice_normalization(runner)`

**Line:** 18 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_command_normalization(runner)`

**Line:** 53 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

---

### `C:\Users\I.C.T\OneDrive\Documents\git\click\tests\test_options.py`

**Language:** python

#### Functions

##### `test_prefixes(runner)`

**Line:** 21 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_invalid_option(runner)`

**Line:** 37 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_deprecated_usage(runner, deprecated)`

**Line:** 48 | **Returns:** `None`

**Parameters:**
- `runner`
- `deprecated`

**Documentation:** _No documentation_

##### `test_deprecated_warning(runner, deprecated)`

**Line:** 62 | **Returns:** `None`

**Parameters:**
- `runner`
- `deprecated`

**Documentation:** _No documentation_

##### `test_deprecated_required(runner)`

**Line:** 83 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_deprecated_prompt(runner)`

**Line:** 88 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_invalid_nargs(runner)`

**Line:** 93 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_nargs_tup_composite_mult(runner)`

**Line:** 102 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_counting(runner)`

**Line:** 114 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_unknown_options(runner, unknown_flag)`

**Line:** 137 | **Returns:** `None`

**Parameters:**
- `runner`
- `unknown_flag`

**Documentation:** _No documentation_

##### `test_suggest_possible_options(runner, value, expect)`

**Line:** 155 | **Returns:** `None`

**Parameters:**
- `runner`
- `value`
- `expect`

**Documentation:** _No documentation_

##### `test_multiple_required(runner)`

**Line:** 163 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_good_defaults_for_multiple(runner, multiple, nargs, default, expected)`

**Line:** 225 | **Returns:** `None`

**Parameters:**
- `runner`
- `multiple`
- `nargs`
- `default`
- `expected`

**Documentation:**

> Comprehensive check of default-value processing for options with
> ``multiple=True`` and/or ``nargs > 1``.
> 
> .. hint::
>     An argument-specific equivalent is in
>     ``test_arguments.py::test_good_defaults_for_nargs``.
> 
>     Smoke tests are in ``test_defaults.py``:
>     ``test_multiple_defaults`` (explicit ``type=FLOAT``)
>     and ``test_nargs_plus_multiple`` (``nargs=2``).

##### `test_bad_defaults_for_multiple(runner, multiple, nargs, default, exception, message)`

**Line:** 372 | **Returns:** `None`

**Parameters:**
- `runner`
- `multiple`
- `nargs`
- `default`
- `exception`
- `message`

**Documentation:** _No documentation_

##### `test_empty_envvar(runner, env_key)`

**Line:** 396 | **Returns:** `None`

**Parameters:**
- `runner`
- `env_key`

**Documentation:** _No documentation_

##### `test_multiple_envvar(runner)`

**Line:** 407 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_boolean_flag_envvar(runner, envvar_name, envvar_value, expected)`

**Line:** 505 | **Returns:** `None`

**Parameters:**
- `runner`
- `envvar_name`
- `envvar_value`
- `expected`

**Documentation:** _No documentation_

##### `test_boolean_envvar_bad_values(runner, value)`

**Line:** 544 | **Returns:** `None`

**Parameters:**
- `runner`
- `value`

**Documentation:** _No documentation_

##### `test_multiple_default_help(runner)`

**Line:** 558 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_show_default_default_map(runner)`

**Line:** 571 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_multiple_default_type()`

**Line:** 583 | **Returns:** `None`

**Documentation:** _No documentation_

##### `test_multiple_default_composite_type()`

**Line:** 592 | **Returns:** `None`

**Documentation:** _No documentation_

##### `test_parse_multiple_default_composite_type(runner)`

**Line:** 602 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_dynamic_default_help_unset(runner)`

**Line:** 616 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_dynamic_default_help_text(runner)`

**Line:** 634 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_dynamic_default_help_special_method(runner)`

**Line:** 652 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_intrange_default_help_text(type, expect)`

**Line:** 675 | **Returns:** `None`

**Parameters:**
- `type`
- `expect`

**Documentation:** _No documentation_

##### `test_count_default_type_help()`

**Line:** 683 | **Returns:** `None`

**Documentation:**

> A count option with the default type should not show >=0 in help.

##### `test_file_type_help_default()`

**Line:** 692 | **Returns:** `None`

**Documentation:**

> The default for a File type is a filename string. The string
> should be displayed in help, not an open file object.
> 
> Type casting is only applied to defaults in processing, not when
> getting the default value.

##### `test_toupper_envvar_prefix(runner)`

**Line:** 708 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_nargs_envvar(runner)`

**Line:** 719 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_show_envvar(runner)`

**Line:** 744 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_show_envvar_auto_prefix(runner)`

**Line:** 755 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_show_envvar_auto_prefix_dash_in_command(runner)`

**Line:** 766 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_custom_validation(runner)`

**Line:** 781 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_callback_validates_prompt(runner, monkeypatch)`

**Line:** 799 | **Returns:** `None`

**Parameters:**
- `runner`
- `monkeypatch`

**Documentation:** _No documentation_

##### `test_winstyle_options(runner)`

**Line:** 815 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_legacy_options(runner)`

**Line:** 832 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_required_option(value, expect_missing, processed_value)`

**Line:** 863 | **Returns:** `None`

**Parameters:**
- `value`
- `expect_missing`
- `processed_value`

**Documentation:** _No documentation_

##### `test_missing_required_flag(runner)`

**Line:** 877 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_missing_choice(runner)`

**Line:** 886 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_missing_envvar(runner)`

**Line:** 901 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_case_insensitive_choice(runner)`

**Line:** 924 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_case_insensitive_choice_returned_exactly(runner)`

**Line:** 957 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_option_help_preserve_paragraphs(runner)`

**Line:** 968 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_argument_custom_class(runner)`

**Line:** 995 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_option_custom_class(runner)`

**Line:** 1011 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_option_custom_class_can_override_type_cast_value_and_never_sees_unset(runner, param_decl, option_kwargs, pass_argv)`

**Line:** 1039 | **Returns:** `None`

**Parameters:**
- `runner`
- `param_decl`
- `option_kwargs`
- `pass_argv`

**Documentation:**

> Test that overriding type_cast_value is supported
> 
> In particular, the option is never passed an UNSET sentinel value.

##### `test_option_custom_class_reusable(runner)`

**Line:** 1063 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:**

> Ensure we can reuse a custom class option. See Issue #926

##### `test_help_option_custom_names_and_class(runner, custom_class, name_specs, expected)`

**Line:** 1110 | **Returns:** `None`

**Parameters:**
- `runner`
- `custom_class`
- `name_specs`
- `expected`

**Documentation:** _No documentation_

##### `test_bool_flag_with_type(runner)`

**Line:** 1130 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_aliases_for_flags(runner)`

**Line:** 1140 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_option_names(runner, option_args, expected)`

**Line:** 1181 | **Returns:** `None`

**Parameters:**
- `runner`
- `option_args`
- `expected`

**Documentation:** _No documentation_

##### `test_flag_duplicate_names(runner)`

**Line:** 1195 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_show_default_boolean_flag_name(runner, default, expect)`

**Line:** 1201 | **Returns:** `None`

**Parameters:**
- `runner`
- `default`
- `expect`

**Documentation:**

> When a boolean flag has distinct True/False opts, it should show
> the default opt name instead of the default value. It should only
> show one name even if multiple are declared.

##### `test_show_true_default_boolean_flag_value(runner)`

**Line:** 1218 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:**

> When a boolean flag only has one opt and its default is True,
> it will show the default value, not the opt name.

##### `test_hide_false_default_boolean_flag_value(runner, default)`

**Line:** 1236 | **Returns:** `None`

**Parameters:**
- `runner`
- `default`

**Documentation:**

> When a boolean flag only has one opt and its default is False or
> None, it will not show the default

##### `test_show_default_string(runner)`

**Line:** 1253 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:**

> When show_default is a string show that value as default.

##### `test_string_show_default_shows_custom_string_in_prompt(runner)`

**Line:** 1262 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_show_default_with_empty_string(runner, default, expected)`

**Line:** 1295 | **Returns:** `None`

**Parameters:**
- `runner`
- `default`
- `expected`

**Documentation:**

> The empty-string check in help rendering must not break on objects
> whose ``__eq__`` raises for string operands.
> 
> Regression test for https://github.com/pallets/click/issues/3298.

##### `test_do_not_show_no_default(runner)`

**Line:** 1307 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:**

> When show_default is True and no default is set do not show None.

##### `test_do_not_show_default_empty_multiple()`

**Line:** 1316 | **Returns:** `None`

**Documentation:**

> When show_default is True and multiple=True is set, it should not
> print empty default value in --help output.

##### `test_show_default_precedence(ctx_value, opt_value, extra_value, expect)`

**Line:** 1342 | **Returns:** `None`

**Parameters:**
- `ctx_value`
- `opt_value`
- `extra_value`
- `expect`

**Documentation:** _No documentation_

##### `test_option_with_optional_value(runner, args, expect)`

**Line:** 1369 | **Returns:** `None`

**Parameters:**
- `runner`
- `args`
- `expect`

**Documentation:** _No documentation_

##### `test_multiple_option_with_optional_value(runner)`

**Line:** 1381 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_type_from_flag_value()`

**Line:** 1404 | **Returns:** `None`

**Documentation:** _No documentation_

##### `test_flag_value_and_default(runner, opt_params, args, expected)`

**Line:** 1518 | **Returns:** `None`

**Parameters:**
- `runner`
- `opt_params`
- `args`
- `expected`

**Documentation:** _No documentation_

##### `test_invalid_flag_definition(runner, args, opts)`

**Line:** 1537 | **Returns:** `None`

**Parameters:**
- `runner`
- `args`
- `opts`

**Documentation:** _No documentation_

##### `test_default_dual_option_callback(runner, default, args, expected)`

**Line:** 1586 | **Returns:** `None`

**Parameters:**
- `runner`
- `default`
- `args`
- `expected`

**Documentation:**

> Check how default is processed by the callback when options compete for the same
> variable name.
> 
> Reproduction of the issue reported in
> https://github.com/pallets/click/pull/3030#discussion_r2271571819
> 
> .. hint::
>     Similar to ``test_basic.py::test_flag_value_dual_options``.
> 
>     ``test_defaults.py::test_shared_param_prefers_first_default``
>     is a smoke-test complement that exercises both default placements.

##### `test_envvar_string_flag_value(runner, flag_value, envvar_value, expected)`

**Line:** 1702 | **Returns:** `None`

**Parameters:**
- `runner`
- `flag_value`
- `envvar_value`
- `expected`

**Documentation:**

> Ensure that flag_value is recognized by the envvar.

##### `test_flag_auto_detection(opt_decls, opt_params, expect_is_flag, expect_is_bool_flag)`

**Line:** 1732 | **Returns:** `None`

**Parameters:**
- `opt_decls`
- `opt_params`
- `expect_is_flag`
- `expect_is_bool_flag`

**Documentation:** _No documentation_

##### `test_invalid_flag_combinations(runner, kwargs, message)`

**Line:** 1747 | **Returns:** `None`

**Parameters:**
- `runner`
- `kwargs`
- `message`

**Documentation:** _No documentation_

##### `test_non_flag_with_non_negatable_default(runner)`

**Line:** 1754 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_choice_usage_rendering(runner, choices, metavar)`

**Line:** 1812 | **Returns:** `None`

**Parameters:**
- `runner`
- `choices`
- `metavar`

**Documentation:**

> BY default ``--help`` prints choice's values in the usage message.
> 
> But ``show_choices=False`` makes ``--help`` prints choice's METAVAR instead of
> values.
> 
> Also check that usage error message always suggests the actual values.

##### `test_choice_default_rendering(runner, choices, default, default_string)`

**Line:** 1896 | **Returns:** `None`

**Parameters:**
- `runner`
- `choices`
- `default`
- `default_string`

**Documentation:** _No documentation_

##### `test_duplicate_names_warning(runner, opts_one, opts_two)`

**Line:** 1928 | **Returns:** `None`

**Parameters:**
- `runner`
- `opts_one`
- `opts_two`

**Documentation:** _No documentation_

##### `test_dual_options_custom_type_sentinel_flag_value(runner, sentinel, args, expected)`

**Line:** 2023 | **Returns:** `None`

**Parameters:**
- `runner`
- `sentinel`
- `args`
- `expected`

**Documentation:**

> Check that an object-based sentinel, used as a flag value, is returned as-is
> to a custom type that is shared by two options, competing for the same variable
> name.
> 
> A reproduction of
> https://github.com/pallets/click/issues/3024#issuecomment-3146511356

##### `test_custom_type_flag_value_standalone_option(runner, opt_params, args, expected)`

**Line:** 2163 | **Returns:** `None`

**Parameters:**
- `runner`
- `opt_params`
- `args`
- `expected`

**Documentation:**

> Test how the type and flag_value influence the returned value.
> 
> Cover cases reported in:
> https://github.com/pallets/click/issues/3024#issuecomment-3146480714
> https://github.com/pallets/click/issues/2012#issuecomment-892437060

##### `test_custom_type_flag_value_dual_options(runner, opt1_params, opt2_params, args, expected)`

**Line:** 2294 | **Returns:** `None`

**Parameters:**
- `runner`
- `opt1_params`
- `opt2_params`
- `args`
- `expected`

**Documentation:**

> Test how flag values are processed with dual options competing for the same
> variable name.
> 
> Reproduce issues reported in:
> https://github.com/pallets/click/issues/3024#issuecomment-3146508536
> https://github.com/pallets/click/issues/2012#issue-946471049
> https://github.com/pallets/click/issues/2012#issuecomment-892437060

##### `test_callable_flag_value_not_instantiated(runner, opt_params, args, expected)`

**Line:** 2357 | **Returns:** `None`

**Parameters:**
- `runner`
- `opt_params`
- `args`
- `expected`

**Documentation:**

> A callable ``flag_value`` like a class, with ``default=True`` should not be
> invoked when resolving the default. This is the single-option variant of
> the regression reported in https://github.com/pallets/click/issues/3121.

##### `test_callable_flag_value_default_map(runner)`

**Line:** 2376 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:**

> A ``default_map`` entry should override the auto-aligned callable ``flag_value``.
> 
> When ``default=True`` and ``flag_value=SomeClass``, the default is aligned to
> ``SomeClass``. If ``default_map`` provides a different value (including a
> callable), it should take precedence and callables from ``default_map`` should
> still be invoked.

##### `test_callable_flag_value_show_default(runner)`

**Line:** 2403 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:**

> Help text with ``show_default=True`` should display the class name, not
> instantiate it.

##### `test_callable_flag_value_get_default_override(runner, opt_params, expected_default_attr, expected_get_default)`

**Line:** 2456 | **Returns:** `None`

**Parameters:**
- `runner`
- `opt_params`
- `expected_default_attr`
- `expected_get_default`

**Documentation:**

> The ``default=True`` to ``flag_value`` alignment is resolved lazily in
> ``get_default()`` rather than eagerly in ``__init__``. This means
> ``option.default`` stays as ``True`` while ``get_default()`` returns the
> ``flag_value``.
> 
> A user subclass that reads ``self.default`` directly (bypassing
> ``get_default()``) will see ``True`` instead of the ``flag_value``.

##### `test_flag_value_not_stringified_for_custom_types(runner)`

**Line:** 2483 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:**

> Non-basic flag_value types are passed through unchanged without
> requiring ``type=click.UNPROCESSED``.
> 
> Regression test for https://github.com/pallets/click/issues/2012

##### `test_custom_type_frozenset_flag_value(runner)`

**Line:** 2525 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:**

> Check that frozenset is correctly handled as a type, a flag value and a default.
> 
> Reproduces https://github.com/pallets/click/issues/2610

##### `test_bool_flag_pair_default(runner, default, args, expected)`

**Line:** 2567 | **Returns:** `None`

**Parameters:**
- `runner`
- `default`
- `args`
- `expected`

**Documentation:**

> Boolean flag pairs pass ``default`` through literally.
> 
> Ensures ``default=True`` is not replaced by ``flag_value`` for boolean
> flags, and that ``default=None`` enables 3-state logic.

##### `test_flag_value_on_option_with_zero_or_one_args(flag_type, args, expect_output)`

**Line:** 2595 | **Returns:** `None`

**Parameters:**
- `flag_type`
- `args`
- `expect_output`

**Documentation:**

> An option with flag_value and is_flag=False can be
> omitted or used with 0 or 1 args.
> 
> Regression test for https://github.com/pallets/click/issues/3084

#### Classes

##### Class: `Value`

**Line:** 653

**Documentation:** _No documentation_

**Methods:**

- **`__call__(self)`** (Line 654)
  - Returns: `None`
  - _No documentation_

- **`__str__(self)`** (Line 657)
  - Returns: `None`
  - _No documentation_

##### Class: `CustomArgument`

**Line:** 996

**Documentation:** _No documentation_

**Methods:**

- **`get_default(self, ctx, call)`** (Line 997)
  - Returns: `None`
  - a dumb override of a default value for testing

##### Class: `CustomOption`

**Line:** 1012

**Documentation:** _No documentation_

**Methods:**

- **`get_help_record(self, ctx)`** (Line 1013)
  - Returns: `None`
  - a dumb override of a help text for testing

##### Class: `CustomOption`

**Line:** 1048

**Documentation:** _No documentation_

**Methods:**

- **`type_cast_value(self, ctx, value)`** (Line 1049)
  - Returns: `None`
  - _No documentation_

##### Class: `CustomOption`

**Line:** 1066

**Documentation:** _No documentation_

**Methods:**

- **`get_help_record(self, ctx)`** (Line 1067)
  - Returns: `None`
  - a dumb override of a help text for testing

##### Class: `CustomHelpOption`

**Line:** 1111

**Documentation:** _No documentation_

##### Class: `_StrictEq`

**Line:** 1275

**Documentation:**

> Object whose ``__eq__`` raises on string comparison (like semver.Version).

**Methods:**

- **`__eq__(self, other)`** (Line 1278)
  - Returns: `None`
  - _No documentation_

- **`__str__(self)`** (Line 1283)
  - Returns: `None`
  - _No documentation_

##### Class: `NonNegatable`

**Line:** 1755

**Documentation:** _No documentation_

**Methods:**

- **`__bool__(self)`** (Line 1756)
  - Returns: `None`
  - _No documentation_

##### Class: `HashType`

**Line:** 1768

**Documentation:** _No documentation_

##### Class: `Number`

**Line:** 1774

**Documentation:** _No documentation_

##### Class: `Letter`

**Line:** 1779

**Documentation:** _No documentation_

##### Class: `Color`

**Line:** 1785

**Documentation:** _No documentation_

##### Class: `ColorInt`

**Line:** 1791

**Documentation:** _No documentation_

##### Class: `EnumSentinel`

**Line:** 1943

**Documentation:** _No documentation_

**Methods:**

- **`__bool__(self)`** (Line 1946)
  - Returns: `Literal[False]`
  - Force the sentinel to be falsy to make sure it is not caught by Click

##### Class: `ConfigParamType`

**Line:** 2032

**Documentation:**

> A custom type that accepts a file path or a sentinel value.

**Methods:**

- **`convert(self, value, param, ctx)`** (Line 2035)
  - Returns: `None`
  - _No documentation_

##### Class: `EngineType`

**Line:** 2065

**Documentation:** _No documentation_

##### Class: `Class1`

**Line:** 2071

**Documentation:** _No documentation_

##### Class: `Class2`

**Line:** 2075

**Documentation:** _No documentation_

---

### `C:\Users\I.C.T\OneDrive\Documents\git\click\tests\test_parser.py`

**Language:** python

#### Functions

##### `test_split_arg_string(value, expect)`

**Line:** 18 | **Returns:** `None`

**Parameters:**
- `value`
- `expect`

**Documentation:** _No documentation_

##### `test_parser_default_prefixes()`

**Line:** 22 | **Returns:** `None`

**Documentation:** _No documentation_

##### `test_parser_collects_prefixes()`

**Line:** 27 | **Returns:** `None`

**Documentation:** _No documentation_

---

### `C:\Users\I.C.T\OneDrive\Documents\git\click\tests\test_shell_completion.py`

**Language:** python

#### Functions

##### `_get_completions(cli, args, incomplete)`

**Line:** 20 | **Returns:** `None`

**Parameters:**
- `cli`
- `args`
- `incomplete`

**Documentation:** _No documentation_

##### `_get_words(cli, args, incomplete)`

**Line:** 25 | **Returns:** `None`

**Parameters:**
- `cli`
- `args`
- `incomplete`

**Documentation:** _No documentation_

##### `test_command()`

**Line:** 29 | **Returns:** `None`

**Documentation:** _No documentation_

##### `test_group()`

**Line:** 39 | **Returns:** `None`

**Documentation:** _No documentation_

##### `test_nested_group(args, word, expect)`

**Line:** 56 | **Returns:** `None`

**Parameters:**
- `args` (list[str])
- `word` (str)
- `expect` (list[str])

**Documentation:** _No documentation_

##### `test_group_command_same_option()`

**Line:** 75 | **Returns:** `None`

**Documentation:** _No documentation_

##### `test_chained()`

**Line:** 85 | **Returns:** `None`

**Documentation:** _No documentation_

##### `test_help_option()`

**Line:** 104 | **Returns:** `None`

**Documentation:** _No documentation_

##### `test_argument_order()`

**Line:** 110 | **Returns:** `None`

**Documentation:** _No documentation_

##### `test_argument_default()`

**Line:** 127 | **Returns:** `None`

**Documentation:** _No documentation_

##### `test_type_choice()`

**Line:** 142 | **Returns:** `None`

**Documentation:** _No documentation_

##### `test_choice_special_characters()`

**Line:** 149 | **Returns:** `None`

**Documentation:** _No documentation_

##### `test_choice_conflicting_prefix()`

**Line:** 156 | **Returns:** `None`

**Documentation:** _No documentation_

##### `test_option_count()`

**Line:** 168 | **Returns:** `None`

**Documentation:** _No documentation_

##### `test_option_optional()`

**Line:** 174 | **Returns:** `None`

**Documentation:** _No documentation_

##### `test_path_types(type, expect)`

**Line:** 192 | **Returns:** `None`

**Parameters:**
- `type`
- `expect`

**Documentation:** _No documentation_

##### `test_absolute_path()`

**Line:** 201 | **Returns:** `None`

**Documentation:** _No documentation_

##### `test_option_flag()`

**Line:** 209 | **Returns:** `None`

**Documentation:** _No documentation_

##### `test_flag_option_with_nargs_option()`

**Line:** 223 | **Returns:** `None`

**Documentation:** _No documentation_

##### `test_option_custom()`

**Line:** 236 | **Returns:** `None`

**Documentation:** _No documentation_

##### `test_option_multiple()`

**Line:** 252 | **Returns:** `None`

**Documentation:** _No documentation_

##### `test_option_nargs()`

**Line:** 264 | **Returns:** `None`

**Documentation:** _No documentation_

##### `test_argument_nargs()`

**Line:** 271 | **Returns:** `None`

**Documentation:** _No documentation_

##### `test_double_dash()`

**Line:** 289 | **Returns:** `None`

**Documentation:** _No documentation_

##### `test_hidden()`

**Line:** 304 | **Returns:** `None`

**Documentation:** _No documentation_

##### `test_add_different_name()`

**Line:** 325 | **Returns:** `None`

**Documentation:** _No documentation_

##### `test_completion_item_data()`

**Line:** 332 | **Returns:** `None`

**Documentation:** _No documentation_

##### `_patch_for_completion(monkeypatch)`

**Line:** 339 | **Returns:** `None`

**Parameters:**
- `monkeypatch`

**Documentation:** _No documentation_

##### `test_full_source(runner, shell)`

**Line:** 347 | **Returns:** `None`

**Parameters:**
- `runner`
- `shell`

**Documentation:** _No documentation_

##### `test_full_complete(runner, shell, env, expect)`

**Line:** 366 | **Returns:** `None`

**Parameters:**
- `runner`
- `shell`
- `env`
- `expect`

**Documentation:** _No documentation_

##### `test_zsh_full_complete_with_colons(runner, env, expect)`

**Line:** 424 | **Returns:** `None`

**Parameters:**
- `runner`
- `env` (Mapping[str, str])
- `expect` (str)

**Documentation:** _No documentation_

##### `test_context_settings(runner)`

**Line:** 447 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_choice_case_sensitive(value, expect)`

**Line:** 461 | **Returns:** `None`

**Parameters:**
- `value`
- `expect`

**Documentation:** _No documentation_

##### `_restore_available_shells(tmpdir)`

**Line:** 471 | **Returns:** `None`

**Parameters:**
- `tmpdir`

**Documentation:** _No documentation_

##### `test_add_completion_class()`

**Line:** 480 | **Returns:** `None`

**Documentation:** _No documentation_

##### `test_add_completion_class_with_name()`

**Line:** 500 | **Returns:** `None`

**Documentation:** _No documentation_

##### `test_add_completion_class_decorator()`

**Line:** 526 | **Returns:** `None`

**Documentation:** _No documentation_

##### `test_files_closed(runner)`

**Line:** 542 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_fish_multiline_help_complete(runner)`

**Line:** 565 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:**

> Test Fish completion with multi-line help text doesn't cause errors.

#### Classes

##### Class: `MyshComplete`

**Line:** 484

**Documentation:** _No documentation_

##### Class: `MyshComplete`

**Line:** 505

**Documentation:** _No documentation_

##### Class: `MyshComplete`

**Line:** 531

**Documentation:** _No documentation_

---

### `C:\Users\I.C.T\OneDrive\Documents\git\click\tests\test_stream_lifecycle.py`

**Language:** python

#### Functions

##### `test_wrapper_close_does_not_close_underlying_buffer()`

**Line:** 62 | **Returns:** `None`

**Documentation:**

> Calling ``close()`` on the wrapper must leave the buffer open.

##### `test_wrapper_del_does_not_close_underlying_buffer()`

**Line:** 73 | **Returns:** `None`

**Documentation:**

> Garbage-collecting the wrapper must leave the buffer open.

##### `test_multiple_wrappers_same_buffer()`

**Line:** 85 | **Returns:** `None`

**Documentation:**

> Multiple wrappers on the same buffer can be closed independently.

##### `test_wrapper_preserves_name_and_mode()`

**Line:** 101 | **Returns:** `None`

**Documentation:** _No documentation_

##### `test_mixer_buffers_survive_wrapper_gc()`

**Line:** 113 | **Returns:** `None`

**Documentation:**

> After wrappers are garbage-collected, mixer buffers remain open.

##### `test_getvalue_after_isolation_exit()`

**Line:** 138 | **Returns:** `None`

**Documentation:**

> After the isolation context exits, stream values are readable.

##### `test_no_streammixer_del()`

**Line:** 155 | **Returns:** `None`

**Documentation:**

> ``StreamMixer`` should not have a ``__del__`` method.
> 
> PR #2991 added ``__del__`` which caused issue #3110. PR #3139 removes it.

##### `test_bytesiocopy_writes_to_both()`

**Line:** 165 | **Returns:** `None`

**Documentation:**

> ``BytesIOCopy`` writes to itself and to ``copy_to``.

##### `test_bytesiocopy_flush_propagates()`

**Line:** 175 | **Returns:** `None`

**Documentation:**

> ``BytesIOCopy.flush()`` also flushes ``copy_to``.

##### `test_invoke_with_logger_warning()`

**Line:** 189 | **Returns:** `None`

**Documentation:**

> Basic ``logging.warning()`` inside a command must not crash.

##### `test_invoke_with_logger_and_prompt()`

**Line:** 204 | **Returns:** `None`

**Documentation:**

> Logging + prompt (the exact #824 reproducer).

##### `test_sequential_invokes_with_logging()`

**Line:** 220 | **Returns:** `None`

**Documentation:**

> Multiple sequential ``invoke()`` calls with logging (#3110 reproducer).
> 
> Issue #3110: the ``__del__`` from PR #2991 caused logging failures on
> the second invocation because the first ``StreamMixer``'s ``__del__`` would
> close buffers that logging still referenced.

##### `test_invoke_with_stream_handler_on_stderr()`

**Line:** 242 | **Returns:** `None`

**Documentation:**

> A ``StreamHandler`` explicitly attached to stderr must survive ``invoke()``.

##### `test_logging_with_cli_log_level()`

**Line:** 263 | **Returns:** `None`

**Documentation:**

> Simulate what ``--log-cli-level`` does: add a handler to root
> before invoke.
> 
> This reproduces the original #824 scenario without needing pytest
> CLI flags.

##### `test_invoke_with_thread_pool()`

**Line:** 297 | **Returns:** `None`

**Documentation:**

> Basic ``ThreadPoolExecutor`` usage inside a command.

##### `test_invoke_with_threads_writing_to_streams()`

**Line:** 313 | **Returns:** `None`

**Documentation:**

> Threads writing to ``click.echo()`` during invocation.

##### `test_invoke_with_thread_pool_and_exit()`

**Line:** 337 | **Returns:** `None`

**Documentation:**

> ``ThreadPoolExecutor`` + ``SystemExit`` (the exact #2993 reproducer).

##### `test_sequential_threaded_invokes()`

**Line:** 352 | **Returns:** `None`

**Documentation:**

> Multiple sequential invocations with threads don't leak state.

##### `test_output_isolation_across_invokes()`

**Line:** 374 | **Returns:** `None`

**Documentation:**

> Each ``invoke()`` must capture only its own output.

##### `test_stderr_isolation_across_invokes()`

**Line:** 389 | **Returns:** `None`

**Documentation:**

> Each ``invoke()`` must capture only its own stderr.

##### `test_mixed_output_order_preserved()`

**Line:** 405 | **Returns:** `None`

**Documentation:**

> stdout/stderr interleaving is captured in order.

##### `test_exception_does_not_corrupt_next_invoke()`

**Line:** 422 | **Returns:** `None`

**Documentation:**

> A failed invoke must not break subsequent invocations.

##### `test_sys_streams_restored_after_invoke()`

**Line:** 449 | **Returns:** `None`

**Documentation:**

> ``sys.stdout``/``stderr``/``stdin`` are restored after ``invoke()``.

##### `test_sys_streams_restored_after_exception()`

**Line:** 467 | **Returns:** `None`

**Documentation:**

> sys streams are restored even when the command raises.

##### `test_stress_thread_pool_with_exit(_)`

**Line:** 493 | **Returns:** `None`

**Parameters:**
- `_`

**Documentation:**

> Exact #2993 reproducer: ``ThreadPoolExecutor`` + ``SystemExit``.

##### `test_stress_logging_sequential_invocations(_)`

**Line:** 510 | **Returns:** `None`

**Parameters:**
- `_`

**Documentation:**

> #3110/#824 reproducer: sequential invocations with logging.

##### `test_stress_gc_between_invocations(_)`

**Line:** 526 | **Returns:** `None`

**Parameters:**
- `_`

**Documentation:**

> Force GC after each invocation to provoke finalizer races.

---

### `C:\Users\I.C.T\OneDrive\Documents\git\click\tests\test_termui.py`

**Language:** python

#### Functions

##### `_create_progress(length, **kwargs)`

**Line:** 28 | **Returns:** `None`

**Parameters:**
- `length`
- `**kwargs`

**Documentation:** _No documentation_

##### `test_progressbar_strip_regression(runner, monkeypatch)`

**Line:** 35 | **Returns:** `None`

**Parameters:**
- `runner`
- `monkeypatch`

**Documentation:** _No documentation_

##### `test_progressbar_length_hint(runner, monkeypatch)`

**Line:** 51 | **Returns:** `None`

**Parameters:**
- `runner`
- `monkeypatch`

**Documentation:** _No documentation_

##### `test_progressbar_no_tty(runner, monkeypatch)`

**Line:** 81 | **Returns:** `None`

**Parameters:**
- `runner`
- `monkeypatch`

**Documentation:** _No documentation_

##### `test_progressbar_hidden_manual(runner, monkeypatch)`

**Line:** 92 | **Returns:** `None`

**Parameters:**
- `runner`
- `monkeypatch`

**Documentation:** _No documentation_

##### `test_progressbar_time_per_iteration(runner, avg, expected)`

**Line:** 104 | **Returns:** `None`

**Parameters:**
- `runner`
- `avg`
- `expected`

**Documentation:** _No documentation_

##### `test_progressbar_eta(runner, finished, expected)`

**Line:** 110 | **Returns:** `None`

**Parameters:**
- `runner`
- `finished`
- `expected`

**Documentation:** _No documentation_

##### `test_progressbar_format_eta(runner, eta, expected)`

**Line:** 127 | **Returns:** `None`

**Parameters:**
- `runner`
- `eta`
- `expected`

**Documentation:** _No documentation_

##### `test_progressbar_format_pos(runner, pos, length)`

**Line:** 133 | **Returns:** `None`

**Parameters:**
- `runner`
- `pos`
- `length`

**Documentation:** _No documentation_

##### `test_progressbar_format_bar(runner, length, finished, pos, avg, expected)`

**Line:** 146 | **Returns:** `None`

**Parameters:**
- `runner`
- `length`
- `finished`
- `pos`
- `avg`
- `expected`

**Documentation:** _No documentation_

##### `test_progressbar_format_progress_line(runner, length, show_percent, show_pos, pos, expected)`

**Line:** 163 | **Returns:** `None`

**Parameters:**
- `runner`
- `length`
- `show_percent`
- `show_pos`
- `pos`
- `expected`

**Documentation:** _No documentation_

##### `test_progressbar_format_progress_line_with_show_func(runner, test_item)`

**Line:** 177 | **Returns:** `None`

**Parameters:**
- `runner`
- `test_item`

**Documentation:** _No documentation_

##### `test_progressbar_init_exceptions(runner)`

**Line:** 190 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_progressbar_iter_outside_with_exceptions(runner)`

**Line:** 195 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_progressbar_is_iterator(runner, monkeypatch)`

**Line:** 202 | **Returns:** `None`

**Parameters:**
- `runner`
- `monkeypatch`

**Documentation:** _No documentation_

##### `test_choices_list_in_prompt(runner, monkeypatch)`

**Line:** 217 | **Returns:** `None`

**Parameters:**
- `runner`
- `monkeypatch`

**Documentation:** _No documentation_

##### `test_file_prompt_default_format(runner, file_kwargs)`

**Line:** 245 | **Returns:** `None`

**Parameters:**
- `runner`
- `file_kwargs`

**Documentation:** _No documentation_

##### `test_secho(runner)`

**Line:** 255 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_secho_non_text(runner, value, expect)`

**Line:** 266 | **Returns:** `None`

**Parameters:**
- `runner`
- `value`
- `expect`

**Documentation:** _No documentation_

##### `test_progressbar_yields_all_items(runner)`

**Line:** 273 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_progressbar_update(runner, monkeypatch)`

**Line:** 278 | **Returns:** `None`

**Parameters:**
- `runner`
- `monkeypatch`

**Documentation:** _No documentation_

##### `test_progressbar_item_show_func(runner, monkeypatch)`

**Line:** 301 | **Returns:** `None`

**Parameters:**
- `runner`
- `monkeypatch`

**Documentation:**

> item_show_func should show the current item being yielded.

##### `test_progressbar_update_with_item_show_func(runner, monkeypatch)`

**Line:** 317 | **Returns:** `None`

**Parameters:**
- `runner`
- `monkeypatch`

**Documentation:** _No documentation_

##### `test_progress_bar_update_min_steps(runner)`

**Line:** 337 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_getchar_windows(runner, monkeypatch, key_char, echo)`

**Line:** 350 | **Returns:** `None`

**Parameters:**
- `runner`
- `monkeypatch`
- `key_char`
- `echo`

**Documentation:** _No documentation_

##### `test_getchar_special_key_windows(runner, monkeypatch, special_key_char, key_char)`

**Line:** 363 | **Returns:** `None`

**Parameters:**
- `runner`
- `monkeypatch`
- `special_key_char`
- `key_char`

**Documentation:** _No documentation_

##### `test_getchar_windows_exceptions(runner, monkeypatch, key_char, exc)`

**Line:** 376 | **Returns:** `None`

**Parameters:**
- `runner`
- `monkeypatch`
- `key_char`
- `exc`

**Documentation:** _No documentation_

##### `test_fast_edit(runner)`

**Line:** 385 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_edit(runner)`

**Line:** 391 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_editor_path_normalization(editor_cmd, filenames, expected_args)`

**Line:** 505 | **Returns:** `None`

**Parameters:**
- `editor_cmd`
- `filenames`
- `expected_args`

**Documentation:** _No documentation_

##### `test_editor_windows_path_normalization(editor_cmd, expected_cmd)`

**Line:** 532 | **Returns:** `None`

**Parameters:**
- `editor_cmd`
- `expected_cmd`

**Documentation:**

> Windows-specific tests: verify ``Popen`` receives unquoted paths that
> ``subprocess.list2cmdline`` can re-quote for ``CreateProcess``.

##### `test_editor_env_passed_through()`

**Line:** 544 | **Returns:** `None`

**Documentation:** _No documentation_

##### `test_editor_failure_exception()`

**Line:** 554 | **Returns:** `None`

**Documentation:** _No documentation_

##### `test_editor_nonexistent_exception()`

**Line:** 561 | **Returns:** `None`

**Documentation:** _No documentation_

##### `test_pager_shlex_split(pager_env, expected_parts)`

**Line:** 613 | **Returns:** `None`

**Parameters:**
- `pager_env`
- `expected_parts`

**Documentation:**

> Verify shlex.split produces the expected argv for PAGER values.
> 
> Tests the splitting logic used by :func:`click._termui_impl.pager` to
> turn the ``PAGER`` environment variable into an ``argv`` list. See
> issue #1026, PR #1477, PR #1543, PR #2775.

##### `test_editor_unclosed_quote()`

**Line:** 623 | **Returns:** `None`

**Documentation:**

> An unclosed quote in the editor command raises ValueError.

##### `test_prompt_required_with_required(runner, prompt_required, required, args, expect)`

**Line:** 638 | **Returns:** `None`

**Parameters:**
- `runner`
- `prompt_required`
- `required`
- `args`
- `expect`

**Documentation:** _No documentation_

##### `test_prompt_required_false(runner, args, expect)`

**Line:** 665 | **Returns:** `None`

**Parameters:**
- `runner`
- `args`
- `expect`

**Documentation:** _No documentation_

##### `test_confirmation_prompt(runner, prompt, input, default, expect)`

**Line:** 689 | **Returns:** `None`

**Parameters:**
- `runner`
- `prompt`
- `input`
- `default`
- `expect`

**Documentation:** _No documentation_

##### `test_false_show_default_cause_no_default_display_in_prompt(runner)`

**Line:** 709 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_string_show_default_in_prompt(runner, show_default, default, user_input, in_prompt, not_in_prompt)`

**Line:** 749 | **Returns:** `None`

**Parameters:**
- `runner`
- `show_default`
- `default`
- `user_input`
- `in_prompt`
- `not_in_prompt`

**Documentation:**

> When show_default is a string, the prompt should display that
> string in parentheses instead of the actual default value,
> matching the help text behavior. See pallets/click#2836.

##### `test_flag_value_prompt(runner, opt_decls, opt_params, args, prompt, input, expected)`

**Line:** 941 | **Returns:** `None`

**Parameters:**
- `runner`
- `opt_decls`
- `opt_params`
- `args`
- `prompt`
- `input`
- `expected`

**Documentation:**

> Check how flag value are prompted and handled by all combinations of
> ``prompt``, ``default``, and ``flag_value`` parameters.
> 
> Covers concerns raised in issue https://github.com/pallets/click/issues/1992.

#### Classes

##### Class: `FakeClock`

**Line:** 17

**Documentation:** _No documentation_

**Methods:**

- **`__init__(self)`** (Line 18)
  - Returns: `None`
  - _No documentation_

- **`advance_time(self, seconds)`** (Line 21)
  - Returns: `None`
  - _No documentation_

- **`time(self)`** (Line 24)
  - Returns: `None`
  - _No documentation_

##### Class: `Hinted`

**Line:** 52

**Documentation:** _No documentation_

**Methods:**

- **`__init__(self, n)`** (Line 53)
  - Returns: `None`
  - _No documentation_

- **`__length_hint__(self)`** (Line 56)
  - Returns: `None`
  - _No documentation_

- **`__iter__(self)`** (Line 59)
  - Returns: `None`
  - _No documentation_

- **`__next__(self)`** (Line 62)
  - Returns: `None`
  - _No documentation_

---

### `C:\Users\I.C.T\OneDrive\Documents\git\click\tests\test_testing.py`

**Language:** python

#### Functions

##### `test_runner()`

**Line:** 14 | **Returns:** `None`

**Documentation:** _No documentation_

##### `test_echo_stdin_stream()`

**Line:** 32 | **Returns:** `None`

**Documentation:** _No documentation_

##### `test_echo_stdin_prompts()`

**Line:** 50 | **Returns:** `None`

**Documentation:** _No documentation_

##### `test_runner_with_stream()`

**Line:** 90 | **Returns:** `None`

**Documentation:** _No documentation_

##### `test_prompts()`

**Line:** 113 | **Returns:** `None`

**Documentation:** _No documentation_

##### `test_getchar()`

**Line:** 135 | **Returns:** `None`

**Documentation:** _No documentation_

##### `test_catch_exceptions()`

**Line:** 165 | **Returns:** `None`

**Documentation:** _No documentation_

##### `test_catch_exceptions_cli_runner()`

**Line:** 189 | **Returns:** `None`

**Documentation:**

> Test that invoke `catch_exceptions` takes the value from CliRunner if not set
> explicitly.

##### `test_with_color()`

**Line:** 211 | **Returns:** `None`

**Documentation:** _No documentation_

##### `test_with_color_errors()`

**Line:** 227 | **Returns:** `None`

**Documentation:** _No documentation_

##### `test_with_color_but_pause_not_blocking()`

**Line:** 247 | **Returns:** `None`

**Documentation:** _No documentation_

##### `test_exit_code_and_output_from_sys_exit()`

**Line:** 258 | **Returns:** `None`

**Documentation:** _No documentation_

##### `test_env()`

**Line:** 328 | **Returns:** `None`

**Documentation:** _No documentation_

##### `test_stderr()`

**Line:** 346 | **Returns:** `None`

**Documentation:** _No documentation_

##### `test_args(args, expected_output)`

**Line:** 383 | **Returns:** `None`

**Parameters:**
- `args`
- `expected_output`

**Documentation:** _No documentation_

##### `test_setting_prog_name_in_extra()`

**Line:** 395 | **Returns:** `None`

**Documentation:** _No documentation_

##### `test_command_standalone_mode_returns_value()`

**Line:** 406 | **Returns:** `None`

**Documentation:** _No documentation_

##### `test_file_stdin_attrs(runner)`

**Line:** 419 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_isolated_runner(runner)`

**Line:** 430 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_isolated_runner_custom_tempdir(runner, tmp_path)`

**Line:** 437 | **Returns:** `None`

**Parameters:**
- `runner`
- `tmp_path`

**Documentation:** _No documentation_

##### `test_isolation_stderr_errors()`

**Line:** 445 | **Returns:** `None`

**Documentation:**

> Writing to stderr should escape invalid characters instead of
> raising a UnicodeEncodeError.

##### `test_isolation_flushes_unflushed_stderr()`

**Line:** 456 | **Returns:** `None`

**Documentation:**

> An un-flushed write to stderr, as with `print(..., file=sys.stderr)`, will end up
> flushed by the runner at end of invocation.

##### `test_pdb_uses_real_streams()`

**Line:** 476 | **Returns:** `None`

**Documentation:**

> ``pdb.Pdb()`` inside ``CliRunner`` defaults to real terminal streams
> so that interactive debuggers work instead of reading from the
> captured ``BytesIO`` stdin.

##### `test_pdb_explicit_streams_honored()`

**Line:** 494 | **Returns:** `None`

**Documentation:**

> Explicit ``stdin``/``stdout`` arguments to ``pdb.Pdb()`` are not
> overridden by the ``CliRunner`` patch.

##### `test_pdb_init_restored_after_invoke()`

**Line:** 511 | **Returns:** `None`

**Documentation:**

> ``pdb.Pdb.__init__`` is restored to its original after invoke.

##### `test_faulthandler_enable(runner)`

**Line:** 525 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:**

> ``faulthandler.enable()`` inside ``CliRunner`` should not crash with
> ``io.UnsupportedOperation: fileno``.
> 
> ``faulthandler.enable()`` needs a real OS file descriptor to register
> its signal handler. ``CliRunner`` replaces ``sys.stderr`` with a
> ``BytesIO`` wrapper that has no ``fileno()``, causing the call to fail.
> 
> Reproduce:https://github.com/pallets/click/issues/2865

#### Classes

##### Class: `CustomError`

**Line:** 166

**Documentation:** _No documentation_

##### Class: `CustomError`

**Line:** 193

**Documentation:** _No documentation_

##### Class: `CLIError`

**Line:** 228

**Documentation:** _No documentation_

**Methods:**

- **`format_message(self)`** (Line 229)
  - Returns: `str`
  - _No documentation_

---

### `C:\Users\I.C.T\OneDrive\Documents\git\click\tests\test_types.py`

**Language:** python

#### Functions

##### `test_range(type, value, expect)`

**Line:** 31 | **Returns:** `None`

**Parameters:**
- `type`
- `value`
- `expect`

**Documentation:** _No documentation_

##### `test_range_fail(type, value, expect)`

**Line:** 47 | **Returns:** `None`

**Parameters:**
- `type`
- `value`
- `expect`

**Documentation:** _No documentation_

##### `test_float_range_no_clamp_open()`

**Line:** 54 | **Returns:** `None`

**Documentation:** _No documentation_

##### `test_cast_multi_default(runner, nargs, multiple, default, expect)`

**Line:** 77 | **Returns:** `None`

**Parameters:**
- `runner`
- `nargs`
- `multiple`
- `default`
- `expect`

**Documentation:** _No documentation_

##### `test_path_type(runner, cls, expect)`

**Line:** 98 | **Returns:** `None`

**Parameters:**
- `runner`
- `cls`
- `expect`

**Documentation:** _No documentation_

##### `_symlinks_supported()`

**Line:** 109 | **Returns:** `None`

**Documentation:** _No documentation_

##### `test_path_resolve_symlink(tmp_path, runner)`

**Line:** 125 | **Returns:** `None`

**Parameters:**
- `tmp_path`
- `runner`

**Documentation:** _No documentation_

##### `_non_utf8_filenames_supported()`

**Line:** 148 | **Returns:** `None`

**Documentation:** _No documentation_

##### `test_path_surrogates(tmp_path, monkeypatch)`

**Line:** 163 | **Returns:** `None`

**Parameters:**
- `tmp_path`
- `monkeypatch`

**Documentation:** _No documentation_

##### `test_file_surrogates(type, tmp_path)`

**Line:** 226 | **Returns:** `None`

**Parameters:**
- `type`
- `tmp_path`

**Documentation:** _No documentation_

##### `test_file_error_surrogates()`

**Line:** 238 | **Returns:** `None`

**Documentation:** _No documentation_

##### `test_invalid_path_with_esc_sequence()`

**Line:** 246 | **Returns:** `None`

**Documentation:** _No documentation_

##### `test_choice_get_invalid_choice_message()`

**Line:** 254 | **Returns:** `None`

**Documentation:** _No documentation_

---

### `C:\Users\I.C.T\OneDrive\Documents\git\click\tests\test_utils.py`

**Language:** python

#### Functions

##### `test_unset_sentinel()`

**Line:** 22 | **Returns:** `None`

**Documentation:** _No documentation_

##### `test_echo(runner)`

**Line:** 70 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_echo_custom_file()`

**Line:** 94 | **Returns:** `None`

**Documentation:** _No documentation_

##### `test_echo_no_streams(monkeypatch, runner)`

**Line:** 100 | **Returns:** `None`

**Parameters:**
- `monkeypatch`
- `runner`

**Documentation:**

> echo should not fail when stdout and stderr are None with pythonw on Windows.

##### `test_styling(styles, ref)`

**Line:** 149 | **Returns:** `None`

**Parameters:**
- `styles`
- `ref`

**Documentation:** _No documentation_

##### `test_unstyle_other_ansi(text, expect)`

**Line:** 155 | **Returns:** `None`

**Parameters:**
- `text`
- `expect`

**Documentation:** _No documentation_

##### `test_filename_formatting()`

**Line:** 159 | **Returns:** `None`

**Documentation:** _No documentation_

##### `test_prompts(runner)`

**Line:** 167 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_confirm_repeat(runner)`

**Line:** 207 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_prompts_abort(monkeypatch, capsys)`

**Line:** 216 | **Returns:** `None`

**Parameters:**
- `monkeypatch`
- `capsys`

**Documentation:** _No documentation_

##### `test_full_prompt_passed_to_readline(monkeypatch, call, expected_prompt)`

**Line:** 243 | **Returns:** `None`

**Parameters:**
- `monkeypatch`
- `call`
- `expected_prompt`

**Documentation:**

> On non-Windows, prompt and confirm pass the full prompt text to the
> underlying prompt function so readline handles editing correctly.
> 
> https://github.com/pallets/click/issues/2968
> https://github.com/pallets/click/pull/2969

##### `test_prompts_eof(runner)`

**Line:** 262 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:**

> If too few lines of input are given, prompt should exit, not hang.

##### `_test_gen_func()`

**Line:** 275 | **Returns:** `None`

**Documentation:** _No documentation_

##### `_test_gen_func_fails()`

**Line:** 282 | **Returns:** `None`

**Documentation:** _No documentation_

##### `_test_gen_func_echo(file)`

**Line:** 287 | **Returns:** `None`

**Parameters:**
- `file`

**Documentation:** _No documentation_

##### `_test_simulate_keyboard_interrupt(file)`

**Line:** 293 | **Returns:** `None`

**Parameters:**
- `file`

**Documentation:** _No documentation_

##### `test_echo_via_pager(monkeypatch, capfd, pager_cmd, test, tmp_path)`

**Line:** 411 | **Returns:** `None`

**Parameters:**
- `monkeypatch`
- `capfd`
- `pager_cmd`
- `test`
- `tmp_path`

**Documentation:** _No documentation_

##### `test_echo_color_flag(monkeypatch, capfd)`

**Line:** 449 | **Returns:** `None`

**Parameters:**
- `monkeypatch`
- `capfd`

**Documentation:** _No documentation_

##### `test_prompt_cast_default(capfd, monkeypatch)`

**Line:** 483 | **Returns:** `None`

**Parameters:**
- `capfd`
- `monkeypatch`

**Documentation:** _No documentation_

##### `test_echo_writing_to_standard_error(capfd, monkeypatch)`

**Line:** 491 | **Returns:** `None`

**Parameters:**
- `capfd`
- `monkeypatch`

**Documentation:** _No documentation_

##### `test_echo_with_capsys(capsys)`

**Line:** 574 | **Returns:** `None`

**Parameters:**
- `capsys`

**Documentation:** _No documentation_

##### `test_open_file(runner)`

**Line:** 580 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_open_file_pathlib_dash(runner)`

**Line:** 602 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_open_file_ignore_errors_stdin(runner)`

**Line:** 618 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_open_file_respects_ignore(runner)`

**Line:** 629 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_open_file_ignore_invalid_utf8(runner)`

**Line:** 638 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_open_file_ignore_no_encoding(runner)`

**Line:** 647 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_open_file_atomic_permissions_existing_file(runner, permissions)`

**Line:** 658 | **Returns:** `None`

**Parameters:**
- `runner`
- `permissions`

**Documentation:** _No documentation_

##### `test_open_file_atomic_permissions_new_file(runner)`

**Line:** 675 | **Returns:** `None`

**Parameters:**
- `runner`

**Documentation:** _No documentation_

##### `test_iter_keepopenfile(tmpdir)`

**Line:** 694 | **Returns:** `None`

**Parameters:**
- `tmpdir`

**Documentation:** _No documentation_

##### `test_iter_lazyfile(tmpdir)`

**Line:** 703 | **Returns:** `None`

**Parameters:**
- `tmpdir`

**Documentation:** _No documentation_

##### `test_detect_program_name(path, main, expected)`

**Line:** 731 | **Returns:** `None`

**Parameters:**
- `path`
- `main`
- `expected`

**Documentation:** _No documentation_

##### `test_expand_args(monkeypatch)`

**Line:** 735 | **Returns:** `None`

**Parameters:**
- `monkeypatch`

**Documentation:** _No documentation_

##### `test_make_default_short_help(value, max_length, alter, expect)`

**Line:** 775 | **Returns:** `None`

**Parameters:**
- `value`
- `max_length`
- `alter`
- `expect`

**Documentation:** _No documentation_

#### Classes

##### Class: `MockMain`

**Line:** 713

**Documentation:** _No documentation_

**Methods:**

- **`__init__(self, package_name)`** (Line 716)
  - Returns: `None`
  - _No documentation_

---

### `C:\Users\I.C.T\OneDrive\Documents\git\click\tests\typing\typing_aliased_group.py`

**Language:** python

#### Functions

##### `cli()`

**Line:** 32 | **Returns:** `None`

**Documentation:** _No documentation_

##### `push()`

**Line:** 40 | **Returns:** `None`

**Documentation:** _No documentation_

##### `pop()`

**Line:** 45 | **Returns:** `None`

**Documentation:** _No documentation_

#### Classes

##### Class: `AliasedGroup`

**Line:** 10

**Documentation:** _No documentation_

**Methods:**

- **`get_command(self, ctx, cmd_name)`** (Line 11)
  - Returns: `click.Command | None`
  - _No documentation_

- **`resolve_command(self, ctx, args)`** (Line 22)
  - Returns: `tuple[str | None, click.Command, list[str]]`
  - _No documentation_

---

### `C:\Users\I.C.T\OneDrive\Documents\git\click\tests\typing\typing_confirmation_option.py`

**Language:** python

#### Functions

##### `dropdb()`

**Line:** 10 | **Returns:** `None`

**Documentation:** _No documentation_

---

### `C:\Users\I.C.T\OneDrive\Documents\git\click\tests\typing\typing_group_kw_options.py`

**Language:** python

#### Functions

##### `hello()`

**Line:** 7 | **Returns:** `None`

**Documentation:** _No documentation_

---

### `C:\Users\I.C.T\OneDrive\Documents\git\click\tests\typing\typing_help_option.py`

**Language:** python

#### Functions

##### `hello()`

**Line:** 8 | **Returns:** `None`

**Documentation:**

> Simple program that greets NAME for a total of COUNT times.

---

### `C:\Users\I.C.T\OneDrive\Documents\git\click\tests\typing\typing_options.py`

**Language:** python

#### Functions

##### `hello(count, name)`

**Line:** 11 | **Returns:** `None`

**Parameters:**
- `count` (int)
- `name` (str)

**Documentation:** _No documentation_

---

### `C:\Users\I.C.T\OneDrive\Documents\git\click\tests\typing\typing_password_option.py`

**Language:** python

#### Functions

##### `encrypt(password)`

**Line:** 10 | **Returns:** `None`

**Parameters:**
- `password` (str)

**Documentation:** _No documentation_

---

### `C:\Users\I.C.T\OneDrive\Documents\git\click\tests\typing\typing_progressbar.py`

**Language:** python

#### Functions

##### `test_length_is_int()`

**Line:** 9 | **Returns:** `None`

**Documentation:** _No documentation_

##### `it()`

**Line:** 16 | **Returns:** `tuple[str, ...]`

**Documentation:** _No documentation_

##### `test_generic_on_iterable()`

**Line:** 20 | **Returns:** `None`

**Documentation:** _No documentation_

---

### `C:\Users\I.C.T\OneDrive\Documents\git\click\tests\typing\typing_simple_example.py`

**Language:** python

#### Functions

##### `hello(count, name)`

**Line:** 11 | **Returns:** `None`

**Parameters:**
- `count` (int)
- `name` (str)

**Documentation:**

> Simple program that greets NAME for a total of COUNT times.

---

### `C:\Users\I.C.T\OneDrive\Documents\git\click\tests\typing\typing_version_option.py`

**Language:** python

#### Functions

##### `hello()`

**Line:** 12 | **Returns:** `None`

**Documentation:** _No documentation_

---

## 📈 Summary Statistics

- **Total Files Scanned:** 63
- **Total Functions/Methods:** 1087
- **Total Classes:** 153
- **Documentation Coverage:** 33.4%
- **Documented Items:** 363
- **Undocumented Items:** 724

---

_Generated by Codebase Scanner_