# Cálculo del promedio de un conjunto de números
# Pedir al usuario que ingrese la cantidad de números
import heapq as hq, folium, webbrowser, PySimpleGUI as sg, sys

# Definir la función que calcula la ruta más corta con el algoritmo de Dijkstra
def dijkstra(graph, source, destination):
    node_data={}
    for node in graph:
        node_data[node]=dict(cost=float('inf'),pred=[])
    node_data[source]['cost'] = 0
    visited = set()
    current_node = source
    for _ in range(5):
        if current_node not in visited:
            visited.add(current_node)
            min_heap = []
            for j in graph[current_node]:
                if j not in visited:
                    cost = node_data[current_node]['cost'] + graph[current_node][j]
                    if cost < node_data[j]['cost']:
                        node_data[j]['cost'] = cost
                        node_data[j]['pred'] = [*node_data[current_node]['pred'], current_node]
                    hq.heappush(min_heap,(node_data[j]['cost'],j))
        hq.heapify(min_heap)
        current_node = min_heap[0][1]
    return node_data[destination]['cost'],[*node_data[destination]['pred'], destination]

# Definir el grafo
grafica = {
'A':{	'B' :3.1},						
'B':{	'A' :3.1    ,'H' :1.8   ,'C' :6.3   ,'G' :3.7},
'C':{	'B' :8.4},		
'D':{	'E' :10.8   ,'AP':3.4},		
'E':{	'D' :10.8   ,'F' :1.5},		
'F':{	'E' :1.5	,'G' :5.1   ,'AK':4.4},		
'G':{	'B' :3.3	,'F' :5.1   ,'H' :3.4},		
'H':{	'G' :4.4	,'B' :1.8	,'I' :7.5},			
'I':{	'H' :7.5	,'J' :8.7},				
'J':{	'I' :8.7	,'K' :1.5},				
'K':{	'L' :2.5	,'J' :1.5},				
'L':{	'K' :4.8	,'M' :6.5},				
'M':{	'L' :4.8	,'BF':3.7},					
'N':{	'K' :3.7	,'Ñ' :0.3   ,'AO':0.32},			
'Ñ':{	'BF':0.3    ,'O' :2},				
'O':{	'P' :2.5	,'Ñ' :2},					
'P':{	'O' :2.5	,'Q' :1},				
'Q':{	'R' :2.5	,'P' :1},			
'R':{	'Q' :2.5	,'S' :1.9},	
'S':{	'R' :1.9	,'T' :0.53  ,'BA':2.2},			
'T':{	'S' :1.9	,'U' :2.5},					
'U':{	'W' :2.5	,'T' :2.5},
'W':{	'W' :2.3	,'U' :2.5   ,'BF':1.2   ,'BD':5},
'W':{	'X' :1.7	,'W' :2.3},					
'X':{	'Y' :1.4	,'W' :1.7},					
'Y':{	'Z' :1.4	,'X' :1.4},					
'Z':{	'AA':0.9    ,'Y' :1.4},					
'AA':{	'AB':1.3	,'Z' :0.9},					
'AB':{	'AC':1.5	,'AA':1.3},					
'AC':{	'AD':1.3	,'AB':1.5},				
'AD':{	'AE':1.6	,'BH':3.8   ,'AC':1.3},			
'AE':{	'AF':5.2	,'AD':1.8   ,'BH':4.9},		
'AF':{	'AG':1	    ,'AE':5},					
'AG':{	'AH':0.8	,'BL':0.75  ,'AF':1},		
'AH':{	'AI':3	    ,'AG':3},				
'AI':{	'AJ':2	    ,'AH':3},					
'AJ':{	'AI':2},							
'AK':{	'AL':3.4	,'F' :2.8},					
'AL':{	'AM':3.2	,'AK':3.4},					
'AM':{	'AN':2	    ,'AU':2.6   ,'AL':3.2},			
'AN':{	'AÑ':1.3	,'AM':2},				
'AÑ':{	'AO':1	    ,'AN':1.3},					
'AO':{	'N' :1.6	,'AÑ':1.6},					
'AP':{	'AQ':2	    ,'D' :4.1},					
'AQ':{	'AR':0.9	,'AP':2},				
'AR':{	'AS':1.7	,'AQ':0.9},					
'AS':{	'AT':2.7	,'AR':1.7},				
'AT':{	'AU':3.6	,'AS':2.7},				
'AU':{	'AV':2	    ,'AM':2.6   ,'AT':3.6},		
'AV':{	'AW':2	    ,'AU':2	},				
'AW':{	'AX':2.7	,'AV':2	},				
'AX':{	'AY':1.2	,'AX':2.7},					
'AY':{	'AZ':3.9	,'AX':1.2},					
'AZ':{	'BN':1.7	,'AY':3.9},					
'BN':{	'BA':2.3    ,'AZ':1.7},				
'BA':{	'S' :2.2    ,'BN':2.3},					
'BB':{	'BC':4},							
'BC':{	'BD':0.6    ,'BB':4},					
'BD':{	'W' :5      ,'BF':5.1   ,'BC':0.6},		
'BE':{	'BF':2.8    ,'W' :1.2   ,'BD':5.1},			
'BF':{	'BG':2.6    ,'BF':2.8},					
'BG':{	'BH':2.9    ,'BF':2.6},					
'BH':{	'AD':3.8    ,'AE':4.9   ,'BG':2.9},			
'BI':{	'BJ':2},							
'BJ':{	'AD':4.3    ,'BI':2},					
'AD':{	'BK':1.8    ,'BJ':4.3},				
'BK':{	'BL':3      ,'AD':1.8},					
'BL':{	'AG':0.75	,'AF':1.1   ,'BK':3}
}

# Definir las coordenadas de cada nodo
nodos = {
'A': (19.314858, -69.574497),
'B': (19.30552,-69.55870),
'C': (19.29651, -69.6009644),
'D': (19.23066, -69.61535),
'E': (19.270879, -69.55461),
'F': (19.26938, -69.56529),
'G': (19.28845, -69.56696),
'H': (19.30056, -69.55592),
'I': (19.32721, -69.51438),
'J': (19.30890, -69.44486),
'K': (19.25872, -69.57018),
'L': (19.29299, -69.43092),
'M': (19.2703, -69.44617),
'N': (19.25431, -69.46188),
'Ñ': (19.25218, -69.455608),
'O': (19.23976, -69.4334),
'P': (19.23524, -69.41762),
'Q': (19.2348, -69.3822),
'R': (19.22451, -69.39344),
'S': (19.21263, -69.35548),
'T': (19.20968, -69.35551),
'U': (19.2055, -69.3362),
'V': (19.20724, -69.31732),
'W': (19.19903, -69.30732),
'X': (19.19915, -69.3082),
'Y': (19.19557, -69.29426),
'Z': (19.18895, -69.27530),
'AA':(19.19145, -69.28194),
'AB':(19.18463, -69.25994),
'AC':(19.18353, -69.244495),
'AD':(19.26403, -69.23533),
'AE':(19.19811, -69.21615),
'AF':(19.23179, -69.21403),
'AG':(19.24421, -69.2067),
'AH':(19.24733, -69.21218),
'AI':(19.27645, -69.200289),
'AJ':(19.28238, -69.203911),
'AK':(19.26010, -69.530153),
'AL':(19.25247, -69.51896),
'AM':(19.24243, -69.50786),
'AN':(19.24459, -69.49447),
'AÑ':(19.25368, -69.481),
'AO':(19.25452, -69.46504),
'AP':(19.22678, -69.58302),
'AQ':(19.22645, -69.57635),
'AR':(19.22579, -69.55302),
'AS':(19.22444, -69.54539),
'AT':(19.22469, -69.53719),
'AU':(19.22114, -69.50545),
'AV':(19.21946, -69.49595),
'AW':(19.21393, -69.47151),
'AX':(19.20357, -69.44366),
'AY':(19.20259, -69.43162),
'AZ':(19.19779, -69.4041),
'BA':(19.21263, -69.35548),
'BB':(19.20946, -69.36141),
'BC':(19.271, -69.33574),
'BD':(19.25339, -69.33355),
'BE':(19.24427, -69.33107),
'BF':(19.2144, -69.31342),
'BG':(19.21131, -69.29846),
'BH':(19.20541, -69.27655),
'BI':(19.20557, -69.26099),
'BJ':(19.28339, -69.25641),
'BK':(19.27714, -69.25745),
'BL':(19.26386, -69.23568),
'BM':(19.26191, -69.21699),
'BN':(19.23887, -69.22161)
}

def layout():
    return [
    [sg.T('Introduzca el Origen: '),sg.In(size=2,key='Origen')],
    [sg.T('Introduzca el Destino: '),sg.In(size=2,key='Destino')],
    [sg.OK(),sg.Cancel()]
    ]

def main():
    sg.theme('DarkAmber')
    window=sg.Window(title='Algoritmo de Búsqueda',layout=layout(),font=('Courier 16'))
    event,data=window.read()
    if event=='OK':
        # Obtener el punto de inicio y el punto final del usuario
        nodo_inicio = data['Origen']
        nodo_final = data['Destino']

        # Obtener la ruta más corta
        distancia, ruta = dijkstra(grafica, nodo_inicio, nodo_final)
        sg.popup_scrolled(f"La ruta más corta es {' -> '.join(ruta)}\nLa distancia es de {distancia}km",
            font=('Courier 16'))

        # Crear un mapa inicial centrado en el primer nodo
        mapa = folium.Map(location=nodos[nodo_inicio], zoom_start=13)

        # Agregar los nodos del grafo al mapa
        for nodo, coordenadas in nodos.items():
            folium.Marker(location=coordenadas, tooltip=nodo).add_to(mapa)

        # Agregar la ruta más corta al mapa
        coordenadas_ruta = [nodos[nodo] for nodo in ruta]
        folium.PolyLine(locations=coordenadas_ruta, color='red').add_to(mapa)

        # Mostrar el mapa
        #mapa 

        mapa.save('rutacorta.html')
        webbrowser.open('rutacorta.html')

if __name__ == '__main__':
    main();