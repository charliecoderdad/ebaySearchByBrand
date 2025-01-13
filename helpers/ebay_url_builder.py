import urllib


def getBaseUrl(searchTerm, brand, category, condition):
  url = "https://www.ebay.com/sch/i.html?_nkw=" + \
      urllib.parse.quote(searchTerm)
  url += "&LH_BIN=1" # Buy-it-now
  if category is not None:
    url += "&_sacat=" + str(category)
  match (condition):
    case "used":
      url += "&LH_ItemCondition=3000"
    case "new":
      url += "&LH_ItemCondition=1000"
  # Have to double encode for some reason
  brand = urllib.parse.quote(brand)
  brand = brand.replace(".", "%2E")
  brand = brand.replace("-", "%2D")
  brand = urllib.parse.quote(brand)
  
  url += "&Brand=" + brand
  return url


def buildUrlCurrentListings(searchTerm, brand, category, condition):
  url = getBaseUrl(searchTerm, brand, category, condition)
  url += "&_sop=16"  # Sort order highest to lowest
  return url


def buildUrlSoldListings(searchTerm, brand, category, condition):
  url = getBaseUrl(searchTerm, brand, category, condition)
  url += "&_sop=16"  # Sort order by highest to lowest
  url += "&LH_Sold=1&LH_Complete=1"
  return url


def buildUrlRecentlySoldListings(searchTerm, brand, category, condition):
  url = getBaseUrl(searchTerm, brand, category, condition)
  url += "&_sop=13"
  url += "&LH_Sold=1&LH_Complete=1"
  return url
