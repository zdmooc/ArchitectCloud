import logging
import mon_module

def compute():
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%d-%m-%Y %H:%M:%S', level=logging.DEBUG)
    logging.info('début du traitement')
    mon_module.ma_fonction()
    logging.info('Fin du traitement')

if __name__ == '__main__':
    compute()
