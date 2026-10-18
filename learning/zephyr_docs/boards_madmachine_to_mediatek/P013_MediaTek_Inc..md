---
id: learning.zephyr-docs.boards-madmachine-to-mediatek.page-13
title: MediaTek Inc.
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/mediatek/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="mediatek-inc"></a>

<a id="boards-mediatek"></a>

# 第13章\_联发科技（MediaTek Inc.）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/mediatek/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。


- [Genio 510评估套件（EVK）](P014_Genio_510_EVK.md)
- [Genio 700评估套件（EVK）](P015_Genio_700_EVK.md)

<a id="audio-dsps"></a>

<a id="boards-mtk-adsp"></a>

## 音频数字信号处理器（Audio DSPs）

Zephyr可构建并运行于多款MediaTek MT8xxx系列Arm SoC中的音频DSP，这些SoC用于多个厂商的Chromebook及MediaTek Genio评估套件。

原文列出已有四种DSP随相关SoC进入市场：MT8195，Kompanio 1380；MT8186，Kompanio 520；MT8188，Kompanio 838；MT8365，Genio 350 EVK。至少在以下设备上进行过开发和验证，此外还存在其他设备：

> <table>
> <tr>
> <th>片上系统（SoC）</th>
> <th>产品名称（Product Name）</th>
> <th>设备示例（Example Device）</th>
> <th>ChromeOS代号（Codename）</th>
> </tr>
> <tr>
> <td>MT8195</td>
> <td>Kompanio 1380</td>
> <td>HP Chromebook x360 13b</td>
> <td>dojo</td>
> </tr>
> <tr>
> <td>MT8186</td>
> <td>Kompanio 520</td>
> <td>Lenovo 300e Yoga Chromebook Gen 4</td>
> <td>steelix</td>
> </tr>
> <tr>
> <td>MT8188</td>
> <td>Kompanio 838</td>
> <td>Lenovo Chromebook Duet 11</td>
> <td>ciri</td>
> </tr>
> <tr>
> <td>MT8365</td>
> <td>Genio 350</td>
> <td>Genio 350 EVK</td>
> <td></td>
> </tr>
> </table>

<a id="hardware"></a>

### 硬件（Hardware）

这些设备采用Xtensa DSP内核，概念上与Intel ADSP系列十分相似。显著区别是它们均为单核，不支持并行SMP，同时也较少需要处理缓存不一致（Incoherent Cache）问题。

地址空间分为专用高速SRAM及约16 MB、速度慢得多的系统DRAM。Zephyr当前按SOF惯例加载并链接到DRAM；这些设备缓存较大，所有访问都使用缓存，与intel_adsp不同。SRAM目前用于中断向量及栈。

片上硬件相对较少。架构上，I2S编解码器、数字麦克风（DMIC）输入等片外音频硬件由主机内核管理；DSP通过一组定制DMA控制器接收数据。

除此之外，Zephyr可见硬件仅包括多个定时器，其中使用两个，以及用于同主机内核通信的双向中断源，即邮箱（Mailbox）。

<a id="programming-and-debugging"></a>

### 烧录与调试（Programming and Debugging）

这些设备完全在RAM中工作，因此没有通常意义的闪存烧录过程；内存状态由主机Linux环境初始化。流程由mtk_adsp_load.py脚本控制，只依赖Python标准库，可在具有Python 3.8或更高版本、兼容性适当的Linux环境中以root运行。处于开发者模式且安装开发包的Chromebook即可使用，详情见ChromiumOS开发者文档库：


- [开发者模式（Developer Mode）](https://www.chromium.org/chromium-os/developer-library/guides/device/developer-mode/)
- [Dev-Install：在Chrome OS设备安装开发及测试软件包（Developer and Test Packages）](https://www.chromium.org/chromium-os/developer-library/guides/device/install-software-on-base-images/)

设备准备好后，将构建目录的zephyr.img复制到设备，通常使用SSH，然后通过脚本运行即可。以下示例来自原作者名为steelix的MT8186设备：

```text
user@dev_host:~$ west build -b mt8186/mt8186/adsp samples/hello_world
...
... # build output
...
user@dev_host:~$ scp build/zephyr/zephyr.img root@steelix:
user@dev_host:~$ scp soc/mediatek/mt8xxx/common/adsp/mtk_adsp_load.py root@steelix:
user@dev_host:~$ ssh steelix

root@steelix:~ # ./mtk_adsp_load.py load zephyr.img
*** Booting Zephyr OS build v4.2.0-4743-g80fdfabcba48 ***
Hello World! mt8186/mt8186/adsp
```

<a id="debugging"></a>

#### 调试（Debugging）

由于I/O能力有限，这些平台的调试支持仍较有限。具备Cadence等硬件级调试及跟踪工具的用户可照常使用这些工具；Zephyr自身目前主要依靠printk及日志调试。理论上可将winstream等双向控制台与gdb_stub结合，后者在Xtensa及SDK调试器中有支持，但尚未集成。

<a id="toolchains"></a>

### 工具链（Toolchains）

MT8195、MT818X及MT8365工具链已包含在Zephyr SDK中。按入门指南中的通用构建步骤，即可为mt8195/mt8195/adsp、mt8186/mt8186/adsp、mt8188/mt8188/adsp及mt8365/mt8365/adsp目标构建。

<a id="closed-source-tools"></a>

#### 闭源工具（Closed-Source Tools）

Zephyr也可使用Cadence专有xcc及xt-clang工具链构建。这些工具的支持超出本文范围，但使用方式类似，通过环境变量指定工具链、内核标识及路径，例如：

```text
export XTENSA_TOOLS_ROOT=/path/to/XtDevTools
export XTENSA_CORE=hifi5_7stg_I64D128
export TOOLCHAIN_VER=RI-2021.6-linux
export ZEPHYR_TOOLCHAIN_VARIANT=xt-clang
export XTENSA_TOOLCHAIN_PATH=$XTENSA_TOOLS_ROOT/install/tools
west build -b mt8186/mt8186/adsp samples/hello_world
```

## 译注

MediaTek目录页包含音频DSP正文，已完整翻译。DSP单核运行、DRAM与SRAM用途、mtk_adsp_load.py只依赖标准库及原文调试限制均保留；原文steelix为示例目标设备名，不是本仓库主机。

---

[上一章](P012_Matouch_MTRO128G.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P014_Genio_510_EVK.md)
