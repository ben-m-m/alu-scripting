#!/usr/bin/env python3

import re
import xml.etree.ElementTree as ET

tree = ET.parse('./modified_sms_v2.xml')
root = tree.getroot()

received_pattern = re.compile(r'You have received (\d+) RWF')
payments_pattern = re.compile(r'TxId: \d+\. Your payment of (\d+) RWF')
transfered_pattern = re.compile(r'\*165\*S\*(\d+) RWF')
bank_deposit_pattern = re.compile(r'bank deposit of (\d+) RWF')


received_total = 0
payments_pattern_total = 0
transfered_pattern_total = 0
bank_deposit_pattern_total = 0


for each_sms in root.findall('sms'):
    body = each_sms.get('body')


    if body:
        payments_pattern_match = payments_pattern.search(body)
        received_pattern_match = received_pattern.search(body)
        transfered_pattern_match = transfered_pattern.search(body)
        bank_deposit_pattern_match = bank_deposit_pattern.search(body)
        if payments_pattern_match:
            amount = int(payments_pattern_match.group(1))
            payments_pattern_total += amount
        if received_pattern_match:
            amount = int(received_pattern_match.group(1))
            received_total += amount
        if transfered_pattern_match:
            amount = int(transfered_pattern_match.group(1))
            transfered_pattern_total += amount
        if bank_deposit_pattern_match:
            amount = int(bank_deposit_pattern_match.group(1))
            bank_deposit_pattern_total += amount
print(f"Total amount spent is: {payments_pattern_total + transfered_pattern_total} RWF")
print(f"Total amount deposited to acc. is: {received_total + bank_deposit_pattern_total} RWF")



print(5 + 5)

# for msg in root.findall('sms'):
#     body = msg.get('body')

#     if body:
#         match = pattern.search(body)

#         if match:
#             amount = int(match.group(1))
#             received_total += amount

# print(f"Total received: {total} RWF")
