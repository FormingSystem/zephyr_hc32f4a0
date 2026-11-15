---
id: learning.zephyr-docs.hardware.headers-1
title: ArduCamFFC40针连接器
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__arducam-ffc-40pin.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第292章\_ArduCamFFC40针连接器

原文：[group__arducam-ffc-40pin](https://docs.zephyrproject.org/latest/doxygen/html/group__arducam-ffc-40pin.html)。读取日期：2026-10-13，官方 `latest` 文档版本。

## 292.1\_接口与术语

本页定义ArduCam柔性扁平电缆（Flexible Flat Cable，FFC）40针摄像头连接器对外引脚的常量，声明来自 `zephyr/dt-bindings/gpio/arducam-ffc-40pin-connector.h`。通用输入/输出（General Purpose Input/Output，GPIO）连接关系使用下表的原常量。

集成电路间总线（Inter-Integrated Circuit，I²C）使用串行时钟线（Serial Clock，SCL）与串行数据线（Serial Data，SDA）。

摄像头接口分为移动产业处理器接口（Mobile Industry Processor Interface，MIPI）摄像头串行接口第2版（Camera Serial Interface 2，CSI-2）、数字视频端口（Digital Video Port，DVP）及公共引脚。数据通道（Data Lane）与时钟通道（Clock Lane）分别列出正端和负端。水平同步（Horizontal Sync）、垂直同步（Vertical Sync）、外部时钟（External Clock）和像素时钟（Pixel Clock）均保留原信号标识。

## 292.2\_完整引脚常量

| 宏 | 原定义 | 中文说明 | 原说明 |
| --- | --- | --- | --- |
| [`ARDUCAM_FFC_40PIN_MIPI_CSI_DL1_P`](https://docs.zephyrproject.org/latest/doxygen/html/group__arducam-ffc-40pin.html#gabb6aedf55d73f0fa49a31ff9fd8a6c7b) | `5` | MIPI-CSI2数据通道1正端 | MIPI‑CSI2 data lane 1 positive. |
| [`ARDUCAM_FFC_40PIN_MIPI_CSI_DL1_N`](https://docs.zephyrproject.org/latest/doxygen/html/group__arducam-ffc-40pin.html#gaac66eea5bb1da4ee66fe6432d72af2f0) | `6` | MIPI-CSI2数据通道1负端 | MIPI‑CSI2 data lane 1 negative. |
| [`ARDUCAM_FFC_40PIN_MIPI_CSI_CL_P`](https://docs.zephyrproject.org/latest/doxygen/html/group__arducam-ffc-40pin.html#ga0dc63ab020664db01467a2e267827945) | `8` | MIPI-CSI2时钟通道正端 | MIPI‑CSI2 clock lane positive. |
| [`ARDUCAM_FFC_40PIN_MIPI_CSI_CL_N`](https://docs.zephyrproject.org/latest/doxygen/html/group__arducam-ffc-40pin.html#gab3700b20fe7293bbe9ece6e68b1dd070) | `9` | MIPI-CSI2时钟通道负端 | MIPI‑CSI2 clock lane negative. |
| [`ARDUCAM_FFC_40PIN_MIPI_CSI_DL0_P`](https://docs.zephyrproject.org/latest/doxygen/html/group__arducam-ffc-40pin.html#gaa0c2dd364246a8dee85c66efbf9c3451) | `11` | MIPI-CSI2数据通道0正端 | MIPI‑CSI2 data lane 0 positive. |
| [`ARDUCAM_FFC_40PIN_MIPI_CSI_DL0_N`](https://docs.zephyrproject.org/latest/doxygen/html/group__arducam-ffc-40pin.html#ga022041fab0a2b9820ee66fba9c620642) | `12` | MIPI-CSI2数据通道0负端 | MIPI‑CSI2 data lane 0 negative. |
| [`ARDUCAM_FFC_40PIN_D11`](https://docs.zephyrproject.org/latest/doxygen/html/group__arducam-ffc-40pin.html#ga1f77d502764f1d6e9d01333532c17680) | `2` | 并行端口数据位11 | Parallel port data bit 11. |
| [`ARDUCAM_FFC_40PIN_D10`](https://docs.zephyrproject.org/latest/doxygen/html/group__arducam-ffc-40pin.html#gae97c772ca72994a8f0e4eccde93b8274) | `3` | 并行端口数据位10 | Parallel port data bit 10. |
| [`ARDUCAM_FFC_40PIN_D9`](https://docs.zephyrproject.org/latest/doxygen/html/group__arducam-ffc-40pin.html#gab807bcf22dd4dcb968a432d4aceb0aa7) | `5` | 并行端口数据位9 | Parallel port data bit 9. |
| [`ARDUCAM_FFC_40PIN_D8`](https://docs.zephyrproject.org/latest/doxygen/html/group__arducam-ffc-40pin.html#gae83ce151d5778709350f1e6bab91c984) | `6` | 并行端口数据位8 | Parallel port data bit 8. |
| [`ARDUCAM_FFC_40PIN_D7`](https://docs.zephyrproject.org/latest/doxygen/html/group__arducam-ffc-40pin.html#gad9a2fc591fe8f94692705c124b4697fa) | `8` | 并行端口数据位7 | Parallel port data bit 7. |
| [`ARDUCAM_FFC_40PIN_D6`](https://docs.zephyrproject.org/latest/doxygen/html/group__arducam-ffc-40pin.html#gad4f7515f56e2f34a7e217cd9c7f16f2b) | `9` | 并行端口数据位6 | Parallel port data bit 6. |
| [`ARDUCAM_FFC_40PIN_D5`](https://docs.zephyrproject.org/latest/doxygen/html/group__arducam-ffc-40pin.html#ga55fca4f40d00b27d8469101b49812726) | `11` | 并行端口数据位5 | Parallel port data bit 5. |
| [`ARDUCAM_FFC_40PIN_D4`](https://docs.zephyrproject.org/latest/doxygen/html/group__arducam-ffc-40pin.html#gac120cd2491f19d974b20742e82d40429) | `12` | 并行端口数据位4 | Parallel port data bit 4. |
| [`ARDUCAM_FFC_40PIN_D3`](https://docs.zephyrproject.org/latest/doxygen/html/group__arducam-ffc-40pin.html#ga4d4aa4ee86687fb92fb13580b6e4b2c0) | `14` | 并行端口数据位3 | Parallel port data bit 3. |
| [`ARDUCAM_FFC_40PIN_D2`](https://docs.zephyrproject.org/latest/doxygen/html/group__arducam-ffc-40pin.html#gaaf6736df362643af6321260d5f2278c3) | `15` | 并行端口数据位2 | Parallel port data bit 2. |
| [`ARDUCAM_FFC_40PIN_D1`](https://docs.zephyrproject.org/latest/doxygen/html/group__arducam-ffc-40pin.html#gade0cdafb74fa35efe256e8cdad6185f5) | `17` | 并行端口数据位1 | Parallel port data bit 1. |
| [`ARDUCAM_FFC_40PIN_D0`](https://docs.zephyrproject.org/latest/doxygen/html/group__arducam-ffc-40pin.html#gaccf841d3005d2f866c5d1032e80c089b) | `18` | 并行端口数据位0 | Parallel port data bit 0. |
| [`ARDUCAM_FFC_40PIN_VSYNC`](https://docs.zephyrproject.org/latest/doxygen/html/group__arducam-ffc-40pin.html#ga58a0c824a505b5f3d2cf7d4f59012a09) | `23` | 垂直同步 | Vertical sync. |
| [`ARDUCAM_FFC_40PIN_HSYNC`](https://docs.zephyrproject.org/latest/doxygen/html/group__arducam-ffc-40pin.html#ga6e5f141c0edae7ef269ac2e70a1f89ba) | `24` | 水平同步 | Horizontal sync. |
| [`ARDUCAM_FFC_40PIN_SCL`](https://docs.zephyrproject.org/latest/doxygen/html/group__arducam-ffc-40pin.html#ga42ceb11cb1bd0f390a3d78f74cdcf671) | `20` | I²C时钟线 | I2C clock line. |
| [`ARDUCAM_FFC_40PIN_SDA`](https://docs.zephyrproject.org/latest/doxygen/html/group__arducam-ffc-40pin.html#gafebcd14da9eef19c104733af0051991c) | `21` | I²C数据线 | I2C data line. |
| [`ARDUCAM_FFC_40PIN_RESET`](https://docs.zephyrproject.org/latest/doxygen/html/group__arducam-ffc-40pin.html#ga404ac00062b9f45de38ba62a50ca8958) | `25` | 复位 | Reset. |
| [`ARDUCAM_FFC_40PIN_XCLK`](https://docs.zephyrproject.org/latest/doxygen/html/group__arducam-ffc-40pin.html#ga9a2a47c52a47e8e1137cd173e5b6a536) | `26` | 外部时钟 | External clock. |
| [`ARDUCAM_FFC_40PIN_PCLK`](https://docs.zephyrproject.org/latest/doxygen/html/group__arducam-ffc-40pin.html#gaef5e7d33523513b57c2a88d6baac24d0) | `27` | 像素时钟 | Pixel clock. |
| [`ARDUCAM_FFC_40PIN_INT`](https://docs.zephyrproject.org/latest/doxygen/html/group__arducam-ffc-40pin.html#gacff351acd94fc562f0ea7b1a81197744) | `28` | 来自传感器的中断 | Interrupt from sensor. |

---

[上一章：GPIO排针目录](P291_GPIO排针目录.md) · [下一章：ArducamDVP连接器](P293_ArducamDVP连接器.md) · [返回大纲](大纲.md)
