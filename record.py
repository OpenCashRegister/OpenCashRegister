import sheeto

def ins(itemId,prof,namee):
  numofpurch=len(list(filter(lambda x: x != "", sheeto.orders.getColumn(1))))
  sheeto.orders[1, numofpurch+1]=itemId
  sheeto.orders[3, numofpurch+1]=prof
  sheeto.orders[2, numofpurch+1]=namee