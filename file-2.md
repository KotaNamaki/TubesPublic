Berdasarkan data dan instruksi yang diberikan, berikut adalah penyelesaian untuk menentukan jumlah produksi "Hot Pangsit" dengan menggunakan metode Fuzzy Tsukamoto dan Mamdani.

**Diketahui:**
* **Input Crisp:**
    * Permintaan : 1600 Pcs
    * Persediaan : 210 Pcs
* **Rule (Aturan Fuzzy):**
    * [R1]: JIKA Permintaan TURUN **DAN** Persediaan BANYAK **MAKA** Produksi BERKURANG.
    * [R2]: JIKA Permintaan TURUN **DAN** Persediaan SEDIKIT **MAKA** Produksi BERKURANG.
    * [R3]: JIKA Permintaan NAIK **DAN** Persediaan BANYAK **MAKA** Produksi BERTAMBAH.
    * [R4]: JIKA Permintaan NAIK **DAN** Persediaan SEDIKIT **MAKA** Produksi BERTAMBAH.

---

### **Langkah 1: Analisis Variabel dan Himpunan Fuzzy**

Berdasarkan tabel data yang diberikan, kita tentukan rentang nilai untuk setiap variabel:

* **Permintaan:**
    * Nilai Minimum = 400
    * Nilai Maksimum = 2100
* **Persediaan:**
    * Nilai Minimum = 50
    * Nilai Maksimum = 300
* **Produksi:**
    * Nilai Minimum = 400
    * Nilai Maksimum = 1950

Selanjutnya, kita definisikan fungsi keanggotaan linear untuk setiap himpunan fuzzy.

* **Fungsi Keanggotaan Permintaan**
    * $\mu_{Permintaan TURUN}(x) = \frac{2100 - x}{2100 - 400} = \frac{2100 - x}{1700}$
    * $\mu_{Permintaan NAIK}(x) = \frac{x - 400}{2100 - 400} = \frac{x - 400}{1700}$

* **Fungsi Keanggotaan Persediaan**
    * $\mu_{Persediaan SEDIKIT}(y) = \frac{300 - y}{300 - 50} = \frac{300 - y}{250}$
    * $\mu_{Persediaan BANYAK}(y) = \frac{y - 50}{300 - 50} = \frac{y - 50}{250}$

* **Fungsi Keanggotaan Produksi**
    * $\mu_{Produksi BERKURANG}(z) = \frac{1950 - z}{1950 - 400} = \frac{1950 - z}{1550}$
    * $\mu_{Produksi BERTAMBAH}(z) = \frac{z - 400}{1950 - 400} = \frac{z - 400}{1550}$

---

### **Langkah 2: Fuzzifikasi**

Kita hitung derajat keanggotaan untuk input crisp yang diberikan (Permintaan = 1600, Persediaan = 210).

* **Permintaan (x = 1600)**
    * $\mu_{TURUN}(1600) = \frac{2100 - 1600}{1700} = \frac{500}{1700} \approx 0.294$
    * $\mu_{NAIK}(1600) = \frac{1600 - 400}{1700} = \frac{1200}{1700} \approx 0.706$

* **Persediaan (y = 210)**
    * $\mu_{SEDIKIT}(210) = \frac{300 - 210}{250} = \frac{90}{250} = 0.36$
    * $\mu_{BANYAK}(210) = \frac{210 - 50}{250} = \frac{160}{250} = 0.64$

---

### **a. Metode Tsukamoto**

#### **Langkah 3: Aplikasi Aturan (Inferensi)**

Kita hitung nilai predikat (fire strength, $\alpha$) untuk setiap aturan menggunakan operator MIN, lalu cari nilai crisp output (z) untuk setiap aturan.

* **[R1] JIKA Permintaan TURUN DAN Persediaan BANYAK MAKA Produksi BERKURANG**
    * $\alpha_1 = \min(\mu_{TURUN}(1600), \mu_{BANYAK}(210)) = \min(0.294, 0.64) = 0.294$
    * Menggunakan konsekuen (Produksi BERKURANG): $\frac{1950 - z_1}{1550} = 0.294 \implies z_1 = 1950 - (0.294 \cdot 1550) = 1494.3$

* **[R2] JIKA Permintaan TURUN DAN Persediaan SEDIKIT MAKA Produksi BERKURANG**
    * $\alpha_2 = \min(\mu_{TURUN}(1600), \mu_{SEDIKIT}(210)) = \min(0.294, 0.36) = 0.294$
    * Menggunakan konsekuen (Produksi BERKURANG): $\frac{1950 - z_2}{1550} = 0.294 \implies z_2 = 1950 - (0.294 \cdot 1550) = 1494.3$

* **[R3] JIKA Permintaan NAIK DAN Persediaan BANYAK MAKA Produksi BERTAMBAH**
    * $\alpha_3 = \min(\mu_{NAIK}(1600), \mu_{BANYAK}(210)) = \min(0.706, 0.64) = 0.64$
    * Menggunakan konsekuen (Produksi BERTAMBAH): $\frac{z_3 - 400}{1550} = 0.64 \implies z_3 = (0.64 \cdot 1550) + 400 = 1392$

* **[R4] JIKA Permintaan NAIK DAN Persediaan SEDIKIT MAKA Produksi BERTAMBAH**
    * $\alpha_4 = \min(\mu_{NAIK}(1600), \mu_{SEDIKIT}(210)) = \min(0.706, 0.36) = 0.36$
    * Menggunakan konsekuen (Produksi BERTAMBAH): $\frac{z_4 - 400}{1550} = 0.36 \implies z_4 = (0.36 \cdot 1550) + 400 = 958$

#### **Langkah 4: Defuzzifikasi (Weighted Average)**

Kita hitung output akhir (Z) menggunakan rata-rata terbobot.
$$Z = \frac{\sum(\alpha_i \cdot z_i)}{\sum\alpha_i}$$
$$Z = \frac{(\alpha_1 \cdot z_1) + (\alpha_2 \cdot z_2) + (\alpha_3 \cdot z_3) + (\alpha_4 \cdot z_4)}{\alpha_1 + \alpha_2 + \alpha_3 + \alpha_4}$$
$$Z = \frac{(0.294 \cdot 1494.3) + (0.294 \cdot 1494.3) + (0.64 \cdot 1392) + (0.36 \cdot 958)}{0.294 + 0.294 + 0.64 + 0.36}$$
$$Z = \frac{439.32 + 439.32 + 890.88 + 344.88}{1.588} = \frac{2114.4}{1.588} \approx 1331.49$$

**Hasil (Tsukamoto):**
Jumlah produksi yang harus dihasilkan adalah **1331** Pcs (dibulatkan).

---

### **b. Metode Mamdani**

#### **Langkah 3: Implikasi dan Agregasi Aturan**

Nilai predikat ($\alpha$) sama dengan yang dihitung pada metode Tsukamoto.
* $\alpha_1 = 0.294$ (Konsekuen: Produksi BERKURANG)
* $\alpha_2 = 0.294$ (Konsekuen: Produksi BERKURANG)
* $\alpha_3 = 0.64$ (Konsekuen: Produksi BERTAMBAH)
* $\alpha_4 = 0.36$ (Konsekuen: Produksi BERTAMBAH)

Kita agregasi hasil dari semua aturan menggunakan operator MAX.
* Agregasi untuk Produksi BERKURANG: $\max(\alpha_1, \alpha_2) = \max(0.294, 0.294) = 0.294$
* Agregasi untuk Produksi BERTAMBAH: $\max(\alpha_3, \alpha_4) = \max(0.64, 0.36) = 0.64$

Daerah solusi fuzzy gabungan adalah $\mu_{agregat}(z) = \max(\min(0.294, \mu_{BERKURANG}), \min(0.64, \mu_{BERTAMBAH}))$.

#### **Langkah 4: Defuzzifikasi (Centroid of Area - COA)**

Kita akan menghitung titik pusat (centroid) dari daerah solusi fuzzy gabungan. Daerah ini dapat dibagi menjadi tiga bagian geometris untuk mempermudah perhitungan:
1.  **Daerah 1 (Persegi Panjang):**
    * Batas: z = 400 hingga z = 855.7 (titik di mana $\mu_{BERTAMBAH} = 0.294$)
    * Tinggi: 0.294
    * Luas $A_1 = (855.7 - 400) \cdot 0.294 = 133.98$
    * Titik Berat $C_1 = 400 + \frac{855.7 - 400}{2} = 627.85$
    * Momen $M_1 = A_1 \cdot C_1 = 84124.9$

2.  **Daerah 2 (Trapesium):**
    * Batas: z = 855.7 hingga z = 1392 (titik di mana $\mu_{BERTAMBAH} = 0.64$)
    * Tinggi kiri = 0.294, Tinggi kanan = 0.64
    * Luas $A_2 = \frac{0.294 + 0.64}{2} \cdot (1392 - 855.7) = 250.45$
    * Titik Berat $C_2 \approx 1157.0$ (Dihitung menggunakan rumus centroid trapesium)
    * Momen $M_2 = A_2 \cdot C_2 = 289770.6$

3.  **Daerah 3 (Persegi Panjang):**
    * Batas: z = 1392 hingga z = 1950
    * Tinggi: 0.64
    * Luas $A_3 = (1950 - 1392) \cdot 0.64 = 357.12$
    * Titik Berat $C_3 = 1392 + \frac{1950 - 1392}{2} = 1671$
    * Momen $M_3 = A_3 \cdot C_3 = 596690.5$

**Perhitungan Centroid Total:**
$$Z = \frac{M_1 + M_2 + M_3}{A_1 + A_2 + A_3}$$
$$Z = \frac{84124.9 + 289770.6 + 596690.5}{133.98 + 250.45 + 357.12}$$
$$Z = \frac{970586}{741.55} \approx 1308.87$$

**Hasil (Mamdani):**
Jumlah produksi yang harus dihasilkan adalah **1309** Pcs (dibulatkan).
