from solcx import compile_standard, install_solc
import json
from web3 import Web3
#This is the basic version

install_solc("0.6.0")

with open("./SimpleStorage.sol", "r") as file:
    simple_storage_file = file.read()
    print(simple_storage_file)

    # Complie our sol

    compiled_sol = compile_standard(
        {
            "language": "Solidity",
            "sources": {"SimpleStorage.sol": {"content": simple_storage_file}},
            "settings": {
                "outputSelection": {
                    "*": {"*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}
                }
            },
        },
        solc_version="0.6.0",
    )

with open("compiled_code.json", "w") as file:
    json.dump(compiled_sol, file)

# get bytecode

bytecode = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"][
    "bytecode"
]["object"]

# get abi
abi = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["abi"]

# for connecting to blockchain
w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
chaind_id = 5777
my_address = "0x551d6e26860B19a6A0434089DAF637cac67Ac182"
private_key = "1cd314d88625f29ee4926405a85fe3de89071d4462747362b28bed2eee2d54ef"

# Create the contract in python
SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)

# Get the lastest txn
nonce = w3.eth.getTransactionCount(my_address)
print(nonce)


# 1. Build a txn
# 2. Sign a txn
# 3. Send a txn
transation = SimpleStorage.constructor().buildTransaction({"chainId": chaind_id})
