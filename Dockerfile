FROM python:3.12

# Make a new group and user so we don't run as root.
RUN addgroup --system appgroup && adduser --system appuser --ingroup appgroup

WORKDIR /app

# Let the appuser own the files so he can rwx during runtime.
COPY --chown=appuser:appgroup . .

# We install all our Python dependencies. Add the extra index url because some
# packages are in the meemoo repo.
RUN pip install git+https://https://github.com/viaacode/chassis.py.git \
pip install .

USER appuser

# This command will be run when starting the container. It is the same one that can be used to run the application locally.
CMD [ "python", "main.py"]
