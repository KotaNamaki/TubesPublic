Kita kerjakan soal-soal pada gambar secara **step by step** dan **singkat namun jelas**, agar mudah ditulis ulang.

---

### **1. Diketahui:**

* $f(x) = \frac{1}{3}$ untuk $0 < x < 3$, distribusi uniform $U(0, 3)$
* Ukuran sampel $n = 27$

#### a. $\mu$ dan varian dari $\bar{X}$

* $\mu = \frac{a + b}{2} = \frac{0 + 3}{2} = 1.5$
* $\sigma^2 = \frac{(b - a)^2}{12} = \frac{(3 - 0)^2}{12} = 0.75$
* Varian $\bar{X} = \frac{\sigma^2}{n} = \frac{0.75}{27} = 0.02778$

#### b. Hitung $P(4/3 < \bar{X} < 5/3)$

* Ubah batas ke Z:

  * $Z_1 = \frac{4/3 - 1.5}{\sqrt{0.02778}} = \frac{-0.167}{0.1667} \approx -1.00$
  * $Z_2 = \frac{5/3 - 1.5}{\sqrt{0.02778}} = \frac{0.167}{0.1667} \approx 1.00$
* Cari dari tabel Z:

  * $P(-1 < Z < 1) = P(Z < 1) - P(Z < -1) = 0.8413 - 0.1587 = 0.6826$

---

### **2. Diketahui:**

* $f(x) = 2x$, $0 < x < 1$
* Ukuran sampel $n = 50$

#### a. $\mu$ dan varian dari $\bar{X}$

* Distribusi: $f(x) = 2x$, gunakan:

  * $\mu = \int_0^1 x \cdot 2x \, dx = 2 \int_0^1 x^2 \, dx = 2 \cdot \frac{1}{3} = \frac{2}{3}$
  * $E(X^2) = \int_0^1 x^2 \cdot 2x \, dx = 2 \int_0^1 x^3 \, dx = 2 \cdot \frac{1}{4} = \frac{1}{2}$
  * $\sigma^2 = E(X^2) - \mu^2 = \frac{1}{2} - \left(\frac{2}{3}\right)^2 = \frac{1}{2} - \frac{4}{9} = \frac{1}{18}$
  * Varian $\bar{X} = \frac{1}{18 \cdot 50} = \frac{1}{900}$

#### b. Hitung $P(0.70 < \bar{X} < 0.75)$

* Mean = $\frac{2}{3}$, SD = $\sqrt{\frac{1}{900}} = \frac{1}{30} \approx 0.0333$
* Z1: $\frac{0.70 - 2/3}{1/30} = \frac{0.0333}{0.0333} = 1$
* Z2: $\frac{0.75 - 2/3}{1/30} = \frac{0.0833}{0.0333} \approx 2.5$
* $P(1 < Z < 2.5) = 0.9938 - 0.8413 = 0.1525$

---

### **3. Diketahui:**

* $f(x) = 1$, $0 < x < 1$, distribusi uniform $U(0,1)$
* Ukuran sampel $n = 75$

#### a. $\mu$ dan varian dari $\bar{X}$

* $\mu = \frac{0 + 1}{2} = 0.5$
* $\sigma^2 = \frac{(1 - 0)^2}{12} = \frac{1}{12}$
* Varian $\bar{X} = \frac{1/12}{75} = \frac{1}{900}$

#### b. Hitung $P(0.45 < \bar{X} < 0.55)$

* Mean = 0.5, SD = $\sqrt{1/900} = 1/30 \approx 0.0333$
* Z1: $\frac{0.45 - 0.5}{1/30} = -1.5$
* Z2: $\frac{0.55 - 0.5}{1/30} = 1.5$
* $P(-1.5 < Z < 1.5) = 0.9332 - 0.0668 = 0.8664$

---

## **Soal 1 (Distribusi Eksponensial, rata-rata 0.25 tahun, n = 25)**

### a. Ekspektasi dan Varian $\bar{X}$

* $\mu = 0.25$
* $\sigma^2 = 0.25^2 = 0.0625$
* $\text{Var}(\bar{X}) = \frac{\sigma^2}{n} = \frac{0.0625}{25} = 0.0025$

### b. Peluang $\bar{X} > 0.2$

* SD $\bar{X} = \sqrt{0.0025} = 0.05$
* Z = $\frac{0.2 - 0.25}{0.05} = -1$
* $P(\bar{X} > 0.2) = P(Z > -1) = 0.8413$

### c. Peluang $0.15 < \bar{X} < 0.3$

* Z1 = $\frac{0.15 - 0.25}{0.05} = -2$
* Z2 = $\frac{0.3 - 0.25}{0.05} = 1$
* $P(-2 < Z < 1) = 0.8413 - 0.0228 = 0.8185$

---

## **Soal 2 (Distribusi Eksponensial, rata-rata 0.2 jam, n = 25)**

### a. Ekspektasi dan Varian $\bar{X}$

* $\mu = 0.2$
* $\sigma^2 = 0.2^2 = 0.04$
* $\text{Var}(\bar{X}) = \frac{0.04}{25} = 0.0016$

### b. Peluang $\bar{X} > 0.22$

* SD = $\sqrt{0.0016} = 0.04$
* Z = $\frac{0.22 - 0.2}{0.04} = 0.5$
* $P(Z > 0.5) = 1 - 0.6915 = 0.3085$

### c. Peluang $0.17 < \bar{X} < 0.26$

* Z1 = $\frac{0.17 - 0.2}{0.04} = -0.75$
* Z2 = $\frac{0.26 - 0.2}{0.04} = 1.5$
* $P(-0.75 < Z < 1.5) = 0.9332 - 0.2266 = 0.7066$

---

## **Soal 3 (Distribusi Uniform(0,3), n = 27)**

### a. Ekspektasi dan Varian $\bar{X}$

* $\mu = \frac{0+3}{2} = 1.5$
* $\sigma^2 = \frac{(3 - 0)^2}{12} = 0.75$
* $\text{Var}(\bar{X}) = \frac{0.75}{27} = 0.02778$

### b. Peluang $4/3 < \bar{X} < 5/3$

* Z1 = $\frac{4/3 - 1.5}{\sqrt{0.02778}} = -1$
* Z2 = $\frac{5/3 - 1.5}{\sqrt{0.02778}} = 1$
* $P(-1 < Z < 1) = 0.8413 - 0.1587 = 0.6826$

### c. Peluang $\bar{X} > 1.7$

* Z = $\frac{1.7 - 1.5}{\sqrt{0.02778}} \approx \frac{0.2}{0.1667} = 1.2$
* $P(Z > 1.2) = 1 - 0.8849 = 0.1151$

---

## **Soal 4 (Distribusi Uniform(1,4), n = 36)**

### a. Ekspektasi dan Varian $\bar{X}$

* $\mu = \frac{1 + 4}{2} = 2.5$
* $\sigma^2 = \frac{(4 - 1)^2}{12} = 0.75$
* $\text{Var}(\bar{X}) = \frac{0.75}{36} = 0.02083$

### b. Peluang $3/2 < \bar{X} < 7/2$

* Batas: 1.5 dan 3.5
* Z1 = $\frac{1.5 - 2.5}{\sqrt{0.02083}} = \frac{-1}{0.1443} \approx -6.93$
* Z2 = $\frac{3.5 - 2.5}{0.1443} \approx 6.93$
* Karena nilai Z sangat besar, peluang = hampir 1

### c. Peluang $\bar{X} > 3$

* Z = $\frac{3 - 2.5}{\sqrt{0.02083}} = \frac{0.5}{0.1443} \approx 3.47$
* $P(Z > 3.47) = 1 - 0.9997 = 0.0003$

---

Jika ingin versi tabel atau dalam format LaTeX, saya bisa bantu juga.
