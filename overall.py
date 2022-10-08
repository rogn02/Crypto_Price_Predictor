from libraries import *

urlBNB="https://crypto.com/price/bnb" 
urlBTC="https://crypto.com/price/bitcoin"
urlETH="https://crypto.com/price/ethereum"
urlUSDT="https://crypto.com/price/tether"
urlBTC2="https://coinmarketcap.com/currencies/bitcoin/markets/"
urlBNB2="https://coinmarketcap.com/currencies/bnb/markets/"
urlETH2="https://coinmarketcap.com/currencies/ethereum/markets/"
urlUSDT2="https://coinmarketcap.com/currencies/tether/markets/"
def Scraper(url,url2,num,coin_name):
    for _ in range(num):
        try:
            res,res2,List=get(url),get(url2),[coin_name]
        except:
            print("Connection Error!")
        soup=BeautifulSoup(res.content,'html.parser')
        soup2 = BeautifulSoup(res2.content, 'html.parser')
        #Current Price
        container_11=soup.find_all('div',{"class":"chakra-stack css-a9porv"})
        container_12=container_11[0].find("h2").find("span")
        List.append(str(container_12))
        #Market Cap(USD_Billion)
        container_21=soup.find_all('div',{"class":"css-95687q"})
        container_22=container_21[0].find_all("p")
        List.append(str(container_22))
        #24H Volume(USD_Billion)
        container_23=container_21[1].find_all("p")
        List.append(str(container_23))
        #Circulating supply(USD_Billion)
        container_41=soup.find_all('div',{"class":"css-8l88pi"})
        container_42=container_41[0].find_all("p")
        List.append(str(container_42))
        # 24hr high/low
        raw = soup2.find_all("span", {"class": "n78udj-5 dBJPYV"})
        ans = str(raw[0].find("span"))
        fin_ans_high = ans[7:len(ans)-len(ans[::-1][:7])]
        List.append(fin_ans_high)

        ans2 = str(raw[1].find("span"))
        fin_ans_low = ans2[7:len(ans2)-len(ans2[::-1][:7])]
        List.append(fin_ans_low)
        Writer(List)
        time.sleep(2)