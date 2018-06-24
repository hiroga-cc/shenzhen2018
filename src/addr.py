class AddrHandler():
    def __init__(self):
        # print("init!")
        self.filepath = "addrfile"

    def read_addr(self):
        with open(self.filepath, "r") as f:
            addr = f.readline().replace("\n", "")
            return addr

    def cut_addr(self):
        with open(self.filepath, "r+") as f:
            addr = f.readline().replace("\n", "")
            f.truncate(0)
            return addr

    def write_addr(self, addr):
        with open(self.filepath, "w") as f:
            f.truncate(0)
            f.write(addr)

if __name__ == "__main__":
    h = AddrHandler()
    print(h.read_addr())
