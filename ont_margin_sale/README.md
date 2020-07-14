Define un margin_percent en los sale.order y en un margin y margin_percent en las líneas (sale.order.line)

El margen se obtiene del coste de cada una de las líneas (según el coste de la ficha del producto o según el coste del valor de inventario de los sotck.picking que se hayan movido).

## Crones
### Regenerate Purchase Prices All 

Frecuencia: 1 vez al mes

Descripción: Realiza la misma acción que Regenerate Purchase Prices Send Orders  PERO de todos los ptos

### Regenerate Purchase Prices Send Orders 
Frecuencia: 1 vez al día

Descripción: Revisa todos los ptos en estado 'Pedido de venta' y 'Bloqueado' con importe > 0€ cuya fecha de confirmación sea el último mes y de ellos regenera el precio de compra
