from abc import ABC
from distutils.dir_util import copy_tree
from typing import List


source = "C:\\ti\\DRV8353Rx-1.0.1\\DRV8353Rx_InstaspinFOC_FW\\drv83xx_foc\\"
destination = "C:\\ti\\motorware\\motorware_1_01_00_18\\sw\\"


class Operation(ABC):
    def execute():
        """Execute an operation"""


class CopyDirectioryOperation(Operation):
    source: str
    destination: str

    def __init__(self, source: str, destination: str) -> None:
        self.source = source
        self.destination = destination

    def execute(self):
        copy_tree(self.source, self.destination)

    def __repr__(self) -> str:
        return (
            "COPY DIRECTORY\n"
            + "FROM: "
            + self.source
            + "\n"
            + "TO: "
            + self.destination
        )


operations: List[Operation] = [
    CopyDirectioryOperation(
        source + "drvic\\drv8353", destination + "drivers\\drvic\\drv8353"
    ),
    CopyDirectioryOperation(
        source + "hal\\boards\\drv8353", destination + "modules\\hal\\boards\\drv8353"
    ),
    CopyDirectioryOperation(
        source + "instaspin_foc\\src", destination + "modules\\hal\\src"
    ),
    CopyDirectioryOperation(
        source + "instaspin_foc\\boards\\drv8353",
        destination + "solutions\\instaspin_foc\\boards\\drv8353",
    ),
    CopyDirectioryOperation(
        source + "instaspin_foc\\src", destination + "solutions\\instaspin_foc\\src"
    ),
]

print(
    "Operations copied from https://www.ti.com/lit/ug/slvubh8b/slvubh8b.pdf?ts=1662811995014",
    end="\n\n",
)

print(
    "COPY DIRECTORY operation will merge src directory in to dest. It will overwrite existing files with matching names.",
    end="\n\n",
)

print("Do you want to execute the following operations:")
for o in operations:
    print(o, end="\n\n")

print("PLEASE MAKE SURE THE MOTORWARE PATH IS CORRECT!")
print("\nPaths can be modified in main.py\n")

i = input("Please enter 'yes' to continue: ")

if i != "yes":
    print("Operation halted by user.")
    exit(1)
else:
    print("Initiating operations")

for operation in operations:
    print("Executing: " + str(operation))
    operation.execute()
