from collections import defaultdict

def get_top_5_products_from_data(transaction_data, item_info_data):
    transaction_headers = transaction_data[0]
    item_info_headers = item_info_data[0]

    transaction_idx = {header: idx for idx, header in enumerate(transaction_headers)}
    item_info_idx = {header: idx for idx, header in enumerate(item_info_headers)}

    material_to_product = {
        row[item_info_idx["Material No"]]: row[item_info_idx["Product Head"]]
        for row in item_info_data[1:]
    }

    product_quantities = defaultdict(int)
    for row in transaction_data[1:]:
        material_no = row[transaction_idx["Material No"]]
        qty = row[transaction_idx["Qty"]]

        product_head = material_to_product.get(material_no)

        # ✅ Skip if product head is not found (material not in item_info)
        if product_head is None:
            continue

        if isinstance(qty, (int, float)):
            product_quantities[(product_head, material_no)] += qty

    top_5 = sorted(product_quantities.items(), key=lambda x: x[1], reverse=True)[:5]

    return [
        {"Product Head": k[0], "Material No": k[1], "Qty": v}
        for k, v in top_5
    ]
