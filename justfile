clean:
    if [ -d "build/posts" ]; then \
        rm -r build/posts; \
    fi
    python3 main.py flush

get-posts:
    if [ ! -d "posts" ]; then \
        git clone https://github.com/FortressNebula/doerofthings-articles posts; \
    fi
    cd posts && git pull

[default]
build: get-posts clean
    mkdir build/posts
    python3 main.py

