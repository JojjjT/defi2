# DEFI 2 — Dashboard Quarto

Dashboard sobre precios históricos (yfinance) con siete páginas:

- **Precio histórico**: varios tickers, base 100, eje log, media móvil, selector de rango y control deslizante de fechas, volatilidad móvil y distribución de retornos.
- **Vasicek**, **Merton** y **Ornstein-Uhlenbeck**: calibración visible (regresión AR(1) o detección de saltos), tabla de parámetros calibrados vs. usados y simulación Monte Carlo comparada con el precio real. Cada una añade visualizaciones propias (abanicos analíticos exactos, mapas de probabilidad, VaR/ES, calibración móvil, QQ-plots, ACF, sensibilidad al umbral de saltos, superficie de volatilidad implícita 3D, etc.): efecto de la velocidad de reversión, distribución al horizonte contra la analítica, primer cruce del nivel de equilibrio, diagnóstico de residuos, descomposición difusión/saltos, sonrisa de volatilidad implícita de Merton (1976) y tamaño de los saltos.
- **Herding: activos**: test de manada de Chang, Cheng y Khorana (CSAD) sobre el universo de tickers, con errores de Newey-West, mercados al alza y a la baja, días extremos, γ₂ móvil y correlación media.
- **Herding: opciones**: modelo de Kirman (agentes optimistas/pesimistas con imitación) que mueve drift y volatilidad; opciones europeas valoradas por Monte Carlo con corrección de martingala y sonrisa de volatilidad implícita.
- **Opciones reales**: diferir, expandir y abandonar, valoradas en un retículo binomial CRR con ejercicio americano, umbral crítico V*, umbral perpetuo de McDonald-Siegel y sensibilidad a σ y al plazo.

La barra lateral de cada página (que ocupa toda la altura de la página y mantiene los controles visibles al hacer scroll) permite cambiar ticker, ventana de calibración, horizonte, número de trayectorias, semilla y cada parámetro del modelo; todo se recalcula en el navegador. Cambiar horizonte, trayectorias o semilla ya no reinicia los sliders de parámetros.

Cada página incluye además la calibración de referencia de FinStoch (muestra completa).

## Uso local

```bash
git clone https://github.com/<usuario>/defi2-dashboard.git
cd defi2-dashboard
pip install -r requirements.txt
python download_data.py
quarto render
```

Abre `docs/index.html`. Si Quarto no encuentra tu Python o tu kernel, define `QUARTO_PYTHON` con la ruta de `python.exe` o cambia `jupyter: python3` en `dashboard.qmd` por el nombre de un kernel que tenga los paquetes instalados.

## Despliegue en GitHub Pages

1. Ejecuta `quarto render` en local al menos una vez: crea la carpeta `_freeze/`.
2. Sube el repositorio a GitHub **incluyendo `_freeze/`** (el CI no ejecuta Python ni descarga datos, solo reconstruye el HTML congelado).
3. Haz push a `main`: el workflow renderiza y publica en la rama `gh-pages`.
4. En Settings > Pages elige *Deploy from a branch* → `gh-pages` / `(root)`.

## Notas

- Las simulaciones y los gráficos interactivos corren en JavaScript dentro del navegador; no hace falta servidor. Plotly se carga desde `cdn.plot.ly`, así que la página necesita conexión a internet.
- `freeze: true` reutiliza `_freeze/`; si cambias el código Python **o las celdas OJS (gráficas, parámetros)**, borra `_freeze/` y renderiza de nuevo en local.
- `data/prices.parquet` no se sube; el HTML publicado lleva los precios incrustados.
