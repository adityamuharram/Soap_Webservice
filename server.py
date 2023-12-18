from config import conn
from spyne import (Application, Array, ComplexModel, Integer, ServiceBase,
                   Unicode, rpc)
from spyne.protocol.http import HttpRpc
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication


# fungsi query database
def get_query(limit=100):
    cursor = conn.cursor()
    cursor.execute(f'select row_to_json(row) from (select mahasiswa.id, mahasiswa.nama, mahasiswa.nim, mahasiswa.fakultas, mahasiswa.prodi from mahasiswa) row limit {limit};')
    data = cursor.fetchall()
    return [x[0] for x in data]

# class Mahasiswa yang menunjukan struktur dari data mahasiswa
class Mahasiswa(ComplexModel):
    id = Integer
    nama = Unicode
    nim = Unicode
    fakultas = Unicode
    prodi = Unicode

# class MahasiswaService yang merupakan service dari API
class MahasiswaService(ServiceBase):
    @rpc(_returns=Array(Mahasiswa))
    # fungsi get yang akan dijalankan ketika ada request ke endpoint /mahasiswa
    def get(ctx):
        query = ctx.in_body_doc
        limit = 100
        if query != {}:
            limit = query["limit"][0]

        students = get_query(limit)
       
        return students

# inisialisasi aplikasi SOAP dengan endpoint /mahasiswa
application = Application([MahasiswaService], tns="mahasiswa",
        in_protocol=HttpRpc(), out_protocol=Soap11())

# membuat WSGI server dengan aplikasi SOAP
wsgi_application = WsgiApplication(application)

# jalankan server
if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    # jalankan WSGI server di port 6000
    server = make_server('0.0.0.0', 6000, wsgi_application)
    print("Listening on http://0.0.0.0:6000")
    # server akan berjalan terus menerus sampai dihentikan
    server.serve_forever()
