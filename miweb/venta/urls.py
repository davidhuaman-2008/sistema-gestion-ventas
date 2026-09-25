from django.urls import path
from venta.views import (
    user_login,
    home,
    user_logout,
    consulta_clientes,
    crear_cliente,
    actualizar_cliente,
    borrar_cliente,
    exportar_clientes_excel,
    exportar_clientes_pdf,
    consulta_productos,
    crear_producto,
    actualizar_producto,
    activar_desactivar_producto,
    borrar_producto,
    exportar_productos_excel,
    exportar_productos_pdf,
    consulta_ventas_simples,
    crear_venta_simple,
    buscar_venta_modificar,
    actualizar_venta_simple,
    buscar_venta_eliminar,
    eliminar_venta_simple,
    exportar_ventas_excel,
    exportar_ventas_pdf,
    get_product_price,
)

urlpatterns = [
    # Autenticación
    path('', user_login, name='login'),
    path('home/', home, name='home'),
    path('logout/', user_logout, name='logout'),

    # Clientes
    path('clientes/', consulta_clientes, name='lista_clientes'),
    path('clientes/crear/', crear_cliente, name='crear_cliente'),
    path('clientes/actualizar/', actualizar_cliente, name='actualizar_cliente'),
    path('clientes/borrar/', borrar_cliente, name='borrar_cliente'),
    path('clientes/exportar/excel/', exportar_clientes_excel, name='exportar_clientes_excel'),
    path('clientes/exportar/pdf/', exportar_clientes_pdf, name='exportar_clientes_pdf'),

    # Productos
    path('productos/', consulta_productos, name='lista_productos'),
    path('productos/crear/', crear_producto, name='crear_producto'),
    path('productos/actualizar/', actualizar_producto, name='actualizar_producto'),
    path('productos/activar-desactivar/', activar_desactivar_producto, name='activar_desactivar_producto'),
    path('productos/borrar/', borrar_producto, name='borrar_producto'),
    path('productos/exportar/excel/', exportar_productos_excel, name='exportar_productos_excel'),
    path('productos/exportar/pdf/', exportar_productos_pdf, name='exportar_productos_pdf'),

    # Ventas Simples
    path('ventas-simples/', consulta_ventas_simples, name='lista_ventas_simples'),
    path('ventas-simples/crear/', crear_venta_simple, name='crear_venta_simple'),
    path('ventas-simples/modificar/', buscar_venta_modificar, name='buscar_venta_modificar'),
    path('ventas-simples/editar/<int:pk>/', actualizar_venta_simple, name='actualizar_venta_simple'),
    path('ventas-simples/eliminar/', buscar_venta_eliminar, name='buscar_venta_eliminar'),
    path('ventas-simples/anular/<int:pk>/', eliminar_venta_simple, name='eliminar_venta_simple'),
    path('ventas-simples/exportar/excel/', exportar_ventas_excel, name='exportar_ventas_excel'),
    path('ventas-simples/exportar/pdf/', exportar_ventas_pdf, name='exportar_ventas_pdf'),

    # AJAX
    path('get_product_price/<int:producto_id>/', get_product_price, name='get_product_price'),
]