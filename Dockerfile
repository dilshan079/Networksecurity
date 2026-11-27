FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# Install dependencies in a separate layer so Docker can reuse this layer
# when only application code changes. The empty requirements.txt is valid too.
COPY requirements.txt ./
RUN python -m pip install --upgrade pip \
    && if [ -s requirements.txt ]; then \
         python -m pip install -r requirements.txt; \
       fi

# Copy only the project files needed by the current package.
COPY networksecurity ./networksecurity
COPY setup.py ./

# There is currently no executable application module in the repository.
# This verifies that the package can be imported and keeps the image useful
# until a real application entrypoint is added.
CMD ["python", "-c", "import networksecurity; print('networksecurity package is ready')"]
