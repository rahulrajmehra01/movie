mkdir -p ~/.streamlit/


echo "\
[sever]\n\
port = $PORT\n\
enableCORE = false\n\
headless = true\n\
\n\
" > ~/.streamlit/credentials.toml
