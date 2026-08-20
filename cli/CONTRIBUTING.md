# Contributing to `cli`

Thank you for your interest!

## Development Workflow

First, a local project environment needs to be created, then the project's modules will be installed into locally into a virtual environment.

1. Clone the repository.

   ```sh
   git clone https://github.com/bellanov/gcp.git
   cd gcp/cli
   ```

2. Create a virtual environment. 

    **Virtual Environments** enable you isolate installations of *Python*, so you are able to test your changes against multiple Python versions. They also help you avoid polluting the default Python installation.

   ```sh
   # Create Virtual Environment
   python3 -m venv .venv

   # Activate Virtual Environment
   source .venv/bin/activate

   # Install all dependencies (runtime and development)
   scripts/ci/install.sh

   # Deactivate Virtual Environment
   deactivate
   ```

3. Make your changes and open a **Pull Request**.

   ```sh
   # Create a branch to isolate your changes
   git branch my-new-feature

   # Hop onto the branch to add your changes
   git checkout my-new-feature

   # Make your changes and commit them
   git add .
   git commit -m "Added My New Feature"

   # Push the changes to your branch (first push)
   git push --set-upstream origin my-new-feature

   # All future pushes
   git push

   # Create a pull request using the provided link after pushing
   remote: 
   remote: Create a pull request for 'my-new-feature' on GitHub by visiting:
   remote:      https://github.com/bellanov/pythonic-programming/pull/new/my-new-feature

   ```