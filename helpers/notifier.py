import requests, logging


def send_notification(itemDesc, newItemurl):
  url = "https://ntfy.sh/cwh1981"
  data = "New item found for " + itemDesc + " - " + newItemurl
  response = requests.post(url,
                data=data.encode(encoding='utf-8'))
  if response.status_code == 200:
    logging.info(itemDesc + ": Notification of new item sent successfully!")
  else:
    logging.error(f"Failed to send notification: {response.status_code}")
