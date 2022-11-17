from dataclasses import dataclass

COMMANDS = {
    '/start': 'start',
    '/donate': 'donar',
    '/help': 'help'
}

SONG = {
    1: 'te olvide',2: 'mentira',3: 'soy un desastre',4: 'mi algo',5: 'mente sucia',
    6: 'tu negro',7: 'como yo',8: 'Qqqq',9: 'vicio',10: 'hoy',
    11: 'eres una piedra',12: 'extratriste',13: 'chicago x',14: 'nsbdnosotros',15: 'te recordé',
    16: 'tu negro y mi algo',17: 'fumo weed',18: 'te recorde',19: '',20: '',
    21: '',22: '',23: '',24: '',25: '',
    26: '',27: '',28: '',29: '',30: '',
    31: '',32: '',33: '',34: '',35: '',
    36: '',37: '',38: '',39: '',40: '',
    41: '',42: '',43: '',44: '',45: '',
    46: '',47: '',48: '',49: '',50: '',
    51: '',52: '',53: '',54: '',55: '',
    56: '',57: '',58: '',59: '',60: '',
    61: '',62: '',63: '',64: '',65: '',
    66: '',67: '',68: '',69: '',70: '',
    71: '',72: '',73: '',74: '',75: '',
    76: '',77: '',78: '',79: '',80: '',
    81: '',82: '',83: '',84: '',85: '',
    86: '',87: '',88: '',89: '',90: '',
    91: '',92: '',93: '',94: '',95: '',
    96: '',97: '',98: '',99: '',100: '',
    
}
a = 'á'
e = 'é'
i = 'i'
o = 'ó'
u = 'ú'

@dataclass
class ES:
    WELCOME_BOT_USER = '''Hola! {}.
Gracias por unirte! Esta es una nueva experiencia y aun esta en desarrollo. Puedes darle mucho apoyo \
compartir el bot y que lo pueda ver el mismísimo Neeus, si tienes problemas con el bot: @fcoagz.'''
    DONATE_FOR_THE_BOT = 'Este bot se mantiene por un host para estar activo casi las 24h \
si quieres que se mantenga las 24/7 para dar apoyo al bot y poder añadir mas funciones que descargar musica \
de Neeus \n\
    PayPal: https://paypal.me/fcoagz'
    HELP = '¿Como se Utiliza? Neeus Bot reconoce que canción estas buscando de el, tan solo escribir \
por ejemplo, Te Recordé, automaticamente sera enviado la canción🎵.'
    HELP_PRIVATE = 'Para informar un problema, coloque su nombre de usuario (@examples) y luego el problema del bot \
ya que este mensaje sera automaticamente enviado al creador y te respondera en privado.'
