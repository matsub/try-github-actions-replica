FROM alpine:3.8

LABEL "com.github.actions.name"="Hello World"
LABEL "com.github.actions.description"="Write arguments to the standard output"
LABEL "com.github.actions.icon"="anchor"

LABEL "repository"="https://github.com/matsub/try-github-actions"
LABEL "maintainer"="matsub <matsub.rk@gmail.com>"

ADD entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
