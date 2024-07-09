from pandocfilters import Para, RawInline, toJSONFilters, CodeBlock
import sys

STARTING_LINE_FMT = '<div class="include" {}>'
ENDING_LINE = "</div>"


def get_value(kvs, key):
    for k, v in kvs:
        if k == key:
            return v
    return None


def include(key, value, format, meta):
    if key == "Div":
        [[_, classes, kvs], _] = value
        if classes == ["include"]:
            new_contents = []
            include_file = get_value(kvs, "file")
            kvs_str = " ".join(["=".join(kv) for kv in kvs])
            starting_line = STARTING_LINE_FMT.format(kvs_str)
            new_contents.append(Para([RawInline("markdown", starting_line)]))
            start = get_value(kvs, "start")
            end = get_value(kvs, "end")
            start = int(start) if start else 1
            end = int(end) if end else -1
            with open(include_file, "r", encoding="utf-8") as f:
                lines = f.readlines()
                start = max(start, 1)
                end = min(end, len(lines))
                lines = lines[start - 1 : end]
                include_contents = [Para([RawInline("markdown", "".join(lines))])]
            new_contents.extend(include_contents)
            new_contents.append(Para([RawInline("markdown", ENDING_LINE)]))
            return new_contents


def keepCodeBlockLanguage(key, value, format, meta):
    if key == "CodeBlock":
        [[ident, classes, kvs], code] = value
        new_contents = [Para([RawInline("markdown", "```{}".format(classes[0]))])]
        new_contents.append(Para([RawInline("markdown", code)]))
        new_contents.append(Para([RawInline("markdown", "```")]))
        return new_contents


if __name__ == "__main__":
    toJSONFilters([include, keepCodeBlockLanguage])
