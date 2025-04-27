.PHONY: all run build test clean

# Variables
IMAGE_NAME = python-word-counter
CONTAINER_NAME = word-counter
PYTHON_FILE = main.py
INPUT_FILE = words.txt
REMOVE_DUPLICATES = yes

# Regla principal
all: build run

# Construir imagen personalizada
build:
	docker build -t $(IMAGE_NAME) .

# Correr el contenedor
run:
	docker run --rm --name $(CONTAINER_NAME) \
		--volume `pwd`:/opt/app \
		--env PYTHON_PATH=/opt/app \
		-w /opt/app \
		$(IMAGE_NAME) \
		python3 $(PYTHON_FILE) $(INPUT_FILE) $(REMOVE_DUPLICATES)

# Ejecutar tests (puedes mejorarlo luego)
test:
	echo "Test rápido: Ejecutando script..."
	docker run --rm --volume `pwd`:/opt/app --workdir /opt/app $(IMAGE_NAME) python3 $(PYTHON_FILE) $(INPUT_FILE) $(REMOVE_DUPLICATES)

# Limpiar (borrar la imagen docker)
clean:
	docker rmi -f $(IMAGE_NAME) || true