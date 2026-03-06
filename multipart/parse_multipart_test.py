# This is a test case for how multipart requests work
def test():
    request = Request(
        b'POST /form-path HTTP/1.1\r\n'
        b'Content-Length: 379\r\n'
        b'Content-Type: multipart/form-data; boundary=----WebKitFormBoundarycriD3u6M0UuPR1ia\r\n\r\n'
        b'------WebKitFormBoundarycriD3u6M0UuPR1ia\r\n'
        b'Content-Disposition: form-data; name="commenter"\r\n\r\n'
        b'Jesse\r\n'
        b'------WebKitFormBoundarycriD3u6M0UuPR1ia\r\n'
        b'Content-Disposition: form-data; name="upload"; filename=discord.png\r\n'
        b'Content-Type: image/png\r\n\r\n' 
        b'iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR4XmNgYGD4DwABBAEA43qFxAAAAABJRU5ErkJggg==\r\n'
        b'------WebKitFormBoundarycriD3u6M0UuPR1ia--'
    )

    multipart_request = parse_multipart(request)
    assert multipart_request.boundary == "WebKitFormBoundarycriD3u6M0UuPR1ia"
    assert len(multipart_request.parts) == 3

    Part_1 = multipart_request.parts[0]
    assert Part_1.headers.__contains__('Content-Disposition')
    assert Part_1.headers['Content-Disposition'] == 'form-data; name="commenter"'
    assert Part_1.name == 'commenter'
    assert Part_1.content == 'Jesse'

    Part_2 = multipart_request.parts[1]
    assert Part_2.headers.__contains__('Content-Disposition')
    assert Part_2.headers['Content-Disposition'] == 'form-data; name="upload"; filename=discord.png'
    assert Part_2.name == 'upload'
    assert Part_2.content == 'iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR4XmNgYGD4DwABBAEA43qFxAAAAABJRU5ErkJggg=='

    print('Test Passed!')