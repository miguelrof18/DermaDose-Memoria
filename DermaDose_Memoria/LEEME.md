# DermaDose: memoria con revisión gráfica

Edición de 26 de octubre de 2026. Idioma: español.

La revisión rehace las 17 figuras anteriores y añade 15: 32 figuras en TikZ/PGFPlots. `INVENTARIO_FIGURAS.md` relaciona cada figura con su archivo editable y su objetivo didáctico. El número de página PDF incluye portada e índices.

## Abrir y compilar

El archivo principal es `memoria.tex`. Los capítulos se encuentran en `capitulos/`, las figuras en `figuras/` y los datos de los gráficos en `datos/`. Todos los diagramas y curvas son vectoriales; no se necesitan imágenes externas ni servicios web para compilar.

En Overleaf: subir el ZIP como proyecto, elegir `memoria.tex` y pdfLaTeX. Localmente, instalar TeX Live o MiKTeX con TikZ, PGFPlots, natbib, xurl, needspace, tcolorbox, babel y títulos:

    latexmk -pdf -interaction=nonstopmode -halt-on-error memoria.tex

Alternativa: pdfLaTeX, BibTeX y dos pasadas de pdfLaTeX. Se recomiendan babel-spanish y siunitx; hay alternativas en el preámbulo cuando no están instalados.

## Convenciones de las figuras

- Esquemas conceptuales: geometría y valores inventados se identifican en el pie. No representan anatomía ni mediciones clínicas.
- Gráficos numéricos: conservan las condiciones del espectro, la tabla y el estudio del que proceden.
- Color, texto y estilo de línea se complementan para permitir lectura en escala de grises.
- Los parámetros del perfil histórico y los del refinamiento condicionado permanecen diferenciados.

## Datos de las nuevas curvas

`mono_s5.csv`, `mono_s20.csv` y `mono_s35.csv` seleccionan nodos de la tabla monoenergética original y añaden su producto B*f. `kernel_integracion.csv` combina la densidad de kerma conservada a 80 kVp, 4,1 mm Al, 0,1 mm Cu y 12 grados con el producto monoenergético interpolado a lado 20 cm. Su integral es un factor relativo, no un rendimiento ni una nueva medición.

Los esquemas HVL y dosis-área usan ejemplos adimensionales declarados. La comparación condicionada reutiliza las observaciones y resultados que ya figuraban en la memoria; no se añaden resultados experimentales ni incertidumbres supuestas.

## Anexos de uso

Los apéndices G y H de la memoria explican el contrato de configuración JSON y el subconjunto de datos por evento y acumulados que interpreta el lector RDSR. Incluyen unidades, campos requeridos, datos opcionales, conversiones y límites relevantes (por ejemplo, ausencia de filtración declarada no equivale a filtración cero).

## Alcance

Esta edición modifica la documentación y las figuras; no cambia el motor de DermaDose. No incluye RDSR, TC, STL del paciente ni documentos originales de la instalación. La memoria no constituye una validación clínica. El ZIP es el proyecto documental, no una distribución del programa.

Los scripts de `scripts/` corresponden a los estudios numéricos previos. Requieren el código DermaDose y SpekPy 2.5.4 para repetirlos. Los gráficos se compilan directamente con los datos CSV incluidos.
