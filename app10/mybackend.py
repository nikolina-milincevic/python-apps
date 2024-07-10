def get_dates_and_temperature(my_file):
    with open(my_file, "r") as file:
        content = file.read()

    rows = content.split("\n")[1:-1]

    dates = []
    temperatures = []

    for row in rows:
        date = row.split(",")[0]
        temperature = row.split(",")[1]
        temperature = int(temperature)
        dates.append(date)
        temperatures.append(temperature)
        
    return dates, temperatures

# I could've easily read this as csv using pandas.read_csv()
# df = pd.read_csv("app10/temperature.txt")
# dates = df["date"]
# temperatures = df["temperature"]
# and this all could've been written in frontend file