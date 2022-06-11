import web
import json
import random


carta = {}
urls = (
    '/(.*)',
    'Carta',
)
app = web.application(urls, globals())

class Carta():
  def __init__(self):
    pass
    
    
  def GET(self, carta_astral):
    try:
      fech_dia = int(carta_astral[0:2])
      fech_mes = int(carta_astral[3:5])
      print(fech_dia, fech_mes)
      
      
      if fech_dia >= 21 and fech_mes == 1 or fech_mes == 2 and fech_dia <= 19:
        horoscopo = {}
        horoscopo["Nombre"] = "Acuario"
        horoscopo["Fecha"] = "Enero  21 – Febrero 19"
        horoscopo["Elemento"] = "Aire"
        horoscopo["Numero de la suerte"] = "7, 14 y 20"
        horoscopo["Color"] = "Gris, azul y verde"
        horoscopo["Horóscopo del día"] =(random.choice([ "Estarás inexplicablemente tenso, pese a las mil y una bondades que te reserva la jornada. No olvides que todo pasa.","Estás pasando por un momento un poco inexplicable, Acuario, como si tu planeta regente se hubiera eclipsado. Parece que tienes falta de confianza en ti misma a diario y estás con la autoestima un poco por los suelos. Has dejado de valorar tu talento quizá a raíz de un contratiempo sin importancia. Hoy intenta recuperar la seguridad y convéncete de que tienes capacidad de sobra para llevar a cabo cualquier tema que se te encomiende.", "Te costará bastante que tus impulsos sean más moderados. Y por ello deberías mantener tus vacilaciones, hasta un momento en el que sientas mayor seguridad para llevar a adelante lo que tienes planificado para este día.","Hoy prodigarás y recibirás innumerables expresiones de afecto. La energía del día es propicia para las buenas comunicaciones, la armonía y el bienestar. Por ello, tú y los demás sentirán la necesidad de expresar lo que sienten mutuamente. Aprovecha para decirles a las personas especiales en tu vida lo que sientes por ellas. Es hora de que lo hagas y no necesitas una ocasión especial para demostrarles tu aprecio."]))
        result= json.dumps(horoscopo)
        return result

      elif fech_dia >= 20  and fech_mes == 2 or fech_mes == 3 and fech_dia <= 20:
        horoscopo = {}
        horoscopo["Nombre"] = "Picis"
        horoscopo["Fecha"] = "Febrero  20 – Marzo 20"
        horoscopo["Elemento"] = "Agua"
        horoscopo["Numero de la suerte"] = "75, 11 y 19"
        horoscopo["Color"] = "Verde, azul y morado."
        horoscopo["Horóscopo del día"] = (random.choice([ "Escucha una propuesta que rompe con tus prejuicios. Un elogio llega desde el lugar menos esperado. No lo descartes.","Hoy tu gran desafío estará relacionado con la manera en la que llevas a cabo tus prioridades", "Sentirás que necesitas poner tu vitalidad y profundidad, y especialmente tus percepciones, al servicio de tus obras y de tus actuaciones. Y por ello lo más importante es que utilices tu ecuanimidad y tu equilibrio para que tu entorno y tu forma de sentir sea equilibrado y más armónico.","Hoy tus capacidades psíquicas van a estar presentes con mucha fuerza. Siempre tuviste una parte intuitiva, y hoy esos sentidos extras estarán elevados. Podrás anticipar lo que alguien dirá o hará. ¡O podrás saber quién te llamará por teléfono antes de que suene! Quizás experimentes graciosas coincidencias, como por ejemplo estar pensando en alguien justo antes de encontrártelo"]))
        result= json.dumps(horoscopo)
        return result

      elif fech_dia >= 21  and fech_mes == 3 or fech_mes == 4 and fech_dia <= 19:
        horoscopo = {}
        horoscopo["Nombre"] = "Aries"
        horoscopo["Fecha"] = "Marzo  21 – Abril 19"
        horoscopo["Elemento"] = "Fuego"
        horoscopo["Numero de la suerte"] = " 7, 17 y 21."
        horoscopo["Color"] = "Gris, azul y verde"
        horoscopo["Horóscopo del día"] = (random.choice(["Contarás con una energía potenciada para encarar los cambios que tanto deseas. Te adaptarás a los tiempos que se avecinan.","Es un día para tener mayor tranquilidad y mantener la lengua a buen recaudo para evitar la ironía imperfecta. Evita sobrecargar tu sistema nervioso. Planifica tus actuaciones con bastante tiempo y separando unas actividades de otras; ya que así dedicarás el tiempo preciso a cada una.","Será un día en el que te sentirás con mucho entusiasmo, y esta gran vitalidad te llevará ejecutar un montón de proyectos que tenías pendientes. Como te moverás con una gran actividad deberás mantener la calma y la paciencia con personas más lentas que tú. Deberás dedicarte más tiempo a trabajar individualmente y a sacar tus ideas adelante."]))
        result= json.dumps(horoscopo)
        return result

      elif fech_dia >= 20  and fech_mes == 4 or fech_mes == 5 and fech_dia <= 20:
        horoscopo = {}
        horoscopo["Nombre"] = "Tauro"
        horoscopo["Fecha"] = "Abril  20 – Mayo 20"
        horoscopo["Elemento"] = "Tierra"
        horoscopo["Numero de la suerte"] = "4, 6 y 11."
        horoscopo["Color"] = "Verde claro, rosa y turquesa."
        horoscopo["Horóscopo del día"] = (random.choice(["Para encontrar la solución, separa cada cosa y analiza cada plano. Sentirás todo el apoyo familiar y de tu entorno más cercano.","Necesitas sentirte libre e ir a tu aire. Y tú estado positivo y alegre atraerá a otras personas que también se sientan de esa manera. Así que, lo más importante es que te sientas bien. Olvida las críticas o pensar qué es lo que has hecho mal. Lo importante es comenzar de cero, y así introducirás un revulsivo en tu vida.", "Recapacitarás en un área de tu vida que siempre es proclive a los cambios de humor y a la inestabilidad; y se refiere a las relaciones con los demás, y especialmente a las de pareja. Te gusta ir a tu aire y con un gran sentido de la libertad, pero a veces tienes que intentar flexibilizar posturas y ajustarte también a los demás."]))
        result= json.dumps(horoscopo)
        return result

      elif fech_dia >= 21  and fech_mes == 5 or fech_mes == 6 and fech_dia <= 21:
        horoscopo = {}
        horoscopo["Nombre"] = "Géminis"
        horoscopo["Fecha"] = "Mayo  21 – Junio 21"
        horoscopo["Elemento"] = "Aire"
        horoscopo["Numero de la suerte"] = "2, 4, 7 y 9"
        horoscopo["Color"] = "Azul, violeta y amarillo"
        horoscopo["Horóscopo del día"] = (random.choice(["Mientras tú quieres hacer un balance y cerrar una etapa surgirán otras alternativas y nuevos caminos para recorrer.","Hoy sentirás que necesitas mayor tranquilidad y que tus pensamientos fluyan más lentamente, e inclusive que paren. Ese es el estado perfecto. Podrás ocuparte con calma de cada pequeño asunto que trates. Y por eso es importante que utilices el razonamiento y a la vez la percepción sutil; ya que podrás combinar ambos","Estás en un día importante en el cual te plantearás nuevas metas qué tienen visos de salir adelante y de ser fructíferas. Pero para ello necesitas vigilar tus pensamientos para evitar una crítica en exceso, tanto en tus actuaciones como en las de los otros. Así que fluye como una hoja a través del río y déjate llevar por tu naturaleza bondadosa y altruista."]))
        result= json.dumps(horoscopo)
        return result

      elif fech_dia >= 20  and fech_mes == 6 or fech_mes == 7 and fech_dia <= 20:
        horoscopo = {}