# GMGN Address Opener

批量打开地址的 [gmgn.ai](https://gmgn.ai) 分析页面，支持 Solana 和 BSC 链。

## 功能

- 从文件读取地址列表
- 支持 Solana (sol) 和 BSC (bsc) 链
- 自动在浏览器中打开对应的 gmgn.ai 页面
- 支持指定浏览器（Chrome、Safari、Opera、Brave、Edge、Firefox）
- 可配置打开间隔，避免浏览器卡顿

## 环境要求

- macOS
- Python 3.6+

## 使用方法

### 基本用法

```bash
# 打开 Solana 地址
python gmgn_opener.py sol

# 打开 BSC 地址
python gmgn_opener.py bsc
```

### 指定浏览器

```bash
python gmgn_opener.py sol -b chrome
python gmgn_opener.py bsc -b brave
```

支持的浏览器：`chrome`、`safari`、`opera`、`brave`、`edge`、`firefox`

### 自定义延迟

```bash
# 每次打开间隔 1 秒
python gmgn_opener.py sol -d 1
```

### 指定地址文件

```bash
python gmgn_opener.py sol -f wallets.txt
```

### 组合使用

```bash
python gmgn_opener.py bsc -b chrome -d 0.8 -f my_addresses.txt
```

## 地址文件格式

每行一个地址，支持两种格式：

```
# 纯地址
7xKXtg2CW87d97TXJSDpbD5jBkheTqA83TZRuJosgAsU

# 地址:备注（冒号后的内容会被忽略）
7xKXtg2CW87d97TXJSDpbD5jBkheTqA83TZRuJosgAsU:smart money
```

## 参数说明

| 参数 | 简写 | 说明 | 默认值 |
|------|------|------|--------|
| `chain` | - | 链类型（sol/bsc） | 必填 |
| `--browser` | `-b` | 指定浏览器 | 系统默认 |
| `--delay` | `-d` | 打开间隔（秒） | 0.5 |
| `--file` | `-f` | 地址文件路径 | address.txt |

## 示例输出

```
链: Solana
浏览器: Google Chrome
共找到 3 个地址

[1/3] 7xKXtg2C...sAsU
[2/3] 9aE8nXkT...4jPq
[3/3] BvLwcNZh...7mRs

完成!
```