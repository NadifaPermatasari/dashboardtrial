import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def simulate_until_empty(stock_awal, daily_usage, supply=0, supply_day=None):
    data = []
    stock = stock_awal
    day = 1

    while stock > 0:
        incoming = 0
        if supply_day is not None and day == supply_day:
            stock += supply

        stock -= daily_usage

        data.append({
            "Hari": day,
            "Stock": max(stock, 0)
        })

        day += 1

    return pd.DataFrame(data)

st.title("Dashboard Monitoring Stock")

stock_awal = st.number_input("Stock Awal", value=120)
daily_usage = st.number_input("Daily Usage", value=10)
supply = st.number_input("Supply", value=100)
supply_day = st.number_input("Supply Day", value=6)

scenario = simulate_until_empty(stock_awal, daily_usage, supply, supply_day)

st.metric("Sisa Hari", f"{len(scenario)} Hari")

fig, ax = plt.subplots(figsize=(10,5))
ax.plot(scenario["Hari"], scenario["Stock"], marker="o")
ax.set_xlabel("Hari")
ax.set_ylabel("Stock")
st.pyplot(fig)
