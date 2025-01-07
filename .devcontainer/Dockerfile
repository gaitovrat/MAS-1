FROM python:3.12.8-bullseye

# Install git
RUN apt-get update
RUN apt-get install -y git build-essential

# Create dev user
RUN groupadd devgroup && useradd -ms /bin/bash -g devgroup dev
USER dev

# Install pipx
RUN python -m pip install -U pip
RUN python -m pip install pipx

ENV PATH="$PATH:/home/dev/.local/bin"

# Install cli tools via pipx
RUN python -m pipx install pre-commit poetry black isort nbqa

CMD ["/bin/bash"]
