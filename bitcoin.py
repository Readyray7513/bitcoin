import requests
import sys

def main():
    try:
        # Make a request to the CoinDesk API
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()  # Raise an exception for HTTP errors
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return

    # Parse the JSON response
    content = response.json()

    # Access the "bpi" key (Bitcoin Price Index)
    bpi = content.get("bpi")
    if not bpi:
        print("No Bitcoin price data found.")
        return

    # Print the rate for GBP
    gbp_data = bpi.get("USD")
    if gbp_data:
        rate = gbp_data.get("rate")
        

    # Call the `i` function with the GBP rate
    if gbp_data and "rate" in gbp_data:
        try:
            rate_float = float(gbp_data["rate"].replace(",", ""))  # Convert rate to float
            i(rate_float)
        except ValueError:
            print("Command-line argument is not a number")


def i(rate):
    try:
        x = float(sys.argv[1])
        y = x * rate  # Multiply input by the GBP rate
        print(f"${y:,.4f}")
    except ValueError:
        print("Command-line argument is not a number")
        sys.exit(1)



if __name__ == "__main__":
    main()

    

    


