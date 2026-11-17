get-posts:
    if [ ! -d "posts" ]; then \
        git clone https://github.com/FortressNebula/doerofthings-articles posts; \
    fi
    cd posts
    git pull