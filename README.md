## Bitcoin Price Converter 💰  

This Python program fetches the current **Bitcoin price** from the **CoinDesk API** and allows the user to convert a specified amount of Bitcoin into **USD**.  

### **How It Works**  
✅ Retrieves the latest **Bitcoin price in USD**  
✅ Multiplies the price by a user-provided amount of Bitcoin  
✅ Prints the total value in **USD** (formatted with commas and four decimal places)  

### **Requirements**  
📌 Python 3  
📌 `requests` library (install with `pip install requests`)  
📌 Internet connection (to fetch live Bitcoin prices)  

### **How to Use**  
Run the script from the command line, passing the number of **Bitcoin** you want to convert as an argument:  
```bash
python bitcoin_converter.py 2
```
(This would convert **2 BTC** to USD using the latest exchange rate.)  

### **Example Inputs & Outputs**  
| Command  | Output  |
|----------|--------|
| `python bitcoin_converter.py 1`  | `$43,256.1289`  |
| `python bitcoin_converter.py 2.5`  | `$108,140.3225`  |
| `python bitcoin_converter.py abc`  | `Command-line argument is not a number`  |

### **Error Handling**  
🚫 If the API request fails, the program will print an error message.  
🚫 If the argument isn't a valid number, an error message will be displayed.  

💸 Stay updated on Bitcoin prices and convert your BTC easily! 🚀
