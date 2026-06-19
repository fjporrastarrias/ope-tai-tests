# CLAUDE.md

## Proyecto
Aplicación web estática para realizar tests tipo examen a partir de bloques de preguntas en ficheros JSON.
Se publica en GitHub Pages y debe seguir siendo compatible con un despliegue estático sin backend.

## Arquitectura obligatoria
- La aplicación debe implementarse como una SPA en `index.html`
- `index.html` debe contener toda la aplicación
- Usar HTML, CSS y JavaScript vanilla integrados en el mismo archivo
- No crear archivos JS o CSS separados salvo necesidad técnica clara y previamente explicada
- No usar frameworks
- Los datos de preguntas deben cargarse desde la carpeta `json/`

## Estructura funcional de la SPA
La SPA debe resolver estas vistas dentro de `index.html`:
- vista de inicio
- vista de test
- vista de resultados
- vista de revisión
- vista de historial, si se considera útil dentro del mismo flujo

## Datos
- La carpeta `json/` contiene los bloques de preguntas
- Cada bloque está en un fichero `.json`
- Cada bloque contiene 10 preguntas
- Cada pregunta tiene 4 respuestas posibles
- Solo una respuesta es correcta y está marcada en el JSON
- No modificar la estructura de los JSON salvo petición explícita

## Reglas funcionales
- El usuario puede seleccionar como máximo 8 bloques
- En cada generación del test, las respuestas deben mostrarse en orden aleatorio
- Durante la resolución no se debe indicar si la respuesta elegida es correcta o incorrecta
- No es obligatorio contestar todas las preguntas
- Debe existir contador regresivo de 90 minutos
- Debe mostrarse cuántas preguntas están contestadas sobre el total
- Deben existir botones de anterior, siguiente y finalizar

## Resultados
Mostrar:
- tiempo empleado
- preguntas contestadas
- preguntas correctas
- preguntas erróneas
- puntuación = correctas * 0.125 - erróneas * 0.05
- mostrar la puntuación con 3 decimales
- botón para revisar la resolución
- botón para volver al inicio

## Revisión
- Mostrar listado de preguntas
- Mostrar respuesta correcta
- Mostrar la opción elegida por el usuario
- Si la elegida fue correcta, marcar en verde
- Si fue incorrecta, marcar en rojo la opción elegida
- Mantener visible cuál era la respuesta correcta

## Persistencia
- Guardar historial de intentos con:
  - bloques seleccionados
  - fecha
  - hora
  - resultado obtenido
- Priorizar soluciones simples compatibles con GitHub Pages

## Restricciones técnicas
- Compatibilidad con GitHub Pages
- Sin backend
- Sin frameworks
- Código simple, legible y mantenible
- Reutilizar la estructura existente antes de crear nada nuevo

## UX y accesibilidad
- HTML semántico
- Responsive básico
- Focus visible
- Navegación clara entre vistas
- Botones y controles bien identificados

## Forma de trabajo
- Primero inspeccionar el proyecto actual
- Resumir el plan antes de implementar
- Preguntar si hay dudas sobre el formato de los JSON o el flujo
- Implementar de forma incremental y fácil de revisar

## Verificación mínima
Comprobar siempre:
- selección máxima de 8 bloques
- carga correcta de JSON
- aleatorización de respuestas
- contador regresivo
- navegación anterior/siguiente/finalizar
- cálculo correcto con 3 decimales
- persistencia del historial
- funcionamiento de las vistas SPA en `index.html`

Si no detectas impedimentos técnicos, implementa la SPA con una única plantilla `index.html` y con un estado global en JavaScript que controle las vistas `inicio`, `test`, `resultados` y `revision`.