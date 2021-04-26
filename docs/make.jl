using Documenter

deploydocs(
    target="_build/dirhtml",
    repo="github.com/dfm/sphinx-documenter-deploy.git",
    devbranch="main",
    devurl="latest"
)
