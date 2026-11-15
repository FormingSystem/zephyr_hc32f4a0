---
id: learning.zephyr-docs.bluetooth-samples.page-67
title: BAP广播音频源
kind: reference
status: maintained
domains: [zephyr, bluetooth, samples]
source_url: https://docs.zephyrproject.org/latest/samples/bluetooth/audio/bap_broadcast_source/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="bluetooth_bap_broadcast_source"></a>

# 第67章\_基本音频配置文件（Basic Audio Profile，BAP）广播音频源（Broadcast Audio Source）

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/bluetooth/audio/bap_broadcast_source/README.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

[在 GitHub 浏览源码（Browse source code on GitHub）](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/bluetooth/audio/bap_broadcast_source/README.rst/..)

<a id="overview"></a>

## 67.1 概述（Overview）

本应用演示 BAP 广播源功能。它先发送带音频标志的扩展广播，再发送包含广播音频源端点（Broadcast Audio Source Endpoint，BASE）的周期广播，最后发送 BIGinfo 以及模拟的音频等时（ISO）数据。

> 译注——数据与可听音频：原文已说明音频数据可为模拟数据。源码还有 LC3 编码及 USB 音频输入等配置路径；建立 BIG、发送 ISO 数据成功，不自动证明接收端已经解码并从音频硬件播放声音。应分别确认流建立、编解码和输入／输出链路。

BAP 广播源每隔 30 秒重置一次，以展示完整 API 的使用过程。

> 译注——文档与源码版本差异：原文写 30 秒；本次取得的官方 main.c 将 `BROADCAST_SOURCE_LIFETIME` 定义为 120 秒，之后停止并删除广播源及广播集合，再进入下一轮创建。启用 `CONFIG_LIBLC3` 且使用 `CONFIG_USE_USB_AUDIO_INPUT` 时还会一直流送，不执行该定时停止。因此这里的 reset 不应理解成必然重启整块开发板，实际周期以所用源码与配置为准。

通用信息请参阅[蓝牙示例（Bluetooth samples）](https://docs.zephyrproject.org/latest/samples/bluetooth/bluetooth.html#bluetooth)。

<a id="requirements"></a>

## 67.2 前提条件（Requirements）

- 主机上运行 BlueZ，或者

- 一块支持 Bluetooth Low Energy 5.2 的开发板。

<a id="building-and-running"></a>

## 67.3 构建与运行（Building and Running）

> 译注——执行环境与前提：以下命令从读者自己的 Zephyr 源码根目录执行，实际开发板构建可使用 UCRT64 Bash 或 Linux Bash；模拟板的 Linux 可执行程序应在具备相应模拟环境的 Linux 中构建／运行。先按[入门指南](../getting_started/大纲.md)准备工具链、west 工作区和板支持，并核对所选控制器实际支持的角色及 ISO 等功能；“Bluetooth 5.2”名称本身不能代替功能核验。`samples/...` 是官方目录，`<board>` 替换为实际板目标，构建输出由工具生成。构建、烧录、发现对端、流／服务配置和收发分别检查；失败时先回查当前阶段的配置、板文档及配套角色。本次未执行固件构建、烧录或蓝牙通信。

以 nrf52 系列开发板和 Zephyr 蓝牙控制器为目标构建时，使用 `-DEXTRA_CONF_FILE=overlay-bt_ll_sw_split.conf` 启用所需的 ISO 功能支持。示例默认按顺序打包 BIS 子事件；添加 `-DCONFIG_ISO_PACKING_INTERLEAVED=y` 可使用交错打包（Interleaved packing）。

<a id="building-for-an-nrf5340dk"></a>

### 67.3.1 为 nrf5340dk 构建（Building for an nrf5340dk）

可以同时构建应用核镜像，以及供网络核使用的适当控制器镜像：

> 译注——两种构建路线：`--sysbuild` 管理应用核与网络核等镜像；下一段不带该参数的命令只构建应用核，随后须另行准备匹配的 HCI IPC 控制器镜像。`extra-iso-bt_ll_sw_split.conf` 是官方已有的 Kconfig 配置片段，应用于控制器构建，并非设备树 overlay。切换应用、板或构建路线时使用独立的相对输出目录或重新配置，避免把旧缓存和错误核的镜像混用；参见[HCI IPC 译文](../intercore_reference/P189_蓝牙HCI的IPC示例.md)。

```text
# From the root of the zephyr repository
west build -b nrf5340dk/nrf5340/cpuapp --sysbuild samples/bluetooth/audio/bap_broadcast_source/
```

若只想构建应用核镜像，则改用：

```text
# From the root of the zephyr repository
west build -b nrf5340dk/nrf5340/cpuapp samples/bluetooth/audio/bap_broadcast_source/
```

此时可将该应用核镜像与 [HCI IPC](../intercore_reference/P189_蓝牙HCI的IPC示例.md#bluetooth_hci_ipc) 示例配合使用，并为后者添加 [samples/bluetooth/hci_ipc/extra-iso-bt_ll_sw_split.conf](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/hci_ipc/extra-iso-bt_ll_sw_split.conf) 附加配置。

<a id="building-for-a-simulated-nrf5340bsim"></a>

### 67.3.2 为模拟的 nrf5340bsim 构建（Building for a simulated nrf5340bsim）

与真实硬件的构建方式类似，可以执行：

```text
# From the root of the zephyr repository
west build -b nrf5340bsim/nrf5340/cpuapp --sysbuild samples/bluetooth/audio/bap_broadcast_source/
```

注意，这会在 `./build/zephyr/zephyr.exe` 生成 Linux 可执行文件。更多信息请参阅[该板文档](../bsim_reference/P003_NRF5340模拟开发板.md#nrf5340bsim)。

> 译注——模拟产物：这里的 `.exe` 后缀不代表 Windows PE 程序，原文明确指 Linux 可执行文件。`./build/zephyr/zephyr.exe` 是原文给出的相对示例路径；指定其他构建目录或采用 sysbuild 多镜像布局时，实际产物位置应以构建输出和所选镜像目录为准。成功生成模拟程序也不等于已启动模拟器或完成真实板验证。

<a id="building-for-a-simulated-nrf52-bsim"></a>

### 67.3.3 为模拟的 nrf52\_bsim 构建（Building for a simulated nrf52\_bsim）

```text
# From the root of the zephyr repository
west build -b nrf52_bsim samples/bluetooth/audio/bap_broadcast_source/ -- -DEXTRA_CONF_FILE=overlay-bt_ll_sw_split.conf
```

<a id="see-also"></a>

## 67.4 另请参阅（See also）

[蓝牙 API（Bluetooth APIs）](https://docs.zephyrproject.org/latest/doxygen/html/group__bluetooth.html)

[蓝牙音频（Bluetooth Audio）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio.html)

[蓝牙基本音频配置文件（Bluetooth Basic Audio Profile）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html)

> 译注——源码入口：[samples/bluetooth/audio/bap_broadcast_source/src/main.c](../../../samples/bluetooth/audio/bap_broadcast_source/src/main.c)；[samples/bluetooth/audio/bap_broadcast_source/prj.conf](../../../samples/bluetooth/audio/bap_broadcast_source/prj.conf)。均按所在译文解析相对链接，仓库移动后仍可跟踪；本地源码版本可能与官方快照不同。

对应官方文档源码：[samples/bluetooth/audio/bap_broadcast_source/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/bluetooth/audio/bap_broadcast_source/README.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../samples/bluetooth/audio/bap_broadcast_source/README.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建、烧录、运行无线通信或连接设备。

[上一章](P066_BAP广播音频接收端.md) · [返回大纲](大纲.md) · [下一章](P068_BAP单播音频客户端.md)
