# GMGN Address Opener

Bulk-open [gmgn.ai](https://gmgn.ai) analytics pages for a list of wallet addresses. Supports Solana and BSC chains.

## Features

- Reads addresses from a text file
- Supports Solana (sol) and BSC (bsc) chains
- Automatically opens the corresponding gmgn.ai page in your browser
- Choose your preferred browser (Chrome, Safari, Opera, Brave, Edge, Firefox)
- Configurable delay between tabs to prevent browser lag

## Requirements

- macOS
- Python 3.6+

## Usage

### Basic

```bash
# Open Solana addresses
python gmgn_opener.py sol

# Open BSC addresses
python gmgn_opener.py bsc
```

### Specify a Browser

```bash
python gmgn_opener.py sol -b chrome
python gmgn_opener.py bsc -b brave
```

Supported browsers: `chrome`, `safari`, `opera`, `brave`, `edge`, `firefox`

### Custom Delay

```bash
# Wait 1 second between each tab
python gmgn_opener.py sol -d 1
```

### Custom Address File

```bash
python gmgn_opener.py sol -f wallets.txt
```

### Putting It All Together

```bash
python gmgn_opener.py bsc -b chrome -d 0.8 -f my_addresses.txt
```

## Address File Format

One address per line. Two formats are supported:

```
# Plain address
7xKXtg2CW87d97TXJSDpbD5jBkheTqA83TZRuJosgAsU

# Address with a label (everything after the colon is ignored)
7xKXtg2CW87d97TXJSDpbD5jBkheTqA83TZRuJosgAsU:smart money
```

## Options

| Option | Short | Description | Default |
|---|---|---|---|
| `chain` | - | Chain type (`sol` / `bsc`) | required |
| `--browser` | `-b` | Browser to use | system default |
| `--delay` | `-d` | Delay between tabs (seconds) | 0.5 |
| `--file` | `-f` | Path to the address file | address.txt |

## Sample Output

```
Chain: Solana
Browser: Google Chrome
Found 3 addresses

[1/3] 7xKXtg2C...sAsU
[2/3] 9aE8nXkT...4jPq
[3/3] BvLwcNZh...7mRs

Done!
```