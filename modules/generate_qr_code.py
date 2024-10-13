import qrcode
from io import BytesIO
import base64


def generate_qr_code(url: str) -> str:
    """ Generates QR code based on requested url
    :param url: URL to make QR code
    :return: QR code
    """

    if not url:
        return ""

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    buffered = BytesIO()
    img.save(buffered)
    img_str = base64.b64encode(buffered.getvalue()).decode()

    return f"data:image/png;base64,{img_str}"
