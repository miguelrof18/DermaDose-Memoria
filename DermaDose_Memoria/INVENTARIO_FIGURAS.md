# Inventario de figuras

Revisión de 26 de octubre de 2026: **17 figuras rehechas + 15 nuevas = 32**. Todas se editan con TikZ o PGFPlots y se compilan desde `memoria.tex`.

| Figura | Página PDF | Archivo | Revisión | Objetivo |
|---|---:|---|---|---|
| 3.1 | 20 | `figuras/distancia_pka.tex` | Nueva | Relacionar divergencia, inverso del cuadrado y producto kerma-área. |
| 3.2 | 22 | `figuras/ecuacion.tex` | Nueva | Leer la ecuación del motor por función física y por unidades. |
| 3.3 | 25 | `figuras/mesa.tex` | Nueva | Distinguir cruce del segmento, transmisión escalar y endurecimiento futuro. |
| 3.4 | 26 | `figuras/superposicion.tex` | Rehecha | Mostrar suma espacial y diferencia entre máximo de suma y suma de máximos. |
| 4.1 | 27 | `figuras/coordenadas.tex` | Nueva | Distinguir cambio de base, unidades y registro anatómico. |
| 4.2 | 28 | `figuras/geometria.tex` | Rehecha | Separar distancia axial de distancia foco-punto. |
| 4.3 | 29 | `figuras/areas_campo.tex` | Nueva | Separar campo normal, huella oblicua y argumento tabulado. |
| 4.4 | 29 | `figuras/primera_entrada.tex` | Nueva | Ilustrar oclusión, caras de salida y primera intersección. |
| 4.5 | 30 | `figuras/centroides.tex` | Nueva | Mostrar error de clasificación en una cara parcialmente irradiada. |
| 4.6 | 31 | `figuras/metricas.tex` | Nueva | Explicar ponderación por área e histograma acumulado. |
| 5.1 | 32 | `figuras/flujo.tex` | Rehecha | Integrar las tres entradas, cálculo por evento y salidas auditables. |
| 5.2 | 34 | `figuras/estados_filtro.tex` | Nueva | Separar ausencia declarada, material conocido e información indeterminada. |
| 6.1 | 37 | `figuras/slicer.tex` | Rehecha | Mostrar segmentación, validación y conservación de la original si falla reducción. |
| 7.1 | 41 | `figuras/monoenergeticos.tex` | Nueva | Visualizar dependencia energética y de campo de B y C nodales. |
| 7.2 | 42 | `figuras/dominio.tex` | Nueva | Mostrar familias discretas de Al y límites de Cu sin extrapolación. |
| 8.1 | 45 | `figuras/filtracion.tex` | Rehecha | Representar Al fijo y capas añadidas sin equivalencias materiales constantes. |
| 9.1 | 48 | `figuras/espectral.tex` | Rehecha | Explicar generación de espectro, producto nodal, dominio e integración. |
| 9.2 | 51 | `figuras/espectros_grafico.tex` | Rehecha | Comparar distribuciones de fotones y de kerma con normalización explícita. |
| 9.3 | 52 | `figuras/kernel_integracion.tex` | Nueva | Mostrar el integrando cuyo área da el combinado espectral. |
| 10.1 | 54 | `figuras/convergencia.tex` | Rehecha | Mostrar estabilidad numérica histórica, sin identificarla con exactitud física. |
| 11.1 | 58 | `figuras/validacion.tex` | Rehecha | Separar niveles y evidencia necesaria para cada tipo de evaluación. |
| 11.2 | 60 | `figuras/incertidumbre.tex` | Rehecha | Relacionar fuentes físicas, geométricas, numéricas y de adecuación. |
| 13.1 | 68 | `figuras/ponderacion.tex` | Rehecha | Conectar fluencia, energía, kerma normalizado y respuesta superficial. |
| 13.2 | 69 | `figuras/retrodispersion.tex` | Rehecha | Distinguir primarios, retorno disperso y región superficial central. |
| 13.3 | 70 | `figuras/kerma_dosis.tex` | Rehecha | Explicar transferencia inicial y depósito con transporte a través de límites. |
| 13.4 | 71 | `figuras/promedios.tex` | Rehecha | Demostrar la no conmutatividad con ejemplo algebraico verificable. |
| 13.5 | 71 | `figuras/hvl.tex` | Rehecha | Distinguir HVL1 y HVL2 adicional con igual HVL1 para curvas diferentes. |
| 13.6 | 72 | `figuras/discretizacion.tex` | Rehecha | Separar error de forma, error de muestreo y error de registro. |
| 14.1 | 74 | `figuras/ajuste_hvl.tex` | Rehecha | Distinguir grupos de ajuste, grupo reservado y residuos sin errores supuestos. |
| 14.2 | 75 | `figuras/impacto_factores.tex` | Nueva | Visualizar cambio entre perfiles sin convertirlo en incertidumbre o exactitud. |
| 14.3 | 75 | `figuras/malla_dataset.tex` | Nueva | Separar 182 espectros de 910 filas con eje de campo. |
| 14.4 | 76 | `figuras/consulta_C.tex` | Nueva | Comparar políticas combinada y separada, respetando versiones de datasets. |

## Comprobaciones gráficas y científicas

- Revisión visual de las 32 figuras en su contexto de página; corrección de cruces de texto, tamaños, flechas y leyendas.
- Compilación final con bibliografía y referencias resueltas, sin desbordamientos de cajas.
- 32 figuras vectoriales; ausencia de imágenes rasterizadas dentro del PDF.
- Valores de los gráficos conservados; las nuevas curvas monoenergéticas son selecciones y productos de datos existentes.
- Ejemplos docentes adimensionales identificados; sin trayectorias de transporte atribuidas al motor.
- Perfil de 12 grados y 3,1 mm Al separado del perfil condicionado de 11 grados y Al efectivo ajustado.
- Edición científica posterior: correcciones de código documentadas en el capítulo de revisión; sin nuevos resultados de dosis clínica.
