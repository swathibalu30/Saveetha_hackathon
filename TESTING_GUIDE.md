# Testing Guide for Improved Model

## Model Performance
- **Accuracy: 80%** (improved from 33%)
- **Training Samples: 72** (improved from 30)
- **Most Important Features:** 
  1. Glucose (32.84%)
  2. Blood Pressure (23.83%)
  3. Heart Rate (19.86%)

## How to Get Different Diagnoses

### 🫀 Heart Disease
**Characteristics:**
- **Age:** 50-60 years
- **BP:** 140-160 mmHg (High)
- **Glucose:** 115-130 mg/dL (Moderate)
- **Heart Rate:** 86-92 bpm (High)
- **Symptoms:** Chest pain, cardiac issues

**Example Test:**
- Age: 55, Gender: Male
- BP: 150, Glucose: 120, Heart Rate: 90
- Symptoms: "Chest Pain"

---

### 🩸 Diabetes
**Characteristics:**
- **Age:** 58-66 years
- **BP:** 135-145 mmHg (Moderate-High)
- **Glucose:** 175-200 mg/dL (VERY High)
- **Heart Rate:** 72-84 bpm (Normal-Low)
- **Symptoms:** High sugar, frequent urination, fatigue

**Example Test:**
- Age: 60, Gender: Male
- BP: 140, Glucose: 190, Heart Rate: 78
- Symptoms: "High blood sugar"

---

### 💉 Hypertension
**Characteristics:**
- **Age:** 40-48 years
- **BP:** 154-160 mmHg (VERY High)
- **Glucose:** 96-100 mg/dL (Normal)
- **Heart Rate:** 80-86 bpm (Moderate)
- **Symptoms:** High blood pressure, dizziness

**Example Test:**
- Age: 45, Gender: Female
- BP: 158, Glucose: 98, Heart Rate: 84
- Symptoms: "High blood pressure"

---

### 🧠 Migraine
**Characteristics:**
- **Age:** 32-39 years
- **BP:** 116-124 mmHg (Normal-Low)
- **Glucose:** 88-94 mg/dL (Normal-Low)
- **Heart Rate:** 70-76 bpm (Normal-Low)
- **Symptoms:** Headache, migraine pain

**Example Test:**
- Age: 35, Gender: Female
- BP: 120, Glucose: 90, Heart Rate: 72
- Symptoms: "Severe headache"

---

## Quick Test Cases

### Test 1: Should predict **Heart Disease**
```
Name: John Test
Age: 55
Gender: Male
BP: 148
Glucose: 122
Heart Rate: 88
Symptoms: Chest pain and discomfort
```

### Test 2: Should predict **Diabetes**
```
Name: Mary Test
Age: 62
Gender: Female
BP: 140
Glucose: 188
Heart Rate: 78
Symptoms: High blood sugar levels
```

### Test 3: Should predict **Hypertension**
```
Name: Sarah Test
Age: 46
Gender: Female
BP: 156
Glucose: 98
Heart Rate: 82
Symptoms: High blood pressure readings
```

### Test 4: Should predict **Migraine**
```
Name: Lisa Test
Age: 36
Gender: Female
BP: 120
Glucose: 92
Heart Rate: 74
Symptoms: Severe throbbing headache
```

---

## Key Insights

1. **Glucose is the strongest predictor** (32.84% importance)
   - High glucose (>175) → Usually Diabetes
   - Normal glucose (<100) → Usually Migraine or Hypertension

2. **Blood Pressure is second** (23.83% importance)
   - Very high BP (>154) → Usually Hypertension
   - High BP (140-150) + High Glucose → Usually Diabetes
   - High BP (145-150) + Moderate Glucose → Usually Heart Disease

3. **Heart Rate helps distinguish**
   - High heart rate (>86) + High BP → Heart Disease
   - Low heart rate (<76) + Normal BP → Migraine

---

## Tips for Testing

1. **Use extreme values** to get clearer predictions
2. **Combine multiple indicators** that match the pattern
3. **Age and gender** provide context but are less important
4. **Symptoms field** doesn't affect prediction (model uses only numeric features)

## Model Limitations

- Still a small dataset (72 samples)
- Real medical diagnosis requires much more data
- This is for educational purposes only
- Always consult healthcare professionals for real diagnosis
