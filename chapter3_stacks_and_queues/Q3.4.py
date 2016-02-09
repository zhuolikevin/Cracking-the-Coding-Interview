class Tower:
    def __init__(self, index):
        self.disks = []
        self.index = index

    def add(self, disk):
        if self.disks and self.disks[-1] <= disk:
            raise ValueError('Error placing disk')
        self.disks.append(disk)

    def moveTopTo(self, tower):
        if not self.disks:
            raise IndexError('This tower is empty')
        disk = self.disks.pop()
        tower.add(disk)
        print 'Move disk [' + str(disk) + '] from (' + str(self.index) + ') to (' + str(tower.index) + ')'

    def moveDisks(self, n, destinationTower, bufferTower):
        if n > 0:
            self.moveDisks(n-1, bufferTower, destinationTower)
            self.moveTopTo(destinationTower)
            bufferTower.moveDisks(n-1, destinationTower, self)

n = 3
towers = []
for i in range(n):
    towers.append(Tower(i))

for i in range(n-1, -1, -1):
    towers[0].add(i)

for i in range(n):
    print i, '-----------'
    for disk in towers[i].disks:
        print disk

towers[0].moveDisks(n, towers[2], towers[1])
for i in range(n):
    print i, '-----------'
    for disk in towers[i].disks:
        print disk
