---
id: hc32-usb-console
title: HC32F4A0 USB1 CDC ACM 日志实验
kind: lab
status: maintained
domains: [zephyr, usb, hc32]
---

<!-- SPDX-FileCopyrightText: Copyright The Zephyr HC32F4A0 Contributors -->
<!-- SPDX-License-Identifier: Apache-2.0 -->

# 第1章\_USB1\_CDC\_ACM\_日志实验

## 1.1\_接口与前提

本例在已集成 HC32 适配的工程根目录执行，目标为 `uyup_rpi_a/hc32f4a0pitb`。USB1 连接 HC32 的 PA11/PA12，运行 Zephyr 原生 CDC ACM；USB2/DAP 连接板载调试器，用于下载和单步，两者不是同一个 COM 口。

```mermaid
flowchart LR
    A[USB2 DAP 2.x 下载] --> B[HC32 USBFS 与 48 MHz 时钟]
    B --> C[Zephyr CDC ACM 枚举 USB1 COM]
    C --> D[串口工具打开并置 DTR]
    D --> E[每秒日志与收发回显]
```

先按[开发板模式切换说明](../../project-docs/hardware.md#板载-dap-模式切换与下载故障提示)确认 DAP 模式。普通重启不按 SW2；切换模式才使用 SW1 关电、按住 SW2、SW1 开电、松开 SW2的顺序，每轮后检查 USB 枚举。

原理图 `UYUP-RPI-A-2.5.pdf` 的默认 USB1 跳线 R68/R69 将 D+/D− 接到主芯片物理脚 71/70，即 HC32 PA12/PA11。PA9 已接 USART1 TX，未作为 USB VBUS 输入；设备树显式禁用 VBUS 感知，因此本例不提供物理拔线的 VBUS 事件检测。

## 1.2\_构建和下载

以下均为 **工程根目录的 MSYS2 UCRT64 Bash** 命令，先完成 SDK 与根 `.venv` 配置。Linux 使用 `source .venv/bin/activate` 激活同用途环境。

```bash
source .venv/Scripts/activate
python scripts/project_env.py exec cmake -S samples/usb_console -B build/usb-console -G Ninja -DBOARD=uyup_rpi_a/hc32f4a0pitb
python scripts/project_env.py exec cmake --build build/usb-console
python scripts/verify_hc32_image.py --build-dir build/usb-console
python -m pyocd list
python -m pyocd flash --project . --config debug/pyocd.yaml --erase sector build/usb-console/zephyr/zephyr.hex
```

下载命令用于仅连接一个探针的情况；多个探针时加 `--uid` 和上一步实际编号。不要照抄其他 DAP 模式的编号。配置保留 `auto_unlock: false`，不自动解锁擦除。烧录成功与镜像离线审计、运行验收分别记录。

CMake 自动选用 Zephyr 自带的 `cdc-acm-console` snippet；它选择原生新 USB 栈、CDC ACM UART 并重定向控制台，不在应用里重复初始化协议栈。示例使用原生 `LOG_INF` 每秒输出序号和运行时间，输入数据原样回显，蓝灯按秒翻转。不打开串口时仍正常运行，应用心跳日志等待 DTR 后输出。

## 1.3\_打开 COM 观察日志

在工程根已激活的 `.venv` 中运行：

```bash
python -m serial.tools.list_ports -v
```

选择 USB1 的 `VID:PID=2FE3:0004` 设备，不选 USB2/DAP 的串口。2026-10-06 最终测试枚举为 COM8，实际端口号以自己的电脑为准。使用串口工具设置 **115200、8N1、无硬件流控，DTR 打开**；波特率是 CDC ACM 的线路编码，本例不据此改变 USB 总线速率。例如本次 Windows/UCRT64 执行：

```bash
python -m serial.tools.miniterm COM8 115200 --raw
```

miniterm 默认置 DTR；退出为 Ctrl+]。Linux 将 COM8 替换为实际 `/dev/ttyACM*` 设备。串口被其他程序占用时先关闭占用者。

可见的应用日志形如：

```text
[00:00:48.176,000] <inf> hc32_usb_console: USB1 CDC ACM heartbeat 48, uptime 48175 ms
```

USB 序列号来自 HC32 的 96 位 EFM 唯一 ID。固件首次从无序列号切换到有序列号时，Windows 可能分配新 COM 号。示例沿用 Zephyr 官方示例 VID/PID；独立发布产品时应配置自己获准使用的 VID/PID。

## 1.4\_移植依据与验证范围

- 时钟：晶振仍是 12 MHz；PLLH 输入 12 MHz，倍频 64 得到 768 MHz VCO，P/Q/R 分频 16 得到 48 MHz。SYSCLK/HCLK 为 48 MHz，USB 使用 PLLQ 48 MHz；切换前设置 Flash/SRAM 等待周期。范围依据 DS Rev1.60 的 PLLH 参数，USB时钟和 TRDT=5 依据 RM Rev1.50 USBFS 章节。
- 驱动：复用 Zephyr `snps,dwc2`，HC32 quirk 负责时钟检查、固定 PHY 引脚、INTC 源 399 → NVIC 30、VBUS override 与周转时间。ISR/vector 由 Zephyr 管理，不接入厂商中断分发表。
- HWINFO：实现原生设备 ID 接口，以厂商 `EFM_GetUID` 读出 96 位编号供 USB 序列号使用；没有声称支持尚未实现的复位原因 API。
- 已测：下载及全部固件字节回读匹配、Windows COM 枚举、日志连续性、双向回显、关闭/重新打开串口，以及调试器连接期间的日志和 GPIO 翻转。具体结果见[移植记录](../../project-docs/porting-status.md)。
- 当前实现为 USBFS Device CDC ACM；Host、USBHS、DMA、远程唤醒、低功耗和长时间压力测试不在本次验收范围。

此实验属于后续 USB 适配阶段，`learning/board/labs/hc32_port` 仍是 12 MHz 直驱的 GPIO/UART 入门快照，不把该快照误记为已包含 USB。

如需用 `printf()` / `scanf()` 进行标准输入输出，使用独立的 [USB 标准输入输出实验](../usb_stdio/README.md)。它保留本例的 USB 驱动和控制台路径，另接入 Picolibc stdin；两个固件分别构建和下载。
