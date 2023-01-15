import multiprocessing

class MonProcess(multiprocessing.Process):

    def run(self):
        print('Je suis le %s' % self.name)
        return

if __name__ == '__main__':
    PROC = []
    for i in range(5):
        p = MonProcess()
        PROC.append(p)
        p.start()

    for p in PROC:
        p.join()

