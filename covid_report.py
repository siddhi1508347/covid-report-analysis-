
import pandas as pd
import matplotlib.pyplot as plt


data = {
    "state": ["Kerala", "Gujarat", "Delhi", "Karnataka", "West Bengal",
              "Tamil Nadu", "Andhra Pradesh", "Rajasthan", "Uttar Pradesh"],
    "total_cases": [599892, 584486, 478739, 392615, 389116,
                     329705, 324079, 249882, 236958],
    "total_deaths": [8005, 7919, 6229, 5159, 5195,
                      4250, 4197, 3208, 3045],
    "fatality_rate": [1.33, 1.35, 1.3, 1.31, 1.34,
                       1.29, 1.3, 1.28, 1.29],
    "cases_per_million": [17961.0, 9677.0, 28496.0, 6426.0, 4262.0,
                           4573.0, 6534.0, 3648.0, 1186.0],
    "vaccination_v": [66.54, 66.54, 66.54, 66.54, 66.54,
                       66.54, 66.54, 66.54, 66.54],
    "positivity_rate": [44.71, 44.45, 39.13, 35.06, 35.07,
                         30.49, 30.68, 24.49, 23.7],
}

df = pd.DataFrame(data)

print("=== FULL TABLE ===")
print(df.to_string(index=False))

print("\n=== TOP 5 STATES BY TOTAL CASES ===")
print(df.sort_values("total_cases", ascending=False).head(5)[["state", "total_cases"]].to_string(index=False))

print("\n=== TOP 5 STATES BY CASES PER MILLION (normalized) ===")
print(df.sort_values("cases_per_million", ascending=False).head(5)[["state", "cases_per_million"]].to_string(index=False))

print("\n=== TOP 5 STATES BY POSITIVITY RATE (possible under-testing) ===")
print(df.sort_values("positivity_rate", ascending=False).head(5)[["state", "positivity_rate"]].to_string(index=False))

print("\n=== OVERALL TOTALS ===")
total_cases_all = df["total_cases"].sum()
total_deaths_all = df["total_deaths"].sum()
overall_fatality = round(total_deaths_all / total_cases_all * 100, 2)
print(f"Total Cases (all states):  {total_cases_all:,}")
print(f"Total Deaths (all states): {total_deaths_all:,}")
print(f"Overall Fatality Rate:     {overall_fatality}%")

print("\n=== STATES ABOVE AVERAGE FATALITY RATE ===")
avg_fatality = df["fatality_rate"].mean()
above_avg = df[df["fatality_rate"] > avg_fatality].sort_values("fatality_rate", ascending=False)
print(f"Average fatality rate across states: {round(avg_fatality, 2)}%")
print(above_avg[["state", "fatality_rate"]].to_string(index=False))


plt.figure(figsize=(10, 6))
sorted_df = df.sort_values("total_cases", ascending=True)
plt.barh(sorted_df["state"], sorted_df["total_cases"], color="#c0392b")
plt.title("Total COVID-19 Cases by State")
plt.xlabel("Total Cases")
plt.tight_layout()
plt.savefig("chart_total_cases.png", dpi=150)
plt.close()


plt.figure(figsize=(10, 6))
sorted_cpm = df.sort_values("cases_per_million", ascending=True)
plt.barh(sorted_cpm["state"], sorted_cpm["cases_per_million"], color="#e67e22")
plt.title("COVID-19 Cases per Million Population by State")
plt.xlabel("Cases per Million")
plt.tight_layout()
plt.savefig("chart_cases_per_million.png", dpi=150)
plt.close()


plt.figure(figsize=(10, 6))
sorted_fr = df.sort_values("fatality_rate", ascending=True)
colors = ["#e74c3c" if v > avg_fatality else "#95a5a6" for v in sorted_fr["fatality_rate"]]
plt.barh(sorted_fr["state"], sorted_fr["fatality_rate"], color=colors)
plt.axvline(avg_fatality, color="black", linestyle="--", linewidth=1, label=f"Average ({round(avg_fatality,2)}%)")
plt.title("Fatality Rate (%) by State")
plt.xlabel("Fatality Rate (%)")
plt.legend()
plt.tight_layout()
plt.savefig("chart_fatality_rate.png", dpi=150)
plt.close()


plt.figure(figsize=(10, 6))
sorted_pos = df.sort_values("positivity_rate", ascending=True)
plt.barh(sorted_pos["state"], sorted_pos["positivity_rate"], color="#8e44ad")
plt.title("Test Positivity Rate (%) by State")
plt.xlabel("Positivity Rate (%)")
plt.tight_layout()
plt.savefig("chart_positivity_rate.png", dpi=150)
plt.close()


plt.figure(figsize=(10, 6))
plt.scatter(df["total_cases"], df["total_deaths"],
            s=df["cases_per_million"] / 30, alpha=0.6, color="#2980b9")
for _, row in df.iterrows():
    plt.annotate(row["state"], (row["total_cases"], row["total_deaths"]),
                 fontsize=8, xytext=(5, 5), textcoords="offset points")
plt.title("Total Cases vs Total Deaths (bubble size = cases per million)")
plt.xlabel("Total Cases")
plt.ylabel("Total Deaths")
plt.tight_layout()
plt.savefig("chart_cases_vs_deaths.png", dpi=150)
plt.close()

print("\nCharts saved:")
print("chart_total_cases.png, chart_cases_per_million.png,")
print("chart_fatality_rate.png, chart_positivity_rate.png, chart_cases_vs_deaths.png")