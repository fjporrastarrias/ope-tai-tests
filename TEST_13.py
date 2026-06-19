import json
import zipfile
import os

# Estructura de las 40 preguntas divididas en los 4 bloques oficiales
bloques = {
    "01": [
        {"id": 1, "pregunta": "¿Qué dispositivo mecánico del siglo XVII, creado por Blaise Pascal, es considerado uno de los primeros antecedentes de las calculadoras mecánicas?", "opciones": {"a": "El ábaco", "b": "La Pascalina", "c": "La máquina analítica", "d": "La máquina tabuladora"}, "correcta": "b"},
        {"id": 2, "pregunta": "¿Quién diseñó la Máquina Analítica en el siglo XIX, incorporando conceptos modernos como unidad de cálculo y memoria?", "opciones": {"a": "Gottfried Leibniz", "b": "Herman Hollerith", "c": "Charles Babbage", "d": "Alan Turing"}, "correcta": "c"},
        {"id": 3, "pregunta": "¿Qué innovación introdujo Joseph Marie Jacquard a principios del siglo XIX que influyó directamente en la informática?", "opciones": {"a": "El uso de relés electromecánicos", "b": "Las tarjetas perforadas para el control de patrones", "c": "El sistema numérico binario", "d": "La rueda de engranajes dentados"}, "correcta": "b"},
        {"id": 4, "pregunta": "¿A quién se considera la primera programadora de la historia por su trabajo con la Máquina Analítica?", "opciones": {"a": "Grace Hopper", "b": "Ada Lovelace", "c": "Joan Clarke", "d": "Margaret Hamilton"}, "correcta": "b"},
        {"id": 5, "pregunta": "¿Qué sistema desarrolló Herman Hollerith para el censo de EE. UU. de 1890, marcando un hito en el procesamiento de datos?", "opciones": {"a": "Una máquina tabuladora eléctrica basada en tarjetas perforadas", "b": "Un telar automatizado electrónico", "c": "Un calculador de tubos de vacío", "d": "Un multiplicador de engranajes"}, "correcta": "a"},
        {"id": 6, "pregunta": "¿Cuál es el component electrónico característico de los ordenadores de la Primera Generación?", "opciones": {"a": "El transistor", "b": "El circuito integrado", "c": "La válvula o tubo de vacío", "d": "El microprocesador"}, "correcta": "c"},
        {"id": 7, "pregunta": "¿Qué modelo teórico propuesto en 1945 define la estructura interna de la mayoría de los ordenadores modernos con CPU, memoria y E/S?", "opciones": {"a": "La arquitectura Harvard", "b": "La arquitectura Von Neumann", "c": "La máquina de Turing cuántica", "d": "El modelo OSI"}, "correcta": "b"},
        {"id": 8, "pregunta": "¿Cuál de los siguientes fue uno de los primeros ordenadores completamente electrónicos y de propósito general (1946)?", "opciones": {"a": "IBM PC", "b": "UNIVAC I", "c": "ENIAC", "d": "Apple II"}, "correcta": "c"},
        {"id": 9, "pregunta": "¿Cómo se realizaba principalmente la programación en los ordenadores de la Primera Generación?", "opciones": {"a": "Mediante lenguajes de alto nivel como COBOL", "b": "Mediante lenguaje de máquina y cableado físico", "c": "A través de sistemas operativos multitarea", "d": "Con entornos de desarrollo gráficos"}, "correcta": "b"},
        {"id": 10, "pregunta": "¿Qué hito teórico de 1936 sentó las bases de la informática determinando qué es computable y qué no?", "opciones": {"a": "La Pascalina", "b": "El artículo sobre los Números Computables de Alan Turing", "c": "La patente del transistor", "d": "La creación de ARPANET"}, "correcta": "b"}
    ],
    "02": [
        {"id": 11, "pregunta": "¿Qué componente tecnológico sustituyó a las válvulas de vacío y dio inicio a la Segunda Generación de ordenadores?", "opciones": {"a": "El circuito integrado", "b": "El microprocesador", "c": "El transistor", "d": "El relé"}, "correcta": "c"},
        {"id": 12, "pregunta": "¿Cuál de las siguientes es una ventaja clave del transistor frente a las válvulas de vacío?", "opciones": {"a": "Mayor consumo de energía", "b": "Mayor tamaño físico", "c": "Menor generación de calor y mayor fiabilidad", "d": "Uso exclusivo de lógica analógica"}, "correcta": "c"},
        {"id": 13, "pregunta": "¿Qué lenguajes de programación de alto nivel surgieron durante la Segunda Generación de ordenadores?", "opciones": {"a": "C y C++", "b": "FORTRAN y COBOL", "c": "Java y Python", "d": "Assembler puramente"}, "correcta": "b"},
        {"id": 14, "pregunta": "¿Qué tipo de memoria de almacenamiento interno se popularizó sustancialmente en la Segunda Generación?", "opciones": {"a": "Memorias de núcleos magnéticos", "b": "Memorias ópticas (CD-ROM)", "c": "Memorias Flash", "d": "Líneas de retardo de mercurio"}, "correcta": "a"},
        {"id": 15, "pregunta": "¿Qué elemento tecnológico define inequívocamente a la Tercera Generación de ordenadores (1964-1971)?", "opciones": {"a": "El microprocesador monochip", "b": "El circuito integrado (chip de silicio)", "c": "El disco duro magnético externo de tambor", "d": "La válvula de vacío miniaturizada"}, "correcta": "b"},
        {"id": 16, "pregunta": "¿Qué mítica familia de ordenadores de IBM, lanzada en 1964, marcó la era de la Tercera Generación por su compatibilidad de software?", "opciones": {"a": "IBM PC 5150", "b": "IBM System/360", "c": "IBM ENIAC II", "d": "IBM PDP-11"}, "correcta": "b"},
        {"id": 17, "pregunta": "¿Qué avance a nivel de software de sistema se consolidó durante la Tercera Generación de ordenadores?", "opciones": {"a": "La multiprogramación y los primeros sistemas operativos primitivos", "b": "Los entornos gráficos de usuario basados en ventanas (GUI)", "c": "Los navegadores web multimedia", "d": "La inteligencia artificial generativa"}, "correcta": "a"},
        {"id": 18, "pregunta": "¿Qué permitió la invención de los circuitos integrados respecto a la fabricación de ordenadores?", "opciones": {"a": "El aumento masivo del tamaño físico", "b": "La agrupación de miles de componentes electrónicos en una pequeña pastilla de silicio", "c": "La eliminación total del uso de electricidad", "d": "La obsolescencia inmediata de los lenguajes de programación"}, "correcta": "b"},
        {"id": 19, "pregunta": "¿Cuál fue el primer ordenador comercial que utilizó masivamente válvulas de vacío y se empleó para procesar el censo estadounidense de 1950?", "opciones": {"a": "UNIVAC I", "b": "EDVAC", "c": "MARK I", "d": "Intel 4004"}, "correcta": "a"},
        {"id": 20, "pregunta": "¿Qué laboratorio fue la cuna de la invención del transistor en diciembre de 1947?", "opciones": {"a": "Xerox PARC", "b": "Bell Laboratories", "c": "MIT", "d": "IBM Research"}, "correcta": "b"}
    ],
    "03": [
        {"id": 21, "pregunta": "¿Qué elemento integrador marca el inicio de la Cuarta Generación de ordenadores a partir de 1971?", "opciones": {"a": "Las tarjetas perforadas ópticas", "b": "El microprocesador", "c": "El transistor de germanio pura", "d": "La red ARPANET"}, "correcta": "b"},
        {"id": 22, "pregunta": "¿Cuál fue considerado el primer microprocesador en un solo chip comercializado de la historia, lanzado en 1971?", "opciones": {"a": "Intel 8086", "b": "Intel 4004", "c": "Motorola 68000", "d": "Zilog Z80"}, "correcta": "b"},
        {"id": 23, "pregunta": "¿Qué tecnología de integración de circuitos permitió meter decenas de miles de componentes en un solo chip en la 4ª Generación?", "opciones": {"a": "LSI y VLSI (Very Large Scale Integration)", "b": "ULSI exclusivamente", "c": "Sistemas de tubos de descarga", "d": "Relés termoiónicos"}, "correcta": "a"},
        {"id": 24, "pregunta": "¿En qué año se lanzó el IBM PC (modelo 5150), estandarizando la arquitectura del ordenador personal en oficinas y hogares?", "opciones": {"a": "1975", "b": "1981", "c": "1985", "d": "1990"}, "correcta": "b"},
        {"id": 25, "pregunta": "¿Qué sistema operativo venía integrado por defecto en el primer IBM PC fruto de una alianza comercial?", "opciones": {"a": "Unix", "b": "Linux", "c": "MS-DOS", "d": "Mac OS"}, "correcta": "c"},
        {"id": 26, "pregunta": "La Quinta Generación de ordenadores se asocia comúnmente con proyectos de qué tipo de desarrollo tecnológico?", "opciones": {"a": "Inteligencia Artificial and procesamiento en paralelo", "b": "Sustitución de silicio por válvulas", "c": "Creación exclusiva de lenguajes ensambladores", "d": "Eliminación completa de conexiones inalámbricas"}, "correcta": "a"},
        {"id": 27, "pregunta": "¿Qué ambicioso proyecto estatal de los años 80 intentó liderar el desarrollo de la Quinta Generación mediante arquitecturas de computación masiva en paralelo?", "opciones": {"a": "El proyecto ARPA de EE. UU.", "b": "El Proyecto de Quinta Generación de Japón (FGCS)", "c": "El Plan Alvey del Reino Unido", "d": "El programa Eureka de la UE"}, "correcta": "b"},
        {"id": 28, "pregunta": "¿Cuál de las siguientes características NO es propia de los ordenadores actuales englobados en las últimas evoluciones tecnológicas?", "opciones": {"a": "Procesadores multinúcleo", "b": "Conectividad ubicua (Wi-Fi, 5G)", "c": "Almacenamiento exclusivo en tarjetas perforadas", "d": "Integración de arquitecturas de propósito específico (GPUs/NPUs)"}, "correcta": "c"},
        {"id": 29, "pregunta": "¿Quién propuso el concept original de que los programas y los datos se almacenasen juntos en la memoria del ordenador?", "opciones": {"a": "John Von Neumann", "b": "Charles Babbage", "c": "Blaise Pascal", "d": "Steve Jobs"}, "correcta": "a"},
        {"id": 30, "pregunta": "¿Qué hito comercial de Apple en 1984 popularizó la interfaz gráfica de usuario (GUI) y el uso del ratón al gran público?", "opciones": {"a": "Apple I", "b": "Apple Macintosh", "c": "Apple IIe", "d": "iPad"}, "correcta": "b"}
    ],
    "04": [
        {"id": 31, "pregunta": "En la evolución de las memorias, ¿qué diferencia estructural supuso el paso de las líneas de retardo a los núcleos de ferrita?", "opciones": {"a": "El almacenamiento pasó a ser puramente secuencial e inestable", "b": "Permitió un acceso aleatorio (RAM) mucho más rápido y no volátil mecánicamente", "c": "Obligó a usar exclusivamente lógica decimal", "d": "Hizo que los ordenadores consumieran diez veces más energía"}, "correcta": "b"},
        {"id": 32, "pregunta": "¿Cuál de las siguientes opciones describe el orden cronológico correcto de la tecnología base (de 1ª a 4ª generación)?", "opciones": {"a": "Transistor -> Válvula -> Circuito Integrado -> Microprocesador", "b": "Válvula -> Transistor -> Circuito Integrado -> Microprocesador", "c": "Válvula -> Circuito Integrado -> Transistor -> Microprocesador", "d": "Microprocesador -> Circuito Integrado -> Transistor -> Válvula"}, "correcta": "b"},
        {"id": 33, "pregunta": "¿Qué ordenador de la primera generación fue diseñado originalmente para calcular tablas de tiro de artillería en la Segunda Guerra Mundial?", "opciones": {"a": "UNIVAC I", "b": "ENIAC", "c": "IBM 360", "d": "Altair 8800"}, "correcta": "b"},
        {"id": 34, "pregunta": "¿Qué se entiende por 'Ley de Moore', formulada en la era de los circuitos integrados?", "opciones": {"a": "Que el número de transistores en un circuito integrado se duplica aproximadamente cada dos años", "b": "Que la velocidad de internet se reduce a la mitad cada año", "c": "Que el software siempre se ralentiza el doble que el hardware", "d": "Que el coste de los ordenadores aumenta exponencialmente"}, "correcta": "a"},
        {"id": 35, "pregunta": "¿Qué máquina electromecánica construida por Konrad Zuse entre 1938 y 1941 en Alemania es considerada una de las primeras máquinas de computación programables automáticas?", "opciones": {"a": "Z3", "b": "Colossus", "c": "Harvard Mark I", "d": "Pascalina"}, "correcta": "a"},
        {"id": 36, "pregunta": "¿Cuál de los siguientes hitos NO pertenece a la evolución de los ordenadores personales de los años 70 y 80?", "opciones": {"a": "Altair 8800", "b": "Apple II", "c": "EDVAC", "d": "Commodore 64"}, "correcta": "c"},
        {"id": 37, "pregunta": "¿Qué nombre recibe el elemento de la arquitectura Von Neumann encargado de realizar las operaciones aritméticas y lógicas?", "opciones": {"a": "Unidad de Control (UC)", "b": "Unidad Aritmético Lógica (ALU)", "c": "Memoria Principal", "d": "Subsistema de Entrada/Salida"}, "correcta": "b"},
        {"id": 38, "pregunta": "¿Qué componente de la arquitectura de Von Neumann se encarga de secuenciar, decodificar y coordinar la ejecución de las instrucciones?", "opciones": {"a": "La ALU", "b": "La Unidad de Control (UC)", "c": "El bus de datos", "d": "El registro de estado"}, "correcta": "b"},
        {"id": 39, "pregunta": "¿Qué aportación de Gottfried Leibniz a finales del siglo XVII es fundamental para la lógica de los ordenadores modernos?", "opciones": {"a": "El desarrollo de la teoría de circuitos integrados", "b": "El perfeccionamiento del sistema binario", "c": "La invención de las tarjetas perforadas magnéticas", "d": "La creación de la primera válvula de vacío termoiónica"}, "correcta": "b"},
        {"id": 40, "pregunta": "En el contexto de la evolución tecnológica, ¿cuál fue el principal factor que propició la aparición de los Sistemas Operativos?", "opciones": {"a": "La necesidad de automatizar y optimizar el uso del costoso tiempo de CPU de la Tercera Generación mediante multiprogramación", "b": "La aparición de internet de banda ancha", "c": "La invención de la interfaz táctil", "d": "El desuso total de las arquitecturas basadas en Von Neumann"}, "correcta": "a"}
    ]
}

archivos_creados = []
zip_name = "TEST13_COMPLETO.zip"

# Generar los archivos JSON
for sub_bloque, preguntas in bloques.items():
    filename = f"TEST13-{sub_bloque}.json"
    data = {"tema": "13", "bloque": sub_bloque, "preguntas": preguntas}
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    archivos_creados.append(filename)
    print(f"Creado con éxito: {filename}")

# Comprimir en un archivo ZIP
with zipfile.ZipFile(zip_name, 'w') as zipf:
    for archivo in archivos_creados:
        zipf.write(archivo)
        os.remove(archivo) # Limpia los sueltos para dejar solo el zip limpio

print(f"\n¡Listo! Se ha creado el archivo comprimido '{zip_name}' con los 4 bloques en tu directorio actual.")