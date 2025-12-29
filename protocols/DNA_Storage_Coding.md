# 🧪 Protocol: DNA Data Storage Coding (Base64 to ACGT)

Bu protokol, dijital verinin DNA sarmallarına nasıl kodlanacağına dair temel bir algoritma çerçevesi sunar.

## 1. Veri Hazırlama (Preprocessing)
Dijital veri (ikili format), gürültüye karşı dirençli olması için önce bir hata düzeltme kodu (örneğin **Reed-Solomon**) ile işlenmelidir.

## 2. Eşleme (Mapping Strategy)
İkili veriyi DNA bazlarına (A, C, G, T) dönüştürmek için yaygın olarak kullanılan eşleme:
- `00` -> **A** (Adenin)
- `01` -> **C** (Sitozin)
- `10` -> **G** (Guanin)
- `11` -> **T** (Timin)

### Örnek:
Veri: `01100011`
DNA: `C G A T`

## 3. Sınırlamalar (Biophysical Constraints)
DNA sentezi sırasında "Homopolymer" (ardışık aynı bazlar) ve "GC Content" dengesi kritiktir.
- **Homopolymers:** Arda arda 3'ten fazla aynı baz (örn. `AAAA`) gelmemelidir (Seq-error riski).
- **GC Content:** Toplam baz sayısının %40-60 arası G ve C olması istenir (Stabilite için).

## 4. İndeksleme (Indexing)
DNA sarmalları kısa parçalar (100-200nt) halinde sentezlendiği için her parçanın başına ve sonuna **Primer Binding Site** ve **Address Index** eklenmelidir.

---

*Bu protokol TRL 5 seviyesindeki çalışmalar için temel teşkil eder.*
