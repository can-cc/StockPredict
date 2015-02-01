from .models import Stock
def loadNYSE():
    for line in open("predictCenter/Data/NYSE"):
            cells = line.split('\t')
            print cells
            stock = Stock(stockName=cells[1],
                          symbol=cells[0],
                          IPOyear=cells[4],
                          sector=cells[5],
                          industry=cells[6],
                          SE='NYSE')
            stock.save()

def loadSH():
    for line in open('predictCenter/Data/SH.txt'):
        try:
            cells = line.split('\t')
            print cells
            stock = Stock(stockName=cells[1][0:-2],
                          symbol=cells[0] + '.SH',
                          SE='SHSE')
            stock.save()
        except:
            pass

def loadSZ():
    for line in open('predictCenter/Data/SZ.txt'):
        try:
            cells = line.split('\t')
            print cells
            stock = Stock(stockName=cells[1][0:-2],
                          symbol=cells[0] + '.SZ',
                          SE='SZSE')
            stock.save()
        except:
            pass