def process_data(data):
    # Simple data processing: convert all text to upper case
    processed_data = []
    for item in data:
        item['name'] = item['name'].upper()
        processed_data.append(item)
    return processed_data