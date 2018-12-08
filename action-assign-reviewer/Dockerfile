FROM python:3.6-alpine3.7

LABEL "com.github.actions.name"="Assign Reviewer"
LABEL "com.github.actions.description"="Assign a PR reviewer when it does not have enough reviewers"
LABEL "com.github.actions.icon"="edit"
LABEL "com.github.actions.color"="blue"

LABEL "repository"="https://github.com/matsub/try-github-actions"
LABEL "maintainer"="matsub <matsub.rk@gmail.com>"

ADD main.py /main.py
CMD ["python", "/main.py"]
