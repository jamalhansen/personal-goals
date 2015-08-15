# Commands are:
# pg-add <content-type> - Opens up content page in Vim for adding resources.
# pg-ch - Opens up README.md for quick checking off of weekly goals.
# pg-gh - Pushes to your master branch with a commit message of "push from terminal" and opens the Github page online


# check off personal goals (open main README.md in vim)
# i.e. alias pg-ch="vim ~/Dev/personal-goals/README.md
alias pg-ch="vim ~/goals/README.md"

# add to content list (opens content list folder in vim)
# usage example: pg-add blog-post
function pg-add() {
    if [ $# -eq 0 ]; then
        print "Oops. Please enter a content type! (i.e. pg-add book)"
    else
        vim ~/goals/content-list/"$@"s.md
    fi
}

# pull refresh my goals from github
alias pg-pl="cd ~/goals &&
    git pull"

# push my changes to my github master branch and open the page
# The commit message will always be "push from termianl" since I'll probably just be adding more resources or checking things off when using this
alias pg-gh="cd ~/goals &&
    git checkout master &&
    git add -A &&
    git commit -m 'push from terminal' &&
    git push origin master &&
    open http://github.com/kylegalloway/personal-goals"

# To add to zshrc/bashrc use `source "{PATH_TO_ALIAS_FILE)/"
