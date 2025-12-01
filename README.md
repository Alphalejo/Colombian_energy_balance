# Natural Gas Consumption and Production Analysis in Colombia

This project analyzes historical trends in Colombia’s natural gas consumption, production, imports, and exports, and forecasts future demand up to 2040 using Prophet. Through visual analytics and machine learning forecasting, the study provides insights into the country’s energy dynamics and long-term dependency patterns.

## Project Objectives

- Examine historical natural gas consumption and production in Colombia.
- Compare hydroelectric generation with natural-gas-based generation to identify consumption patterns.
- Analyze import and export behavior to understand energy dependency.
- Forecast consumption, generation, and imports through 2040 using time-series modeling.

## Key Features
### Data Analysis and Visualization

- Gas consumption trends over time.
- Domestic production vs. imported gas percentages.
- Hydroelectric generation vs. natural gas generation comparison.
- Imports and exports analysis.
- Forecast plots for consumption, generation, and imports up to 2040.

### Prediction Model

- Time-series forecasting using Meta’s Prophet.
- Trend modeling, yearly seasonality, and uncertainty intervals.
- Cross-validation to verify prediction accuracy.

### Code Structure

- Logging system that tracks data loading, preprocessing, model training, and forecasting.
- Error handling with try-except blocks for safe execution and clear debugging messages.
- Modular functions for cleaning, visualization, forecasting, and evaluation.

### Tech Stack

- Programming Language: Python
- Data Processing: Pandas, NumPy
- Visualization: Matplotlib, Seaborn
- Forecasting Model: Prophet
- Error Handling and Logging: Python logging module
- Data Sources: Open datasets from Colombian national energy agencies

### Results and Conclusions

- Colombia remains a significant natural gas producer, but import dependency has increased in recent years.
- Hydroelectric energy continues to dominate the power mix, with natural gas serving as a reliable complementary source.
- Forecasts suggest moderate growth in consumption and potential increases in imports if domestic production does not expand.
- These insights support strategic planning and diversification of the country’s energy matrix for long-term sustainability.
