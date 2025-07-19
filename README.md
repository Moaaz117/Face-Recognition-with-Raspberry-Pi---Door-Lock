# Face Recognition-Based Door Lock System with Raspberry Pi 🔐

Bu proje, Raspberry Pi kullanılarak YOLOv5 tabanlı bir yüz tanıma sistemi ile çalışan **akıllı kapı kilidi** sisteminin geliştirilmesini amaçlamaktadır. Sistem, gerçek zamanlı görüntü işleyerek **sadece tanınan kişilere** erişim izni verir. Model eğitimi **Roboflow** üzerinden işaretlenen özel veri seti ile gerçekleştirilmiş, daha sonra `YOLOv5` eğitimiyle `exp` klasörü altında model çıktısı alınmıştır. Python, OpenCV ve GPIO kontrolü ile sistem son haline getirilmiştir.

This project aims to develop a smart door lock system that works with a YOLOv5-based face recognition system using Raspberry Pi. The system processes images in real time and grants access only to recognized individuals. The model training was conducted using a specially labeled dataset via Roboflow, and the model output was obtained under the `exp` folder after YOLOv5 training. The system was finalized using Python, OpenCV, and GPIO control.
---

## 📷 Project Images | Proje Görselleri

- System summary | Sistem özeti
  
<img width="2000" height="1414" alt="mikroişlemciler poster" src="https://github.com/user-attachments/assets/1bf9da1c-703e-46b6-8254-b268e44c980a" />
  
- Examples of data sets used during training | Eğitim sırasında kullanılan veri seti örnekleri

<img width="1558" height="804" alt="image" src="https://github.com/user-attachments/assets/762bfb79-4cb9-4d9f-a7df-687947067dec" />

- System connection | Sistem bağlantısı
  
![15](https://github.com/user-attachments/assets/1cce725b-2e1d-467e-961a-b927c219b1c7)

## 📁 Project File Structure | Proje Dosya Yapısı

```bash
yuz-tanima-kapi-kilidi/               Açıklama                             Description 
├── yolov5/                 # YOLOv5 klasörü (Ultralytics)        # YOLOv5 folder (Ultralytics)
├── runs/train/exp/         # Eğitim sonrası model çıktısı        # Post-training model output
├── detect.py               # Algılama ve servo kontrolü          # Detection and servo control
├── data.yaml               # Veri seti tanımlama dosyası         # Data set definition file
├── requirements.txt        # Gerekli Python kütüphaneleri        # Required Python libraries
└── model_best.pt           # Eğitilen model (export edilmiş)     # Trained model (exported)
````

---

## 🚀 Technologies Used | Kullanılan Teknolojiler

| Teknoloji    | Açıklama                          | Description                        |
| ------------ | --------------------------------- | ---------------------------------- |
| Raspberry Pi | Sistemin merkezi kontrol birimi   | Central control unit of the system |
| Python       | Yazılım dili                      | Programming language               |
| OpenCV       | Görüntü işleme                    | Image processing                   |
| YOLOv5       | Gerçek zamanlı nesne/yüz tanıma   | Real-time object/face recognition  |
| Roboflow     | Veri seti oluşturma ve işaretleme | Data set creation and labeling     |
| GPIO         | Servo motor kontrolü              | Servo motor control                |
| Servo Motor  | Kilit mekanizması kontrolü        | Lock mechanism control             |
| VS Code      | Geliştirme ortamı                 | Development environment            |

---

## 📦 Installation and Requirements | Kurulum ve Gereksinimler

### For Raspberry Pi | Raspberry Pi İçin:

```bash
sudo apt update
sudo apt install python3-pip
pip3 install -r requirements.txt
```

### Contents of requirements.txt | requirements.txt içeriği:

```
torch>=1.7
opencv-python
ultralytics
numpy
RPI.GPIO
dlib
```

---

## 🧠 Preparing Datasets with Roboflow | Roboflow ile Veri Hazırlama

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


1. Log in to the Roboflow website.
2. Create a new project (`Face Lock Project`).
3. Upload photos of your own face or the faces of people you want to recognize.
4. Manually mark the faces (bounding box).
5. Select the `YOLOv5 PyTorch` format in the Export section.
6. The dataset is downloaded as a `.zip` file and extracted into the `datasets` folder.
7. The `data.yaml` file is updated:

```yaml
train: ../datasets/images/train
val: ../datasets/images/val
nc: 1
names: [‘face’]
```
---

## 🏋️‍♂️ Model Training with YOLOv5 | YOLOv5 ile Model Eğitimi

### Eğitim komutu:

```bash
python train.py --img 416 --batch 16 --epochs 50 --data data.yaml --weights yolov5s.pt --name face_lock
```

* Eğitim sonunda `runs/train/face_lock/weights/best.pt` modeli elde edilir.


### Training command:

```bash
python train.py --img 416 --batch 16 --epochs 50 --data data.yaml --weights yolov5s.pt --name face_lock
```

* At the end of training, the `runs/train/face_lock/weights/best.pt` model is obtained.

---

## 🧪 Face Recognition and Servo Control | Yüz Tanıma ve Servo Kontrol

Eğitilen model ile gerçek zamanlı yüz tanıma yapılır. Eğer yüz güven oranı ≥ 0.6 ise kapı açılır.

### `detect.py` içeriğinde şu işlemler yapılır:

* Kamera açılır
* YOLOv5 ile yüz aranır
* Eşleşme varsa:

  * GPIO üzerinden servo motor 90° döndürülür
  * 10 saniye sonra kilit tekrar kapanır


Real-time face recognition is performed using the trained model. If the face confidence score is ≥ 0.6, the door opens.

### The following operations are performed in `detect.py`:

* The camera is opened
* The face is searched for using YOLOv5
* If there is a match:

* The servo motor is rotated 90° via GPIO
* The lock closes again after 10 seconds
---

## 📊 Project Summary and Advantages | Proje Özeti ve Avantajlar

* Anahtarsız erişim sağlar
* Engelliler ve yaşlılar için kolay kullanım sunar
* Kamera destekli anlık güvenlik kontrolü yapılır
* Python ile geliştirildiği için esnek ve özelleştirilebilir
* Düşük maliyetli Raspberry Pi ile çalışır


* Provides keyless access
* Easy to use for people with disabilities and the elderly
* Instant security checks with camera support
* Flexible and customizable as it is developed with Python
* Works with low-cost Raspberry Pi
  
---

## 📄 Technical Report | Teknik Rapor

Proje detayları için teknik raporu inceleyebilirsiniz
You can review the technical report for project details
---

## 📈 Development Plans | Geliştirme Planları

* 📌 Uzaktan erişim kontrolü (IoT)
* 📌 Parmak izi veya ses tanıma ile çoklu güvenlik
* 📌 Alarm sistemi entegrasyonu
* 📌 Düşük ışıkta tanıma için infrared kamera desteği


* 📌 Remote access control (IoT)
* 📌 Multi-security with fingerprint or voice recognition
* 📌 Alarm system integration
* 📌 Infrared camera support for low-light recognition
