import cmd

class CLI(cmd.Cmd):
    def do_bonjour(self, line):
        print("Bonjour")

    def do_EOF(self, line):
        return True

if __name__ == '__main__':
    CLI().cmdloop()
