import urllib


def getBaseUrl(searchTerm, brand, category, condition):
  url = "https://www.ebay.com/sch/i.html?_nkw=" + \
      urllib.parse.quote(searchTerm)
  url += "&LH_BIN=1"
  if category is not None:
    url += "&_sacat=" + str(category)
  match (condition):
    case "used":
      url += "&LH_ItemCondition=3000"
    case "new":
      url += "&LH_ItemCondition=1000"
  brand = urllib.parse.quote(urllib.parse.quote(brand)) # Have to double encode for some reason
  url += "&Brand=" + brand
  return url


def buildUrlCurrentListings(searchTerm, brand, category, condition):
  url = getBaseUrl(searchTerm, brand, category, condition)
  url += "&_sop=15"  # Sort order by lowest to highest to get more accurate count
  return url


def buildUrlSoldListings(searchTerm, brand, category, condition):
  url = buildUrlCurrentListings(searchTerm, brand, category, condition)
  url += "&LH_Sold=1&LH_Complete=1"
  return url


def buildUrlRecentlySoldListings(searchTerm, brand, category, condition):
  url = getBaseUrl(searchTerm, brand, category, condition)
  url += "&_sop=13"
  url += "&LH_Sold=1&LH_Complete=1"
  return url
