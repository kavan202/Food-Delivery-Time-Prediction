# Food Delivery Time Prediction

Predict how many **minutes** a food delivery will take, given the order details —
who is delivering it, how far it has to travel, the weather, traffic, time of day,
and more. Framed as a **supervised regression** problem and solved end-to-end, from
raw messy data to a saved model ready for inference.

---

## Results

Four models were trained and compared. XGBoost (with tuned hyperparameters) came out on top.

| Model | Test R² | Train R² | Notes |
|---|---|---|---|
| Linear Regression | 0.57 | 0.58 | Baseline — relationships aren't linear |
| Decision Tree | 0.67 | 1.00 | Overfits (memorises the training set) |
| Random Forest | 0.82 | 0.97 | Big gain — averaging tames overfitting |
| **XGBoost (tuned)** | **0.83** | 0.85 | Best score *and* healthiest train/test gap |

*RMSE is in minutes, so the final model is off by roughly 4 minutes on average.*

---

## Approach

1. **Load & inspect** the raw data
2. **Clean** messy text and missing values (e.g. `"conditions Sunny"` → `Sunny`, `"(min) 24"` → `24`)
3. **EDA** — find which features actually move delivery time
4. **Feature engineering**
   - `distance_km` from restaurant/customer coordinates via the **Haversine formula**
   - `order_hour` extracted from the order timestamp
5. **Encode** categoricals (ordinal for traffic density, one-hot for the rest) and **scale** features
6. **Train & compare** Linear Regression, Decision Tree, Random Forest, XGBoost
7. **Tune** the best model (RandomizedSearchCV), **evaluate** (RMSE, R², Adjusted R²), and **save** it for inference

The maths and reasoning behind each step are explained inline in the notebook.

---

## Dataset

The dataset contains historical food-delivery orders with features such as the
delivery person's age and rating, restaurant and delivery coordinates, weather,
road-traffic density, vehicle type, order type, festival flag, and city type.
The target is `Time_taken(min)`.

---

## Tech stack

Python · pandas · NumPy · Matplotlib · seaborn · scikit-learn · XGBoost · joblib

---

## How to run

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Launch the app
Food_app.py

# 3. Also can open from Deployed app
link: "https://food-delivery-time-prediction-gusqvwvuqgs69tkxpie72u.streamlit.app/"
```

Then update the dataset path in the first load cell to point at your local CSV.

---

## Repository structure

```
food-delivery-time-prediction/
├── README.md
├── requirements.txt
├── Food_Delivery_Time_Prediction.ipynb   # the full, documented notebook
├── food_delivery.csv                      # dataset (or link it in the README)
├── pipe.pkl                              # saved pipeline model
```
