from django.shortcuts import redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.utils.html import strip_tags
from .forms import ContactoForm

def procesar_contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            email_cliente = form.cleaned_data['email']
            mensaje = form.cleaned_data['mensaje']

            # --- LÓGICA DE DISEÑO DEL CORREO (HTML) ---
            asunto = f'🍰 Nuevo Pedido Web: {nombre}'
            
            html_message = f"""
            <!DOCTYPE html>
            <html>
            <body style="margin: 0; padding: 0; background-color: #fdfbf7; font-family: 'Arial', sans-serif;">
                <div style="max-width: 600px; margin: 0 auto; background-color: #ffffff; border-radius: 8px; overflow: hidden; box-shadow: 0 4px 10px rgba(0,0,0,0.05); margin-top: 20px;">
                    <div style="background-color: #d48c96; padding: 20px; text-align: center;">
                        <h1 style="color: #ffffff; margin: 0; font-size: 24px;">Dulces Anylonso</h1>
                    </div>
                    <div style="padding: 30px; color: #5d4037;">
                        <h2 style="color: #d48c96;">¡Nuevo Mensaje!</h2>
                        <p><strong>De:</strong> {nombre} ({email_cliente})</p>
                        <p style="background: #fff5eb; padding: 15px; border-radius: 5px;">"{mensaje}"</p>
                        <div style="text-align: center; margin-top: 30px;">
                            <a href="mailto:{email_cliente}" style="background-color: #d48c96; color: white; padding: 10px 20px; text-decoration: none; border-radius: 20px;">Responder</a>
                        </div>
                    </div>
                </div>
            </body>
            </html>
            """
            
            plain_message = strip_tags(html_message)

            try:
                send_mail(
                    asunto,
                    plain_message,
                    settings.EMAIL_HOST_USER,
                    [settings.EMAIL_HOST_USER],
                    html_message=html_message,
                    fail_silently=False,
                )
                messages.success(request, '¡Mensaje enviado con éxito! Te responderemos pronto.')
            except Exception as e:
                messages.error(request, 'Error al enviar el correo. Intenta más tarde.')
                print(e)
        else:
            messages.error(request, 'Por favor revisa los datos del formulario.')

    # Sea exitoso o falle, siempre volvemos a la página de inicio
    return redirect('index')