from controller.dao_algortimo import DaoAlgoritmo
from flask import Flask, request, jsonify, render_template
import time
app = Flask(__name__)
dao_algoritmo = DaoAlgoritmo()
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ordenar', methods=['POST'])
def ordenar():
    data = request.json
    algoritmo = data.get('algoritmo')
    arr = data.get('arr')
    tiempo_inicio = time.time()
    if algoritmo == 'quick':
        sorted_arr = dao_algoritmo.ordenar_quick(arr)
    elif algoritmo == 'bubble':
        sorted_arr = dao_algoritmo.ordenar_bubble(arr)
    elif algoritmo == 'merge':
        sorted_arr = dao_algoritmo.ordenar_merge(arr)
    elif algoritmo == 'heapsort':
        sorted_arr = dao_algoritmo.ordenar_heapsort(arr)
    elif algoritmo == 'timsort':
        sorted_arr = dao_algoritmo.ordenar_timsort(arr)
    else:
        return jsonify({'error': 'Algoritmo no soportado'}), 400
    tiempo_fin = time.time()
    tiempo_ejecucion = tiempo_fin - tiempo_inicio

    return jsonify({
        'sorted_array': sorted_arr,
        'execution_time': tiempo_ejecucion
    })



if __name__ == '__main__':
    app.run(debug=True)