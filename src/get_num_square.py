import os

# get the input and convert it to int
num = os.environ.get("INPUT_NUM")
if num:
    try:
        num = int(num)
    except Exception:
        exit('ERROR: the INPUT_NUM provided ("{}") is not an integer'.format(num))
else:
    num = 1

# to set output, print to shell in following syntax
print(f"::set-output name=num_squared::{num ** 2}")
