import logging
import helpers.ebay_url_builder as ebay_url_builder
import helpers.ebay_requests as ebay_requests


def getSellTrhoughRate(soldListings, currentListings):
  if (currentListings != 0):
    return soldListings / currentListings * 100
  else:
    return 0


def performSearch(searchTerm, brand, category=None, condition=None, saveResults=False):
  logging.info("SEARCH TERM: '" + searchTerm + "' / CATEGORY: " + str(category) + " / CONDITION: " + condition)

  # Build URLs
  currentListingsUrl = ebay_url_builder.buildUrlCurrentListings(
      searchTerm=searchTerm, brand=brand, category=category, condition=condition)
  soldListingsUrl = ebay_url_builder.buildUrlSoldListings(
      searchTerm=searchTerm, brand=brand, category=category, condition=condition)
  recentlySoldListingsUrl = ebay_url_builder.buildUrlRecentlySoldListings(
      searchTerm=searchTerm, brand=brand, category=category, condition=condition)

  # Perform Requests (Handle error try catching here???)
  try:
    currentListings = ebay_requests.getListingsAmountFromUrl(currentListingsUrl)
    numSoldListings = ebay_requests.getListingsAmountFromUrl(soldListingsUrl)
    sellThroughRate = getSellTrhoughRate(numSoldListings, currentListings)
    avgSoldPrice = ebay_requests.getAverageSoldPrice(
        recentlySoldListingsUrl, numSoldListings)
  except Exception as e:
    logging.error("Error trying to get ebay requests: " + str(e))
    currentListings = -1
    numSoldListings = -1
    sellThroughRate = -1
    avgSoldPrice = -1
  finally:
    # logging.info("Current URL: " + currentListingsUrl)
    logging.info("Sold Listings URL: " + recentlySoldListingsUrl)
    logging.info("Current Listings: " + str(currentListings))
    logging.info("Sold Listings: " + str(numSoldListings))
    logging.info("Average Sold Price: $" + format(avgSoldPrice, ".2f"))
    logging.info("STR: " + format(sellThroughRate, ".1f") + "%")
    logging.info("*===========================================================================*")

    object = {
      "brand": brand,
      "currentListings": currentListings,
      "numSoldListings": numSoldListings,
      "totalListedAndSold": currentListings + numSoldListings,
      "sellThroughRate": format(sellThroughRate, ".1f"),
      "avgSoldPrice": format(avgSoldPrice, ".2f")
    }
    return object
