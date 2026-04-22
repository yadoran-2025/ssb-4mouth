import codecs

file_path = "c:\\Users\\user\\ssb-4mouth\\index.html"

with codecs.open(file_path, 'r', 'utf-8') as f:
    content = f.read()

# Finding the exact block to replace for CSS
css_start = content.find("<style>")
css_end = content.find("</style>") + len("</style>")

if css_start != -1 and css_end != -1:
    css_content = content[css_start + len("<style>"):css_end-len("</style>")].strip()
    with codecs.open("c:\\Users\\user\\ssb-4mouth\\style.css", 'w', 'utf-8') as f:
        f.write(css_content)
    content = content[:css_start] + '<link rel="stylesheet" href="style.css">' + content[css_end:]

# Finding the exact block to replace for JS (the last script block)
js_start = content.rfind("<script>")
js_end = content.rfind("</script>") + len("</script>")

if js_start != -1 and js_end != -1:
    js_content = content[js_start + len("<script>"):js_end - len("</script>")].strip()
    with codecs.open("c:\\Users\\user\\ssb-4mouth\\game.js", 'w', 'utf-8') as f:
        f.write(js_content)
    content = content[:js_start] + '<script src="game.js"></script>' + content[js_end:]

with codecs.open("c:\\Users\\user\\ssb-4mouth\\index.html", 'w', 'utf-8') as f:
    f.write(content)

print("Files successfully split into index.html, style.css, and game.js")
