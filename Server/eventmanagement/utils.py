import qrcode
from PIL import Image
from .models import TicketQrCode
import io
from django.core.files.base import ContentFile

def createQrCode(index, type_ticket, event):
    datas = f"num : {index}, type_ticket : {type_ticket}"
    qr = qrcode.QRCode(version = 1, box_size = 10, border = 5)
    qr.add_data(datas)
    # Make the QR code
    qr.make(fit=True)

    # Create an image from the QR code
    img = qr.make_image(fill_color="black", back_color="white")
    # Convert the image to bytes
    buffer = io.BytesIO()
    img.save(buffer, format='PNG')
    image_bytes = buffer.getvalue()

    # Create TicketQrCode object and save it to the database
    ticket_qr_code = TicketQrCode.objects.create(num=index, type_ticket = type_ticket, event=event, addOwner=None)

    # Save the image to qr_image field
    ticket_qr_code.qr_image.save(f'qrcode_{event}_{index}.png', ContentFile(image_bytes))
    print(ticket_qr_code)
    # return image