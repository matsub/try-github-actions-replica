workflow "Test" {
  on = "push"
  resolves = "npm test"
}

action "npm test" {
  needs = "npm lint"
  uses = "actions/npm@master"
  args = "run test"
}

action "npm lint" {
  needs = "npm install"
  uses = "actions/npm@master"
  args = "run lint"
}

action "npm install" {
  uses = "actions/npm@master"
  args = "install"
}

#===========================
workflow "Assign Reviewer" {
  on = "pull_request"
  resolves = "Assign"
}

action "Assign" {
  uses = "./action-assign-reviewer"
  env = {
    MAX_REVIEWER = "2"
  }
  secrets = ["GITHUB_TOKEN"]
}
