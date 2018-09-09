from urllib import request

file_url="https://pkgstore.datahub.io/core/nyse-other-listings/nyse-listed_csv/data/3c88fab8ec158c3cd55145243fe5fcdf/nyse-listed_csv.csv"

def download_file_from_web(csv_url):
    response=request.urlopen(csv_url)
    csv_content=response.read()
    csv_str=str(csv_content)
    lines=csv_str.split("\\n")

    dest_path=r"C:\Users\N51254\Pictures\Camera Roll\hubble_data.csv"
    fx=open(dest_path,"w")
    for line in lines:
        fx.write(line+"\n")
    fx.close();

download_file_from_web(file_url)    