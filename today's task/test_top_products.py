import pytest
from top_products import get_top_5_products_from_data

test_data = []

# Generate 100 standard variations
for i in range(1, 101):
    transaction_data = [["Material No", "Qty"]]
    item_info_data = [["Material No", "Product Head"]]

    for j in range(20):
        material_no = f"M{j}"
        qty = (j * i) % 103
        product_head = f"Product{i}_{j}"
        transaction_data.append([material_no, qty])
        item_info_data.append([material_no, product_head])

    joined = [
        {"Product Head": f"Product{i}_{j}", "Material No": f"M{j}", "Qty": (j * i) % 103}
        for j in range(20)
    ]
    expected_top_5 = sorted(joined, key=lambda x: x["Qty"], reverse=True)[:5]
    test_data.append((transaction_data, item_info_data, expected_top_5))

# ------------------ Edge Cases ------------------

# Empty data
test_data.append((
    [["Material No", "Qty"]],
    [["Material No", "Product Head"]],
    []
))

# All zero quantities
test_data.append((
    [["Material No", "Qty"]] + [[f"M{i}", 0] for i in range(5)],
    [["Material No", "Product Head"]] + [[f"M{i}", f"Product_Zero_{i}"] for i in range(5)],
    [{"Product Head": f"Product_Zero_{i}", "Material No": f"M{i}", "Qty": 0} for i in range(5)]
))

# Duplicate material numbers
test_data.append((
    [["Material No", "Qty"], ["M1", 10], ["M1", 20]],
    [["Material No", "Product Head"], ["M1", "Product_Duplicate"]],
    [{"Product Head": "Product_Duplicate", "Material No": "M1", "Qty": 30}]
))

# Material present in transaction but missing in item_info
test_data.append((
    [["Material No", "Qty"], ["M404", 50]],
    [["Material No", "Product Head"], ["M1", "Product_A"]],
    []
))

# ------------------ Test Function ------------------

@pytest.mark.parametrize("transaction_data,item_info_data,expected", test_data)
def test_get_top_5_products_from_data(transaction_data, item_info_data, expected):
    actual = get_top_5_products_from_data(transaction_data, item_info_data)
    assert sorted(actual, key=lambda x: x["Qty"], reverse=True) == expected

# ✅ Benchmark test at the end
def test_benchmark_top_5(benchmark):
    transaction_data, item_info_data, _ = test_data[-1]  # Use last (complex) case
    benchmark(get_top_5_products_from_data, transaction_data, item_info_data)
