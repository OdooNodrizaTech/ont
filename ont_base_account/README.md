El módulo añade campos (ya existentes) a diferentes vistas de facturas, asientos, apuntes, etc

Añade el apartado de modo de pago a los pedidos de venta (sale.order)

Si no existe el campo vat para el partner_id relacionado mostrará el aviso: Es necesario definir un CIF/NIF para el cliente de la factura

Al confirmar la factura se realizan las siguientes validaciones:

- Si es una factura de compra y NO existe reference mostrará el aviso: Es necesario definir una referencia de proveedor para validar la factura de compra
