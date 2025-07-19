# Raspberry Pi ile Yüz Tanıma Tabanlı Kapı Kilidi Sistemi 🔐

Bu proje, Raspberry Pi kullanılarak YOLOv5 tabanlı bir yüz tanıma sistemi ile çalışan **akıllı kapı kilidi** sisteminin geliştirilmesini amaçlamaktadır. Sistem, gerçek zamanlı görüntü işleyerek **sadece tanınan kişilere** erişim izni verir. Model eğitimi **Roboflow** üzerinden işaretlenen özel veri seti ile gerçekleştirilmiş, daha sonra `YOLOv5` eğitimiyle `exp` klasörü altında model çıktısı alınmıştır. Python, OpenCV ve GPIO kontrolü ile sistem son haline getirilmiştir.

---

## 📷 Proje Görselleri

- Sistem özeti
- 
<img width="2000" height="1414" alt="mikroişlemciler poster" src="https://github.com/user-attachments/assets/1bf9da1c-703e-46b6-8254-b268e44c980a" />
  
- Eğitim sırasında kullanılan veri seti örnekleri

<img width="1558" height="804" alt="image" src="https://github.com/user-attachments/assets/762bfb79-4cb9-4d9f-a7df-687947067dec" />

- Sistem bağlantısı
![15](https://github.com/user-attachments/assets/1cce725b-2e1d-467e-961a-b927c219b1c7)

## 📁 Proje Dosya Yapısı

```bash
yuz-tanima-kapi-kilidi/
├── yolov5/                  # YOLOv5 klasörü (Ultralytics)
├── runs/train/exp/         # Eğitim sonrası model çıktısı
├── detect.py               # Algılama ve servo kontrolü
├── data.yaml               # Veri seti tanımlama dosyası
├── requirements.txt        # Gerekli Python kütüphaneleri
└── model_best.pt           # Eğitilen model (export edilmiş)
````

---

## 🚀 Kullanılan Teknolojiler

| Teknoloji    | Açıklama                          |
| ------------ | --------------------------------- |
| Raspberry Pi | Sistemin merkezi kontrol birimi   |
| Python       | Yazılım dili                      |
| OpenCV       | Görüntü işleme                    |
| YOLOv5       | Gerçek zamanlı nesne/yüz tanıma   |
| Roboflow     | Veri seti oluşturma ve işaretleme |
| GPIO         | Servo motor kontrolü              |
| Servo Motor  | Kilit mekanizması kontrolü        |
| VS Code      | Geliştirme ortamı                 |

---

## 📦 Kurulum ve Gereksinimler

### Raspberry Pi İçin:

```bash
sudo apt update
sudo apt install python3-pip
pip3 install -r requirements.txt
```

### requirements.txt içeriği:

```
torch>=1.7
opencv-python
ultralytics
numpy
RPI.GPIO
dlib
```

---

## 🧠 Roboflow ile Veri Hazırlama

1. Roboflow sitesine giriş yapılır.
2. Yeni bir proje oluşturulur (`Face Lock Project`).
3. Kendi yüzünüzün veya tanınmasını istediğiniz kişilerin fotoğrafları yüklenir.
4. Yüzler elle işaretlenir (bounding box).
5. Export kısmında `YOLOv5 PyTorch` formatı seçilir.
6. Veri seti `.zip` olarak indirilir ve `datasets` klasörüne açılır.
7. `data.yaml` dosyası güncellenir:

```yaml
train: ../datasets/images/train
val: ../datasets/images/val
nc: 1
names: ['face']
```

---

## 🏋️‍♂️ YOLOv5 ile Model Eğitimi

### Eğitim komutu:

```bash
python train.py --img 416 --batch 16 --epochs 50 --data data.yaml --weights yolov5s.pt --name face_lock
```

* Eğitim sonunda `runs/train/face_lock/weights/best.pt` modeli elde edilir.

---

## 🧪 Yüz Tanıma ve Servo Kontrol

Eğitilen model ile gerçek zamanlı yüz tanıma yapılır. Eğer yüz güven oranı ≥ 0.6 ise kapı açılır.

### `detect.py` içeriğinde şu işlemler yapılır:

* Kamera açılır
* YOLOv5 ile yüz aranır
* Eşleşme varsa:

  * GPIO üzerinden servo motor 90° döndürülür
  * 10 saniye sonra kilit tekrar kapanır

## 📊 Proje Özeti ve Avantajlar

* Anahtarsız erişim sağlar
* Engelliler ve yaşlılar için kolay kullanım sunar
* Kamera destekli anlık güvenlik kontrolü yapılır
* Python ile geliştirildiği için esnek ve özelleştirilebilir
* Düşük maliyetli Raspberry Pi ile çalışır

---

## 📄 Teknik Rapor

Proje detayları için teknik raporu inceleyebilirsiniz:

---

## 📈 Geliştirme Planları

* 📌 Uzaktan erişim kontrolü (IoT)
* 📌 Parmak izi veya ses tanıma ile çoklu güvenlik
* 📌 Alarm sistemi entegrasyonu
* 📌 Düşük ışıkta tanıma için infrared kamera desteği
