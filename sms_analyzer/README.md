SMS Transaction Analyzer

A simple Python script that parses exported XML SMS backup files and calculates total money spent and received from mobile money transaction messages in Rwandan Francs (RWF).

Features
Extracts transaction amounts from SMS messages
Calculates:
Total amount spent
Total amount received
Supports multiple transaction types:
Received money
Payments
Transfers
Bank deposits
Uses regular expressions for flexible message matching
Works directly with XML SMS backup files
Project Structure
.
├── sms_analyzer.py
├── modified_sms_v2.xml
└── README.md
Requirements
Python 3.x

No external libraries are required since the script only uses Python standard libraries.

Installation

Clone the repository:

git clone <your-repository-url>
cd <repository-folder>
Usage
Place your SMS XML backup file in the project directory.
Ensure the XML file is named:
modified_sms_v2.xml
Run the script:
python3 sms_analyzer.py
Example Output
Total amount spent is: 125000 RWF
Total amount deposited to acc. is: 210000 RWF
10
Supported SMS Patterns

The script currently detects the following transaction formats:

Received Money
You have received 5000 RWF
Payment Transactions
TxId: 123456. Your payment of 2000 RWF
Transfers
*165*S*3000 RWF
Bank Deposits
bank deposit of 10000 RWF
How It Works

The script:

Loads the XML SMS file using xml.etree.ElementTree
Iterates through every <sms> entry
Extracts the body attribute
Uses regex patterns to identify transaction amounts
Sums totals for:
Spending
Deposits/received funds
Prints the final totals
Future Improvements

Possible enhancements:

Support more mobile money formats
Export results to CSV or Excel
Add transaction categorization
Build a CLI interface
Add graphs and analytics
Detect dates and monthly summaries
Improve regex handling for commas and decimals
Example XML Format
<sms body="You have received 5000 RWF from John Doe" />
License

This project is open-source and available under the MIT License.
