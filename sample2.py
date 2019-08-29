import amazonscraper
results = amazonscraper.search("", max_product_nb=2)

def get_title(url):
  ctr = 0
  for i in range(len(url)):
    if url[i] == "/":
      ctr +=1
    if ctr ==3:
      url_new = url[i+1:]
      break
  for j in range(len(url_new)):
    if url_new[j] == "/":
      url_new = url_new[:j]
      break
  url_new.replace("-"," ")
  return url_new
with open("test.html", "w") as f:
    f.write(results.last_html_page)
for result in results:
    print("{}".format(result.title))
    print("  - ASIN : {}".format(result.asin))
    print("  - {} out of 5 stars, {} customer reviews".format(result.rating, result.review_nb))
    print(" link - {}".format(result.url))
    print("  - Image : {}".format(result.img))
    print("  - prices : {}".format(result.prices_main))
    print("  - title : {}".format(result.title))  
    try:
        title1 = get_title(result.url)
        print(title1)
    except:
        print('a')
    

print("Number of results : %d" % (len(results)))































