# Internet-Service-JmeterAuto

This program will generate Jmeter configuration and execute Jmeter automatically.

Input: 

1. platform: 'OpenLambda' or 'Clofly' or 'Iron'
2. inputURL.txt: containing serverless URL line-by-line
3. number\_URL: the number of processing line is min(#lines in inputURL.txt, number\_URL)

Output:

1. Generate temp\_configure folder: containing generated Jmeter configuration
2. Generate temp\_temp\_output\_data folder: containing Jmeter results

example
Jmeter Iron inputURL.txt 2

cat inputURL.txt
http://35.185.221.212/r/myapp/f5
http://35.185.221.212/r/myapp/f4
http://35.185.221.212/r/myapp/f3

Then, the result only uses the first of two lines in inputURL.txt
