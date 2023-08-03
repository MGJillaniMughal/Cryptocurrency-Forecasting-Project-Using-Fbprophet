
# Cryptocurrency Price Prediction System

This project implements a cryptocurrency price prediction system using the FB-Prophet library. The system allows users to analyze charts and make informed investment decisions by predicting the price of different cryptocurrencies. The aim of the project is to help generate profitable investment opportunities in the cryptocurrency market.

## Installation

The project is built with Python and uses the following libraries: 
- streamlit
- fbprophet
- plotly
- pandas
- investpy

Install the necessary libraries by running:

\```shell
pip install streamlit fbprophet plotly pandas investpy
\```

## Usage

To run the app, navigate to the project directory and run the following command:

\```shell
streamlit run main.py
\```

This will start the Streamlit app in your web browser where you can select the cryptocurrency of your choice and set the prediction period.

## Code

The code for the project is organized as follows:

- `main.py`: The main script for the prediction system. It uses Streamlit to create an interactive web application.

## Dataset

The system uses a CSV file, 'Updateddataset.csv', which contains a list of cryptocurrencies. The historical data of the selected cryptocurrency is then fetched using the `investpy` library.

## Forecast

The system predicts the future prices of the selected cryptocurrency using Facebook's Prophet library. The user can select the prediction period ranging from 1 to 5 years.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Contact

You can get in touch with me on my [GitHub](https://github.com/MGJillaniMughal) profile.
