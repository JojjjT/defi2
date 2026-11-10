# DEFI 2 — Dashboard Quarto

Dashboard sobre precios históricos (yfinance) con cuatro páginas:

- **Precio histórico**: varios tickers, base 100, eje log, media móvil, selector de rango y control deslizante de fechas, volatilidad móvil y distribución de retornos.
- **Vasicek**, **Merton** y **Ornstein-Uhlenbeck**: cada una muestra el algoritmo de calibración (regresión AR(1) o detección de saltos), la tabla de parámetros calibrados vs. usados y una simulación Monte Carlo comparada con el precio real. La barra lateral permite cambiar ticker, ventana de calibración, horizonte, número de trayectorias, semilla y cada parámetro del modelo; todo se recalcula en el navegador.

Cada página incluye además la calibración de referencia de FinStoch (muestra completa).

## Uso local

```bash
git clone https://github.com/JojjjT/defi2-dashboard.git
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
- `freeze: true` reutiliza `_freeze/`; si cambias el código Python, borra `_freeze/` y renderiza de nuevo en local.
- `data/prices.parquet` no se sube; el HTML publicado lleva los precios incrustados.
