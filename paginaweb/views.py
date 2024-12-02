from django.shortcuts import render
from django.conf import settings
from twilio.rest import Client
from django.shortcuts import redirect
from django.contrib import messages


def home(request):
    data={
        'info1':{'name':'num1','presentacion':'Al concentramos y elegir relajadamente una carta, lo hacemos a través de nuestro subconsciente.Según Carl Gustav Jung, la mente subconsciente está en contacto permanente con los arquetipos universales y el inconsciente colectivo, donde se acumula toda la sabiduría y experiencias universales, por tanto las respuestas.'},
        'info2':{'name':'num2','presentacion':'Va más allá de la mente consciente, que es la que utilizamos para leer estas líneas. El tarot trabaja a nivel subconsciente y según distintas corrientes filosóficas, esta parte inconsciente lo sabe todo y tiene acceso a respuestas.'},
        'info3':{'name':'num3','presentacion':'El Reiki Usui, también conocido como Reiki Oriental o Jikiden Reiki, es una técnica que utiliza un toque suave y preciso para equilibrar la energía vital en diversas zonas del cuerpo del paciente. Esta terapia induce a una profunda relajación, al tiempo que fomenta una sensación de calma, paz interior y bienestar, aliviando al paciente de cargas y mejorando sus constantes vitales.'},
        'info4':{'name':'num4','presentacion':'Las esencias florales se encuadran en lo que conocemos como medicinas energéticas o vibracionales. La terapia tiene varios niveles de complejidad, desde usos domésticos hasta otros netamente profesionales.'}}
    return render(request,"home.html",data)

def reiki(request):
    data={
        'info1':{'prof':'Profesional: ','name':'América Hurtado'},
        'info2':{'prof':'inf','name':'Maestra en Reiki Usui con más de 10 años de experiencia.'},
        'info3':{'titulo':'Valor por sesión: ','valor':'$35.000 CLP'},
        'info4':{'prof':'inf ','name':'Qué es Reiki Usui'},
        'info5':{'prof':'inf ','name':'El Reiki Usui, también conocido como Reiki Oriental o Jikiden Reiki, es una técnica que utiliza un toque suave y preciso para equilibrar la energía vital en diversas zonas del cuerpo del paciente...'},}
    return render(request,"reiki.html",data)

def floral(request):
    data={
        'info1':{'prof':'Profesional: ','name':'Pepa Puentes'},
        'info2':{'prof':'inf','name':'Terapeuta Floral'},
        'info3':{'titulo':'Valor por sesión: ','valor':'$25.000 Consulta más Frasco de gotitas'},
        'info4':{'prof':'inf ','name':'Qué es la Terapia Floral'},
        'info5':{'prof':'inf ','name':'La terapia floral del Dr. Bach es un sistema de medicina natural que basa su efecto en la acción terapéutica de 38 esencias florales...'},}
    return render(request,"floral.html",data)

def tienda(request):
    data={
        'prod1':{'name':'Lectura presencial u online de Tarot 30Min','valor':'Precio: $20,000'},
        'prod2':{'name':'Lectura de Tarot presencial u online 1 hr','valor':'Precio: $30,000'},
        'prod3':{'name':'Lectura de Tarot 1 pregunta por Whatsapp','valor':'Precio: $5,000'},
        'prod4':{'name':'Limpieza energética con sahumos','valor':'Precio: $30,000'},
        'prod5':{'name':'Sesión de Reiki Usui 1 hora','valor':'Precio: $35,000'},
        'prod6':{'name':'Escultura Virgen de Guadalupe','valor':'Precio: $45,000'},
        'prod7':{'name':'Macetero Buda con suculenta','valor':'Precio: $30,000'},
        'prod8':{'name':'Porta incienso Budita','valor':'Precio: $10,000'},
        'prod9':{'name':'Virgen vela Guadalupe','valor':'Precio: $5,500'},
        'prod10':{'name':'Terapia Floral','valor':'Precio: $25.000'},}
    return render(request,"tienda.html",data)

def nosotros(request):
    data={
        'tar1':{'name':'Libertad Hurtado','info':'Experiencia : 10 años','enfoque':'Enfoque: Tarot terapéutico y Predictivo','mod':'Modalidad online y presencial'},
        'tar2':{'name':'América Hurtado','info':'Experiencia : 10 años','enfoque':'Enfoque: Maestra en Reiki Usui','mod':'Modalidad online y presencial'},
        'tar3':{'name':'Pepa Puentes','info':'Flores de Bach','enfoque':'Terapeuta Floral','mod':'Modalidad online y presencial'},

    }
    return render(request,"nosotros.html",data)

def contacto(request):
    data={}
    return render(request,"contacto.html",data)

def resenas(request):
    data={}
    return render(request,"resenas.html",data)

def tarot(request):
    data={
        'info1':{'prof':'Profesional: ','name':'Libertad Hurtado'},
        'info2':{'prof':'inf','name':'Maestra en Tarot terapeutico y Predictivo con más de 20 años de experiencia.'},
        'info3':{'titulo':'Valor por sesión: ','valor':'$30.000'},
        'info4':{'prof':'inf ','name':'Qué es el Tarot terapeutico y Predictivo'},
        'info5':{'prof':'inf ','name':'El tarót terapéutico logra ver tu sombra y luz a través del mazo de cartas. El enfoque predictivo del futuro es más en cómo debes abrir tu mente y cambiar lo que debes cambiar...'},}
    return render(request,"tarot.html",data)

def login(request):
    data={}
    return render(request,"login.html",data)
def horas(request):
    data={}
    return render(request,"horas.html",data)


def send_sms(request):
    if request.method == 'POST':
        try:
            # Crea el cliente de Twilio
            client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

            # Enviar el mensaje
            client.messages.create(
                body='MENSAJE DE PRUEBA PAGINA TAROT',
                from_=settings.TWILIO_PHONE_NUMBER,  # Número de Twilio
                to='+56937321476'  # Número de destino
            )

            # Redirigir con un mensaje de éxito
            messages.success(request, 'Cita agendada. Recibirás toda la información a través de un SMS en tu celular.')
            return redirect('post_mensaje')  # Asegúrate de que 'send_sms_page' sea la URL correcta

        except Exception as e:
            # Manejo de errores
            messages.error(request, f'Ocurrió un error: {str(e)}')
            return redirect('home')

    return redirect('post_mensaje')  # Redirige si no es un POST

def post_mensaje(request):
    data={}
    return render(request,"post_mensaje.html",data)