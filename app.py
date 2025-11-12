import flask
import random 
import time 
import logging

app = flask.Flask(_name_)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def simular_latencia():
    #simula un retraso de red
    time.sleep(random.uniform(0.1, 0.4))

@app.route('/api/inventario/actualizar', methods=['POST'])
def actualizar_inventario():
    
    logging.info("Recibida solicitud para ACTUALIZAR inventario")
    simular_latencia()
# Decimos si hay stock o no al azar
    if random.choice([True, True, False]): # hay mas probabilidad de q si de q no
        # Éxito
        logging.info("Inventario actualizado EXITOSAMENTE (Status 200)")
        return flask.jsonify({"mensaje": "Inventario actualizado"}), 200
    else:
        # Fallo (Sin Stock)
        logging.warning("Fallo al actualizar inventario: SIN STOCK (Status 409)")
        return flask.jsonify({"mensaje": "Fallo: Sin stock disponible"}), 409

if _name_ == '__main__':
    # Corremos en el puerto 5003
    app.run(host= "0.0.0.0", port=5003,debug=True)