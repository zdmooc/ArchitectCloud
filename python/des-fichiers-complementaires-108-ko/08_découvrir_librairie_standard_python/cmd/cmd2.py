import cmd
import multiprocessing as mp
import time

processes = {}

p_id = 0

class MonProcess(mp.Process):
    def __init__(self, temps=5):
        self.temps = temps
        super().__init__()

    def run(self):
        time.sleep(self.temps)
        return

class Cli(cmd.Cmd):
    def do_create(self, line):
        global p_id
        if line:
            try:
                obj, temps = line.split()
            except:
                temps = 5
                pass
            obj = line
            if obj == "process":
                p = MonProcess(int(temps))
                p_id += 1
                processes[str(p_id)] = p

    def help_create(self):
        s = """
        create process [temps] par défaut temps=5
        """
        print(s)

    def do_list(self, line):
        if processes:
            tit = "| %10s | %20s | %10s | %10s |" % ("Process No", "Name","Pid", "Is Alive")
            print(tit)
            print("-" * len(tit))
            for k,p in processes.items():
                print( "| %10s | %20s | %10s | %10s |" % (k, p.name, p.pid, p.is_alive() ))
            print("-" * len(tit))
        else:
            print("No processes")

    ## -------------------------
    ## Demarrage des processus
    ## -------------------------
    def start_proc(self, proc):
        p = processes[proc]
        print("Lancement de : %s " % p.name)
        p.start()

    def do_start(self, line):
        if line == "ALL":
            for p in processes:
                self.start_proc(p)
        else:
            if line in processes:
                self.start_proc(line)
            else:
                print("Processus No : %s inexistant" % line)

    def help_start(self):
        s = """
        start <No processe>
        start ALL
        démarre un processus pour un no
        ou demarre tout les processus
        """
        print(s)

    ## ---------------
    ## Join Processes
    ## ---------------
    def do_join(self, line):
        if line in processes:
            p = processes[line]
            print("Join sur : %s " % p.name)
            p.join()

    ## -------------------
    ## Autres fonctions
    ## -------------------
    def default(self, line):
        print("Line = [%s] " % line)

    def do_bonjour(self, line):
        """ Dire bonjour """
        print("Bonjour")

    def do_quit(self, line):
        return True

    def do_EOF(self, line):
        return True

if __name__ == '__main__':
    Cli().cmdloop()
