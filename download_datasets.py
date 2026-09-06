from pathlib import Path
import urllib.request, zipfile
ROOT=Path(__file__).parent
FILES={"unemployment.csv": "https://raw.githubusercontent.com/amankharwal/Website-data/master/unemployment.csv", "car data.csv": "https://raw.githubusercontent.com/RimjimRazdan/cars_price_prediction/master/car%20data.csv", "Advertising.csv": "https://raw.githubusercontent.com/nguyen-toan/ISLR/master/dataset/Advertising.csv"}
for name,url in FILES.items():
    out=ROOT/({"unemployment.csv":"Task2_Unemployment_Analysis","car data.csv":"Task3_Car_Price_Prediction","Advertising.csv":"Task5_Sales_Prediction"}[name])/name
    if not out.exists():
        print("Downloading",name); urllib.request.urlretrieve(url,out)
    else: print("Exists",out)
# UCI SMS Spam Collection
out=ROOT/"Task4_Email_Spam_Detection"/"SMSSpamCollection"
if not out.exists():
    z=ROOT/"sms_spam_collection.zip"; urllib.request.urlretrieve("https://archive.ics.uci.edu/static/public/228/sms+spam+collection.zip",z)
    with zipfile.ZipFile(z) as f: out.write_bytes(f.read("SMSSpamCollection"))
    z.unlink()
    print("Downloaded SMSSpamCollection")
else: print("Exists",out)
