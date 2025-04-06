#!/bin/bash

echo "Cargando variables desde .env..."
set -o allexport
source .env
set +o allexport

echo "🛠️ Generando archivo config_parameters.xml a partir de config_parameters.template.xml..."

TEMPLATE_PATH="./addons/movie_manager/data/config_parameters.template.xml"
OUTPUT_PATH="./addons/movie_manager/data/config_parameters.xml"

if [ ! -f "$TEMPLATE_PATH" ]; then
  echo "Archivo de plantilla no encontrado: $TEMPLATE_PATH"
  exit 1
fi

envsubst < "$TEMPLATE_PATH" > "$OUTPUT_PATH"

echo " Archivo generado en: $OUTPUT_PATH"
