image bg blck = "images/blck.png"

define e = Character("Detektif")
define s = Character("Saksi")
define b = Character("Bos")
define w = Character("Kolega")

define char_pos = Position(xalign=0.14, yalign=0.7)

init python:
    # Node class to store data and the next node reference
    class Node:
        def _init_(self, data, next_node=None):
            self.data = data
            self.next_node = next_node

# LinkedList class to manage nodes
    class LinkedList:
        def _init_(self):
            self.head = None

        def add(self, data):
            if not self.head:
                self.head = Node(data)
            else:
                current = self.head
                while current.next_node:
                    current = current.next_node
                current.next_node = Node(data)

        def get(self, index):
            current = self.head
            count = 0
            while current:
                if count == index:
                    return current.data
                count += 1
                current = current.next_node
            return None

        def length(self):
            count = 0
            current = self.head
            while current:
                count += 1
                current = current.next_node
            return count
    story_bubbles = LinkedList()

$ story_bubbles.add("Node 1")
label start:
    scene bg office

    show detective at char_pos
    e "Hari ini aku menerima sebuah kasus pembunuhan yang rumit. Aku harus berhati-hati dalam mengambil keputusan."
    hide detective

    menu:
        "Interogasi saksi":
            jump interogasi_saksi1
        "Cari petunjuk di TKP":
            jump tkp1

$ story_bubbles.add("Node 2")
label interogasi_saksi1:
    scene bg interrogation

    show detective at char_pos
    e "Baiklah, aku akan mulai dengan menginterogasi saksi pertama."
    hide detective
    show witness1 at char_pos
    s "Saya melihat seseorang berlari dari tempat kejadian dengan membawa tas besar."
    hide witness1
    show detective at char_pos
    e "Bisakah Anda memberikan deskripsi lebih lanjut?"
    hide detective
    show witness1 at char_pos
    s "Dia tinggi, memakai jaket hitam dan topi merah."
    hide witness1

    menu:
        "Interogasi saksi kedua":
            jump interogasi_saksi2
        "Cari petunjuk di TKP":
            jump tkp1
        "Lapor ke bos":
            jump lapor_bos

$ story_bubbles.add("Node 3")
label interogasi_saksi2:
    scene bg interrogation

    show detective at char_pos
    e "Sekarang aku akan menginterogasi saksi kedua."
    hide detective
    show witness2 at char_pos
    s "Saya mendengar suara tembakan dari dalam rumah itu."
    hide witness2
    show detective at char_pos
    e "Apakah Anda melihat siapa yang keluar setelahnya?"
    hide detective
    show witness2 at char_pos
    s "Tidak, saya hanya mendengar suara itu."
    hide witness2

    menu:
        "Interogasi saksi ketiga":
            jump interogasi_saksi3
        "Cari petunjuk di TKP":
            jump tkp2
        "Lapor ke bos":
            jump lapor_bos

$ story_bubbles.add("Node 4")
label interogasi_saksi3:
    scene bg interrogation

    show detective at char_pos
    e "Sekarang aku akan menginterogasi saksi ketiga."
    hide detective
    show witness3 at char_pos
    s "Saya melihat seseorang membuang sesuatu ke tong sampah di dekat situ."
    hide witness3
    show detective at char_pos
    e "Apakah Anda tahu apa yang dibuangnya?"
    hide detective
    show witness3 at char_pos
    s "Tidak, saya tidak melihatnya dengan jelas."
    hide witness3

    menu:
        "Cari petunjuk di TKP":
            jump tkp3
        "Lapor ke bos":
            jump lapor_bos

$ story_bubbles.add("Node 5")
label tkp1:
    scene bg tkp1
    show detective at char_pos

    e "Ini adalah tempat kejadian perkara. Aku harus mencari petunjuk di sini."
    e "Ada bekas kaki di tanah dan sebuah topi merah."
    hide detective

    menu:
        "Periksa lebih lanjut di TKP":
            jump tkp_detail1
        "Interogasi saksi lagi":
            jump interogasi_saksi1
        "Lapor ke bos":
            jump lapor_bos

$ story_bubbles.add("Node 6")
label tkp2:
    scene bg tkp2
    show detective at char_pos

    e "Aku kembali ke TKP untuk mencari petunjuk lebih lanjut."
    e "Ada sebuah tas besar yang tertinggal di sini."
    hide detective

    menu:
        "Periksa isi tas":
            jump periksa_tas
        "Interogasi saksi lagi":
            jump interogasi_saksi2
        "Lapor ke bos":
            jump lapor_bos

$ story_bubbles.add("Node 7")
label tkp3:
    scene bg tkp3
    show detective at char_pos

    e "Aku kembali ke TKP untuk mencari petunjuk lebih lanjut."
    e "Ada bekas darah di tanah, dan ada tong sampah di dekat sini."
    hide detective

    menu:
        "Periksa tong sampah":
            jump periksa_tong
        "Interogasi saksi lagi":
            jump interogasi_saksi3
        "Lapor ke bos":
            jump lapor_bos

$ story_bubbles.add("Node 8")
label tkp_detail1:
    scene bg crime_scene
    show detective at char_pos

    e "Aku menemukan sebuah topi merah dan bekas kaki di tanah. Mungkin ini petunjuk penting."
    hide detective

    menu:
        "Periksa lebih lanjut di TKP":
            jump tkp_detail2
        "Interogasi saksi lagi":
            jump interogasi_saksi1
        "Lapor ke bos":
            jump lapor_bos

$ story_bubbles.add("Node 9")
label tkp_detail2:
    scene bg crime_scene
    show detective at char_pos

    e "Aku menemukan beberapa rambut di topi ini. Ini mungkin bisa dianalisis di lab."
    hide detective

    menu:
        "Kembali ke kantor":
            jump kantor
        "Lapor ke bos":
            jump lapor_bos

$ story_bubbles.add("Node 10")
label periksa_tas:
    scene bg crime_scene
    show detective at char_pos

    e "Aku membuka tas dan menemukan beberapa alat yang mungkin digunakan dalam kejahatan ini."
    hide detective

    menu:
        "Periksa lebih lanjut di TKP":
            jump tkp_detail3
        "Interogasi saksi lagi":
            jump interogasi_saksi2
        "Lapor ke bos":
            jump lapor_bos

$ story_bubbles.add("Node 11")
label periksa_tong:
    scene bg tong_sampah
    show detective at char_pos

    e "Aku menemukan senjata api di dalam tong sampah ini. Ini mungkin senjata yang digunakan."
    hide detective

    menu:
        "Periksa lebih lanjut di TKP":
            jump tkp_detail3
        "Interogasi saksi lagi":
            jump interogasi_saksi3
        "Lapor ke bos":
            jump lapor_bos
        "Kembali ke kantor":
            jump kejanggalan

$ story_bubbles.add("Node 12")
label tkp_detail3:
    scene bg crime_scene
    show detective at char_pos

    e "Aku menemukan beberapa jejak penting yang bisa membantu menyelesaikan kasus ini."
    hide detective

    menu:
        "Kembali ke kantor":
            jump kantor
        "Lapor ke bos":
            jump lapor_bos

$ story_bubbles.add("Node 13")
label lapor_bos:
    scene bg office
    show boss at char_pos

    b "Bagaimana perkembangan kasusnya?"
    hide boss
    show detective at char_pos
    e "Aku menemukan beberapa petunjuk penting. Aku yakin ini akan membantu menyelesaikan kasus ini."
    hide detective
    show boss at char_pos
    b "Bagus, teruskan pekerjaanmu. Kita harus segera menyelesaikan kasus ini."
    hide boss

    menu:
        "Kembali bekerja":
            jump kantor
        "Istirahat sejenak":
            jump istirahat

$ story_bubbles.add("Node 14")
label kantor:
    scene bg office
    show detective at char_pos

    e "Kembali ke kantor untuk menganalisis petunjuk lebih lanjut."
    hide detective

    menu:
        "Analisis rambut di lab":
            jump analisis_rambut
        "Telusuri jejak kaki":
            jump telusuri_jejak
        "Interogasi saksi lagi":
            jump interogasi_saksi1

$ story_bubbles.add("Node 26")
label kejanggalan:
    scene bg office
    show detective at char_pos

    e "Terlalu banyak kejanggalan dalam kasus ini"
    hide detective

    menu:
        "Sepertinya kasus ini tidak akan terpecahkan dalam waktu dekat":
            jump ending_tidak_jelas

$ story_bubbles.add("Node 15")
label analisis_rambut:
    scene bg lab
    show detective at char_pos

    e "Analisis rambut ini menunjukkan bahwa ini milik tersangka yang pernah terlibat kasus serupa sebelumnya."
    hide detective

    menu:
        "Cari tersangka":
            jump cari_tersangka
        "Lapor ke bos":
            jump lapor_bos

$ story_bubbles.add("Node 16")
label telusuri_jejak:
    scene bg street
    show detective at char_pos

    e "Jejak kaki ini mengarah ke sebuah rumah di dekat sini."
    hide detective

    menu:
        "Periksa rumah tersebut":
            jump periksa_rumah
        "Lapor ke bos":
            jump lapor_bos
        "Jejak tersangka menghilang":
            jump ending_kabur

$ story_bubbles.add("Node 17")
label cari_tersangka:
    scene bg street
    show detective at char_pos

    e "Aku menemukan tersangka berdasarkan petunjuk yang ada. Ini harus segera ditindaklanjuti."
    hide detective

    menu:
        "Tahan tersangka":
            jump tahan_tersangka
        "Lapor ke bos":
            jump lapor_bos

$ story_bubbles.add("Node 18")
label periksa_rumah:
    scene bg crime_scene
    show detective at char_pos

    e "Di dalam rumah ini, aku menemukan lebih banyak bukti yang mengarah ke tersangka utama."
    hide detective

    menu:
        "Tahan tersangka":
            jump tahan_tersangka
        "Lapor ke bos":
            jump lapor_bos

$ story_bubbles.add("Node 19")
label tahan_tersangka:
    scene bg jail
    show detective at char_pos

    e "Dengan semua bukti yang ada, aku berhasil menahan tersangka utama."
    hide detective

    menu:
        "Kasus selesai":
            jump ending_sukses
        "Ada masalah":
            jump ending_gagal
        "Kembali ke kantor":
            jump kesalahan

$ story_bubbles.add("Node 27")
label kesalahan:
    scene bg office
    show detective at char_pos

    e "Aku merasa ada yang aneh dari tersangka ini"

    menu:
        "Cari informasi lebih lanjut":
            jump ending_salah_tangkap

$ story_bubbles.add("Node 20")
label istirahat:
    scene bg lounge
    show detective at char_pos

    e "Aku butuh istirahat sejenak sebelum melanjutkan investigasi."
    hide detective

    menu:
        "Kembali bekerja":
            jump kantor
        "Lapor ke bos":
            jump lapor_bos

$ story_bubbles.add("Node 21")
label ending_sukses:
    scene bg office
    show detective at char_pos

    e "Kasus ini akhirnya berhasil dipecahkan. Tersangka sudah ditahan, dan keadilan telah ditegakkan."
    hide detective

    return

$ story_bubbles.add("Node 22")
label ending_gagal:
    scene bg office
    show detective at char_pos

    e "Kasus ini tidak bisa diselesaikan. Ada terlalu banyak bukti yang tidak cukup kuat."
    hide detective

    return

$ story_bubbles.add("Node 23")
label ending_tidak_jelas:
    scene bg office
    show detective at char_pos

    e "Kasus ini masih belum jelas. Banyak pertanyaan yang belum terjawab."
    hide detective

    return

$ story_bubbles.add("Node 24")
label ending_kabur:
    scene bg office
    show detective at char_pos

    e "Tersangka berhasil kabur. Aku harus mengejar dan menangkapnya."
    hide detective

    return

$ story_bubbles.add("Node 25")
label ending_salah_tangkap:
    scene bg office
    show detective at char_pos

    e "Ternyata aku salah tangkap. Orang yang kutahan bukan pelakunya."
    hide detective

    return
