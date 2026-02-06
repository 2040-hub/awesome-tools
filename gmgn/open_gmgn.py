#!/usr/bin/env python3
"""
读取 address.txt 中的地址，用指定浏览器打开 gmgn.ai 对应页面
支持 Solana (sol) 和 BSC (bsc) 链
"""

import subprocess
import time
import argparse
from pathlib import Path

# macOS 浏览器应用名称映射
BROWSERS = {
    "chrome": "Google Chrome",
    "safari": "Safari",
    "opera": "Opera",
    "brave": "Brave Browser",
    "edge": "Microsoft Edge",
    "firefox": "Firefox",
}

# 支持的链
CHAINS = {
    "sol": "Solana",
    "bsc": "BSC",
}

def open_url(url: str, browser: str = None):
    """用指定浏览器打开 URL，不指定则用系统默认"""
    if browser:
        app_name = BROWSERS.get(browser.lower())
        if app_name:
            subprocess.run(["open", "-a", app_name, url])
        else:
            print(f"未知浏览器: {browser}，使用默认浏览器")
            subprocess.run(["open", url])
    else:
        subprocess.run(["open", url])

def main():
    parser = argparse.ArgumentParser(description="批量打开地址的 gmgn.ai 页面")
    parser.add_argument(
        "chain",
        choices=list(CHAINS.keys()),
        help=f"链类型: {', '.join(f'{k} ({v})' for k, v in CHAINS.items())}"
    )
    parser.add_argument(
        "-b", "--browser",
        choices=list(BROWSERS.keys()),
        help=f"指定浏览器: {', '.join(BROWSERS.keys())}（默认使用系统默认浏览器）"
    )
    parser.add_argument(
        "-d", "--delay",
        type=float,
        default=0.5,
        help="每次打开的间隔秒数（默认 0.5）"
    )
    parser.add_argument(
        "-f", "--file",
        default="address.txt",
        help="地址文件路径（默认 address.txt）"
    )
    args = parser.parse_args()
    
    address_file = Path(args.file)
    
    if not address_file.exists():
        print(f"错误: {address_file} 文件不存在")
        return
    
    lines = [line.strip() for line in address_file.read_text().splitlines() if line.strip()]
    
    if not lines:
        print("错误: 文件为空")
        return
    
    # 提取地址（冒号前的部分）
    addresses = []
    for line in lines:
        addr = line.split(':')[0].strip() if ':' in line else line.strip()
        if addr:
            addresses.append(addr)
    
    if not addresses:
        print("错误: 未找到有效地址")
        return
    
    browser_name = BROWSERS.get(args.browser, "系统默认") if args.browser else "系统默认"
    chain_name = CHAINS.get(args.chain)
    
    print(f"链: {chain_name}")
    print(f"浏览器: {browser_name}")
    print(f"共找到 {len(addresses)} 个地址\n")
    
    for i, addr in enumerate(addresses, 1):
        url = f"https://gmgn.ai/{args.chain}/address/{addr}"
        print(f"[{i}/{len(addresses)}] {addr[:8]}...{addr[-4:]}")
        open_url(url, args.browser)
        if i < len(addresses):
            time.sleep(args.delay)
    
    print("\n完成!")

if __name__ == "__main__":
    main()