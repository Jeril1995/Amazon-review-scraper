import re
import requests

def main():
  try:
    count = 0
    headers = {'User-Agent': 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36 Mozilla/50.1.0'}
    asin = input("Enter the ASIN Number:")
    amazon_url = 'http://www.amazon.in/dp/'+ asin
    pnos = input('Number of review pages required:')
    pno = int(pnos)
    sourceCode = requests.get(amazon_url,headers = headers).text

    try:
      numb = re.findall(r'<span id="acrCustomerReviewText" class="a-size-base">(.*?) customer reviews</span>',sourceCode)
      num = int(numb[0].replace(',',''))
      rem=num%10
      if (rem!=0):
       r=int(num/10) +1
      else:
       r=num/10
      if r > pno: 
       r=pno
      links = re.findall(r'<a id="acrCustomerReviewLink" class="a-link-normal" href="(.*?)"',sourceCode)
      path = re.sub("/ref=.*","",links[0])
      # print path
      print("Downloading reviews.....")
      try:
        for i in range(1,r+1):
          pages = 'http://www.amazon.in'+path+'/ref=cm_cr_arp_d_paging_btm_%d?pageNumber=%d'%(i,i)
          linkSource = requests.get(pages,headers = headers).text
          if (count != 0): 
            file = open("new.txt","a")
          else: 
            file = open("new.txt","w")
            count+=1             
          loi= re.findall(r'<span data-hook="review-body" class="a-size-base review-text">(.*?)</span>',linkSource)
          for lo in loi:
            lo = re.sub('<.*?>','',lo)     
            file.write(lo)
            file.write('\n')
      except Exception as e:
        print(str(e))
    except Exception as e:
      print(str(e))
  except Exception as e:
    print(str(e))

main()



