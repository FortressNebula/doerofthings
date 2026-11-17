import markdown, sys

if __name__ == "__main__":
    markdown_text = ""
    with open("posts/test.md", 'rt') as file:
        markdown_text = file.read()
    print(markdown.markdown(markdown_text))