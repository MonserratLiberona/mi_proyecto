# Listas, Tuplas y Diccionarios

# 1. Carga de datos

ventas = [
    {"fecha": "2024-01-01", "producto": "Laptop", "cantidad": 2, "precio": 1200000},
    {"fecha": "2024-01-01", "producto": "Mouse", "cantidad": 5, "precio": 25000},
    {"fecha": "2024-01-02", "producto": "Laptop", "cantidad": 1, "precio": 1250000},
    {"fecha": "2024-01-02", "producto": "Teclado", "cantidad": 3, "precio": 45000},
    {"fecha": "2024-01-03", "producto": "Monitor", "cantidad": 4, "precio": 200000},
    {"fecha": "2024-01-03", "producto": "Mouse", "cantidad": 2, "precio": 27000}
]

print("Lista de ventas original:")
for venta in ventas:
    print("Fecha:", venta['fecha'], "Producto:", venta['producto'], "Cantidad:", venta['cantidad'], "Precio:", venta['precio'])

# 2. Cálculo de ingresos totales

ingresos_totales = 0
for venta in ventas:
    ingresos_totales += venta["cantidad"] * venta["precio"]
print("\nIngresos Totales:", ingresos_totales)

# 3. Producto más vendido

ventas_por_producto = {}
for venta in ventas:
    producto = venta["producto"]
    if producto in ventas_por_producto:
        ventas_por_producto[producto] += venta["cantidad"]
    else:
        ventas_por_producto[producto] = venta["cantidad"]

producto_mas_vendido = max(ventas_por_producto, key=ventas_por_producto.get)
print("\nProducto más vendido:", producto_mas_vendido)
print("Cantidad total vendida:", ventas_por_producto[producto_mas_vendido])

# 4. Promedio precio x producto

precios_por_producto = {}
for venta in ventas:
    producto = venta["producto"]
    total_precio = venta["precio"] * venta["cantidad"]
    if producto in precios_por_producto:
        precios_por_producto[producto][0] += total_precio
        precios_por_producto[producto][1] += venta["cantidad"]
    else:
        precios_por_producto[producto] = [total_precio, venta["cantidad"]]

print("\nPrecio promedio por producto:")
for producto, (suma_precios, total_cant) in precios_por_producto.items():
    promedio = suma_precios / total_cant
    print(producto, ":", int(promedio))

# 5. Ventas x dia

ingresos_por_dia = {}
for venta in ventas:
    fecha = venta["fecha"]
    if fecha in ingresos_por_dia:
        ingresos_por_dia[fecha] += venta["cantidad"] * venta["precio"]
    else:
        ingresos_por_dia[fecha] = venta["cantidad"] * venta["precio"]

print("\nIngresos por día:")
for fecha, ingreso in ingresos_por_dia.items():
    print(fecha, ":", ingreso)

# 6. Resumen ventas x producto

resumen_ventas = {}
for producto in ventas_por_producto:
    cantidad_total = ventas_por_producto[producto]
    ingresos_producto = precios_por_producto[producto][0]
    precio_promedio = ingresos_producto / cantidad_total
    resumen_ventas[producto] = {
        "cantidad_total": cantidad_total,
        "ingresos_totales": int(ingresos_producto),
        "precio_promedio": int(precio_promedio)
    }

print("\nResumen de ventas por producto:")
for producto, info in resumen_ventas.items():
    print(producto, ":", info)