# Steps

1. I developed the expression after trying to read and copy some of the steps in the readings. to get the years (<movie><title>.*?</title>)(\d{4})</movie>
1. I tried to change out the (\d{4}) for ([A-z,a-z]+) to try and capture the country names
1. Finally, I changed that out with (\d+ min) to try and see all the numbers alongside min. for the runtime.