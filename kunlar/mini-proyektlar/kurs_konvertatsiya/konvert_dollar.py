# Search for link values within URL input
import urllib.request, urllib.parse, urllib.error
import ssl
import gradio as gr


def dollar_kursi():
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    url = "https://daryo.uz/"
    html = urllib.request.urlopen(url, context=ctx)
    html_och = html.read()
    html_string = html_och.decode()

    index = html_string.find("<strong>USD</strong><span>") #
    return float(html_string[index + len("<strong>USD</strong><span>"):index + len("<strong>USD</strong><span>") + 8])


def konvert(dollar):
    _dollar_kursi = dollar_kursi()
    jami = dollar * _dollar_kursi

    return _dollar_kursi, jami

# ulug = 50
# _, som = konvert(50)
# print(som)

iface = gr.Interface(fn=konvert, inputs=["number"], outputs=["number", "number"])
iface.launch(share=True)