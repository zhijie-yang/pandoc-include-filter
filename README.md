The Pandoc Inplace Include Filter
==========

This is a repo that provides a pandoc filter to include files in a markdown file.
This filter does not replace the `!include` or `{include}` directives directly
in the markdown file, but instead uses a `<div>` tag with a `class="include"` attribute.
This allows to keep the import relations of the source files, while still being able to
include them in the same markdown file, and invariant of running `pandoc` commands on the
same file if the sources are not changed.

## Installation
```bash
pip install pandoc-inplace-include
```

## Inflate me with
```bash
pandoc README.md -o README.md --filter pandoc-inplace-include
```

## Test me with
```bash
pandoc README.md -o README.1.md --filter include_filter.py
pandoc README.1.md -o README.2.md --filter include_filter.py
diff README.1.md README.2.md
```

## Supported syntax
```markdown
<div class="include" file="some.other.md.file.md" start="starting_line_num" end="ending_line_num">
All the contents within such <div> will be replaced by the contents of the file "some.other.md.file.md"
</div>
```

## To be added
- [ ] Support for recursive includes

## Now try to include some files
The `<div>` stuff should not be rendered, but only kept in the source file.

<div class="include" file="_common/docs/file1.md" start=5 end=100>
This part will be replaced after running `pandoc`
</div>

Other things below won't get replaced.
