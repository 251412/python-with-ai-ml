prices = [499, 1200, 750, 2500, 999, 1800]
def apply_gst(prices):
    return list(map(lambda p: round(p * 1.18, 2), prices))
def premium_products(prices):
    return [p for p in prices if p > 1000]
def total_bill(prices):
    return sum(prices)
prices_after_gst = apply_gst(prices)
premium = premium_products(prices_after_gst)
total = total_bill(prices_after_gst)
print("Prices after GST:", prices_after_gst)
print("Premium Products:", premium)
print("Total Bill Amount:", total)
