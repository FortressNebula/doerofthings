import markdown, os, sys
from funky_markdown_stuff import DashAdderExtension

def collect_post_paths(posts_path="posts"):
    out = []
    for path in os.listdir(posts_path):
        if path.endswith(".md"):
            out.append(path)
    return out

def parse_post(post, posts_path="posts"):
    post_raw_text = ""
    with open(posts_path + '/' + post, 'rt') as file:
        post_raw_text = file.read()

    post_raw_lines = post_raw_text.splitlines()

    TITLE = post_raw_lines[0].lstrip('#').lstrip()
    SUBTITLE = post_raw_lines[1]
    DATE = post_raw_lines[2]

    BODY = markdown.markdown('\n'.join(post_raw_lines[3:]), extensions=[DashAdderExtension()])

    return (post.split('.')[0], TITLE, SUBTITLE, DATE, BODY)

def stylised_title(title:str):
    title_words = title.lower().split(' ')
    out = "/"
    for i, word in enumerate(title_words):
        if i != 0: out += "-"
        out += "<span style=\"color:white\">"
        out += word
        out += "</span>"
    out += "/"
    return out

def create_post_file(post_data):
    id, title, subtitle, date, body = post_data

    template = ""
    with open("template.html", "rt") as file:
        template = file.read()

    out = template.format(
        title=title.lower(),
        stylised_title_html=stylised_title(title),
        subtitle=subtitle,
        body_html=body,
        date=date
    )

    os.mkdir(f"build/posts/{id}")
    with open(f"build/posts/{id}/index.html", "wt") as file:
        file.write(out)
    

def create_post_index_element(post_data):
    id, title, subtitle, date, _ = post_data

    template = ""
    with open("post_index_template.html", "rt") as file:
        template = file.read()

    out = template.format(
        id=id,
        title=title.lower(),
        subtitle=subtitle,
        date=date
    )

    return out 

def write_post_index(post_index):
    template = ""
    with open("build/index.html", "rt") as file:
        template = file.read()

    out = template.format(
        post_index=post_index
    )
    with open("build/index.html", "wt") as file:
        file.write(out)

def reset_index_html():
    template = ""
    with open("home_page.html", "rt") as file:
        template = file.read()

    with open("build/index.html", "wt") as file:
        file.write(template)

def run():
    if len(sys.argv) > 1:
        if sys.argv[1] == "flush":
            reset_index_html()
            return

    paths = collect_post_paths()
    post_index = ""
    for p in paths:
        data = parse_post(p)
        create_post_file(data)
        post_index += create_post_index_element(data)
    write_post_index(post_index)

if __name__ == "__main__":
    run()
    