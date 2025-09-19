# 🏥 Hospital Dashboard System (Partial Stack)

مشروع **Hospital Dashboard System** هو نظام متكامل لإدارة المستشفى يتضمن:
- 🩺 إدارة الأطباء
- 👨‍⚕️ إدارة المرضى
- 📅 نظام الحجوزات
- 💊 الصيدلية
- 👤 إدارة المستخدمين

تم بناء المشروع باستخدام **Django REST Framework** للـ Backend و **HTML/CSS/JS** للـ Frontend.

---

## 🚀 المميزات
- إضافة / تعديل / حذف الأطباء مع عرض معلوماتهم.
- إدارة بيانات المرضى بسهولة.
- إنشاء وحجز المواعيد وربطها بالأطباء والمرضى.
- نظام صيدلية يعرض الأدوية مع الأسعار والكمية المتاحة.
- صفحة عربة (Cart) لحجز الأطباء أو شراء الأدوية وعرض الفاتورة النهائية.
- ربط كامل بين الـ Backend والـ Frontend بحيث أي عملية تحدث تظهر مباشرة على الموقع.

---

## 🛠️ المتطلبات
- Python 3.10+
- Django 5+
- Django REST Framework
- PostgreSQL

---

## ⚙️ خطوات التشغيل

### 1. كلون المشروع:
```bash
git clone https://github.com/wanos25/Hospital-Dashboard-System-Partial_Stack-.git
cd Hospital-Dashboard-System-Partial_Stack-
```

### 2. إنشاء بيئة افتراضية وتثبيت المتطلبات:
```bash
python -m venv venv
venv\Scripts\activate   # على Windows
# أو
source venv/bin/activate   # على Linux/Mac

pip install -r requirements.txt
```

### 3. إعداد قاعدة البيانات:
- تأكد إن PostgreSQL شغال.
- غير إعدادات `DATABASES` في `backend/hospital/settings.py` حسب بياناتك.

### 4. عمل Migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. تشغيل السيرفر:
```bash
python manage.py runserver
```

### 6. الدخول للموقع:
- **الصفحة الرئيسية (Frontend):**  
  [http://127.0.0.1:8000/](http://127.0.0.1:8000/)  
- **API (مثال):**  
  [http://127.0.0.1:8000/api/doctors/](http://127.0.0.1:8000/api/doctors/)

---

## 📂 هيكل المشروع
```
Hospital-Dashboard-System-Partial_Stack-/
│
├── backend/
│   ├── hospital/          # إعدادات المشروع
│   ├── doctors/           # إدارة الأطباء
│   ├── patients/          # إدارة المرضى
│   ├── appointments/      # إدارة الحجوزات
│   ├── pharmacy/          # إدارة الصيدلية
│   ├── users/             # إدارة المستخدمين
│   └── templates/         # ملفات HTML
│
├── static/                # ملفات CSS/JS
├── README.md              # هذا الملف
└── requirements.txt       # باكدجات المشروع
```

---

## 📸 صور (Screenshots)
> يمكن إضافة صور من الموقع لتوضيح النظام لاحقًا.

---

## 👨‍💻 المطور
- **Wanos Moha**  
  GitHub: [wanos25](https://github.com/wanos25)

---

## 📥 تحميل المشروع
[🔗 رابط التحميل المباشر (GitHub ZIP)](https://github.com/wanos25/Hospital-Dashboard-System-Partial_Stack-/archive/refs/heads/main.zip)

# Hospital-Dashboard-System-Partial_Stack-