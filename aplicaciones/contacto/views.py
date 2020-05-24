from django.conf import settings
from django.shortcuts import render

from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives

def enviar_email(mail):
    #definimos coontenido a traves de un template
    contexto = {'mail': mail}

    plantilla = get_template('contacto/correo.html')
    contenido = plantilla.render(contexto)

    #generamos elcorreo
    email = EmailMultiAlternatives(
        'Titulo correo de prueba',
        'Resumen de SICAPOL',
        settings.EMAIL_HOST_USER,
        [mail],
        cc=[settings.EMAIL_HOST_USER]
    )
    #atachamos el contenido y enviamos
    email.attach_alternative(contenido, 'text/html')
    email.send()


def index(request):
    if request.method == 'POST':
        mail = request.POST.get('mail')

        enviar_email(mail)

    return render(request, 'contacto/index.html', {})
