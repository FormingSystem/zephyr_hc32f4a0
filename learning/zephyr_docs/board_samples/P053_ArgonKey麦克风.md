---
id: learning.zephyr-docs.board-samples.page-53
title: ArgonKey麦克风
kind: reference
status: maintained
domains: [zephyr, boards, samples]
source_url: https://docs.zephyrproject.org/latest/samples/boards/96boards/argonkey/microphone/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="argonkey_microphone"></a>

# 第53章\_麦克风（Microphone）

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/boards/96boards/argonkey/microphone/README.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

[在 GitHub 浏览源码（Browse source code on GitHub）](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/boards/96boards/argonkey/microphone/README.rst/..)

<a id="overview"></a>

## 53.1 概述（Overview）

本示例展示如何通过板载 MP34DT05 麦克风采集音频。麦克风产生脉冲密度调制（Pulse-Density Modulation，PDM）流，通过 I2S 取得，再由 OpenPDMFilter 库转换为脉冲编码调制（Pulse-Code Modulation，PCM）数据；原文说明该库的源代码可在此示例中获得。

> 译注——当前源码分层：应用通过数字麦克风（Digital Microphone，DMIC）接口配置、启动和读取 PCM；MPxxDTyy 驱动调用 OpenPDMFilter 完成 PDM 滤波。原文关于“此示例中的库源码”的说明保留，但本次应用目录并不直接实现该滤波库。I2S 是芯片间音频串行总线（Inter-IC Sound）。

<a id="requirements"></a>

## 53.2 前提条件（Requirements）

本示例需要 ArgonKey 开发板，以及用于取得输出音频流的 USB 转 TTL 1.8 V 串口线。开发板可以采用以下两种供电方式之一：

- 夹层板模式（Mezzanine mode）：通过 96Board 低速连接器将 ArgonKey 插接到 HiKey 开发板。

- 独立模式（Standalone mode）：通过 P1 连接器直接提供 5 V 电源。

<a id="references"></a>

## 53.3 参考资料（References）

- [Argonkey](https://docs.zephyrproject.org/latest/boards/96boards/argonkey/doc/index.html#96b_argonkey)

<a id="building-and-running"></a>

## 53.4 构建与运行（Building and Running）

> 译注——执行前提：本节 west 命令从读者的 Zephyr 源码根目录，在 UCRT64 Bash 或 Linux Bash 中执行；先按[入门指南](../getting_started/大纲.md)准备工具、模块、工具链及对应板。构建目录由工具生成，下载与启动方式按具体板文档核对。本次仅核对文档和源码，未执行构建、烧录或硬件实验。

```text
west build -b 96b_argonkey samples/boards/96boards/argonkey/microphone
west build -t run
```

<a id="sample-output"></a>

### 53.4.1 输出示例（Sample Output）

示例采集五秒音频，然后通过 COM 端口输出 PCM 流。USB 转 TTL 1.8 V 串口线可以连接到开发板背面低速连接器的 P3.5（TX）与 P3.7（RX）。

采集一开始，绿色 LED 点亮。采集结束时，绿色和红色 LED 同时点亮，并通过 COM 端口发送 PCM 流。输出完成后，绿色 LED 熄灭，红色 LED 保持点亮。按 RST 复位按钮可再次执行整个过程。

- 音频采集开始：GRN（绿灯）亮，RED（红灯）灭。

- 音频采集结束：GRN（绿灯）亮，RED（红灯）亮。

- 音频输出结束：GRN（绿灯）灭，RED（红灯）亮。

示例中固定设置了以下 PCM 音频参数：

- 16 kHz 采样率。

- 每个样本 16 位。

- 一个声道（单声道，Mono），因为只有一个麦克风。

以 16 kHz 采样五秒，将得到 80000 个 16 位样本。请求的麦克风 PDM 时钟应使 MP34DT05 驱动选择 128 倍过采样／抽取系数（Oversampling/decimation factor），从而得到 2.048 MHz 位时钟。

参见 [samples/boards/96boards/argonkey/microphone/src/main.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/boards/96boards/argonkey/microphone/src/main.c) 文件中的 pcm 与 pdm 配置。

注意（Note）

可以将 AUDIO_FREQ 改为 32000，并只采集 2500 ms；此时过采样／抽取系数为 64。

> 译注——采集长度：默认 16000 Hz × 5 s × 2 字节得到 160000 字节裸 PCM。改为 32000 Hz 时，还需将 NUM_MS 改成 2500 才保持相同样本数和缓冲区规模；只改采样率并不是原文完整的调整。

采集结束后，PCM 数据以二进制或 ASCII 格式输出到终端仿真器。输出格式由 [samples/boards/96boards/argonkey/microphone/src/main.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/boards/96boards/argonkey/microphone/src/main.c) 中以下宏控制，默认关闭：

- `PCM_OUTPUT_IN_ASCII`

<a id="binary-pcm-output"></a>

#### 53.4.1.1 二进制 PCM 输出（Binary PCM Output）

ttyUSB0 端口必须配置为原始模式（Raw mode），避免字符被终端处理机制转换。

> 译注——主机与路径：这一段 stty、cat 命令针对 Linux 串口设备；/dev/ttyUSB0 是系统设备节点，/tmp/sound.raw 是临时输出文件，不是作者仓库的位置。读者按实际串口名和自己的输出目录替换；Windows 的 COM 端口需用支持二进制原始采集的工具配置，不能直接照搬 Linux 设备路径。

```text
stty -F /dev/ttyUSB0 115200 raw
cat /dev/ttyUSB0 > /tmp/sound.raw
```

注意（Note）

“cat /dev/ttyUSB0 > /tmp/sound.raw”命令应在音频采集开始后（绿灯点亮后）、音频采集结束前（红灯点亮前）启动，以免初始启动消息进入文件。

注意（Note）

如果字符 0x0a 被解释为换行（NL），并额外插入了 0x0d（回车，CR），可能需要将添加的字节移除：

> 译注——二进制完整性：下面是原文命令，不是应对裸 PCM 通用执行的步骤。音频数据本身也可能包含合法的 0x0d、0x0a；盲目按文本转换会删改样本。应从采集开始就关闭终端字符转换、排除启动日志并核对预期字节数；只有确认传输过程额外插入字节时才能分析修复，长度相符也不能单独证明内容无损。

```text
dos2unix -f /tmp/sound.raw
```

<a id="ascii-pcm-output"></a>

#### 53.4.1.2 ASCII PCM 输出（ASCII PCM Output）

也可以重新编译，让 PCM 以 ASCII 格式输出，之后再转换成二进制。输出格式如下：

> 译注——两种输出格式：默认二进制逐样本先输出低字节再输出高字节；启用 ASCII 宏后得到的是带起止标记的十六进制文本，需解析为有符号 16 位小端样本后再播放。五秒是采集时长，串口发送还需要额外时间。本页没有可下载的原始音频附件，sound.raw 是实际采集后生成的文件。

```text
ArgonKey test!!
-- start
0xfbe0,
0xfbf0,
0xfc0c,
0xfc24,
0xfc3c,
0xfc4c,
0xfc68,
0xfc48,

[...]

0xfb98,
0xfb98,
0xfbb8,
0xfbac,
0xfbc4,
0xfbe8,
0xfbf4,
-- end
```

<a id="play-pcm-audio"></a>

#### 53.4.1.3 播放 PCM 音频（Play PCM Audio）

得到二进制 PCM 文件（例如 sound.raw）后，可使用 Audacity 等开源编辑／播放工具加载并播放。通过“Import→Raw Data”（导入→原始数据）菜单加载 sound.raw，选择有符号 16 位 PCM、小端序（Little Endian）、单声道、16 kHz 格式。

<a id="see-also"></a>

## 53.5 另请参阅（See also）

[音频（Audio）](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__interface.html)

> 译注——源码入口：[main.c](../../../samples/boards/96boards/argonkey/microphone/src/main.c)；[prj.conf](../../../samples/boards/96boards/argonkey/microphone/prj.conf)；[dmic_mpxxdtyy.c](../../../drivers/audio/dmic_mpxxdtyy.c)；[dmic_mpxxdtyy-i2s.c](../../../drivers/audio/dmic_mpxxdtyy-i2s.c)。链接相对本篇定位，仓库参照版本可能与本次上游快照不同。

对应官方文档源码：[samples/boards/96boards/argonkey/microphone/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/boards/96boards/argonkey/microphone/README.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../samples/boards/96boards/argonkey/microphone/README.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建、烧录或执行硬件实验。

[上一章](P052_Raspberry_Pi示例目录.md) · [返回大纲](大纲.md) · [下一章](P054_ArgonKey传感器.md)
