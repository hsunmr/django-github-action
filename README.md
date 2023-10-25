### Django project github action implementation

#### Jobs
- lint
    - Check python syntax (flake8)
- build
    - Install python dependencies
    - Cache python dependencies
- test
    - Restore cached python dependencies
    - Run test
- package-release
    - Upload project artifacts
- deploy
    - deploy