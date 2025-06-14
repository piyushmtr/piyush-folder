import streamlit as st

st.set_page_config(page_title="Temperature Converter", layout="centered")

st.title("🌡️ Temperature Converter")

# Options for conversion
conversion_options = ["Celsius", "Fahrenheit", "Kelvin"]
from_unit = st.selectbox("Convert from", conversion_options)
to_unit = st.selectbox("Convert to", conversion_options)

# Input temperature value
temperature = st.number_input(f"Enter temperature in {from_unit}:", format="%.2f")

def convert_temperature(temp, from_u, to_u):
    # Convert input to Celsius first
    if from_u == "Fahrenheit":
        temp_c = (temp - 32) * 5/9
    elif from_u == "Kelvin":
        temp_c = temp - 273.15
    else:
        temp_c = temp

    # Convert Celsius to target unit
    if to_u == "Fahrenheit":
        return (temp_c * 9/5) + 32
    elif to_u == "Kelvin":
        return temp_c + 273.15
    else:
        return temp_c

# Output
if from_unit == to_unit:
    st.info("From and To units are same. Result will be the same.")
converted = convert_temperature(temperature, from_unit, to_unit)
st.success(f"{temperature:.2f}° {from_unit} = {converted:.2f}° {to_unit}")
