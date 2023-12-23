import speedtest

def internet_hiz_testi():
    st = speedtest.Speedtest()

    download_hizi = st.download() / 10**6  # Megabit cinsinden
    upload_hizi = st.upload() / 10**6  # Megabit cinsinden
    ping_zamani = st.results.ping

    print("İndirme Hızı: {:.2f} Mbps".format(download_hizi))
    print("Yükleme Hızı: {:.2f} Mbps".format(upload_hizi))
    print("Ping Zamanı: {} ms".format(ping_zamani))

if __name__ == "__main__":
    internet_hiz_testi()
