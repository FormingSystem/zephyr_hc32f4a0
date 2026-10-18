---
id: learning.zephyr-docs.board-samples.page-104
title: 低功耗核GPIO唤醒
kind: reference
status: maintained
domains: [zephyr, boards, samples]
source_url: https://docs.zephyrproject.org/latest/samples/boards/espressif/ulp/lp_core/gpio_wakeup/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="lp-gpio-wakeup"></a>

# 第104章\_低功耗核 GPIO 唤醒（LP GPIO Wakeup）

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/boards/espressif/ulp/lp_core/gpio_wakeup/README.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

[在 GitHub 浏览源码（Browse source code on GitHub）](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/boards/espressif/ulp/lp_core/gpio_wakeup/README.rst/..)

<a id="overview"></a>

## 104.1 概述（Overview）

本示例演示：在低功耗通用输入输出（Low-Power GPIO，LP GPIO）引脚上检测到低电平时，由低功耗核把高性能核从深度睡眠中唤醒。低功耗核使用 Zephyr GPIO API 配置引脚并启用唤醒中断。

高性能核启动后打印唤醒计数，再通过 `sys_poweroff()` 进入深度睡眠。一个带 `RTC_DATA_ATTR` 属性的变量跨深度睡眠周期记录唤醒次数。

> 译注——计数与镜像保持：HP 用 hwinfo_get_reset_cause() 的 RESET_LOW_POWER_WAKE 标志决定是否递增 RTC_DATA_ATTR 计数；该判断本身没有单独解码 GPIO 引脚或 ULP 原因。SoC 加载器在检测到 ESP_SLEEP_WAKEUP_ULP 时跳过 LP 镜像重新加载，以保留 LP RAM；冷启动才加载镜像并用 HP_CPU 触发首次启动。

示例默认使用 GPIO0（LP_IO_0），配置低电平触发并启用内部上拉（Internal pull-up）。修改板级覆盖文件中的 `wakeup-pin` 别名，即可改用任意低功耗 GPIO 引脚，即 GPIO0～GPIO7。

> 译注——配置属于 LP 镜像：wakeup-pin 位于 remote/boards/esp32c6_devkitc_lpcore.overlay，指向 lp_gpio 的 0 号引脚，并使用 GPIO_PULL_UP 与 GPIO_ACTIVE_LOW。remote/src/main.c 将 GPIO_INT_LEVEL_ACTIVE 与该有效电平组合，得到低电平触发；不是下降沿触发。原文日志中的 edge 是旧文字，当前 HP 源码已改成 level。

<a id="how-it-works"></a>

## 104.2 工作过程（How it works）

1. 高性能核加载低功耗核的二进制镜像，将低功耗 IO 配置为唤醒源，然后进入深度睡眠。

2. 低功耗核启动，通过 `ulp_lp_core_wakeup_main_processor()` 通知高性能核，将 GPIO 配置为带上拉和低电平中断的输入，随后停止运行。

3. 将引脚拉低后，低功耗核复位并从步骤 2 重复执行，再次唤醒高性能核。

> 译注——触发次数：这是一种电平唤醒，保持低电平或按钮抖动可能造成多次唤醒，不能把 wake_count 直接当成经过消抖的按键次数。LP 每次从 main() 开始，先通知 HP，再配置 GPIO 并 halt；与中断示例中的 wfi 循环不是同一种恢复方式。

<a id="wiring"></a>

## 104.3 接线（Wiring）

将按钮或跳线连接到 GPIO0。由于启用了内部上拉，引脚默认保持高电平；短暂将该引脚接到地（GND），即可触发唤醒。

<a id="building-and-flashing"></a>

## 104.4 构建与烧录（Building and Flashing）

> 译注——执行前提：在读者的 Zephyr 源码根目录，用 UCRT64 Bash 或 Linux Bash 执行主机命令；先按[入门指南](../getting_started/大纲.md)准备工具、模块、RISC-V 工具链和 ESP32-C6 板。--sysbuild 会构建 HP 主应用及 remote 中的 LP 子应用；烧录使用同一构建目录。提示符和输出日志不作为命令粘贴；本次未构建、烧录、调试或连接设备。

按以下命令构建示例代码：

```text
west build -b esp32c6_devkitc/esp32c6/hpcore --sysbuild samples/boards/espressif/ulp/lp_core/gpio_wakeup
```

使用以下命令将其烧录到设备：

> 译注——Sysbuild 差异：下面原文再次构建时漏了 --sysbuild，不能用它在干净目录中替代前面的双镜像构建。按本页第一条带 --sysbuild 的命令成功构建后，可在同一构建目录直接执行 west flash；如需重新配置，仍须保留 --sysbuild。原命令留作版本对照，不表示单独构建 HP 就已准备好 LP 固件。

```text
west build -b esp32c6_devkitc/esp32c6/hpcore samples/boards/espressif/ulp/lp_core/gpio_wakeup
west flash
```

<a id="sample-output"></a>

### 104.4.1 示例输出（Sample Output）

```text
First boot, LP core will wake us on LP GPIO edge
HP core entering deep sleep...
```

将 GPIO0 短暂接到 GND 后：

```text
Woke up from LP core (LP IO)! Wake count: 1
HP core entering deep sleep...
```

> 译注——源码入口：[src/main.c](../../../samples/boards/espressif/ulp/lp_core/gpio_wakeup/src/main.c)；[remote/src/main.c](../../../samples/boards/espressif/ulp/lp_core/gpio_wakeup/remote/src/main.c)；[sysbuild.cmake](../../../samples/boards/espressif/ulp/lp_core/gpio_wakeup/sysbuild.cmake)；[prj.conf](../../../samples/boards/espressif/ulp/lp_core/gpio_wakeup/prj.conf)；[remote/boards/esp32c6_devkitc_lpcore.overlay](../../../samples/boards/espressif/ulp/lp_core/gpio_wakeup/remote/boards/esp32c6_devkitc_lpcore.overlay)；[soc/espressif/esp32c6/hpcore_init_ulp.c](../../../soc/espressif/esp32c6/hpcore_init_ulp.c)。本地引用随仓库位置解析；上游快照摘要见来源记录，本地源码版本可能不同。

对应官方文档源码：[samples/boards/espressif/ulp/lp_core/gpio_wakeup/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/boards/espressif/ulp/lp_core/gpio_wakeup/README.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../samples/boards/espressif/ulp/lp_core/gpio_wakeup/README.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建、烧录、调试或执行硬件实验。

[上一章](P103_低功耗核串口回显.md) · [返回大纲](大纲.md) · [下一章](P105_主核中断低功耗核.md)
